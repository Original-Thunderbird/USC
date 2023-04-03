# DB Version: MySQL Community Server 8.0.26 Windows 32-bit with Workbench 8.0.26 Windows 64-bit

CREATE SCHEMA `hw2` ;

CREATE TABLE `hw2`.`employee` (
  `employee_ID` VARCHAR(5) NOT NULL,
  `employee_name` VARCHAR(10) NOT NULL,
  `office_num` INT NOT NULL,
  `floor_num` INT NOT NULL,
  `phone_num` VARCHAR(10) NOT NULL,
  `email_address` VARCHAR(20) NULL,
  PRIMARY KEY (`employee_ID`));

CREATE TABLE `hw2`.`meeting` (
  `meeting_ID` VARCHAR(6) NOT NULL,
  `room_num` INT NOT NULL,
  `floor_num` INT NOT NULL,
  `start_time` INT NOT NULL,
  PRIMARY KEY (`meeting_ID`));

CREATE TABLE `hw2`.`attendance` (
  `employee_ID` VARCHAR(5) NOT NULL,
  `meeting_ID` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`employee_ID`, `meeting_ID`),
  INDEX `attnd_FK2_idx` (`meeting_ID` ASC) VISIBLE,
  CONSTRAINT `attnd_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `attnd_FK2`
    FOREIGN KEY (`meeting_ID`)
    REFERENCES `hw2`.`meeting` (`meeting_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `hw2`.`notification` (
  `notif_ID` VARCHAR(6) NOT NULL,
  `employee_ID` VARCHAR(5) NOT NULL,
  `notif_date` DATE NOT NULL,
  `notif_type` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`notif_ID`),
  INDEX `FK1_idx` (`employee_ID` ASC) VISIBLE,
  CONSTRAINT `notif_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `hw2`.`symptom` (
  `row_ID` INT NOT NULL AUTO_INCREMENT,
  `employee_ID` VARCHAR(5) NOT NULL,
  `date_reported` DATE NOT NULL,
  `sym_type` INT NOT NULL,
  PRIMARY KEY (`row_ID`),
  INDEX `sympt_FK1_idx` (`employee_ID` ASC) VISIBLE,
  CONSTRAINT `sympt_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `hw2`.`scan` (
  `scan_ID` VARCHAR(6) NOT NULL,
  `scan_date` DATE NOT NULL,
  `scan time` INT NOT NULL,
  `employee_ID` VARCHAR(5) NOT NULL,
  `temperature` DECIMAL(3,1) NOT NULL,
  PRIMARY KEY (`scan_ID`),
  INDEX `scan_FK1_idx` (`employee_ID` ASC) VISIBLE,
  CONSTRAINT `scan_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `hw2`.`test` (
  `test_ID` VARCHAR(6) NOT NULL,
  `location` VARCHAR(8) NOT NULL,
  `test_date` DATE NOT NULL,
  `test_time` INT NOT NULL,
  `employee_ID` VARCHAR(5) NOT NULL,
  `result` TINYINT NOT NULL,
  PRIMARY KEY (`test_ID`),
  INDEX `test_FK1_idx` (`employee_ID` ASC) VISIBLE,
  CONSTRAINT `test_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `hw2`.`case` (
  `case_ID` VARCHAR(6) NOT NULL,
  `employee_ID` VARCHAR(5) NOT NULL,
  `date` DATE NOT NULL,
  `resolution` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`case_ID`),
  INDEX `case_FK1_idx` (`employee_ID` ASC) VISIBLE,
  CONSTRAINT `case_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE `hw2`.`healthstatus` (
  `row_ID` INT NOT NULL AUTO_INCREMENT,
  `employee_ID` VARCHAR(5) NOT NULL,
  `date` DATE NOT NULL,
  `status` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`row_ID`),
  INDEX `hlthtts_FK1_idx` (`employee_ID` ASC) VISIBLE,
  CONSTRAINT `hlthtts_FK1`
    FOREIGN KEY (`employee_ID`)
    REFERENCES `hw2`.`employee` (`employee_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00000', 'baldwin', '1', '2', '2130000000');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00001', 'barrasso', '2', '3', '2130000001');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00002', 'bennet', '3', '4', '2130000002');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00003', 'blackburn', '4', '5', '2130000003');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00004', 'blumenthal', '5', '6', '2130000004');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00005', 'blunt', '6', '7', '2130000005');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00006', 'booker', '7', '8', '2130000006');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00007', 'boozman', '8', '9', '2130000007');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00008', 'braun', '9', '10', '2130000008');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00009', 'brown', '0', '1', '2130000009');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00010', 'burr', '2', '2', '2130000010');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00011', 'cantwell', '3', '2', '2130000011');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00012', 'capito', '4', '2', '2130000012');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00013', 'cardin', '5', '2', '2130000013');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00014', 'carper', '1', '3', '2130000014');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00015', 'casey', '3', '3', '2130000015');
INSERT INTO `hw2`.`employee` (`employee_ID`, `employee_name`, `office_num`, `floor_num`, `phone_num`) VALUES ('00016', 'cassidy', '4', '3', '2130000016');

INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('1', '00003', '2020-12-12', '3');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('2', '00002', '2020-12-12', '1');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('3', '00002', '2020-12-13', '4');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('4', '00002', '2020-12-14', '5');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('5', '00003', '2020-12-15', '3');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('6', '00001', '2020-12-15', '4');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('7', '00001', '2020-12-15', '3');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('8', '00001', '2020-12-15', '2');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('9', '00001', '2020-12-15', '1');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('10', '00001', '2020-12-15', '5');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('11', '00006', '2020-12-15', '3');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('12', '00009', '2020-12-17', '3');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('13', '00006', '2020-12-17', '5');
INSERT INTO `hw2`.`symptom` (`row_ID`, `employee_ID`, `date_reported`, `sym_type`) VALUES ('14', '00008', '2020-12-18', '3');

INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00001', 'conpany', '2020-12-15', '9', '00001', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00002', 'company', '2020-12-16', '8', '00000', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00003', 'clinic', '2020-12-16', '12', '00010', '0');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00004', 'company', '2020-12-16', '17', '00010', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00005', 'company', '2020-12-16', '18', '00011', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00006', 'clinic', '2020-12-17', '14', '00012', '0');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00007', 'hospital', '2020-12-17', '16', '00012', '0');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00008', 'company', '2020-12-18', '8', '00012', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00009', 'hospital', '2020-12-18', '13', '00013', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00010', 'company', '2020-12-18', '15', '00014', '0');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00011', 'company', '2020-12-18', '16', '00014', '1');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00012', 'clinic', '2020-12-18', '17', '00015', '0');
INSERT INTO `hw2`.`test` (`test_ID`, `location`, `test_date`, `test_time`, `employee_ID`, `result`) VALUES ('t00013', 'hospital', '2020-12-18', '18', '00016', '1');

INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00001', '2020-12-12', '8', '00000', '35.9');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00002', '2020-12-12', '9', '00001', '36.7');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00003', '2020-12-12', '12', '00015', '37.6');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00004', '2020-12-13', '12', '00003', '36.2');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00005', '2020-12-13', '13', '00002', '36.5');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00006', '2020-12-13', '15', '00000', '37.9');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00007', '2020-12-13', '18', '00012', '38.8');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00008', '2020-12-14', '8', '00009', '36.0');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00009', '2020-12-15', '8', '00007', '36.4');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00010', '2020-12-15', '10', '00001', '36.2');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00011', '2020-12-15', '14', '00013', '36.9');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00012', '2020-12-16', '10', '00007', '37.8');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00013', '2020-12-16', '15', '00010', '35.6');
INSERT INTO `hw2`.`scan` (`scan_ID`, `scan_date`, `scan time`, `employee_ID`, `temperature`) VALUES ('s00014', '2020-12-16', '17', '00005', '38.2');

INSERT INTO `hw2`.`meeting` (`meeting_ID`, `room_num`, `floor_num`, `start_time`) VALUES ('m00001', '1', '2', '11');
INSERT INTO `hw2`.`meeting` (`meeting_ID`, `room_num`, `floor_num`, `start_time`) VALUES ('m00002', '3', '7', '12');
INSERT INTO `hw2`.`meeting` (`meeting_ID`, `room_num`, `floor_num`, `start_time`) VALUES ('m00003', '9', '6', '8');
INSERT INTO `hw2`.`meeting` (`meeting_ID`, `room_num`, `floor_num`, `start_time`) VALUES ('m00004', '2', '3', '17');
INSERT INTO `hw2`.`meeting` (`meeting_ID`, `room_num`, `floor_num`, `start_time`) VALUES ('m00005', '6', '6', '15');
INSERT INTO `hw2`.`meeting` (`meeting_ID`, `room_num`, `floor_num`, `start_time`) VALUES ('m00006', '9', '9', '9');

INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00001', 'm00001');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00001', 'm00002');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00001', 'm00006');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00001', 'm00003');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00001', 'm00005');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00002', 'm00004');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00003', 'm00002');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00003', 'm00005');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00003', 'm00006');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00003', 'm00004');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00005', 'm00004');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00006', 'm00001');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00008', 'm00002');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00008', 'm00006');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00008', 'm00005');
INSERT INTO `hw2`.`attendance` (`employee_ID`, `meeting_ID`) VALUES ('00010', 'm00003');