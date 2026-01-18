from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Avg, Sum
from .models import Tutorial, Lecon, Quiz, Question, ProgressionUtilisateur
from .forms import QuizForm
from django.utils import timezone
from django.http import JsonResponse

@login_required
def catalogue_tutoriels(request):
    """Page d'accueil des tutoriels avec filtrage par niveau"""
    # Récupérer le filtre de niveau depuis l'URL
    niveau_filter = request.GET.get('niveau')
    
    # Requête de base avec annotations
    tutorials = Tutorial.objects.annotate(
        nombre_lecons=Count('lecons'),
        duree_totale=Sum('lecons__duree')
    ).order_by('ordre' if hasattr(Tutorial, 'ordre') else 'created_at')
    
    # Filtrer par niveau si spécifié
    if niveau_filter and niveau_filter.upper() in ['DEBUTANT', 'INTERMEDIAIRE', 'AVANCE']:
        tutorials = tutorials.filter(niveau=niveau_filter.upper())
    
    # Pour les utilisateurs connectés, calculer la progression
    user_progress = 0
    if request.user.is_authenticated:
        # Calculer la progression globale de l'utilisateur
        total_lecons = Lecon.objects.count()
        lecons_completees = ProgressionUtilisateur.objects.filter(
            utilisateur=request.user,
            est_completee=True
        ).count()
        user_progress = int((lecons_completees / total_lecons * 100)) if total_lecons > 0 else 0
        
        # Ajouter la progression pour chaque tutoriel
        for tutorial in tutorials:
            # Compter les leçons complétées dans ce tutoriel
            lecons_completees_tuto = ProgressionUtilisateur.objects.filter(
                utilisateur=request.user,
                tutorial=tutorial,
                est_completee=True
            ).count()
            
            tutorial.progression = lecons_completees_tuto
            tutorial.total_lecons = tutorial.lecons.count()
            tutorial.percentage = int((lecons_completees_tuto / tutorial.total_lecons * 100)) if tutorial.total_lecons > 0 else 0
            
            # Compter le nombre d'apprenants (utilisateurs uniques ayant commencé ce tutoriel)
            tutorial.students_count = ProgressionUtilisateur.objects.filter(
                tutorial=tutorial
            ).values('utilisateur').distinct().count()
    else:
        # Pour les utilisateurs non connectés
        for tutorial in tutorials:
            tutorial.progression = 0
            tutorial.total_lecons = tutorial.lecons.count()
            tutorial.percentage = 0
            tutorial.students_count = ProgressionUtilisateur.objects.filter(
                tutorial=tutorial
            ).values('utilisateur').distinct().count()
    
    return render(request, 'tutoriel/catalogue.html', {
        'tutorials': tutorials,
        'user_progress': user_progress,
        'page_title': 'Catalogue des Tutoriels',
        'niveau_filter': niveau_filter,
    })

@login_required
def lecon_detail(request, tutorial_id, lecon_id):
    """Détail d'une leçon avec vidéo"""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    lecon = get_object_or_404(Lecon, id=lecon_id, tutorial=tutorial)
    
    # Récupérer ou créer la progression
    progression, created = ProgressionUtilisateur.objects.get_or_create(
        utilisateur=request.user,
        tutorial=tutorial,
        lecon=lecon,
        defaults={'est_completee': False}
    )
    
    # Récupérer les leçons précédentes/suivantes
    lecons = list(tutorial.lecons.all())
    current_index = lecons.index(lecon)
    prev_lecon = lecons[current_index - 1] if current_index > 0 else None
    next_lecon = lecons[current_index + 1] if current_index < len(lecons) - 1 else None
    
    # Vérifier si l'utilisateur a accès au quiz
    has_quiz_access = progression.est_completee or current_index == 0
    
    return render(request, 'tutoriel/lecon_detail.html', {
        'tutorial': tutorial,
        'lecon': lecon,
        'progression': progression,
        'prev_lecon': prev_lecon,
        'next_lecon': next_lecon,
        'has_quiz_access': has_quiz_access,
    })

@login_required
def passer_quiz(request, quiz_id):
    """Passer un quiz"""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    lecon = quiz.lecon
    
    # Vérifier que l'utilisateur a accès au quiz
    # (doit avoir complété la leçon ou c'est la première leçon)
    progression = ProgressionUtilisateur.objects.filter(
        utilisateur=request.user,
        lecon=lecon
    ).first()
    
    if not progression and lecon.ordre != 1:
        messages.error(request, "Vous devez d'abord compléter la leçon avant de passer le quiz.")
        return redirect('tutoriel:lecon_detail', 
                      tutorial_id=lecon.tutorial.id, 
                      lecon_id=lecon.id)
    
    if request.method == 'POST':
        form = QuizForm(quiz, request.POST)
        if form.is_valid():
            # Calculer le score
            score = form.calculate_score()
            
            # Mettre à jour la progression
            ProgressionUtilisateur.objects.update_or_create(
                utilisateur=request.user,
                tutorial=lecon.tutorial,
                lecon=lecon,
                defaults={
                    'est_completee': True,
                    'score_quiz': score,
                    'date_completion': timezone.now()
                }
            )
            
            # Déterminer si le quiz est réussi
            is_passed = score >= quiz.pass_mark
            
            messages.success(request, f'Quiz terminé ! Score: {score}% - {"Réussi" if is_passed else "Échoué"}')
            return render(request, 'tutoriel/quiz_result.html', {
                'quiz': quiz,
                'score': score,
                'is_passed': is_passed,
                'pass_mark': quiz.pass_mark,
                'lecon': lecon,
            })
    else:
        form = QuizForm(quiz)
    
    return render(request, 'tutoriel/quiz.html', {
        'quiz': quiz,
        'form': form,
        'lecon': lecon,
    })

@login_required
def ma_progression(request):
    """Page de progression de l'utilisateur"""
    progressions = ProgressionUtilisateur.objects.filter(
        utilisateur=request.user
    ).select_related('tutorial', 'lecon').order_by('tutorial__niveau', 'lecon__ordre')
    
    # Statistiques globales
    total_lecons = Lecon.objects.count()
    lecons_completees = progressions.filter(est_completee=True).count()
    pourcentage_global = int((lecons_completees / total_lecons * 100)) if total_lecons > 0 else 0
    
    # Calculer le score moyen
    scores = progressions.filter(score_quiz__isnull=False).aggregate(Avg('score_quiz'))
    score_moyen = scores['score_quiz__avg'] or 0
    
    # Temps total passé
    temps_total = progressions.aggregate(Sum('temps_passe'))['temps_passe__sum'] or 0
    heures = temps_total // 3600
    minutes = (temps_total % 3600) // 60
    
    # Regrouper par tutoriel et par niveau
    by_tutorial = {}
    by_niveau = {
        'DEBUTANT': {'complete': 0, 'total': 0, 'tutorials': []},
        'INTERMEDIAIRE': {'complete': 0, 'total': 0, 'tutorials': []},
        'AVANCE': {'complete': 0, 'total': 0, 'tutorials': []},
    }
    
    for prog in progressions:
        # Regroupement par tutoriel
        tuto_id = prog.tutorial.id
        if tuto_id not in by_tutorial:
            by_tutorial[tuto_id] = {
                'tutorial': prog.tutorial,
                'lecons': [],
                'complete': 0,
                'total': prog.tutorial.lecons.count(),
                'score_moyen': 0
            }
        
        by_tutorial[tuto_id]['lecons'].append(prog)
        if prog.est_completee:
            by_tutorial[tuto_id]['complete'] += 1
        
        # Regroupement par niveau
        niveau = prog.tutorial.niveau
        if niveau in by_niveau:
            if prog.tutorial.id not in [t['id'] for t in by_niveau[niveau]['tutorials']]:
                by_niveau[niveau]['tutorials'].append({
                    'id': prog.tutorial.id,
                    'titre': prog.tutorial.titre
                })
            if prog.est_completee:
                by_niveau[niveau]['complete'] += 1
            by_niveau[niveau]['total'] += 1
    
    # Calculer le score moyen par tutoriel
    for tuto in by_tutorial.values():
        scores_tuto = [p.score_quiz for p in tuto['lecons'] if p.score_quiz is not None]
        tuto['score_moyen'] = sum(scores_tuto) / len(scores_tuto) if scores_tuto else 0
    
    return render(request, 'tutoriel/progression.html', {
        'progressions': progressions,
        'by_tutorial': by_tutorial.values(),
        'by_niveau': by_niveau,
        'stats': {
            'total_lecons': total_lecons,
            'lecons_completees': lecons_completees,
            'pourcentage_global': pourcentage_global,
            'score_moyen': round(score_moyen, 1),
            'temps_total': f"{heures}h {minutes}min",
        }
    })

@login_required
def mark_completed(request, tutorial_id, lecon_id):
    """Marque une leçon comme complétée (AJAX)"""
    if request.method == 'POST':
        tutorial = get_object_or_404(Tutorial, id=tutorial_id)
        lecon = get_object_or_404(Lecon, id=lecon_id, tutorial=tutorial)
        
        # Mettre à jour la progression
        progression, created = ProgressionUtilisateur.objects.update_or_create(
            utilisateur=request.user,
            tutorial=tutorial,
            lecon=lecon,
            defaults={
                'est_completee': True,
                'date_completion': timezone.now()
            }
        )
        
        # Mettre à jour le temps passé (si fourni)
        temps_passe = request.POST.get('temps_passe')
        if temps_passe and temps_passe.isdigit():
            progression.temps_passe = int(temps_passe)
            progression.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Leçon "{lecon.titre}" marquée comme complétée !',
            'progression': {
                'est_completee': progression.est_completee,
                'date_completion': progression.date_completion.strftime('%d/%m/%Y %H:%M'),
                'has_quiz': hasattr(lecon, 'quiz'),
            }
        })
    
    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'}, status=405)

@login_required
def update_temps_passe(request, progression_id):
    """Met à jour le temps passé sur une leçon (AJAX)"""
    if request.method == 'POST':
        progression = get_object_or_404(ProgressionUtilisateur, 
                                       id=progression_id, 
                                       utilisateur=request.user)
        
        temps_passe = request.POST.get('temps_passe')
        if temps_passe and temps_passe.isdigit():
            progression.temps_passe = int(temps_passe)
            progression.save()
            return JsonResponse({
                'success': True,
                'temps_passe': progression.temps_passe
            })
    
    return JsonResponse({'success': False, 'error': 'Données invalides'}, status=400)

def tutorial_detail(request, tutorial_id):
    """Détail d'un tutoriel avec toutes ses leçons"""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    lecons = tutorial.lecons.all()
    
    # Progression de l'utilisateur
    user_progress = None
    if request.user.is_authenticated:
        progression = ProgressionUtilisateur.objects.filter(
            utilisateur=request.user,
            tutorial=tutorial
        )
        lecons_completees = progression.filter(est_completee=True).count()
        user_progress = {
            'complete': lecons_completees,
            'total': lecons.count(),
            'percentage': int((lecons_completees / lecons.count() * 100)) if lecons.count() > 0 else 0
        }
    
    return render(request, 'tutoriel/tutorial_detail.html', {
        'tutorial': tutorial,
        'lecons': lecons,
        'user_progress': user_progress,
    })