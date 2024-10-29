-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ProjPy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ProjPy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ProjPy` DEFAULT CHARACTER SET utf8 ;
USE `ProjPy` ;

-- -----------------------------------------------------
-- Table `ProjPy`.`clients_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`clients_info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(30) NOT NULL,
  `lastname` VARCHAR(40) NOT NULL,
  `country` VARCHAR(42) NOT NULL,
  `city` VARCHAR(58) NOT NULL,
  `cp` VARCHAR(10) NOT NULL,
  `street` VARCHAR(40) NOT NULL,
  `street_nb` SMALLINT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`deliveries_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`deliveries_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `statut_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `statut_type_UNIQUE` (`statut_type` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`deliveries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`deliveries` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tracking_number` INT NOT NULL,
  `date_expedition` DATETIME NOT NULL,
  `date_delivery` DATETIME NOT NULL,
  `delivery_status_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `tracking_number_UNIQUE` (`tracking_number` ASC) VISIBLE,
  INDEX `fk_delivery_delivery_status1_idx` (`delivery_status_id` ASC) VISIBLE,
  CONSTRAINT `fk_delivery_delivery_status1`
    FOREIGN KEY (`delivery_status_id`)
    REFERENCES `ProjPy`.`deliveries_status` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`Packages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`Packages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `size_type` VARCHAR(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `size_type_UNIQUE` (`size_type` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_info_id` INT NOT NULL,
  `deliveries_id` INT NOT NULL,
  `Packages_id` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `price_total` DECIMAL(10,2) NOT NULL,
  `nb_product` SMALLINT NOT NULL,
  `tracking_order` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_order_client_info1_idx` (`client_info_id` ASC) VISIBLE,
  UNIQUE INDEX `tracking_order_UNIQUE` (`tracking_order` ASC) VISIBLE,
  INDEX `fk_orders_deliveries1_idx` (`deliveries_id` ASC) VISIBLE,
  INDEX `fk_orders_Packages1_idx` (`Packages_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_client_info1`
    FOREIGN KEY (`client_info_id`)
    REFERENCES `ProjPy`.`clients_info` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_deliveries1`
    FOREIGN KEY (`deliveries_id`)
    REFERENCES `ProjPy`.`deliveries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_Packages1`
    FOREIGN KEY (`Packages_id`)
    REFERENCES `ProjPy`.`Packages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
