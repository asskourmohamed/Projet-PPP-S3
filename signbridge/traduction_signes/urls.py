# from django.urls import path
# from . import views

# app_name = 'traduction'

# urlpatterns = [
#     path('signe-texte/', views.signe_vers_texte, name='signe_vers_texte'),
# ]
from django.urls import path
from . import views

app_name = 'traduction'

urlpatterns = [
    path('signe-vers-texte/', views.signe_vers_texte, name='signe_vers_texte'),
]