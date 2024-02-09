-- Create database
CREATE DATABASE EIE;

-- Connect to the database
\c EIE;

-- Create table Locations
CREATE TABLE Locations (
    KATOTTG_2023 varchar(32) PRIMARY KEY,
    KOATUU_2020 varchar(32),
    category varchar(32),
    ukrainian_name varchar(64),
    english_name varchar(64)
);

-- Create table Years
CREATE TABLE Years (
    years integer PRIMARY KEY 
);

-- Create table Schools
CREATE TABLE Schools (
    KATOTTG_2023 varchar(32),
    EDRPOU varchar(32),
    years integer,
    eotypename varchar(64),
    PRIMARY KEY (EDRPOU, years),
    FOREIGN KEY (years) REFERENCES Years(years),
    FOREIGN KEY (KATOTTG_2023) REFERENCES Locations(KATOTTG_2023)
);

-- Create table Schools_Stats
CREATE TABLE Schools_Stats (
    EDRPOU varchar(32),
    eotype varchar(16),
    eolevel varchar(16),
    teachstuff float,
    nonteachstuff float,
    teachstuffretage float,
    pupils integer,
    classes integer,
    opex float,
    opexplan float,
    hub varchar(16),
    years integer,
    PRIMARY KEY (EDRPOU, years),
    FOREIGN KEY (EDRPOU, years) REFERENCES Schools(EDRPOU, years),
    FOREIGN KEY (years) REFERENCES Years(years)
);

-- Create table Students
CREATE TABLE Students (
    outid varchar(128) PRIMARY KEY,
    birth integer,
    sextypename varchar(16), 
    classprofilename varchar(128),
    regtypename varchar(128),
    classlangname varchar(128),
    KATOTTG_2023_school varchar(32),
    EDRPOU_school varchar(32),
    years integer,
    FOREIGN KEY (EDRPOU_school, years) REFERENCES Schools(EDRPOU, years),
    FOREIGN KEY (KATOTTG_2023_school) REFERENCES Locations(KATOTTG_2023)
);

-- Create table Tests
CREATE TABLE Tests (
    test_type varchar(8),
    test_subject varchar(16),
    PRIMARY KEY (test_type, test_subject)
);

-- Create table Test_Centers
CREATE TABLE Test_Centers (
    KATOTTG_2023 varchar(32),
    years integer,
    EDRPOU varchar(32),
    PRIMARY KEY (EDRPOU, years),
    FOREIGN KEY (KATOTTG_2023) REFERENCES Locations(KATOTTG_2023)
);

-- Create table Test_Center_Located_In
CREATE TABLE Test_Center_Located_In (
    mapping_id SERIAL PRIMARY KEY,
    test_center_id varchar(32),
    school_id varchar(32),
    years integer,
    -- Add other columns as needed
    FOREIGN KEY (test_center_id, years) REFERENCES Test_Centers(EDRPOU, years),
    FOREIGN KEY (school_id, years) REFERENCES Schools(EDRPOU, years)
);

-- Create table Students_Take_Tests
CREATE TABLE Students_Take_Tests (
    outid varchar(256),
    years integer,
    score100 float,
    score12 float,
    score float,
    test_status varchar(256),
    test_subject varchar(256),
    test_type varchar(100),
    KATOTTG_2023_test_center varchar(256),
    EDRPOU_test_center varchar(256),
    PRIMARY KEY(outid, test_type, test_subject),
    FOREIGN KEY (outid) REFERENCES Students(outid),
    FOREIGN KEY (years) REFERENCES Years(years),
    FOREIGN KEY (test_type, test_subject) REFERENCES Tests(test_type, test_subject),
    FOREIGN KEY (KATOTTG_2023_test_center) REFERENCES Locations(KATOTTG_2023),
    FOREIGN KEY (EDRPOU_test_center, years) REFERENCES Test_Centers(EDRPOU, years)
);

-- Load data into Locations table
COPY Locations FROM '/usr/src/app/final_tables/locations_base.csv' WITH CSV HEADER;

-- Load data into Years table
COPY Years FROM '/usr/src/app/final_tables/years.csv' WITH CSV HEADER;

-- Load data into Schools table
COPY Schools FROM '/usr/src/app/final_tables/schools_edrpou.csv' WITH CSV HEADER;

-- Insert empty records into Schools (assuming EDRPOU is a string column)
-- INSERT INTO Schools (EDRPOU, years) SELECT '', years FROM Years;

-- Load data into Schools_Stats table
COPY Schools_Stats FROM '/usr/src/app/final_tables/school_stats.csv' WITH CSV HEADER;

-- Load data into Students table
COPY Students FROM '/usr/src/app/final_tables/students.csv' WITH CSV HEADER;

-- Load data into Tests table
COPY Tests FROM '/usr/src/app/final_tables/subjects.csv' WITH CSV HEADER;

-- Load data into Test_Centers table
COPY Test_Centers FROM '/usr/src/app/final_tables/test_centers_edrpou.csv' WITH CSV HEADER;

-- Load data into Test_Center_Located_in table
INSERT INTO Test_Center_Located_In (test_center_id, school_id, years)
SELECT
    tc.EDRPOU AS test_center_id,
    s.EDRPOU AS school_id,
    tc.years AS association_year
FROM
    Test_Centers tc
JOIN
    Schools s ON tc.years = s.years and tc.EDRPOU = s.EDRPOU;

-- Load data into Students_Take_Tests table
COPY Students_Take_Tests FROM '/usr/src/app/final_tables/students_take_tests.csv' WITH CSV HEADER;