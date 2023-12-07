DROP DATABASE IF EXISTS EIE;

CREATE DATABASE EIE;

USE EIE;

/*
TO DISCUSS: 
- remove regname, areaname, tername
- use KOATUU_2020 as a primary key

create table Locations (
    regname varchar(256),
    areaname varchar(256),
    tername varchar(256),
    KOATUU_2020 varchar(256),
    KATOTTG_2023 varchar(256),
    category varchar(256),
    region_name varchar(256),
    primary key(regname, areaname, tername)

);
*/

create table Locations (
    KOATUU_2020 varchar(256) primary key,
    KATOTTG_2023 varchar(256),
    category varchar(256),
    region_name varchar(256)
);

create table Years (
    years year primary key 
);

/* TO DISCUSS: do we need eoname
*/
create table Schools (
    eoname varchar(256),
    KOATUU_2020 varchar(256),
    EDRPOU varchar(256),
    years year,
    primary key (EDRPOU, years),
    foreign key (KOATUU_2020) references Locations(KOATUU_2020),
    foreign key (years) references Years(years)
);

/* TO DISCUSS: Schools_Stats and Schools are different
*/
create table Schools_Stats (
    EDRPOU varchar(256),
    eotype varchar(256),
    eolevel varchar(256),
    teachstuff integer,
    nonteachstuff integer,
    teachstuffretage integer,
    pupils integer,
    classes integer,
    opex float,
    opexplan float,
    hub varchar(256),
    years year,
    primary key (EDRPOU, years),
    foreign key (EDRPOU, years) references Schools(EDRPOU, years),
    foreign key (years) references Years(years)
);


create table Students (
    outid varchar(256) primary key,
    birth year,
    sextypename	varchar(256), 
    classprofilename varchar(256),
    regtypename varchar(256),
    classlangname varchar(256),
    years year,
    KOATUU_2020_school	varchar(256),
    EDRPOU_school varchar(256),
    foreign key (EDRPOU_school, years) references Schools(EDRPOU, years),
    foreign key (KOATUU_2020_school) references Locations(KOATUU_2020)
);


create table Tests (
    test_type varchar(100),
    test_subject varchar(256),
    primary key (test_type, test_subject)
);


/* TO DISCUSS: schools change location
change diagram
*/
create table Test_Centers (
    ptname varchar(256),
    KOATUU_2020 varchar(256),
    years year,
    EDRPOU varchar(256),
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

/*
*/


/*Load data from csv


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
*/