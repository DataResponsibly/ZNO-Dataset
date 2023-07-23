CREATE DATABASE ZNO;

USE ZNO;

create table Locations (
    location_codifier integer primary key
);

create table Organizations (
    organization_name varchar(256) primary key
);

create table Years (
    year year primary key 
);

create table Schools (
    school_name varchar(256)  primary key,
    organization_name varchar(256) not null,
    location_codifier integer not null,
    foreign key (organization_name) references Organizations(organization_name),
    foreign key (location_codifier) references Locations(location_codifier)
);

create table Schools_Stats (
    id integer primary key,
    school_name varchar(256) not null,
    year year not null,
    foreign key (school_name) references Schools(school_name),
    foreign key (year) references Years(year),
    unique (school_name, year)
);

create table Students (
    student_id integer primary key,
    school_name varchar(256),
    location_codifier integer not null,
    foreign key (school_name) references Schools(school_name),
    foreign key (location_codifier) references Locations(location_codifier)
);

create table Tests (
    test_type varchar(100),
    test_subject varchar(256),
    primary key(test_type, test_subject)
);

create table Test_Centers (
    test_center_name varchar(256)  primary key,
    location_codifier integer not null,
    foreign key (location_codifier) references Locations(location_codifier)
);

create table Students_Take_Tests (
    test_center_name varchar(256),
    test_type varchar(100),
    test_subject varchar(256),
    student_id integer,
    year year,
    score float(1),
    primary key(test_center_name, test_type, test_subject, student_id, year),
    foreign key (test_center_name) references Test_Centers(test_center_name),
    foreign key (test_type, test_subject) references Tests(test_type, test_subject),
    foreign key (student_id) references Students(student_id),
    foreign key (year) references Years(year)
);
