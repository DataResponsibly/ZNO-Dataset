DROP DATABASE IF EXISTS EIE;

CREATE DATABASE EIE;

USE EIE;

SET sql_log_bin = 0;
SET SESSION sql_log_bin = OFF;
SET GLOBAL max_allowed_packet=101000000000;


create table Locations (
    KOATUU_2020 varchar(32) primary key,
    KATOTTG_2023 varchar(32),
    category varchar(32),
    region_name varchar(64)
/* add official area, tername*/
);

create table Years (
    years year primary key 
);

create table Schools (
    KOATUU_2020 varchar(32),
    EDRPOU varchar(32),
    years year,
    primary key (EDRPOU, years),
    foreign key (years) references Years(years)
);
-- foreign key (KOATUU_2020) references Locations(KOATUU_2020),
-- fix problem with KOATUU_2020 which we don't have in locations

create table Schools_Stats (
    EDRPOU varchar(32),
    eotype varchar(16),
    eolevel varchar(16),
    teachstuff integer,
    nonteachstuff integer,
    teachstuffretage integer,
    pupils integer,
    classes integer,
    opex float,
    opexplan float,
    hub varchar(16),
    years year,
    primary key (EDRPOU, years),
    foreign key (EDRPOU, years) references Schools(EDRPOU, years),
    foreign key (years) references Years(years)
);

create table Students (
    outid varchar(128) primary key,
    birth year,
    sextypename	varchar(16), 
    classprofilename varchar(128),
    regtypename varchar(128),
    classlangname varchar(128),
    KOATUU_2020_school	varchar(32),
    EDRPOU_school varchar(32),
    years year,
    foreign key (EDRPOU_school, years) references Schools(EDRPOU, years),
    foreign key (KOATUU_2020_school) references Locations(KOATUU_2020)
);


create table Tests (
    test_type varchar(8),
    test_subject varchar(16),
    primary key (test_type, test_subject)
);


/* TO DISCUSS: schools change location
change diagram
ptname, add connection to year diagr
*/
create table Test_Centers (
    KOATUU_2020 varchar(32),
    years year,
    EDRPOU varchar(32),
    primary key (EDRPOU, years),
    foreign key (KOATUU_2020) references Locations(KOATUU_2020),
    foreign key (EDRPOU, years) references Schools(EDRPOU, years)
);


create table Students_Take_Tests (
    outid varchar(256),
    years year,
    score100 float,
    score12	float,
    score float,
    test_status varchar(256),
    test_subject varchar(256),
    test_type varchar(100),
    KOATUU_2020_test_center varchar(256),
    EDRPOU_test_center  varchar(256),
    primary key(outid, test_type, test_subject),
    foreign key (outid) references Students(outid),
    foreign key (years) references Years(years),
    foreign key (test_type, test_subject) references Tests(test_type, test_subject),
    foreign key (KOATUU_2020_test_center) references Locations(KOATUU_2020),
    foreign key (EDRPOU_test_center, years) references Test_Centers(EDRPOU, years)
);


-- Load data from csv
LOAD DATA INFILE '../../../../final_tables/locations.csv'
IGNORE INTO TABLE Locations
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; 

LOAD DATA INFILE '../../../../final_tables/years.csv'
INTO TABLE Years
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; 

LOAD DATA INFILE '../../../../final_tables/schools_edrpou.csv'
INTO TABLE Schools
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; 

/* 
ToDo: Thinl about better solution
Insert empty "" as EDROIU_school for each year 
*/
INSERT INTO Schools (EDRPOU, years)
SELECT '', years
FROM Years;

LOAD DATA INFILE '../../../../final_tables/school_stats.csv'
INTO TABLE Schools_Stats
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; 


LOAD DATA INFILE '../../../../final_tables/students.csv'
INTO TABLE Students
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;


LOAD DATA INFILE '../../../../final_tables/subjects.csv'
INTO TABLE Tests
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; 

LOAD DATA INFILE '../../../../final_tables/test_centers_edrpou.csv'
INTO TABLE Test_Centers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; 