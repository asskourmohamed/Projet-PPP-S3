-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: lsf_database
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Utilisateur',6,'add_utilisateur'),(22,'Can change Utilisateur',6,'change_utilisateur'),(23,'Can delete Utilisateur',6,'delete_utilisateur'),(24,'Can view Utilisateur',6,'view_utilisateur'),(25,'Can add Traduction Avatar',7,'add_traductionavatar'),(26,'Can change Traduction Avatar',7,'change_traductionavatar'),(27,'Can delete Traduction Avatar',7,'delete_traductionavatar'),(28,'Can view Traduction Avatar',7,'view_traductionavatar'),(29,'Can add quiz',11,'add_quiz'),(30,'Can change quiz',11,'change_quiz'),(31,'Can delete quiz',11,'delete_quiz'),(32,'Can view quiz',11,'view_quiz'),(33,'Can add tutorial',13,'add_tutorial'),(34,'Can change tutorial',13,'change_tutorial'),(35,'Can delete tutorial',13,'delete_tutorial'),(36,'Can view tutorial',13,'view_tutorial'),(37,'Can add progression utilisateur',9,'add_progressionutilisateur'),(38,'Can change progression utilisateur',9,'change_progressionutilisateur'),(39,'Can delete progression utilisateur',9,'delete_progressionutilisateur'),(40,'Can view progression utilisateur',9,'view_progressionutilisateur'),(41,'Can add question',10,'add_question'),(42,'Can change question',10,'change_question'),(43,'Can delete question',10,'delete_question'),(44,'Can view question',10,'view_question'),(45,'Can add reponse',12,'add_reponse'),(46,'Can change reponse',12,'change_reponse'),(47,'Can delete reponse',12,'delete_reponse'),(48,'Can view reponse',12,'view_reponse'),(49,'Can add lecon',8,'add_lecon'),(50,'Can change lecon',8,'change_lecon'),(51,'Can delete lecon',8,'delete_lecon'),(52,'Can view lecon',8,'view_lecon');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avatar_signeur_traductionavatar`
--

DROP TABLE IF EXISTS `avatar_signeur_traductionavatar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avatar_signeur_traductionavatar` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `texte_original` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `langue_parlee` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `langue_signee` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fichier_pose` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `video_generee` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `statut` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `message_erreur` longtext COLLATE utf8mb4_unicode_ci,
  `temps_traitement` double DEFAULT NULL,
  `date_creation` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `avatar_signeur_tradu_utilisateur_id_3228dba4_fk_lsf_app_u` (`utilisateur_id`),
  CONSTRAINT `avatar_signeur_tradu_utilisateur_id_3228dba4_fk_lsf_app_u` FOREIGN KEY (`utilisateur_id`) REFERENCES `lsf_app_utilisateur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avatar_signeur_traductionavatar`
--

LOCK TABLES `avatar_signeur_traductionavatar` WRITE;
/*!40000 ALTER TABLE `avatar_signeur_traductionavatar` DISABLE KEYS */;
INSERT INTO `avatar_signeur_traductionavatar` VALUES (21,'Pizza','de','sgg','avatars/poses/2026/01/15/pose_1768515048.pose','avatars/videos/2026/01/15/pose_1768515048.mp4','termine',NULL,25.03630757331848,'2026-01-15 22:10:48.028420','2026-01-15 22:11:23.408708',12),(29,'Pizza','de','sgg','avatars/poses/2026/01/17/pose_1768674162.pose','avatars/videos/2026/01/17/pose_1768674162.mp4','termine',NULL,3.146268367767334,'2026-01-17 18:22:42.628510','2026-01-17 18:22:50.255506',1),(30,'Comment tu t appelles','fr','mar','avatars/poses/2026/01/17/pose_1768674702.pose','avatars/videos/2026/01/17/pose_1768674702.mp4','termine',NULL,11.648154258728027,'2026-01-17 18:31:42.316351','2026-01-17 18:32:28.382159',1),(31,'Quel age as tu','fr','mar','avatars/poses/2026/01/17/pose_1768686965.pose','avatars/videos/2026/01/17/pose_1768686965.mp4','termine',NULL,7.861441373825073,'2026-01-17 21:56:05.620810','2026-01-17 21:56:32.002912',1),(32,'ecole','fr','mar','avatars/poses/2026/01/17/pose_1768688316.pose','avatars/videos/2026/01/17/pose_1768688316.mp4','termine',NULL,5.014333009719849,'2026-01-17 22:18:36.425108','2026-01-17 22:18:49.144573',1),(34,'bonjour','fr','mar','avatars/poses/2026/01/18/pose_1768692211.pose','avatars/videos/2026/01/18/pose_1768692211.mp4','termine',NULL,9.237996578216553,'2026-01-17 23:23:31.847443','2026-01-17 23:23:59.147313',1),(35,'bonjour','fr','mar','avatars/poses/2026/01/18/pose_1768732673.pose','avatars/videos/2026/01/18/pose_1768732673.mp4','termine',NULL,56.36426782608032,'2026-01-18 10:37:53.465157','2026-01-18 10:40:06.792211',1);
/*!40000 ALTER TABLE `avatar_signeur_traductionavatar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_lsf_app_utilisateur_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_lsf_app_utilisateur_id` FOREIGN KEY (`user_id`) REFERENCES `lsf_app_utilisateur` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-01-11 00:09:46.700436','2','test_sourd (SOURD)',1,'[{\"added\": {}}]',6,1),(2,'2026-01-11 21:22:40.659421','4','sud1 (SOURD)',3,'',6,1),(3,'2026-01-12 14:51:46.839785','7','azert (SOURD)',3,'',6,1),(4,'2026-01-12 21:54:08.046192','8','zahra (ADMIN)',3,'',6,1),(5,'2026-01-15 22:35:36.015867','1','Les notions de base',1,'[{\"added\": {}}, {\"added\": {\"name\": \"lecon\", \"object\": \"Les moyens de transport - Les notions de base\"}}]',13,1),(6,'2026-01-15 22:38:30.165927','2','hélicoptère - Les notions de base',1,'[{\"added\": {}}]',8,1),(7,'2026-01-15 23:02:11.655147','2','Les notions intermédiares',1,'[{\"added\": {}}, {\"added\": {\"name\": \"lecon\", \"object\": \"Comment tu t\'appelles - Les notions interm\\u00e9diares\"}}]',13,1),(8,'2026-01-15 23:03:59.983367','4','Comment tu t\'appelles - Les notions intermédiares',1,'[{\"added\": {}}]',8,1),(9,'2026-01-17 16:46:37.029111','1','Les bases de la Langue des Signes (Débutant)',1,'[{\"added\": {}}]',13,1),(10,'2026-01-17 16:49:13.255643','2','Communication quotidienne (Intermédiaire)',1,'[{\"added\": {}}]',13,1),(11,'2026-01-17 16:53:40.714834','3','Language des signes professionnelle et culturelle (Avancé)',1,'[{\"added\": {}}]',13,1),(12,'2026-01-17 16:55:20.373839','1','L\'alphabet de A à Z - Les bases de la Langue des Signes',1,'[{\"added\": {}}]',8,1),(13,'2026-01-17 16:57:06.385114','2','Présenter quelqu\'un - Communication quotidienne',1,'[{\"added\": {}}]',8,1),(14,'2026-01-17 16:57:50.857966','3','Demander son chemin - Language des signes professionnelle et culturelle',1,'[{\"added\": {}}]',8,1),(15,'2026-01-17 17:01:32.742780','1','Quiz: Quiz alphabet',1,'[{\"added\": {}}, {\"added\": {\"name\": \"question\", \"object\": \"Q1: Quelles sont les lettres qui se font avec la main ...\"}}]',11,1),(16,'2026-01-17 17:07:46.926911','1','Q1: Quelles sont les lettres qui se font avec la main ...',2,'[{\"changed\": {\"fields\": [\"Explication\"]}}, {\"added\": {\"name\": \"reponse\", \"object\": \"A... (\\u2717)\"}}, {\"added\": {\"name\": \"reponse\", \"object\": \"S... (\\u2717)\"}}, {\"added\": {\"name\": \"reponse\", \"object\": \"B... (\\u2713)\"}}]',10,1),(17,'2026-01-17 17:09:22.034571','2','Q1: La lettre \'L\' en LSF se fait avec l\'index et le po...',1,'[{\"added\": {}}]',10,1),(18,'2026-01-17 17:09:49.559780','2','Q1: La lettre \'L\' en LSF se fait avec l\'index et le po...',2,'[{\"added\": {\"name\": \"reponse\", \"object\": \"Vrai... (\\u2713)\"}}, {\"added\": {\"name\": \"reponse\", \"object\": \"Faux... (\\u2717)\"}}]',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(7,'avatar_signeur','traductionavatar'),(4,'contenttypes','contenttype'),(6,'lsf_app','utilisateur'),(5,'sessions','session'),(8,'tutoriel','lecon'),(9,'tutoriel','progressionutilisateur'),(10,'tutoriel','question'),(11,'tutoriel','quiz'),(12,'tutoriel','reponse'),(13,'tutoriel','tutorial');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-01-10 23:55:09.962283'),(2,'contenttypes','0002_remove_content_type_name','2026-01-10 23:55:10.325940'),(3,'auth','0001_initial','2026-01-10 23:55:11.248334'),(4,'auth','0002_alter_permission_name_max_length','2026-01-10 23:55:11.482082'),(5,'auth','0003_alter_user_email_max_length','2026-01-10 23:55:11.497416'),(6,'auth','0004_alter_user_username_opts','2026-01-10 23:55:11.517720'),(7,'auth','0005_alter_user_last_login_null','2026-01-10 23:55:11.542370'),(8,'auth','0006_require_contenttypes_0002','2026-01-10 23:55:11.550571'),(9,'auth','0007_alter_validators_add_error_messages','2026-01-10 23:55:11.606626'),(10,'auth','0008_alter_user_username_max_length','2026-01-10 23:55:11.618000'),(11,'auth','0009_alter_user_last_name_max_length','2026-01-10 23:55:11.643125'),(12,'auth','0010_alter_group_name_max_length','2026-01-10 23:55:11.694516'),(13,'auth','0011_update_proxy_permissions','2026-01-10 23:55:11.718009'),(14,'auth','0012_alter_user_first_name_max_length','2026-01-10 23:55:11.748530'),(15,'lsf_app','0001_initial','2026-01-10 23:55:12.685613'),(16,'admin','0001_initial','2026-01-10 23:55:13.216570'),(17,'admin','0002_logentry_remove_auto_add','2026-01-10 23:55:13.276583'),(18,'admin','0003_logentry_add_action_flag_choices','2026-01-10 23:55:13.335266'),(19,'sessions','0001_initial','2026-01-10 23:55:13.436398'),(20,'avatar_signeur','0001_initial','2026-01-15 00:30:02.946188'),(22,'tutoriel','0001_initial','2026-01-17 16:26:25.583810'),(23,'avatar_signeur','0002_alter_traductionavatar_langue_signee','2026-01-17 17:57:12.674027');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2unne397gzeq7dhdc3m6iqroo82dikmk','.eJxVjEEOwiAQRe_C2hAoDLQu3XsGwjCDVA0kpV0Z765NutDtf-_9lwhxW0vYOi9hJnEWIE6_G8b04LoDusd6azK1ui4zyl2RB-3y2oifl8P9Oyixl289ZMs-s8IMXqtE2vGoLMQMkIDAgWGccDRpii6RZQPkpwzaoVfDgFa8P_aWOA4:1vf4WR:UySi4gxIBU4na3QyyDcvf1Yc8BrFfQk7I3qYpeCFUJo','2026-01-25 23:06:59.763168'),('3frwsvoyktojqk8ft42ttrbzp8zp74gq','.eJxVjEEOgjAQRe_StWmY6UyhLt1zhqadFosaSCisjHcXEha6_e-9_1Y-bGvxW82LH5O6KkB1-R1jkGeeDpIeYbrPWuZpXcaoD0WftOp-Tvl1O92_gxJq2WuDHKElpsaKYSMUO3LcgoPUOhmgQ4OG40CQcoOBd4ltI2SBMFtG9fkCxWI2SA:1vgTsp:7Klypl9y8_jcRrsicCmp2GHLxCeM8YC4DBYYbWnKjRY','2026-01-29 20:23:55.073010'),('djifjtvvpm3521alkrfofynte5l1dnrv','.eJxVjMsOwiAQRf-FtSE8CohL9_0GMsMMUjU0Ke3K-O_apAvd3nPOfYkE21rT1nlJE4mL0OL0uyHkB7cd0B3abZZ5busyodwVedAux5n4eT3cv4MKvX5rh8ZlcAWULhQAcAiBbShQtNHeGRuzZaZM2pNypkQqg_ERieFs0Srx_gAENjiz:1vgVpI:K8Yahg5NLkXNY3MwdKr7PHPEyN6fOsQw9cSlUgzeNSM','2026-01-29 22:28:24.540342'),('uibo2bdunhoqm2kktqr121bdlhi559ct','.eJxVjMsOwiAQRf-FtSE8CohL9_0GMsMMUjU0Ke3K-O_apAvd3nPOfYkE21rT1nlJE4mL0OL0uyHkB7cd0B3abZZ5busyodwVedAux5n4eT3cv4MKvX5rh8ZlcAWULhQAcAiBbShQtNHeGRuzZaZM2pNypkQqg_ERieFs0Srx_gAENjiz:1vfPoR:ogxgYI6HD-yz9hVeC_ILmHt8tIi8F_SP53h2QpdxroY','2026-01-26 21:50:59.353336'),('yu8i14dzynrzvr3t14k3z0yiz238ct19','.eJxVjMsOwiAQRf-FtSE8CohL9_0GMsMMUjU0Ke3K-O_apAvd3nPOfYkE21rT1nlJE4mL0OL0uyHkB7cd0B3abZZ5busyodwVedAux5n4eT3cv4MKvX5rh8ZlcAWULhQAcAiBbShQtNHeGRuzZaZM2pNypkQqg_ERieFs0Srx_gAENjiz:1veitG:b0P-QmXUPHaoOqxysgUIcC-ajk5_h9CdQ6mYfInKYnk','2026-01-25 00:01:06.275699');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lsf_app_utilisateur`
--

DROP TABLE IF EXISTS `lsf_app_utilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lsf_app_utilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `type_utilisateur` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `niveau_langue_signes` int NOT NULL,
  `date_inscription` datetime(6) NOT NULL,
  `avatar_personnalise` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bio` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lsf_app_utilisateur`
--

LOCK TABLES `lsf_app_utilisateur` WRITE;
/*!40000 ALTER TABLE `lsf_app_utilisateur` DISABLE KEYS */;
INSERT INTO `lsf_app_utilisateur` VALUES (1,'pbkdf2_sha256$1200000$kSuAP9c2MYhD6kv2UJeQd4$bLKZVpyJWIwpKYxc0dN0KQgTMTZlYysZm8Na4rEHD2s=','2026-01-18 10:42:29.763074',1,'asskour','MOHAMED','ASSKOUR','asskourmohamed1@gmail.com',1,1,'2026-01-10 23:58:35.566603','APPRENANT',3,'2026-01-10 23:58:37.945547','avatars/1738887310578.webp','Voici mon bio'),(2,'pbkdf2_sha256$1200000$58SyIfaxILBXY20wVchsrp$UqheNkBlhl9vNCa2YC7ig5P9QevEdn7iWO9g77x7Pcg=',NULL,0,'test_sourd','','','sourd@test.com',0,1,'2026-01-11 00:09:44.054126','SOURD',5,'2026-01-11 00:09:46.687116','',''),(3,'pbkdf2_sha256$1200000$FpoaQVKnveuPOU6h26Cubp$4Fv420j6K28G89w0uGP78B0FjTXyOQVJKIFvDPaoJSc=','2026-01-11 01:04:18.213108',0,'asskour.mohamed','','','asskourmohamed1@gmail.com',0,1,'2026-01-11 01:04:16.768077','ADMIN',3,'2026-01-11 01:04:18.187995','',''),(5,'pbkdf2_sha256$1200000$loIm9Xd0Tar893Isbi2lgZ$nzELiomc52WWLuCgDVFc3l2OFPIAij77XpBoi639PCA=','2026-01-11 23:06:59.752411',0,'asskour.m','','','asskourmohamed1@gmail.com',0,1,'2026-01-11 23:06:56.189034','SOURD',1,'2026-01-11 23:06:59.695375','',''),(9,'pbkdf2_sha256$1200000$zeCLF8CxbiTABSVpwL0Eoa$Vn+4foPJSZQjLqOl6dPpErz1CQZuxBlk+c4ueO3I+4w=','2026-01-12 22:59:56.801023',0,'azertyuh','','','asskourmohamed1@gmail.com',0,1,'2026-01-12 22:59:54.853924','SOURD',1,'2026-01-12 22:59:56.749190','',''),(10,'pbkdf2_sha256$1200000$VVD0ZCO5WcLAjx0kDPTNYG$3WQXnexgNUhBw9EuhVh2uag4gVTaofxy4FkooT0Dy7c=','2026-01-13 15:21:32.572238',0,'admin','','','asskour.mohamed@ine.inpt.ac.ma',0,1,'2026-01-13 14:42:27.435510','SOURD',2,'2026-01-13 14:42:28.790664','',''),(11,'pbkdf2_sha256$1200000$CBmIqy2GkdNoWkWxC41QLb$x9wBFIXhPjLsXezu9n2k77MVNbhrK94ZTagsbDD+PKM=','2026-01-14 16:23:33.768684',0,'saul','','','askur22@gmail.com',0,1,'2026-01-13 15:22:33.275624','APPRENANT',3,'2026-01-13 15:22:35.046054','',''),(12,'pbkdf2_sha256$1200000$8bKqYlWego1MNFobycZP0X$sp37387tzCT/6AyylIU1td+bPIK0d2Jg9Y1FwlBUN+Y=','2026-01-16 08:45:16.166452',0,'hind','','','askur22@gmail.com',0,1,'2026-01-15 15:58:00.728530','ADMIN',3,'2026-01-15 15:58:02.081519','avatars/Gemini_Generated_Image_id2bb7id2bb7id2b.png','');
/*!40000 ALTER TABLE `lsf_app_utilisateur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lsf_app_utilisateur_groups`
--

DROP TABLE IF EXISTS `lsf_app_utilisateur_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lsf_app_utilisateur_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lsf_app_utilisateur_groups_utilisateur_id_group_id_086a4018_uniq` (`utilisateur_id`,`group_id`),
  KEY `lsf_app_utilisateur_groups_group_id_3303839e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `lsf_app_utilisateur__utilisateur_id_896eb51d_fk_lsf_app_u` FOREIGN KEY (`utilisateur_id`) REFERENCES `lsf_app_utilisateur` (`id`),
  CONSTRAINT `lsf_app_utilisateur_groups_group_id_3303839e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lsf_app_utilisateur_groups`
--

LOCK TABLES `lsf_app_utilisateur_groups` WRITE;
/*!40000 ALTER TABLE `lsf_app_utilisateur_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `lsf_app_utilisateur_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lsf_app_utilisateur_user_permissions`
--

DROP TABLE IF EXISTS `lsf_app_utilisateur_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lsf_app_utilisateur_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `utilisateur_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lsf_app_utilisateur_user_utilisateur_id_permissio_077175d9_uniq` (`utilisateur_id`,`permission_id`),
  KEY `lsf_app_utilisateur__permission_id_3e6ab0c5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `lsf_app_utilisateur__permission_id_3e6ab0c5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `lsf_app_utilisateur__utilisateur_id_7f1903a4_fk_lsf_app_u` FOREIGN KEY (`utilisateur_id`) REFERENCES `lsf_app_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lsf_app_utilisateur_user_permissions`
--

LOCK TABLES `lsf_app_utilisateur_user_permissions` WRITE;
/*!40000 ALTER TABLE `lsf_app_utilisateur_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `lsf_app_utilisateur_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutoriel_lecon`
--

DROP TABLE IF EXISTS `tutoriel_lecon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutoriel_lecon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titre` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordre` int NOT NULL,
  `video` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `texte_explicatif` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `duree` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `tutorial_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tutoriel_lecon_tutorial_id_2793ed6f_fk_tutoriel_tutorial_id` (`tutorial_id`),
  CONSTRAINT `tutoriel_lecon_tutorial_id_2793ed6f_fk_tutoriel_tutorial_id` FOREIGN KEY (`tutorial_id`) REFERENCES `tutoriel_tutorial` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutoriel_lecon`
--

LOCK TABLES `tutoriel_lecon` WRITE;
/*!40000 ALTER TABLE `tutoriel_lecon` DISABLE KEYS */;
INSERT INTO `tutoriel_lecon` VALUES (1,'L\'alphabet de A à Z',1,'tutoriels/videos/v3.mp4','L\'alphabet LSF utilise une main pour représenter chaque lettre. Chaque lettre a une configuration spécifique des doigts. Commençons par A, B, C...\"',90,'2026-01-17 16:55:20.333809',1),(2,'Présenter quelqu\'un',1,'tutoriels/videos/v9.mp4','Apprenez à présenter une personne, dire son nom, son métier, ses hobbies.',33,'2026-01-17 16:57:06.344268',2),(3,'Demander son chemin',1,'tutoriels/videos/v14.mp4','Vocabulaire pour demander des directions, comprendre les réponses.',32,'2026-01-17 16:57:50.822799',3);
/*!40000 ALTER TABLE `tutoriel_lecon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutoriel_progressionutilisateur`
--

DROP TABLE IF EXISTS `tutoriel_progressionutilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutoriel_progressionutilisateur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `est_completee` tinyint(1) NOT NULL,
  `date_completion` datetime(6) DEFAULT NULL,
  `score_quiz` int DEFAULT NULL,
  `temps_passe` int NOT NULL,
  `lecon_id` bigint NOT NULL,
  `utilisateur_id` bigint NOT NULL,
  `tutorial_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tutoriel_progressionutil_utilisateur_id_lecon_id_92129252_uniq` (`utilisateur_id`,`lecon_id`),
  KEY `tutoriel_progression_lecon_id_46516082_fk_tutoriel_` (`lecon_id`),
  KEY `tutoriel_progression_tutorial_id_910f4bce_fk_tutoriel_` (`tutorial_id`),
  CONSTRAINT `tutoriel_progression_lecon_id_46516082_fk_tutoriel_` FOREIGN KEY (`lecon_id`) REFERENCES `tutoriel_lecon` (`id`),
  CONSTRAINT `tutoriel_progression_tutorial_id_910f4bce_fk_tutoriel_` FOREIGN KEY (`tutorial_id`) REFERENCES `tutoriel_tutorial` (`id`),
  CONSTRAINT `tutoriel_progression_utilisateur_id_91983a7a_fk_lsf_app_u` FOREIGN KEY (`utilisateur_id`) REFERENCES `lsf_app_utilisateur` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutoriel_progressionutilisateur`
--

LOCK TABLES `tutoriel_progressionutilisateur` WRITE;
/*!40000 ALTER TABLE `tutoriel_progressionutilisateur` DISABLE KEYS */;
INSERT INTO `tutoriel_progressionutilisateur` VALUES (1,1,'2026-01-18 10:43:38.960311',100,0,1,1,1),(2,0,NULL,NULL,0,2,1,2),(3,0,NULL,NULL,0,3,1,3);
/*!40000 ALTER TABLE `tutoriel_progressionutilisateur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutoriel_question`
--

DROP TABLE IF EXISTS `tutoriel_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutoriel_question` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question_text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `type_question` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordre` int NOT NULL,
  `points` int NOT NULL,
  `explication` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `quiz_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tutoriel_question_quiz_id_2e999bfe_fk_tutoriel_quiz_id` (`quiz_id`),
  CONSTRAINT `tutoriel_question_quiz_id_2e999bfe_fk_tutoriel_quiz_id` FOREIGN KEY (`quiz_id`) REFERENCES `tutoriel_quiz` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutoriel_question`
--

LOCK TABLES `tutoriel_question` WRITE;
/*!40000 ALTER TABLE `tutoriel_question` DISABLE KEYS */;
INSERT INTO `tutoriel_question` VALUES (1,'Quelles sont les lettres qui se font avec la main ouverte ? (plusieurs réponses possibles)','CHOIX_MULTIPLE',1,1,'les lettres B, C, D, E, F, G, H, I, K, L, M, N, O, P, Q, R, U, V, W, X, Y, Z se font avec la main ouverte, tandis que A et S se font avec la main fermée.',1),(2,'La lettre \'L\' en LSF se fait avec l\'index et le pouce formant un L.','VRAI_FAUX',1,2,'Vrai ! La lettre L se fait avec l\'index pointé vers le haut et le pouce étendu à angle droit, formant la lettre L.',1);
/*!40000 ALTER TABLE `tutoriel_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutoriel_quiz`
--

DROP TABLE IF EXISTS `tutoriel_quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutoriel_quiz` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titre` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `pass_mark` int NOT NULL,
  `difficulte` int NOT NULL,
  `temps_limite` int NOT NULL,
  `lecon_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lecon_id` (`lecon_id`),
  CONSTRAINT `tutoriel_quiz_lecon_id_58018a66_fk_tutoriel_lecon_id` FOREIGN KEY (`lecon_id`) REFERENCES `tutoriel_lecon` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutoriel_quiz`
--

LOCK TABLES `tutoriel_quiz` WRITE;
/*!40000 ALTER TABLE `tutoriel_quiz` DISABLE KEYS */;
INSERT INTO `tutoriel_quiz` VALUES (1,'Quiz alphabet','Testez votre maîtrise de l\'alphabet en langue des signes',70,1,30,1);
/*!40000 ALTER TABLE `tutoriel_quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutoriel_reponse`
--

DROP TABLE IF EXISTS `tutoriel_reponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutoriel_reponse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reponse_text` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `est_correcte` tinyint(1) NOT NULL,
  `question_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tutoriel_reponse_question_id_0eb0a98f_fk_tutoriel_question_id` (`question_id`),
  CONSTRAINT `tutoriel_reponse_question_id_0eb0a98f_fk_tutoriel_question_id` FOREIGN KEY (`question_id`) REFERENCES `tutoriel_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutoriel_reponse`
--

LOCK TABLES `tutoriel_reponse` WRITE;
/*!40000 ALTER TABLE `tutoriel_reponse` DISABLE KEYS */;
INSERT INTO `tutoriel_reponse` VALUES (1,'A',0,1),(2,'S',0,1),(3,'B',1,1),(4,'Vrai',1,2),(5,'Faux',0,2);
/*!40000 ALTER TABLE `tutoriel_reponse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutoriel_tutorial`
--

DROP TABLE IF EXISTS `tutoriel_tutorial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutoriel_tutorial` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titre` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `niveau` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordre` int NOT NULL,
  `est_actif` tinyint(1) NOT NULL,
  `difficulte` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `image_couverture` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutoriel_tutorial`
--

LOCK TABLES `tutoriel_tutorial` WRITE;
/*!40000 ALTER TABLE `tutoriel_tutorial` DISABLE KEYS */;
INSERT INTO `tutoriel_tutorial` VALUES (1,'Les bases de la Langue des Signes','Apprenez les fondements de la Langue des Signes : alphabet, chiffres et signes essentiels pour communiquer au quotidien.','DEBUTANT',1,1,1,'2026-01-17 16:46:37.025153','2026-01-17 16:46:37.025153','tutoriels/couvertures/langue-signes-mots-1024x1024.jpg'),(2,'Communication quotidienne','Maîtrisez les expressions courantes, la syntaxe de base et les conversations simples en langue des signes.','INTERMEDIAIRE',1,1,2,'2026-01-17 16:49:13.246990','2026-01-17 16:49:13.247127','tutoriels/couvertures/5f9c43340b4c0_signer.png'),(3,'Language des signes professionnelle et culturelle','Perfectionnez votre Language des signes avec du vocabulaire spécialisé, l\'expression des émotions et la culture sourde.','AVANCE',1,1,1,'2026-01-17 16:53:40.710971','2026-01-17 16:53:40.711505','tutoriels/couvertures/5aabbcfd277a157402ec80f2cf7146b2.jpg');
/*!40000 ALTER TABLE `tutoriel_tutorial` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-18 12:09:16
