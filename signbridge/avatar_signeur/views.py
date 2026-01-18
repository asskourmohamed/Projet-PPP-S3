import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, FileResponse
from django.core.files import File
from .models import TraductionAvatar
from .services.text_to_pose_service import TextToPoseService

@login_required
def texte_vers_signe(request):
    """Page principale de traduction texte → signes"""
    
    # Récupérer les 10 dernières traductions de l'utilisateur
    historique = TraductionAvatar.objects.filter(
        utilisateur=request.user
    )[:10]
    
    context = {
        'historique': historique,
    }
    
    return render(request, 'avatar/texte_vers_signe.html', context)


# Dans avatar_signeur/views.py, modifier la fonction generer_pose

@login_required
def generer_pose(request):
    """Génère un fichier pose (et vidéo si possible) à partir du texte"""
    
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Méthode non autorisée'}, status=405)
    
    # Récupérer les données du formulaire
    texte = request.POST.get('texte', '').strip()
    langue_parlee = request.POST.get('langue_parlee', 'fr')
    langue_signee = request.POST.get('langue_signee', 'mar')
    
    if not texte:
        return JsonResponse({'success': False, 'message': 'Le texte est requis'}, status=400)
    
    # Créer l'enregistrement
    traduction = TraductionAvatar.objects.create(
        utilisateur=request.user,
        texte_original=texte,
        langue_parlee=langue_parlee,
        langue_signee=langue_signee,
        statut='en_traitement'
    )
    
    service = TextToPoseService()
    
    try:
        # ÉTAPE 1 : Générer le fichier pose
        result = service.text_to_pose(texte, langue_parlee, langue_signee)
        
        if not result['success']:
            traduction.statut = 'erreur'
            traduction.message_erreur = result['message']
            traduction.save()
            
            return JsonResponse({
                'success': False,
                'message': result['message']
            }, status=500)
        
        # Sauvegarder le fichier pose
        with open(result['pose_path'], 'rb') as f:
            traduction.fichier_pose.save(
                os.path.basename(result['pose_path']),
                File(f),
                save=False
            )
        
        traduction.temps_traitement = result['temps_traitement']
        traduction.statut = 'termine'  # Marqué comme terminé même sans vidéo
        traduction.save()
        
        # ÉTAPE 2 : Tenter de générer la vidéo (optionnel)
        video_result = service.pose_to_video(result['pose_path'])
        
        if video_result['success']:
            # Sauvegarder la vidéo si elle a été générée
            with open(video_result['video_path'], 'rb') as f:
                traduction.video_generee.save(
                    os.path.basename(video_result['video_path']),
                    File(f),
                    save=True
                )
            
            # Nettoyer les fichiers temporaires
            service.cleanup_temp_files(result['pose_path'])
            service.cleanup_temp_files(video_result['video_path'])
            
            return JsonResponse({
                'success': True,
                'message': 'Fichier .pose et vidéo générés avec succès !',
                'traduction_id': traduction.id,
                'pose_url': traduction.fichier_pose.url,
                'video_url': traduction.video_generee.url,
                'temps_traitement': result['temps_traitement']
            })
        else:
            # Si la vidéo échoue, on garde quand même la pose
            # C'est OK, l'utilisateur peut télécharger le .pose
            service.cleanup_temp_files(result['pose_path'])
            
            return JsonResponse({
                'success': True,
                'message': '✅ Fichier .pose généré avec succès ! (Vidéo non disponible)',
                'traduction_id': traduction.id,
                'pose_url': traduction.fichier_pose.url,
                'video_url': None,
                'temps_traitement': result['temps_traitement'],
                'warning': video_result['message']
            })
            
    except Exception as e:
        traduction.statut = 'erreur'
        traduction.message_erreur = str(e)
        traduction.save()
        
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        }, status=500)

@login_required
def generer_video(request, traduction_id):
    """Génère une vidéo à partir d'un fichier pose existant (si besoin)"""
    
    traduction = get_object_or_404(
        TraductionAvatar,
        id=traduction_id,
        utilisateur=request.user
    )
    
    if not traduction.fichier_pose:
        return JsonResponse({
            'success': False,
            'message': 'Aucun fichier pose disponible'
        }, status=400)
    
    # Si la vidéo existe déjà
    if traduction.video_generee:
        return JsonResponse({
            'success': True,
            'message': 'Vidéo déjà disponible',
            'video_url': traduction.video_generee.url
        })
    
    try:
        service = TextToPoseService()
        
        # Générer la vidéo
        result = service.pose_to_video(traduction.fichier_pose.path)
        
        if result['success']:
            # Sauvegarder la vidéo
            with open(result['video_path'], 'rb') as f:
                traduction.video_generee.save(
                    os.path.basename(result['video_path']),
                    File(f),
                    save=True
                )
            
            # Nettoyer le fichier temporaire
            service.cleanup_temp_files(result['video_path'])
            
            return JsonResponse({
                'success': True,
                'message': 'Vidéo générée avec succès !',
                'video_url': traduction.video_generee.url
            })
        else:
            return JsonResponse({
                'success': False,
                'message': result['message']
            }, status=500)
            
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        }, status=500)


@login_required
def telecharger_pose(request, traduction_id):
    """Permet de télécharger un fichier pose"""
    
    traduction = get_object_or_404(
        TraductionAvatar,
        id=traduction_id,
        utilisateur=request.user
    )
    
    if not traduction.fichier_pose:
        messages.error(request, "Aucun fichier pose disponible")
        return redirect('avatar:texte_vers_signe')
    
    response = FileResponse(
        traduction.fichier_pose.open('rb'),
        content_type='application/octet-stream'
    )
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(traduction.fichier_pose.name)}"'
    
    return response


@login_required
def historique_traductions(request):
    """Page d'historique des traductions"""
    
    traductions = TraductionAvatar.objects.filter(
        utilisateur=request.user
    )
    
    context = {
        'traductions': traductions
    }
    
    return render(request, 'avatar/historique.html', context)