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
-- Table `ProjPy`.`categorie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`categorie` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `categories_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `categories_name_UNIQUE` (`categories_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `categories_id` INT NOT NULL,
  `name` VARCHAR(40) NOT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `quantity` TINYINT NOT NULL,
  `description` VARCHAR(500) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_store_categories_idx` (`categories_id` ASC) VISIBLE,
  CONSTRAINT `fk_store_categories`
    FOREIGN KEY (`categories_id`)
    REFERENCES `ProjPy`.`categorie` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`client_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`client_info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(15) NOT NULL,
  `lastname` VARCHAR(20) NOT NULL,
  `country` VARCHAR(42) NOT NULL,
  `city` VARCHAR(58) NOT NULL,
  `cp` VARCHAR(10) NOT NULL,
  `street` VARCHAR(40) NOT NULL,
  `street_nb` SMALLINT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`payment_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`payment_status` (
  `id` INT NOT NULL,
  `status_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `status_name_UNIQUE` (`status_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`payment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `amount` DECIMAL(10,2) NOT NULL,
  `payment_status` VARCHAR(20) NOT NULL,
  `payment_date` DATETIME NOT NULL,
  `payment_status_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_payment_payment_status1_idx` (`payment_status_id` ASC) VISIBLE,
  CONSTRAINT `fk_payment_payment_status1`
    FOREIGN KEY (`payment_status_id`)
    REFERENCES `ProjPy`.`payment_status` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_info_id` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `price_total` DECIMAL(10,2) NOT NULL,
  `nb_product` SMALLINT NOT NULL,
  `tracking_order` VARCHAR(45) NOT NULL,
  `payment_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_order_client_info1_idx` (`client_info_id` ASC) VISIBLE,
  UNIQUE INDEX `tracking_order_UNIQUE` (`tracking_order` ASC) VISIBLE,
  INDEX `fk_order_payment1_idx` (`payment_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_client_info1`
    FOREIGN KEY (`client_info_id`)
    REFERENCES `ProjPy`.`client_info` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_payment1`
    FOREIGN KEY (`payment_id`)
    REFERENCES `ProjPy`.`payment` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`order_has_product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`order_has_product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`id`, `order_id`, `product_id`),
  INDEX `fk_order_has_product_product1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_order_has_product_order1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_has_product_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `ProjPy`.`order` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_product_product1`
    FOREIGN KEY (`product_id`)
    REFERENCES `ProjPy`.`product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`delivery_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`delivery_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `statut_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `statut_type_UNIQUE` (`statut_type` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`delivery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`delivery` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tracking_number` INT NOT NULL,
  `date_expedition` DATETIME NOT NULL,
  `date_delivery` DATETIME NOT NULL,
  `delivery_status_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `tracking_number_UNIQUE` (`tracking_number` ASC) VISIBLE,
  INDEX `fk_delivery_delivery_status1_idx` (`delivery_status_id` ASC) VISIBLE,
  INDEX `fk_delivery_order1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_delivery_delivery_status1`
    FOREIGN KEY (`delivery_status_id`)
    REFERENCES `ProjPy`.`delivery_status` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_delivery_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `ProjPy`.`order` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
