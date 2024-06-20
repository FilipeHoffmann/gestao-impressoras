-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`contrato` (
  `id_contrato` INT NOT NULL AUTO_INCREMENT,
  `data_inicial` DATE NULL DEFAULT NULL,
  `data_final` DATE NULL DEFAULT NULL,
  `data_final_atual` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id_contrato`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`aditivo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aditivo` (
  `id_aditivo` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `data_inicial` DATE NULL DEFAULT NULL,
  `data_final` DATE NULL DEFAULT NULL,
  `situacao` VARCHAR(50) NULL DEFAULT NULL,
  `id_contrato` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_aditivo`),
  INDEX `FK_aditivo_contrato_idx` (`id_contrato` ASC) VISIBLE,
  CONSTRAINT `FK_aditivo_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `mydb`.`contrato` (`id_contrato`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`produto` (
  `id_produto` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(50) NULL DEFAULT NULL,
  `franquia_pb` INT NULL DEFAULT NULL,
  `franquia_color` INT NULL DEFAULT NULL,
  `tipo` VARCHAR(50) NULL DEFAULT NULL,
  `copia_locacao` INT NULL DEFAULT NULL,
  `color` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`excedente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`excedente` (
  `id_excedente` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NULL DEFAULT NULL,
  `saldo` FLOAT NULL DEFAULT NULL,
  `valor_atual` FLOAT NULL DEFAULT NULL,
  `id_produto` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_excedente`),
  INDEX `FK_excedente_produto_idx` (`id_produto` ASC) VISIBLE,
  CONSTRAINT `FK_excedente_produto`
    FOREIGN KEY (`id_produto`)
    REFERENCES `mydb`.`produto` (`id_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`aditivo_excedente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aditivo_excedente` (
  `id_aditivo_excedentes` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `valor` FLOAT NULL DEFAULT NULL,
  `id_aditivo` INT NULL DEFAULT NULL,
  `id_excedente` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_aditivo_excedentes`),
  INDEX `FK_aditivo_excedente_idx` (`id_aditivo` ASC) VISIBLE,
  INDEX `FK_aditivo_excedente_excedente_idx` (`id_excedente` ASC) VISIBLE,
  CONSTRAINT `FK_aditivo_excedente_aditivo`
    FOREIGN KEY (`id_aditivo`)
    REFERENCES `mydb`.`aditivo` (`id_aditivo`),
  CONSTRAINT `FK_aditivo_excedente_excedente`
    FOREIGN KEY (`id_excedente`)
    REFERENCES `mydb`.`excedente` (`id_excedente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`secretaria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`secretaria` (
  `id_secretaria` INT NOT NULL AUTO_INCREMENT,
  `secretaria` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id_secretaria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`item` (
  `id_item` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `saldo` FLOAT NULL DEFAULT NULL,
  `valor_atual` FLOAT NULL DEFAULT NULL,
  `id_contrato` INT NULL DEFAULT NULL,
  `id_produto` INT NULL DEFAULT NULL,
  `id_secretaria` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_item`),
  INDEX `FK_item_contrato_idx` (`id_contrato` ASC) VISIBLE,
  INDEX `FK_item_produto_idx` (`id_produto` ASC) VISIBLE,
  INDEX `FK_item_secretaria_idx` (`id_secretaria` ASC) VISIBLE,
  CONSTRAINT `FK_item_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `mydb`.`contrato` (`id_contrato`),
  CONSTRAINT `FK_item_produto`
    FOREIGN KEY (`id_produto`)
    REFERENCES `mydb`.`produto` (`id_produto`),
  CONSTRAINT `FK_item_secretaria`
    FOREIGN KEY (`id_secretaria`)
    REFERENCES `mydb`.`secretaria` (`id_secretaria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`aditivo_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aditivo_item` (
  `id_aditivo_item` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `valor` FLOAT NULL DEFAULT NULL,
  `id_item` INT NULL DEFAULT NULL,
  `id_aditivo` INT NULL DEFAULT NULL,
  INDEX `FK_aditivo_item_aditvo_idx` (`id_aditivo` ASC) VISIBLE,
  INDEX `FK_aditivo_item_item_idx` (`id_item` ASC) VISIBLE,
  PRIMARY KEY (`id_aditivo_item`),
  CONSTRAINT `FK_aditivo_item_aditvo`
    FOREIGN KEY (`id_aditivo`)
    REFERENCES `mydb`.`aditivo` (`id_aditivo`),
  CONSTRAINT `FK_aditivo_item_item`
    FOREIGN KEY (`id_item`)
    REFERENCES `mydb`.`item` (`id_item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`impressora`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`impressora` (
  `id_impressora` INT NOT NULL AUTO_INCREMENT,
  `marca_modelo` VARCHAR(50) NULL,
  PRIMARY KEY (`id_impressora`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`contador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`contador` (
  `id_contador` INT NOT NULL AUTO_INCREMENT,
  `cont_pb` INT NULL,
  `cont_color` INT NULL,
  `data` DATE NULL,
  `id_impressora` INT NULL,
  PRIMARY KEY (`id_contador`),
  INDEX `FK_contador_impressora_idx` (`id_impressora` ASC) VISIBLE,
  CONSTRAINT `FK_contador_impressora`
    FOREIGN KEY (`id_impressora`)
    REFERENCES `mydb`.`impressora` (`id_impressora`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`instalacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`instalacao` (
  `id_instalacao` INT NOT NULL AUTO_INCREMENT,
  `local_instalacao` VARCHAR(50) NULL,
  `endereco` VARCHAR(50) NULL,
  `transformador` TINYINT NULL,
  `responsavel` VARCHAR(100) NULL,
  `ip` VARCHAR(50) NULL,
  `data_instalacao` DATE NULL,
  `cont_instalacao` INT NULL,
  `data_retirada` DATE NULL,
  `cont_retirada` INT NULL,
  `id_item` INT NULL,
  `id_impressora` INT NULL,
  PRIMARY KEY (`id_instalacao`),
  INDEX `FK_instalacao_impressora_idx` (`id_impressora` ASC) VISIBLE,
  INDEX `FK_instalacao_item_idx` (`id_item` ASC) VISIBLE,
  CONSTRAINT `FK_instalacao_item`
    FOREIGN KEY (`id_item`)
    REFERENCES `mydb`.`item` (`id_item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_instalacao_impressora`
    FOREIGN KEY (`id_impressora`)
    REFERENCES `mydb`.`impressora` (`id_impressora`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`empenho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`empenho` (
  `id_empenho` INT NOT NULL AUTO_INCREMENT,
  `empenho` VARCHAR(50) NULL,
  `descricao` VARCHAR(100) NULL,
  `id_secretaria` INT NULL,
  PRIMARY KEY (`id_empenho`),
  INDEX `FK_empenho_secretaria_idx` (`id_secretaria` ASC) VISIBLE,
  CONSTRAINT `FK_empenho_secretaria`
    FOREIGN KEY (`id_secretaria`)
    REFERENCES `mydb`.`secretaria` (`id_secretaria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`faturamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`faturamento` (
  `id_faturamento` INT NOT NULL AUTO_INCREMENT,
  `competencia` VARCHAR(50) NULL,
  `data_inicial` DATE NULL,
  `data_final` DATE NULL,
  `situacao` VARCHAR(50) NULL,
  PRIMARY KEY (`id_faturamento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`empenho_faturamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`empenho_faturamento` (
  `id_empenho_faturamento` INT NOT NULL AUTO_INCREMENT,
  `id_empenho` INT NULL,
  `id_faturamento` INT NULL,
  PRIMARY KEY (`id_empenho_faturamento`),
  INDEX `FK_empenho_faturamento_empenho_idx` (`id_empenho` ASC) VISIBLE,
  INDEX `FK_empenho_faturamento_faturamento_idx` (`id_faturamento` ASC) VISIBLE,
  CONSTRAINT `FK_empenho_faturamento_empenho`
    FOREIGN KEY (`id_empenho`)
    REFERENCES `mydb`.`empenho` (`id_empenho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_empenho_faturamento_faturamento`
    FOREIGN KEY (`id_faturamento`)
    REFERENCES `mydb`.`faturamento` (`id_faturamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`empenho_excedente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`empenho_excedente` (
  `id_empenho_excedente` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NULL,
  `saldo` INT NULL,
  `valor` FLOAT NULL,
  `id_empenho` INT NULL,
  `id_excedente` INT NULL,
  PRIMARY KEY (`id_empenho_excedente`),
  INDEX `FK_empenho_excedente_empenho_idx` (`id_empenho` ASC) VISIBLE,
  INDEX `FK_empenho_excedente_excedente_idx` (`id_excedente` ASC) VISIBLE,
  CONSTRAINT `FK_empenho_excedente_empenho`
    FOREIGN KEY (`id_empenho`)
    REFERENCES `mydb`.`empenho` (`id_empenho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_empenho_excedente_excedente`
    FOREIGN KEY (`id_excedente`)
    REFERENCES `mydb`.`excedente` (`id_excedente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`empenho_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`empenho_item` (
  `id_empenho_item` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NULL,
  `saldo` FLOAT NULL,
  `valor` FLOAT NULL,
  `id_empenho` INT NULL,
  `id_item` INT NULL,
  `id_empenho_excedente` INT NULL,
  PRIMARY KEY (`id_empenho_item`),
  INDEX `FK_empenho_item_item_idx` (`id_item` ASC) VISIBLE,
  INDEX `FK_empenho_item_empenho_idx` (`id_empenho` ASC) VISIBLE,
  INDEX `FK_empenho_item_empenho_excedente_idx` (`id_empenho_excedente` ASC) VISIBLE,
  CONSTRAINT `FK_empenho_item_empenho_excedente`
    FOREIGN KEY (`id_empenho_excedente`)
    REFERENCES `mydb`.`empenho_excedente` (`id_empenho_excedente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_empenho_item_item`
    FOREIGN KEY (`id_item`)
    REFERENCES `mydb`.`item` (`id_item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_empenho_item_empenho`
    FOREIGN KEY (`id_empenho`)
    REFERENCES `mydb`.`empenho` (`id_empenho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`faturamento_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`faturamento_item` (
  `id_faturamento_item` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NULL,
  `valor` FLOAT NULL,
  `id_faturamento` INT NULL,
  `id_empenho_item` INT NULL,
  PRIMARY KEY (`id_faturamento_item`),
  INDEX `FK_faturamento_item_faturamento_idx` (`id_faturamento` ASC) VISIBLE,
  INDEX `FK_faturamento_item_empenho_item_idx` (`id_empenho_item` ASC) VISIBLE,
  CONSTRAINT `FK_faturamento_item_faturamento`
    FOREIGN KEY (`id_faturamento`)
    REFERENCES `mydb`.`faturamento` (`id_faturamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_faturamento_item_empenho_item`
    FOREIGN KEY (`id_empenho_item`)
    REFERENCES `mydb`.`empenho_item` (`id_empenho_item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`faturamento_excedente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`faturamento_excedente` (
  `id_faturamento_excedente` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NULL,
  `valor` FLOAT NULL,
  `id_faturamento` INT NULL,
  `id_empenho_excedente` INT NULL,
  PRIMARY KEY (`id_faturamento_excedente`),
  INDEX `FK_faturamento_excedente_faturamento_idx` (`id_faturamento` ASC) VISIBLE,
  INDEX `FK_faturamento_excedente_empenho_excedente_idx` (`id_empenho_excedente` ASC) VISIBLE,
  CONSTRAINT `FK_faturamento_excedente_faturamento`
    FOREIGN KEY (`id_faturamento`)
    REFERENCES `mydb`.`faturamento` (`id_faturamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_faturamento_excedente_empenho_excedente`
    FOREIGN KEY (`id_empenho_excedente`)
    REFERENCES `mydb`.`empenho_excedente` (`id_empenho_excedente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
