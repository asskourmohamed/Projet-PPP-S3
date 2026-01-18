from django.urls import path
from . import views

app_name = 'avatar'

urlpatterns = [
    # Page principale
    path('', views.texte_vers_signe, name='texte_vers_signe'),
    
    # API endpoints
    path('generer-pose/', views.generer_pose, name='generer_pose'),
    path('generer-video/<int:traduction_id>/', views.generer_video, name='generer_video'),
    
    # Téléchargements
    path('telecharger/<int:traduction_id>/', views.telecharger_pose, name='telecharger_pose'),
    
    # Historique
    path('historique/', views.historique_traductions, name='historique'),
]