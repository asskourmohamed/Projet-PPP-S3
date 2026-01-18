from django.contrib import admin
from .models import Tutorial, Lecon, Quiz, Question, Reponse, ProgressionUtilisateur

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True
    fields = ('question_text', 'type_question', 'ordre')
    ordering = ('ordre',)

class ReponseInline(admin.TabularInline):
    model = Reponse
    extra = 3
    max_num = 6
    fields = ('reponse_text', 'est_correcte')
    ordering = ('id',)

class LeconInline(admin.TabularInline):
    model = Lecon
    extra = 1
    show_change_link = True
    fields = ('titre', 'ordre', 'duree', 'video')
    ordering = ('ordre',)

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('titre', 'niveau', 'created_at', 'nombre_lecons', 'duree_totale', 'est_actif')
    list_filter = ('niveau', 'created_at', 'est_actif')
    search_fields = ('titre', 'description')
    list_editable = ('est_actif', 'niveau')
    list_per_page = 20
    inlines = [LeconInline]
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'description', 'niveau', 'ordre')
        }),
        ('Média', {
            'fields': ('image_couverture',),
            'classes': ('collapse',)
        }),
        ('Paramètres', {
            'fields': ('est_actif', 'difficulte'),
            'classes': ('collapse',)
        }),
    )
    
    def nombre_lecons(self, obj):
        return obj.lecons.count()
    nombre_lecons.short_description = 'Nb. leçons'
    nombre_lecons.admin_order_field = 'lecons__count'
    
    def duree_totale(self, obj):
        total = sum(lecon.duree for lecon in obj.lecons.all())
        minutes = total // 60
        secondes = total % 60
        return f"{minutes}:{secondes:02d}"
    duree_totale.short_description = 'Durée totale'
    
    # Pour ajouter des actions d'administration
    actions = ['activer_tutoriels', 'desactiver_tutoriels']
    
    def activer_tutoriels(self, request, queryset):
        updated = queryset.update(est_actif=True)
        self.message_user(request, f"{updated} tutoriel(s) activé(s).")
    activer_tutoriels.short_description = "Activer les tutoriels sélectionnés"
    
    def desactiver_tutoriels(self, request, queryset):
        updated = queryset.update(est_actif=False)
        self.message_user(request, f"{updated} tutoriel(s) désactivé(s).")
    desactiver_tutoriels.short_description = "Désactiver les tutoriels sélectionnés"

@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display = ('titre', 'tutorial', 'niveau_tutorial', 'ordre', 'duree_formatee', 'has_quiz')
    list_filter = ('tutorial__niveau', 'tutorial')
    search_fields = ('titre', 'texte_explicatif', 'tutorial__titre')
    ordering = ('tutorial', 'ordre')
    list_select_related = ('tutorial',)
    list_per_page = 30
    
    fieldsets = (
        ('Contenu', {
            'fields': ('tutorial', 'titre', 'ordre', 'texte_explicatif')
        }),
        ('Média', {
            'fields': ('video', 'duree'),
            'description': 'Durée en secondes'
        }),
    )
    
    def niveau_tutorial(self, obj):
        return obj.tutorial.get_niveau_display()
    niveau_tutorial.short_description = 'Niveau'
    niveau_tutorial.admin_order_field = 'tutorial__niveau'
    
    def duree_formatee(self, obj):
        minutes = obj.duree // 60
        secondes = obj.duree % 60
        return f"{minutes}:{secondes:02d}"
    duree_formatee.short_description = 'Durée'
    
    def has_quiz(self, obj):
        return hasattr(obj, 'quiz')
    has_quiz.boolean = True
    has_quiz.short_description = 'Quiz'

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('titre', 'lecon', 'niveau', 'nombre_questions', 'pass_mark', 'difficulte')
    list_filter = ('lecon__tutorial__niveau',)
    inlines = [QuestionInline]
    search_fields = ('titre', 'description', 'lecon__titre')
    list_per_page = 20
    
    fieldsets = (
        ('Informations', {
            'fields': ('lecon', 'titre', 'description')
        }),
        ('Configuration', {
            'fields': ('pass_mark', 'difficulte', 'temps_limite')
        }),
    )
    
    def niveau(self, obj):
        return obj.lecon.tutorial.get_niveau_display()
    niveau.short_description = 'Niveau'
    
    def nombre_questions(self, obj):
        return obj.questions.count()
    nombre_questions.short_description = 'Nb. questions'
    
    # Pour limiter les choix de leçon selon le niveau
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lecon":
            # Vous pouvez filtrer les leçons selon des critères
            kwargs["queryset"] = Lecon.objects.select_related('tutorial').order_by('tutorial__niveau', 'ordre')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_courte', 'quiz', 'type_question', 'ordre', 'niveau_quiz')
    list_filter = ('quiz__lecon__tutorial__niveau', 'type_question', 'quiz')
    ordering = ('quiz', 'ordre')
    inlines = [ReponseInline]
    search_fields = ('question_text', 'quiz__titre')
    list_select_related = ('quiz__lecon__tutorial',)
    list_per_page = 30
    
    fieldsets = (
        ('Question', {
            'fields': ('quiz', 'question_text', 'type_question', 'ordre', 'points')
        }),
        ('Explication', {
            'fields': ('explication',),
            'classes': ('collapse',)
        }),
    )
    
    def question_courte(self, obj):
        return obj.question_text[:50] + '...' if len(obj.question_text) > 50 else obj.question_text
    question_courte.short_description = 'Question'
    
    def niveau_quiz(self, obj):
        return obj.quiz.lecon.tutorial.get_niveau_display()
    niveau_quiz.short_description = 'Niveau'
    niveau_quiz.admin_order_field = 'quiz__lecon__tutorial__niveau'
    
    # Pour limiter les choix de quiz selon le niveau
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "quiz":
            kwargs["queryset"] = Quiz.objects.select_related('lecon__tutorial').order_by('lecon__tutorial__niveau')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(ProgressionUtilisateur)
class ProgressionUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'tutorial', 'niveau', 'lecon', 'est_completee', 'score_quiz', 'date_completion')
    list_filter = ('est_completee', 'tutorial__niveau', 'tutorial', 'utilisateur')
    search_fields = ('utilisateur__username', 'lecon__titre', 'tutorial__titre')
    readonly_fields = ('date_completion', 'temps_passe')
    list_select_related = ('utilisateur', 'tutorial', 'lecon')
    list_per_page = 50
    
    fieldsets = (
        ('Informations', {
            'fields': ('utilisateur', 'tutorial', 'lecon')
        }),
        ('Progression', {
            'fields': ('est_completee', 'score_quiz', 'date_completion', 'temps_passe')
        }),
    )
    
    def niveau(self, obj):
        return obj.tutorial.get_niveau_display()
    niveau.short_description = 'Niveau'
    niveau.admin_order_field = 'tutorial__niveau'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'utilisateur', 'tutorial', 'lecon'
        )
    
    # Pour optimiser les performances dans la liste
    def get_list_display(self, request):
        base_list = super().get_list_display(request)
        return list(base_list) + ['temps_total_formate']
    
    def temps_total_formate(self, obj):
        heures = obj.temps_passe // 3600
        minutes = (obj.temps_passe % 3600) // 60
        return f"{heures}h{minutes:02d}"
    temps_total_formate.short_description = 'Temps passé'
    
    # Actions pour l'admin
    actions = ['marquer_comme_completees', 'marquer_comme_incompletees']
    
    def marquer_comme_completees(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(est_completee=True, date_completion=timezone.now())
        self.message_user(request, f"{updated} progression(s) marquée(s) comme complétées.")
    marquer_comme_completees.short_description = "Marquer comme complétées"
    
    def marquer_comme_incompletees(self, request, queryset):
        updated = queryset.update(est_completee=False, date_completion=None)
        self.message_user(request, f"{updated} progression(s) marquée(s) comme incomplètes.")
    marquer_comme_incompletees.short_description = "Marquer comme incomplètes"