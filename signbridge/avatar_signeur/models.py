from django.db import models
from django.conf import settings

class TraductionAvatar(models.Model):
    """Stocke les traductions texte → signes (pose)"""
    langue_parlee = models.CharField(
        max_length=10,
        default='fr',
        choices=[
            ('de', 'Allemand'),
            ('fr', 'Français'),
            ('it', 'Italien'),
        ],
        verbose_name="Langue parlée"
    )
    
    langue_signee = models.CharField(
        max_length=10,
        default='mar',  # Changé en 'mar'
        choices=[
            ('sgg', 'Langue des signes suisse-allemande'),
            ('ssr', 'Langue des signes française de Suisse'),
            ('slf', 'Langue des signes italienne de Suisse'),
            ('mar', 'Langue des signes marocaine'),  # NOUVEAU
        ],
        verbose_name="Langue signée"
    )
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='traductions_avatar'
    )
    
    texte_original = models.TextField(
        verbose_name="Texte à traduire",
        help_text="Texte en français à convertir en signes"
    )
    
    fichier_pose = models.FileField(
        upload_to='avatars/poses/%Y/%m/%d/',
        verbose_name="Fichier pose généré",
        null=True,
        blank=True
    )
    
    video_generee = models.FileField(
        upload_to='avatars/videos/%Y/%m/%d/',
        verbose_name="Vidéo générée",
        null=True,
        blank=True
    )
    
    statut = models.CharField(
        max_length=20,
        default='en_attente',
        choices=[
            ('en_attente', 'En attente'),
            ('en_traitement', 'En traitement'),
            ('termine', 'Terminé'),
            ('erreur', 'Erreur'),
        ]
    )
    
    message_erreur = models.TextField(
        blank=True,
        null=True,
        verbose_name="Message d'erreur"
    )
    
    temps_traitement = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Temps de traitement (secondes)"
    )
    
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Traduction Avatar"
        verbose_name_plural = "Traductions Avatar"
        ordering = ['-date_creation']
    
    def __str__(self):
        return f"{self.texte_original[:50]} - {self.utilisateur.email}"