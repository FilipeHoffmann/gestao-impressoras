SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gestao-impressoras
-- -----------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `gestao-impressoras` DEFAULT CHARACTER SET utf8mb3 ;
USE `gestao-impressoras` ;

-- -----------------------------------------------------
-- Table `gestao-impressoras`.`contratos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`contratos` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`contratos` (
  `id_contrato` INT NOT NULL,
  `data_inicial` DATE NULL DEFAULT NULL,
  `data_final` DATE NULL DEFAULT NULL,
  `data_final_atual` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id_contrato`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`aditivos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`aditivos` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`aditivos` (
  `id_aditivo` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `data_inicial` DATE NULL DEFAULT NULL,
  `data_final` DATE NULL DEFAULT NULL,
  `situacao` VARCHAR(50) NULL DEFAULT NULL,
  `id_contrato` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_aditivo`),
  INDEX `FK_aditivos_contratos_idx` (`id_contrato` ASC) VISIBLE,
  CONSTRAINT `FK_aditivos_contratos`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `gestao-impressoras`.`contratos` (`id_contrato`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`produtos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`produtos` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`produtos` (
  `id_produto` INT NOT NULL,
  `descricao` VARCHAR(50) NULL DEFAULT NULL,
  `franquia_pb` INT NULL DEFAULT NULL,
  `franquia_color` INT NULL DEFAULT NULL,
  `tipo` VARCHAR(50) NULL DEFAULT NULL,
  `copia_locacao` VARCHAR(50) NULL DEFAULT NULL,
  `color` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`excedentes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`excedentes` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`excedentes` (
  `id_excedente` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NULL DEFAULT NULL,
  `saldo` FLOAT NULL DEFAULT NULL,
  `valor_atual` FLOAT NULL DEFAULT NULL,
  `id_produto` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_excedente`),
  INDEX `FK_excedentes_produtos_idx` (`id_produto` ASC) VISIBLE,
  CONSTRAINT `FK_excedentes_produtos`
    FOREIGN KEY (`id_produto`)
    REFERENCES `gestao-impressoras`.`produtos` (`id_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`aditivos_excedentes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`aditivos_excedentes` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`aditivos_excedentes` (
  `id_aditivo_excedente` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `valor` FLOAT NULL DEFAULT NULL,
  `id_aditivo` INT NULL DEFAULT NULL,
  `id_excedente` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_aditivo_excedente`),
  INDEX `FK_aditivos_excedentes_aditivos_idx` (`id_aditivo` ASC) VISIBLE,
  INDEX `FK_aditivos_excedentes_excedentes_idx` (`id_excedente` ASC) VISIBLE,
  CONSTRAINT `FK_aditivos_excedentes_aditivos`
    FOREIGN KEY (`id_aditivo`)
    REFERENCES `gestao-impressoras`.`aditivos` (`id_aditivo`),
  CONSTRAINT `FK_aditivos_excedentes_excedentes`
    FOREIGN KEY (`id_excedente`)
    REFERENCES `gestao-impressoras`.`excedentes` (`id_excedente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`secretarias`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`secretarias` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`secretarias` (
  `id_secretaria` INT NOT NULL AUTO_INCREMENT,
  `secretaria` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id_secretaria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`itens`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`itens` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`itens` (
  `id_item` INT NOT NULL,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `saldo` FLOAT NULL DEFAULT NULL,
  `valor_atual` FLOAT NULL DEFAULT NULL,
  `id_contrato` INT NULL DEFAULT NULL,
  `id_produto` INT NULL DEFAULT NULL,
  `id_secretaria` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_item`),
  INDEX `FK_itens_contratos_idx` (`id_contrato` ASC) VISIBLE,
  INDEX `FK_itens_produtos_idx` (`id_produto` ASC) VISIBLE,
  INDEX `FK_itens_secretarias_idx` (`id_secretaria` ASC) VISIBLE,
  CONSTRAINT `FK_itens_contratos`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `gestao-impressoras`.`contratos` (`id_contrato`),
  CONSTRAINT `FK_itens_produtos`
    FOREIGN KEY (`id_produto`)
    REFERENCES `gestao-impressoras`.`produtos` (`id_produto`),
  CONSTRAINT `FK_itens_secretarias`
    FOREIGN KEY (`id_secretaria`)
    REFERENCES `gestao-impressoras`.`secretarias` (`id_secretaria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `gestao-impressoras`.`aditivos_itens`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gestao-impressoras`.`aditivos_itens` ;

CREATE TABLE IF NOT EXISTS `gestao-impressoras`.`aditivos_itens` (
  `id_aditivo_item` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(500) NULL DEFAULT NULL,
  `quantidade` INT NULL DEFAULT NULL,
  `valor` FLOAT NULL DEFAULT NULL,
  `id_item` INT NULL DEFAULT NULL,
  `id_aditivo` INT NULL DEFAULT NULL,
  `id_secretaria` INT NULL,
  INDEX `FK_aditivos_itens_aditivos_idx` (`id_aditivo` ASC) VISIBLE,
  INDEX `FK_aditivos_itens_itens_idx` (`id_item` ASC) VISIBLE,
  PRIMARY KEY (`id_aditivo_item`),
  INDEX `FK_aditivos_itens_secretarias_idx` (`id_secretaria` ASC) VISIBLE,
  CONSTRAINT `FK_aditivos_itens_aditivos`
    FOREIGN KEY (`id_aditivo`)
    REFERENCES `gestao-impressoras`.`aditivos` (`id_aditivo`),
  CONSTRAINT `FK_aditivos_itens_itens`
    FOREIGN KEY (`id_item`)
    REFERENCES `gestao-impressoras`.`itens` (`id_item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_aditivos_itens_secretarias`
    FOREIGN KEY (`id_secretaria`)
    REFERENCES `gestao-impressoras`.`secretarias` (`id_secretaria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
