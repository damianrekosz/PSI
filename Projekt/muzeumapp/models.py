from django.db import models

# Create your models here.
from django.db import connection

def mu_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;", [self.baz])
        cursor.execute("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;", [self.baz])
        cursor.execute("SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';", [self.baz])
        cursor.execute("CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;", [self.baz])
        cursor.execute("USE `mydb` ;", [self.baz])
        cursor.execute("CREATE TABLE IF NOT EXISTS `mydb`.`Pracownicy` (`idPracownicy` INT UNSIGNED NOT NULL AUTO_INCREMENT, `Nazwisko` VARCHAR(45) NOT NULL, `Imię` VARCHAR(45) NOT NULL,`PESEL` VARCHAR(45) NOT NULL, PRIMARY KEY (`idPracownicy`),UNIQUE INDEX `PESEL_UNIQUE` (`PESEL` ASC) VISIBLE,UNIQUE INDEX `idPracownicy_UNIQUE` (`idPracownicy` ASC) VISIBLE) ENGINE = InnoDB;", [self.baz])
        cursor.execute("CREATE TABLE IF NOT EXISTS `mydb`.`Wydarzenia` (`idWydarzenia` INT NOT NULL AUTO_INCREMENT,`idPracownicy` INT NOT NULL,`idEksponaty` INT NOT NULL,`idSale` INT NOT NULL,`Nazwa` VARCHAR(45) NOT NULL,PRIMARY KEY (`idWydarzenia`),UNIQUE INDEX `idWydarzenia_UNIQUE` (`idWydarzenia` ASC) VISIBLE)ENGINE = InnoDB;", [self.baz])
        cursor.execute("CREATE TABLE IF NOT EXISTS `mydb`.`Eksponaty` (`idEksponaty` INT NOT NULL AUTO_INCREMENT,`Nazwa` VARCHAR(45) NOT NULL,`DataProdukcji` DATE NULL,`MiejscePochodzenia` VARCHAR(45) NULL,`StanEksponatu` VARCHAR(45) NULL,`CzyZarezerwowany` TINYINT NOT NULL, `DataCzynnościKonserwatorskich` DATE NOT NULL,`Wydarzenia_idWydarzenia` INT NOT NULL,PRIMARY KEY (`idEksponaty`, `Wydarzenia_idWydarzenia`),UNIQUE INDEX `idEksponaty_UNIQUE` (`idEksponaty` ASC) VISIBLE,INDEX `fk_Eksponaty_Wydarzenia1_idx` (`Wydarzenia_idWydarzenia` ASC) VISIBLE,CONSTRAINT `fk_Eksponaty_Wydarzenia1`FOREIGN KEY (`Wydarzenia_idWydarzenia`)REFERENCES `mydb`.`Wydarzenia` (`idWydarzenia`)ON DELETE NO ACTIONON UPDATE NO ACTION)ENGINE = InnoDB;", [self.baz])
        cursor.execute("CREATE TABLE IF NOT EXISTS `mydb`.`Sale` (`idSale` INT NOT NULL AUTO_INCREMENT,`Rozmiar` INT NOT NULL,`Wydarzenia_idWydarzenia` INT NOT NULL,PRIMARY KEY (`idSale`, `Wydarzenia_idWydarzenia`),UNIQUE INDEX `idSale_UNIQUE` (`idSale` ASC) VISIBLE,INDEX `fk_Sale_Wydarzenia1_idx` (`Wydarzenia_idWydarzenia` ASC) VISIBLE,CONSTRAINT `fk_Sale_Wydarzenia1`FOREIGN KEY (`Wydarzenia_idWydarzenia`)REFERENCES `mydb`.`Wydarzenia` (`idWydarzenia`)ON DELETE NO ACTIONON UPDATE NO ACTION) ENGINE = InnoDB;", [self.baz])
        cursor.execute("CREATE TABLE IF NOT EXISTS `mydb`.`Wydarzenia_has_Pracownicy` (`Wydarzenia_idWydarzenia` INT NOT NULL,`Pracownicy_idPracownicy` INT UNSIGNED NOT NULL,PRIMARY KEY (`Wydarzenia_idWydarzenia`, `Pracownicy_idPracownicy`),INDEX `fk_Wydarzenia_has_Pracownicy_Pracownicy1_idx` (`Pracownicy_idPracownicy` ASC) VISIBLE,INDEX `fk_Wydarzenia_has_Pracownicy_Wydarzenia_idx` (`Wydarzenia_idWydarzenia` ASC) VISIBLE,CONSTRAINT `fk_Wydarzenia_has_Pracownicy_Wydarzenia`FOREIGN KEY (`Wydarzenia_idWydarzenia`) REFERENCES `mydb`.`Wydarzenia` (`idWydarzenia`) ON DELETE NO ACTIONON UPDATE NO ACTION,CONSTRAINT `fk_Wydarzenia_has_Pracownicy_Pracownicy1` FOREIGN KEY (`Pracownicy_idPracownicy`) REFERENCES `mydb`.`Pracownicy` (`idPracownicy`) ON DELETE NO ACTIONON UPDATE NO ACTION) ENGINE = InnoDB;", [self.baz])
        cursor.execute("SET SQL_MODE=@OLD_SQL_MODE;", [self.baz])
        cursor.execute("SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;", [self.baz])
        cursor.execute("SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;", [self.baz])
