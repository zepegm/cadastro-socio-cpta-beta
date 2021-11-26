-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cadastro_socioeconomico
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `senha` varchar(32) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beneficio`
--

DROP TABLE IF EXISTS `beneficio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `beneficio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `beneficio` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beneficio`
--

LOCK TABLES `beneficio` WRITE;
/*!40000 ALTER TABLE `beneficio` DISABLE KEYS */;
INSERT INTO `beneficio` VALUES (1,'PBF'),(2,'BPC'),(3,'Renda Cidadã'),(4,'Ação Jovem'),(5,'Aposentadoria'),(6,'Pensão');
/*!40000 ALTER TABLE `beneficio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidadao`
--

DROP TABLE IF EXISTS `cidadao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidadao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chefe_familia` tinyint(1) NOT NULL DEFAULT '0',
  `nome` varchar(255) NOT NULL,
  `rg` varchar(15) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `nis` varchar(45) DEFAULT NULL,
  `sus` tinyint(1) DEFAULT NULL,
  `data_nascimento` varchar(10) NOT NULL,
  `cidade_natal` varchar(255) DEFAULT NULL,
  `uf_natal` varchar(2) DEFAULT NULL,
  `vinculo_familiar` varchar(45) DEFAULT NULL,
  `profissao` varchar(255) DEFAULT NULL,
  `ocupacao_formal` tinyint(1) DEFAULT NULL,
  `renda_familiar_sm` tinyint(4) DEFAULT NULL,
  `numero_filhos` tinyint(4) DEFAULT NULL,
  `participacao_social` tinyint(1) DEFAULT NULL,
  `desc_participacao_social` varchar(255) DEFAULT NULL,
  `obs_saude` varchar(255) DEFAULT NULL,
  `conhece_cidade` tinyint(1) DEFAULT NULL,
  `locais_nao_visitados` tinytext,
  `id_chefe_familia` int(11) DEFAULT NULL,
  `id_situacao_habitacional` int(11) DEFAULT NULL,
  `covid` int(11) DEFAULT NULL,
  `talentos_habilidades` tinytext,
  `raca` enum('B','P','PD','A','I') DEFAULT NULL COMMENT 'B = Branco\nP = Preto\nPD = Pardo\nA = Amarelo\nI = Indio',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  `id_estado_civil` int(11) NOT NULL,
  `id_escolaridade` int(11) NOT NULL,
  `id_religiao` int(11) NOT NULL,
  `observacoes` tinytext,
  `entrevistador` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cidadao_cidadao1_idx` (`id_chefe_familia`),
  KEY `fk_cidadao_situacao_habitacional1_idx` (`id_situacao_habitacional`),
  KEY `fk_cidadao_covid1_idx` (`covid`),
  KEY `fk_cidadao_estado_civil1_idx` (`id_estado_civil`),
  KEY `fk_cidadao_escolaridade1_idx` (`id_escolaridade`),
  KEY `fk_cidadao_religiao1_idx` (`id_religiao`),
  KEY `fk_cidadao_accounts1_idx` (`entrevistador`),
  CONSTRAINT `fk_cidadao_accounts1` FOREIGN KEY (`entrevistador`) REFERENCES `accounts` (`id`),
  CONSTRAINT `fk_cidadao_cidadao1` FOREIGN KEY (`id_chefe_familia`) REFERENCES `cidadao` (`id`),
  CONSTRAINT `fk_cidadao_covid1` FOREIGN KEY (`covid`) REFERENCES `covid` (`id`),
  CONSTRAINT `fk_cidadao_escolaridade1` FOREIGN KEY (`id_escolaridade`) REFERENCES `escolaridade` (`id`),
  CONSTRAINT `fk_cidadao_estado_civil1` FOREIGN KEY (`id_estado_civil`) REFERENCES `estado_civil` (`id`),
  CONSTRAINT `fk_cidadao_religiao1` FOREIGN KEY (`id_religiao`) REFERENCES `religiao` (`id`),
  CONSTRAINT `fk_cidadao_situacao_habitacional1` FOREIGN KEY (`id_situacao_habitacional`) REFERENCES `situacao_habitacional` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidadao`
--

LOCK TABLES `cidadao` WRITE;
/*!40000 ALTER TABLE `cidadao` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidadao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidadaoxbeneficios`
--

DROP TABLE IF EXISTS `cidadaoxbeneficios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidadaoxbeneficios` (
  `id_cidadao` int(11) NOT NULL,
  `id_beneficio` int(11) NOT NULL,
  PRIMARY KEY (`id_cidadao`,`id_beneficio`),
  KEY `fk_cidadao_has_beneficios_beneficios1_idx` (`id_beneficio`),
  KEY `fk_cidadao_has_beneficios_cidadao1_idx` (`id_cidadao`),
  CONSTRAINT `fk_cidadao_has_beneficios_beneficios1` FOREIGN KEY (`id_beneficio`) REFERENCES `beneficio` (`id`),
  CONSTRAINT `fk_cidadao_has_beneficios_cidadao1` FOREIGN KEY (`id_cidadao`) REFERENCES `cidadao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidadaoxbeneficios`
--

LOCK TABLES `cidadaoxbeneficios` WRITE;
/*!40000 ALTER TABLE `cidadaoxbeneficios` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidadaoxbeneficios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidadaoxcultura_lazer`
--

DROP TABLE IF EXISTS `cidadaoxcultura_lazer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidadaoxcultura_lazer` (
  `cidadao_id` int(11) NOT NULL,
  `cultura_lazer_id` int(11) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cidadao_id`,`cultura_lazer_id`),
  KEY `fk_cidadao_has_cultura_lazer_cultura_lazer1_idx` (`cultura_lazer_id`),
  KEY `fk_cidadao_has_cultura_lazer_cidadao1_idx` (`cidadao_id`),
  CONSTRAINT `fk_cidadao_has_cultura_lazer_cidadao1` FOREIGN KEY (`cidadao_id`) REFERENCES `cidadao` (`id`),
  CONSTRAINT `fk_cidadao_has_cultura_lazer_cultura_lazer1` FOREIGN KEY (`cultura_lazer_id`) REFERENCES `cultura_lazer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidadaoxcultura_lazer`
--

LOCK TABLES `cidadaoxcultura_lazer` WRITE;
/*!40000 ALTER TABLE `cidadaoxcultura_lazer` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidadaoxcultura_lazer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidadaoxinformacoes_adicionais`
--

DROP TABLE IF EXISTS `cidadaoxinformacoes_adicionais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidadaoxinformacoes_adicionais` (
  `id_cidadao` int(11) NOT NULL,
  `id_informacoes_adicionais` int(11) NOT NULL,
  PRIMARY KEY (`id_cidadao`,`id_informacoes_adicionais`),
  KEY `fk_cidadao_has_informacoes_adicionais_informacoes_adicionai_idx` (`id_informacoes_adicionais`),
  KEY `fk_cidadao_has_informacoes_adicionais_cidadao1_idx` (`id_cidadao`),
  CONSTRAINT `fk_cidadao_has_informacoes_adicionais_cidadao1` FOREIGN KEY (`id_cidadao`) REFERENCES `cidadao` (`id`),
  CONSTRAINT `fk_cidadao_has_informacoes_adicionais_informacoes_adicionais1` FOREIGN KEY (`id_informacoes_adicionais`) REFERENCES `informacoes_adicionais` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidadaoxinformacoes_adicionais`
--

LOCK TABLES `cidadaoxinformacoes_adicionais` WRITE;
/*!40000 ALTER TABLE `cidadaoxinformacoes_adicionais` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidadaoxinformacoes_adicionais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidadaoxsaude`
--

DROP TABLE IF EXISTS `cidadaoxsaude`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidadaoxsaude` (
  `cidadao_id` int(11) NOT NULL,
  `saude_id` int(11) NOT NULL,
  PRIMARY KEY (`cidadao_id`,`saude_id`),
  KEY `fk_cidadao_has_saude_saude1_idx` (`saude_id`),
  KEY `fk_cidadao_has_saude_cidadao1_idx` (`cidadao_id`),
  CONSTRAINT `fk_cidadao_has_saude_cidadao1` FOREIGN KEY (`cidadao_id`) REFERENCES `cidadao` (`id`),
  CONSTRAINT `fk_cidadao_has_saude_saude1` FOREIGN KEY (`saude_id`) REFERENCES `saude` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidadaoxsaude`
--

LOCK TABLES `cidadaoxsaude` WRITE;
/*!40000 ALTER TABLE `cidadaoxsaude` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidadaoxsaude` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidadaoxservico_saude`
--

DROP TABLE IF EXISTS `cidadaoxservico_saude`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cidadaoxservico_saude` (
  `id_cidadao` int(11) NOT NULL,
  `id_servico_saude` int(11) NOT NULL,
  PRIMARY KEY (`id_cidadao`,`id_servico_saude`),
  KEY `fk_cidadao_has_servico_saude_servico_saude1_idx` (`id_servico_saude`),
  KEY `fk_cidadao_has_servico_saude_cidadao1_idx` (`id_cidadao`),
  CONSTRAINT `fk_cidadao_has_servico_saude_cidadao1` FOREIGN KEY (`id_cidadao`) REFERENCES `cidadao` (`id`),
  CONSTRAINT `fk_cidadao_has_servico_saude_servico_saude1` FOREIGN KEY (`id_servico_saude`) REFERENCES `servico_saude` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidadaoxservico_saude`
--

LOCK TABLES `cidadaoxservico_saude` WRITE;
/*!40000 ALTER TABLE `cidadaoxservico_saude` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidadaoxservico_saude` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `covid`
--

DROP TABLE IF EXISTS `covid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `covid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `infeccao_familia` tinyint(1) NOT NULL DEFAULT '0',
  `quantidade_pessoas` tinyint(4) NOT NULL DEFAULT '0',
  `familia_afetada` tinyint(1) NOT NULL DEFAULT '0',
  `afetacao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covid`
--

LOCK TABLES `covid` WRITE;
/*!40000 ALTER TABLE `covid` DISABLE KEYS */;
/*!40000 ALTER TABLE `covid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cultura_lazer`
--

DROP TABLE IF EXISTS `cultura_lazer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cultura_lazer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cultura_lazer`
--

LOCK TABLES `cultura_lazer` WRITE;
/*!40000 ALTER TABLE `cultura_lazer` DISABLE KEYS */;
INSERT INTO `cultura_lazer` VALUES (1,'Associação de Bairro'),(2,'Quadra'),(3,'Praça/Parque'),(4,'Igreja'),(5,'Outros');
/*!40000 ALTER TABLE `cultura_lazer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `escolaridade`
--

DROP TABLE IF EXISTS `escolaridade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `escolaridade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escolaridade`
--

LOCK TABLES `escolaridade` WRITE;
/*!40000 ALTER TABLE `escolaridade` DISABLE KEYS */;
INSERT INTO `escolaridade` VALUES (1,'Analfabeto'),(2,'Ensino Fundamental'),(3,'Ensino Médio'),(4,'Ensino Superior');
/*!40000 ALTER TABLE `escolaridade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_civil`
--

DROP TABLE IF EXISTS `estado_civil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado_civil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_civil`
--

LOCK TABLES `estado_civil` WRITE;
/*!40000 ALTER TABLE `estado_civil` DISABLE KEYS */;
INSERT INTO `estado_civil` VALUES (1,'Casado'),(2,'Solteiro'),(3,'Amasiado'),(4,'Divorciado'),(5,'Viúvo');
/*!40000 ALTER TABLE `estado_civil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `informacoes_adicionais`
--

DROP TABLE IF EXISTS `informacoes_adicionais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `informacoes_adicionais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `luto_recente` tinyint(1) DEFAULT NULL,
  `falecido` varchar(45) DEFAULT NULL,
  `motivo_falecimento` varchar(255) DEFAULT NULL,
  `amse_psc_la` tinyint(1) DEFAULT NULL,
  `qtde_amse_psc_la` tinyint(4) DEFAULT NULL,
  `amse_fc` tinyint(1) DEFAULT NULL,
  `qtde_amse_fc` tinyint(4) DEFAULT NULL,
  `sistema_prisional` tinyint(1) DEFAULT NULL,
  `quem_sistema_prisional` varchar(255) DEFAULT NULL,
  `sistema_acolhimento` tinyint(1) DEFAULT NULL,
  `sistema_acolhimento_c_i` enum('C','I') DEFAULT NULL,
  `onde_sistema_acolhimento` varchar(255) DEFAULT NULL,
  `situacao_violencia` tinyint(1) DEFAULT NULL,
  `violencia_domestica` tinyint(1) DEFAULT NULL,
  `violencia_trabalho` tinyint(1) DEFAULT NULL,
  `violencia_rua` tinyint(1) DEFAULT NULL,
  `violencia_escola` tinyint(1) DEFAULT NULL,
  `violencia_fisica` tinyint(1) DEFAULT NULL,
  `violencia_verbal` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informacoes_adicionais`
--

LOCK TABLES `informacoes_adicionais` WRITE;
/*!40000 ALTER TABLE `informacoes_adicionais` DISABLE KEYS */;
/*!40000 ALTER TABLE `informacoes_adicionais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `religiao`
--

DROP TABLE IF EXISTS `religiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `religiao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `religiao` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `religiao`
--

LOCK TABLES `religiao` WRITE;
/*!40000 ALTER TABLE `religiao` DISABLE KEYS */;
INSERT INTO `religiao` VALUES (1,'Católica'),(2,'Evangélica'),(3,'Espírita'),(4,'Religiões de Matrizes Africanas');
/*!40000 ALTER TABLE `religiao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retirada_cesta`
--

DROP TABLE IF EXISTS `retirada_cesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retirada_cesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_retirada` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_cidadao` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_retirada_cesta_cidadao1_idx` (`id_cidadao`),
  CONSTRAINT `fk_retirada_cesta_cidadao1` FOREIGN KEY (`id_cidadao`) REFERENCES `cidadao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retirada_cesta`
--

LOCK TABLES `retirada_cesta` WRITE;
/*!40000 ALTER TABLE `retirada_cesta` DISABLE KEYS */;
/*!40000 ALTER TABLE `retirada_cesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `saude`
--

DROP TABLE IF EXISTS `saude`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `saude` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deficiencia_fisica` tinyint(1) NOT NULL DEFAULT '0',
  `saude_mental` tinyint(1) NOT NULL DEFAULT '0',
  `hiv_aids` tinyint(1) NOT NULL DEFAULT '0',
  `dependencia_quimica` tinyint(1) NOT NULL DEFAULT '0',
  `cancer` tinyint(1) NOT NULL DEFAULT '0',
  `diabetes` tinyint(1) NOT NULL DEFAULT '0',
  `hipertensao` tinyint(1) NOT NULL DEFAULT '0',
  `obesidade` tinyint(1) NOT NULL DEFAULT '0',
  `gestante` tinyint(1) NOT NULL DEFAULT '0',
  `outros` tinyint(1) NOT NULL DEFAULT '0',
  `descricao_outros` varchar(255) DEFAULT NULL,
  `dengue` tinyint(1) NOT NULL,
  `vezes_dengue` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `saude`
--

LOCK TABLES `saude` WRITE;
/*!40000 ALTER TABLE `saude` DISABLE KEYS */;
/*!40000 ALTER TABLE `saude` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servico_saude`
--

DROP TABLE IF EXISTS `servico_saude`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servico_saude` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `servico` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servico_saude`
--

LOCK TABLES `servico_saude` WRITE;
/*!40000 ALTER TABLE `servico_saude` DISABLE KEYS */;
INSERT INTO `servico_saude` VALUES (1,'UBS'),(2,'ESF'),(3,'CAPS'),(4,'AME'),(5,'PRAD');
/*!40000 ALTER TABLE `servico_saude` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `situacao_habitacional`
--

DROP TABLE IF EXISTS `situacao_habitacional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `situacao_habitacional` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_imovel` int(11) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `agua` tinyint(1) DEFAULT NULL,
  `luz` tinyint(1) DEFAULT NULL,
  `esgoto` tinyint(1) DEFAULT NULL,
  `coleta_lixo` tinyint(1) DEFAULT NULL,
  `entrega_correios` tinyint(1) DEFAULT NULL,
  `entrega_comercio` tinyint(1) DEFAULT NULL,
  `area_municipio` enum('U','R') NOT NULL COMMENT 'U = Urbano\nR = Rural',
  `num_comodos` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`,`tipo_imovel`),
  KEY `fk_situacao_habitacional_tipo_imovel1_idx` (`tipo_imovel`),
  CONSTRAINT `fk_situacao_habitacional_tipo_imovel1` FOREIGN KEY (`tipo_imovel`) REFERENCES `tipo_imovel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `situacao_habitacional`
--

LOCK TABLES `situacao_habitacional` WRITE;
/*!40000 ALTER TABLE `situacao_habitacional` DISABLE KEYS */;
/*!40000 ALTER TABLE `situacao_habitacional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `situacao_habitacionalxtransporte`
--

DROP TABLE IF EXISTS `situacao_habitacionalxtransporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `situacao_habitacionalxtransporte` (
  `situacao_habitacional_id` int(11) NOT NULL,
  `transporte_id` int(11) NOT NULL,
  PRIMARY KEY (`situacao_habitacional_id`,`transporte_id`),
  KEY `fk_situacao_habitacional_has_transporte_transporte1_idx` (`transporte_id`),
  KEY `fk_situacao_habitacional_has_transporte_situacao_habitacion_idx` (`situacao_habitacional_id`),
  CONSTRAINT `fk_situacao_habitacional_has_transporte_situacao_habitacional` FOREIGN KEY (`situacao_habitacional_id`) REFERENCES `situacao_habitacional` (`id`),
  CONSTRAINT `fk_situacao_habitacional_has_transporte_transporte1` FOREIGN KEY (`transporte_id`) REFERENCES `transporte` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `situacao_habitacionalxtransporte`
--

LOCK TABLES `situacao_habitacionalxtransporte` WRITE;
/*!40000 ALTER TABLE `situacao_habitacionalxtransporte` DISABLE KEYS */;
/*!40000 ALTER TABLE `situacao_habitacionalxtransporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_imovel`
--

DROP TABLE IF EXISTS `tipo_imovel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_imovel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_imovel`
--

LOCK TABLES `tipo_imovel` WRITE;
/*!40000 ALTER TABLE `tipo_imovel` DISABLE KEYS */;
INSERT INTO `tipo_imovel` VALUES (1,'Próprio'),(2,'Cedido'),(3,'Alugado/financiado');
/*!40000 ALTER TABLE `tipo_imovel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transporte`
--

DROP TABLE IF EXISTS `transporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transporte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  `necessario` tinyint(1) NOT NULL DEFAULT '0',
  `disponibilidade` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transporte`
--

LOCK TABLES `transporte` WRITE;
/*!40000 ALTER TABLE `transporte` DISABLE KEYS */;
/*!40000 ALTER TABLE `transporte` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-15  2:13:33
