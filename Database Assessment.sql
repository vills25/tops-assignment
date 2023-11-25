create database db_assessment;
use db_assessment;

create table The_City_Table(
id int primary key auto_increment,
City_name varchar(20) not null,
lot varchar(20) not null,
lon varchar(20) not null,
country_id varchar (20) not null
);

insert into The_City_Table(id, City_name, Lot, lon, country_id)
values
(1, 'Berlin', 52.520008, 13.104954, 1 ),
(2, 'Belgrade', 44.787197, 20.457273, 2 ),
(3, 'Zagrabe', 45.815399, 15.966568, 3 ),
(4, 'New York', 40.730610, -73.935242, 4),
(5, 'Los Angeles', 34.052235, -118.243683, 4),
(6, 'Warsaw', 52.237049, 21.017532, 5);

create table The_Customer_Table(
id int primary key auto_increment,
customer_name varchar(20),
City_id varchar(20),
Customer_Address varchar(20),
Next_call_date varchar(20),
ts_inserted varchar(50)
);

insert into The_Customer_Table(id, customer_name, City_id, Customer_Address, Next_call_date, ts_inserted)
values
(1, 'Jewelry Store', 4, 'Long Street 120', 2020-01-21, '2020-01-09 14:01:20.000'),
(2, 'Bakery', 1, 'Kurfurstendamm 25', 2020-02-21, '2020-01-09 17:52:15.000'),
(3, 'Cafe', 1, 'Tauentzienstrabe 44', 2020-01-21, '2020-01-10 08:02:49.000'),
(4, 'Restaurant', 3, 'Ulica Lipa 15', 2020-01-21, '2020-01-10 09:20:21.000');

create table The_Country_Table(
id int primary key auto_increment,
country_name varchar(30),
country_name_eng varchar(30),
Country_code varchar(30)
);

insert into The_Country_Table(id, country_name, Country_name_eng, Country_code)
values
(1, 'Deutschland', 'Germany', 'DEU'),
(2, 'Sirbija', 'Serbia', 'SRB'),
(3, 'hrvatska', 'Croatia', 'HRV'),
(4, 'United States of America', 'United States of America', 'USA'),
(5, 'Polska', 'Poland', 'POL'),
(6, 'Espana', 'Spain', 'ESP'),
(7, 'Rossiya', 'Russia', 'RUS');

SELECT The_Country_Table.country_name, The_City_Table.City_name, The_Customer_Table.customer_name
FROM The_Customer_Table
LEFT JOIN The_City_Table ON The_Customer_Table.City_id = City_id
LEFT JOIN The_Country_Table ON The_City_Table.country_id = country_id;

SELECT The_Country_Table.country_name, The_City_Table.City_name, The_Customer_Table.customer_name
FROM The_Country_Table
INNER JOIN The_City_Table ON The_City_Table.country_id = The_Country_Table.id
LEFT JOIN The_Customer_Table ON The_Customer_Table.city_id = City_id;
