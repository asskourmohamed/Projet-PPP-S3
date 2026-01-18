# SignBridge   
Plateforme web de traduction et d’apprentissage de la Langue des Signes

##  Présentation
**SignBridge** est une application web dédiée à la **traduction bidirectionnelle entre la langue des signes et le texte**, ainsi qu’à **l’apprentissage interactif de la Langue des Signes **.

Ce projet a été réalisé dans le cadre du **Projet Personnel et Professionnel** à l’**Institut National des Postes et Télécommunications (INPT)**.

 Le projet vise à **réduire les barrières de communication** entre personnes sourdes et entendantes grâce aux technologies web et au Machine Learning.

---

##  Objectifs du projet
- Faciliter la communication entre sourds et entendants  
- Proposer une traduction **Signes ↔ Texte** en temps réel  
- Offrir une **plateforme d’apprentissage interactive** de la langue des signes  
- Promouvoir l’**accessibilité numérique** et l’inclusion sociale  

---
##  Fonctionnalités principales

### 🔹 Module 1 : Traduction Signes → Texte
- Capture vidéo en temps réel via webcam
- Détection des landmarks (mains, bras, visage) avec **MediaPipe**
- Reconnaissance des signes à l’aide de modèles **Machine Learning**
- Affichage du texte traduit avec score de confiance

---

### 🔹 Module 2 : Traduction Texte → Signes (Avatar)
- Saisie de texte en français
- Génération automatique d’une animation en langue des signes
- Avatar 2D animé
- Lecteur vidéo intégré
- Historique des traductions

---

### 🔹 Module 3 : Plateforme d’apprentissage interactive
- Tutoriels classés par niveau et thématique
- Vidéos de démonstration
- Quiz interactifs
- Suivi de progression et statistiques utilisateur

---

##  Fonctionnalités transversales
- Authentification sécurisée (inscription / connexion)
- Profils utilisateurs personnalisés
- Interface moderne, responsive et accessible

---

##  Stack technologique

### Backend
- **Django 4.2.7**
- **Python 3.9+**
- **MySQL 8.0**

### Frontend
- HTML5 / CSS3
- JavaScript (ES6+)
- **Bootstrap 5**

### Machine Learning & Vision
- **MediaPipe**
- **TensorFlow / PyTorch**
- **OpenCV**

---

## Architecture du projet
Le projet suit une architecture **MVT (Model-View-Template)** avec une organisation modulaire :

signebridge/<br>
├── config/               # Configuration du projet Django<br>
├── lsf_app/              # Application principale<br>
├── traduction_signes/    # Module de traduction Signes → Texte<br>
├── avatar_signeur/       # Module de traduction Texte → Signes<br>
├── tutoriel/             # Module d’apprentissage interactif<br>
├── templates/            # Templates HTML<br>
├── static/               # Fichiers statiques (CSS, JS, images)<br>
├── media/                # Fichiers uploadés (vidéos, avatars, etc.)<br>
└── database/             # Scripts SQL (schéma et données de test)<br>


Un **microservice Flask** est utilisé pour le traitement Machine Learning en temps réel afin d’optimiser les performances.

---

## 🗄️ Base de données
- SGBD : **MySQL**
- Le schéma de la base est disponible dans le dossier `database/`
- Import :
```bash
mysql -u root -p lsf_database < database/DB.sql
