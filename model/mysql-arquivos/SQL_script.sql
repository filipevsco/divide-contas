-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema divide_contas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema divide_contas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `divide_contas` ;
USE `divide_contas` ;

-- -----------------------------------------------------
-- Table `divide_contas`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `divide_contas`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `salario_medio` DECIMAL(8,2) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `divide_contas`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `divide_contas`.`categoria` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `divide_contas`.`despesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `divide_contas`.`despesa` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(45) NOT NULL,
  `categoria` INT NOT NULL,
  `valor` DECIMAL(8,2) NOT NULL,
  `id_usuario` INT NOT NULL,
  `emprestado` TINYINT(0) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_despesa_1_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `fk_despesa_2_idx` (`categoria` ASC) VISIBLE,
  CONSTRAINT `fk_despesa_1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `divide_contas`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_despesa_2`
    FOREIGN KEY (`categoria`)
    REFERENCES `divide_contas`.`categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
