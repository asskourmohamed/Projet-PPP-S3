# import os
# import time
# import subprocess
# from pathlib import Path
# from django.conf import settings
# from django.core.files import File

# class TextToPoseService:
#     """Service pour convertir du texte en fichier pose"""
    
#     def __init__(self):
#         # Chemin vers le lexique
#         self.lexicon_path = os.path.join(
#             settings.BASE_DIR,
#             'avatar_signeur',
#             'services',
#             'spoken_to_signed',
#             'assets',
#             'dummy_lexicon'
#         )
        
#         # Dossier temporaire pour les fichiers générés
#         self.temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
#         os.makedirs(self.temp_dir, exist_ok=True)
    
#     def text_to_pose(self, texte, langue_parlee='fr', langue_signee='ssr'):
#         """
#         Convertit du texte en fichier pose
        
#         Args:
#             texte (str): Le texte à convertir
#             langue_parlee (str): Code de la langue parlée (de, fr, it)
#             langue_signee (str): Code de la langue signée (sgg, ssr, slf)
            
#         Returns:
#             dict: {
#                 'success': bool,
#                 'pose_path': str ou None,
#                 'message': str,
#                 'temps_traitement': float
#             }
#         """
#         start_time = time.time()
        
#         try:
#             # Générer un nom de fichier unique
#             timestamp = int(time.time())
#             pose_filename = f"pose_{timestamp}.pose"
#             pose_path = os.path.join(self.temp_dir, pose_filename)
            
#             # Construire la commande
#             cmd = [
#                 'text_to_gloss_to_pose',
#                 '--text', texte,
#                 '--glosser', 'simple',
#                 '--lexicon', self.lexicon_path,
#                 '--spoken-language', langue_parlee,
#                 '--signed-language', langue_signee,
#                 '--pose', pose_path
#             ]
            
#             # Exécuter la commande
#             result = subprocess.run(
#                 cmd,
#                 capture_output=True,
#                 text=True,
#                 timeout=60  # Timeout de 60 secondes
#             )
            
#             temps_traitement = time.time() - start_time
            
#             # Vérifier si le fichier a été créé
#             if result.returncode == 0 and os.path.exists(pose_path):
#                 return {
#                     'success': True,
#                     'pose_path': pose_path,
#                     'message': 'Fichier pose généré avec succès',
#                     'temps_traitement': temps_traitement,
#                     'output': result.stdout
#                 }
#             else:
#                 return {
#                     'success': False,
#                     'pose_path': None,
#                     'message': f'Erreur: {result.stderr}',
#                     'temps_traitement': temps_traitement,
#                     'output': result.stdout
#                 }
                
#         except subprocess.TimeoutExpired:
#             return {
#                 'success': False,
#                 'pose_path': None,
#                 'message': 'Timeout: La génération a pris trop de temps',
#                 'temps_traitement': time.time() - start_time
#             }
            
#         except Exception as e:
#             return {
#                 'success': False,
#                 'pose_path': None,
#                 'message': f'Erreur inattendue: {str(e)}',
#                 'temps_traitement': time.time() - start_time
#             }
    
#     def pose_to_video(self, pose_path):
#         """
#         Convertit un fichier pose en vidéo
        
#         Args:
#             pose_path (str): Chemin vers le fichier .pose
            
#         Returns:
#             dict: {
#                 'success': bool,
#                 'video_path': str ou None,
#                 'message': str
#             }
#         """
#         try:
#             # Générer le nom du fichier vidéo
#             video_path = pose_path.replace('.pose', '.mp4')
            
#             # Commande pour générer la vidéo
#             cmd = [
#                 'visualize_pose',
#                 '-i', pose_path,
#                 '-o', video_path,
#                 '--normalize'
#             ]
            
#             result = subprocess.run(
#                 cmd,
#                 capture_output=True,
#                 text=True,
#                 timeout=120
#             )
            
#             if result.returncode == 0 and os.path.exists(video_path):
#                 return {
#                     'success': True,
#                     'video_path': video_path,
#                     'message': 'Vidéo générée avec succès'
#                 }
#             else:
#                 return {
#                     'success': False,
#                     'video_path': None,
#                     'message': f'Erreur: {result.stderr}'
#                 }
                
#         except Exception as e:
#             return {
#                 'success': False,
#                 'video_path': None,
#                 'message': f'Erreur: {str(e)}'
#             }
    
#     def cleanup_temp_files(self, file_path):
#         """Nettoie les fichiers temporaires"""
#         try:
#             if os.path.exists(file_path):
#                 os.remove(file_path)
#         except Exception as e:
#             print(f"Erreur lors du nettoyage: {e}")
import os
import time
import subprocess
import logging
from pathlib import Path
from django.conf import settings
from django.core.files import File

logger = logging.getLogger(__name__)

class TextToPoseService:
    """Service pour convertir du texte en fichier pose"""
    
    def __init__(self):
        # Chemin de base vers les lexicons
        self.lexicon_base_path = os.path.join(
            settings.BASE_DIR,
            'avatar_signeur',
            'services',
            'spoken_to_signed',
            'assets'
        )
        
        # Dossier temporaire pour les fichiers générés
        self.temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
        os.makedirs(self.temp_dir, exist_ok=True)
        
        logger.info(f"TextToPoseService initialisé avec lexicon_base_path: {self.lexicon_base_path}")
    
    def get_lexicon_path(self, langue_signee):
        """
        Retourne le chemin du lexicon selon la langue signée
        
        Args:
            langue_signee (str): Code de la langue signée (sgg, ssr, slf, mar)
            
        Returns:
            str: Chemin complet vers le lexicon
        """
        if langue_signee == 'mar':  # Marocain
            lexicon_path = os.path.join(self.lexicon_base_path, 'mon_lexicon')
        else:  # Par défaut (sgg, ssr, slf)
            lexicon_path = os.path.join(self.lexicon_base_path, 'dummy_lexicon')
        
        logger.info(f"Lexicon sélectionné pour {langue_signee}: {lexicon_path}")
        return lexicon_path
    
    def text_to_pose(self, texte, langue_parlee='fr', langue_signee='mar'):
        """
        Convertit du texte en fichier pose
        
        Args:
            texte (str): Le texte à convertir
            langue_parlee (str): Code de la langue parlée (de, fr, it)
            langue_signee (str): Code de la langue signée (sgg, ssr, slf, mar)
            
        Returns:
            dict: {
                'success': bool,
                'pose_path': str ou None,
                'message': str,
                'temps_traitement': float,
                'output': str (optionnel),
                'error': str (optionnel)
            }
        """
        start_time = time.time()
        
        logger.info(f"=== Début de la conversion texte → pose ===")
        logger.info(f"Texte: '{texte}'")
        logger.info(f"Langue parlée: {langue_parlee}")
        logger.info(f"Langue signée: {langue_signee}")
        
        try:
            # Obtenir le bon lexicon
            lexicon_path = self.get_lexicon_path(langue_signee)
            
            # Vérifier que le lexicon existe
            if not os.path.exists(lexicon_path):
                error_msg = f'Lexicon introuvable : {lexicon_path}'
                logger.error(error_msg)
                return {
                    'success': False,
                    'pose_path': None,
                    'message': error_msg,
                    'temps_traitement': time.time() - start_time
                }
            
            # Vérifier que index.csv existe
            index_csv = os.path.join(lexicon_path, 'index.csv')
            if not os.path.exists(index_csv):
                error_msg = f'Fichier index.csv introuvable dans {lexicon_path}'
                logger.error(error_msg)
                return {
                    'success': False,
                    'pose_path': None,
                    'message': error_msg,
                    'temps_traitement': time.time() - start_time
                }
            
            logger.info(f"Lexicon trouvé: {lexicon_path}")
            logger.info(f"Index CSV trouvé: {index_csv}")
            
            # Générer un nom de fichier unique
            timestamp = int(time.time())
            pose_filename = f"pose_{timestamp}.pose"
            pose_path = os.path.join(self.temp_dir, pose_filename)
            
            # Adapter la langue signée pour le pipeline
            # Si marocain, utiliser 'ssr' (le plus proche du français)
            pipeline_langue = 'ssr' if langue_signee == 'mar' else langue_signee
            
            logger.info(f"Langue pipeline: {pipeline_langue}")
            logger.info(f"Fichier de sortie: {pose_path}")
            
            # Construire la commande
            cmd = [
                'text_to_gloss_to_pose',
                '--text', texte,
                '--glosser', 'simple',
                '--lexicon', lexicon_path,
                '--spoken-language', langue_parlee,
                '--signed-language', pipeline_langue,
                '--pose', pose_path
            ]
            
            logger.info(f"Commande à exécuter: {' '.join(cmd)}")
            
            # Exécuter la commande
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60  # Timeout de 60 secondes
            )
            
            temps_traitement = time.time() - start_time
            
            logger.info(f"Code de retour: {result.returncode}")
            logger.info(f"STDOUT: {result.stdout}")
            if result.stderr:
                logger.warning(f"STDERR: {result.stderr}")
            
            # Vérifier si le fichier a été créé
            if result.returncode == 0 and os.path.exists(pose_path):
                file_size = os.path.getsize(pose_path)
                logger.info(f"✅ Fichier pose créé avec succès: {pose_path} ({file_size} bytes)")
                
                return {
                    'success': True,
                    'pose_path': pose_path,
                    'message': 'Fichier pose généré avec succès',
                    'temps_traitement': temps_traitement,
                    'output': result.stdout,
                    'file_size': file_size
                }
            else:
                error_msg = f'Erreur lors de la génération: {result.stderr or "Fichier non créé"}'
                logger.error(f"❌ {error_msg}")
                
                return {
                    'success': False,
                    'pose_path': None,
                    'message': error_msg,
                    'temps_traitement': temps_traitement,
                    'output': result.stdout,
                    'error': result.stderr
                }
                
        except subprocess.TimeoutExpired:
            error_msg = 'Timeout: La génération a pris trop de temps (>60s)'
            logger.error(f"❌ {error_msg}")
            
            return {
                'success': False,
                'pose_path': None,
                'message': error_msg,
                'temps_traitement': time.time() - start_time
            }
            
        except FileNotFoundError as e:
            error_msg = f'Commande introuvable. Assurez-vous que le package est installé: {str(e)}'
            logger.error(f"❌ {error_msg}")
            
            return {
                'success': False,
                'pose_path': None,
                'message': error_msg,
                'temps_traitement': time.time() - start_time
            }
            
        except Exception as e:
            error_msg = f'Erreur inattendue: {str(e)}'
            logger.exception(f"❌ {error_msg}")
            
            return {
                'success': False,
                'pose_path': None,
                'message': error_msg,
                'temps_traitement': time.time() - start_time
            }
    
    def pose_to_video(self, pose_path):
        """
        Convertit un fichier pose en vidéo en utilisant visualize_pose
        
        Args:
            pose_path (str): Chemin vers le fichier .pose
            
        Returns:
            dict: {
                'success': bool,
                'video_path': str ou None,
                'message': str
            }
        """
        logger.info(f"=== Début de la conversion pose → vidéo ===")
        logger.info(f"Fichier pose: {pose_path}")
        
        try:
            # Vérifier que le fichier pose existe
            if not os.path.exists(pose_path):
                error_msg = f'Fichier pose introuvable: {pose_path}'
                logger.error(error_msg)
                return {
                    'success': False,
                    'video_path': None,
                    'message': error_msg
                }
            
            # Générer le nom du fichier vidéo
            video_path = pose_path.replace('.pose', '.mp4')
            logger.info(f"Fichier vidéo de sortie: {video_path}")
            
            # OPTION 1 : Essayer avec visualize_pose (de pose-format)
            cmd = [
                'visualize_pose',
                '-i', pose_path,
                '-o', video_path,
                '--normalize'
            ]
            
            logger.info(f"Commande (visualize_pose): {' '.join(cmd)}")
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=120  # Timeout de 2 minutes
                )
                
                logger.info(f"Code de retour: {result.returncode}")
                logger.info(f"STDOUT: {result.stdout}")
                if result.stderr:
                    logger.warning(f"STDERR: {result.stderr}")
                
                if result.returncode == 0 and os.path.exists(video_path):
                    file_size = os.path.getsize(video_path)
                    logger.info(f"✅ Vidéo créée avec succès (visualize_pose): {video_path} ({file_size} bytes)")
                    
                    return {
                        'success': True,
                        'video_path': video_path,
                        'message': 'Vidéo générée avec succès',
                        'file_size': file_size
                    }
            
            except FileNotFoundError:
                logger.warning("⚠️ visualize_pose non trouvé, tentative avec pose_to_video...")
            
            # OPTION 2 : Essayer avec pose_to_video (du projet ZurichNLP)
            cmd = [
                'pose_to_video',
                '--pose', pose_path,
                '--video', video_path
            ]
            
            logger.info(f"Commande (pose_to_video): {' '.join(cmd)}")
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                
                logger.info(f"Code de retour: {result.returncode}")
                logger.info(f"STDOUT: {result.stdout}")
                if result.stderr:
                    logger.warning(f"STDERR: {result.stderr}")
                
                if result.returncode == 0 and os.path.exists(video_path):
                    file_size = os.path.getsize(video_path)
                    logger.info(f"✅ Vidéo créée avec succès (pose_to_video): {video_path} ({file_size} bytes)")
                    
                    return {
                        'success': True,
                        'video_path': video_path,
                        'message': 'Vidéo générée avec succès',
                        'file_size': file_size
                    }
                    
            except FileNotFoundError:
                logger.error("❌ Aucune commande de visualisation trouvée")
            
            # OPTION 3 : Utiliser Python directement avec pose-format
            logger.info("Tentative de génération avec pose-format Python...")
            return self._generate_video_with_python(pose_path, video_path)
                
        except subprocess.TimeoutExpired:
            error_msg = 'Timeout: La génération de la vidéo a pris trop de temps (>120s)'
            logger.error(f"❌ {error_msg}")
            
            return {
                'success': False,
                'video_path': None,
                'message': error_msg
            }
            
        except Exception as e:
            error_msg = f'Erreur lors de la génération de la vidéo: {str(e)}'
            logger.exception(f"❌ {error_msg}")
            
            return {
                'success': False,
                'video_path': None,
                'message': error_msg
            }
    
    def _generate_video_with_python(self, pose_path, video_path):
        """
        Génère une vidéo à partir d'un fichier pose en utilisant Python directement
        
        Args:
            pose_path (str): Chemin du fichier .pose
            video_path (str): Chemin de sortie pour la vidéo
            
        Returns:
            dict: Résultat de la génération
        """
        try:
            import cv2
            import numpy as np
            from pose_format import Pose
            from pose_format.pose_visualizer import PoseVisualizer
            
            logger.info("Chargement du fichier pose...")
            
            # Lire le fichier pose
            with open(pose_path, 'rb') as f:
                pose = Pose.read(f.read())
            
            logger.info(f"Pose chargée: {len(pose.body.data)} frames")
            
            # Créer le visualiseur
            visualizer = PoseVisualizer(pose)
            
            # Paramètres vidéo
            fps = int(pose.body.fps)
            width = 500
            height = 500
            
            # Créer le writer vidéo
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
            
            logger.info(f"Génération de {len(pose.body.data)} frames à {fps} FPS...")
            
            # Générer chaque frame
            for frame_idx in range(len(pose.body.data)):
                # Dessiner la frame
                img = visualizer.draw_frame(frame_idx, width, height)
                
                # Convertir en BGR pour OpenCV
                if img is not None:
                    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                    out.write(img_bgr)
                
                if frame_idx % 10 == 0:
                    logger.info(f"Frame {frame_idx}/{len(pose.body.data)}")
            
            out.release()
            
            if os.path.exists(video_path):
                file_size = os.path.getsize(video_path)
                logger.info(f"✅ Vidéo créée avec Python: {video_path} ({file_size} bytes)")
                
                return {
                    'success': True,
                    'video_path': video_path,
                    'message': 'Vidéo générée avec succès (méthode Python)',
                    'file_size': file_size
                }
            else:
                return {
                    'success': False,
                    'video_path': None,
                    'message': 'Échec de la génération de la vidéo'
                }
                
        except ImportError as e:
            logger.error(f"Bibliothèques manquantes: {e}")
            return {
                'success': False,
                'video_path': None,
                'message': f'Bibliothèques requises non installées: {str(e)}'
            }
        except Exception as e:
            logger.exception(f"Erreur Python: {e}")
            return {
                'success': False,
                'video_path': None,
                'message': f'Erreur lors de la génération: {str(e)}'
            }
    
    def cleanup_temp_files(self, file_path):
        """
        Nettoie les fichiers temporaires
        
        Args:
            file_path (str): Chemin du fichier à supprimer
        """
        try:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"🗑️ Fichier temporaire supprimé: {file_path}")
            else:
                logger.warning(f"⚠️ Fichier introuvable pour suppression: {file_path}")
        except Exception as e:
            logger.error(f"❌ Erreur lors du nettoyage de {file_path}: {e}")
    
    def list_available_glosses(self, langue_signee='mar'):
        """
        Liste les glosses disponibles dans un lexicon
        
        Args:
            langue_signee (str): Code de la langue signée
            
        Returns:
            list: Liste des glosses disponibles
        """
        try:
            lexicon_path = self.get_lexicon_path(langue_signee)
            index_csv = os.path.join(lexicon_path, 'index.csv')
            
            if not os.path.exists(index_csv):
                logger.warning(f"Index CSV introuvable: {index_csv}")
                return []
            
            import csv
            glosses = []
            
            with open(index_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    glosses.append({
                        'gloss': row.get('glosses', ''),
                        'words': row.get('words', ''),
                        'file': row.get('path', '')
                    })
            
            logger.info(f"📚 {len(glosses)} glosses trouvées dans {langue_signee}")
            return glosses
            
        except Exception as e:
            logger.error(f"Erreur lors de la lecture des glosses: {e}")
            return []