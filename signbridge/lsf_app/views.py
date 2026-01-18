from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import InscriptionForm, ProfilForm

def accueil(request):
    """Vue pour la page d'accueil"""
    # Si l'utilisateur est connecté, rediriger vers la traduction
    if request.user.is_authenticated:
        return redirect('traduction:signe_vers_texte')
    
    # Sinon, afficher la page d'accueil normale
    return render(request, 'accueil.html')

def connexion(request):
    """Vue pour la connexion utilisateur"""
    if request.user.is_authenticated:
        # Si déjà connecté, rediriger vers la traduction
        return redirect('traduction:signe_vers_texte')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Connexion réussie ! Bienvenue {username}.')
                
                # Rediriger vers la page demandée ou la traduction par défaut
                next_url = request.POST.get('next', '')
                
                if next_url:
                    return redirect(next_url)
                elif user.is_staff or user.is_superuser:
                    return redirect('traduction:signe_vers_texte')
                else:
                    return redirect('admin:index')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    
    # Récupérer l'URL de redirection si présente dans les paramètres GET
    next_url = request.GET.get('next', '')
    
    return render(request, 'compte/login.html', {
        'form': form,
        'next': next_url
    })

def inscription(request):
    """Vue pour l'inscription d'un nouvel utilisateur"""
    if request.user.is_authenticated:
        # Si déjà connecté, rediriger vers la traduction
        return redirect('traduction:signe_vers_texte')
        
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Connecter automatiquement l'utilisateur
            login(request, user)
            
            messages.success(request, 'Inscription réussie ! Bienvenue sur SignBridge.')
            # Rediriger vers la traduction après inscription
            return redirect('traduction:signe_vers_texte')
    else:
        form = InscriptionForm()
    
    return render(request, 'compte/inscription.html', {'form': form})

@login_required
def profil(request):
    """Vue pour afficher et modifier le profil"""
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour.')
            return redirect('compte:profil')
    else:
        form = ProfilForm(instance=request.user)
    
    return render(request, 'compte/profil.html', {'form': form})

def deconnexion(request):
    """Vue pour la déconnexion"""
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('accueil')