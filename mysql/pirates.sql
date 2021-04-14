-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema 
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `` DEFAULT CHARACTER SET utf8 ;
USE `` ;

-- -----------------------------------------------------
-- Table ``.`pets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ``.`pets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `animal_type` VARCHAR(255) NULL,
  `name` VARCHAR(255) NULL,
  `created_at` VARCHAR(255) NULL,
  `updated_at` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table ``.`pirates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ``.`pirates` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `role` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `pet_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pirates_pets1_idx` (`pet_id` ASC) VISIBLE,
  CONSTRAINT `fk_pirates_pets1`
    FOREIGN KEY (`pet_id`)
    REFERENCES ``.`pets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table ``.`treasures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ``.`treasures` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `amount` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `pirate_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_treasures_pirates_idx` (`pirate_id` ASC) VISIBLE,
  CONSTRAINT `fk_treasures_pirates`
    FOREIGN KEY (`pirate_id`)
    REFERENCES ``.`pirates` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
