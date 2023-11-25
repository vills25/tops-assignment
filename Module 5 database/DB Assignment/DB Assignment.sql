create database Assignment_M_5;
use Assignment_M_5;

create table Student(
Rollno varchar(20),
Name   varchar(20),
Branch varchar(20)
);

ALTER TABLE Student
ADD PRIMARY KEY (Rollno);

insert into Student(Rollno, Name, Branch)
values
(1, 'Jay', 'Computer Science'),
(2, 'Suhani', 'Electronic and Com'),
(3, 'Kriti', 'Electronic and Com');

create table Exam(
Rollno varchar(20),
S_code varchar(20),
Marks varchar(20),
P_code varchar(20)
);

insert into Exam(Rollno, S_code, Marks, P_code)
values
(1,'CS11', '50','CS'),
(1,'CS12', 60, 'CS'),
(2,'EC101', 66, 'EC'),
(2,'EC102', 70, 'EC'),
(3,'EC101', 45, 'EC'),
(3,'EC102', 50, 'EC');

ALTER TABLE Exam
ADD FOREIGN KEY (Rollno) REFERENCES Student(Rollno);

create table Table_1(
First_name varchar(20) not null,
Last_Name varchar(20) not null,
Address varchar(20) not null,
City varchar(20) not null,
Age int(3)
);

insert into Table_1(First_Name, Last_Name, Address, City, Age)
values
('Mickey', 'Mouse', '123 Fantasy Way', 'Anaheim', 73),
('Bat', 'Man', '321 Cavern Ave', 'Gotham',54),
('Wonder', 'Woman', '987 Truth Way', 'Paradise', 39),
('Donald', 'Duck', '555 Quack Street', 'Mallard', 65),
('Bugs', 'Bunny', '567 Carrot Street', 'Rascal', 58),
('Wiley', 'Coyote', '999 Acme Way', 'Canyon', 61),
('Cat', 'Woman', '234 Purrfect Street', 'Hairball', 32),
('Tweety', 'Bird', '534', 'Itotltaw', 28);

-- Table :- Employee and Incentive

create table Employee(
Employee_id int primary key auto_increment,
First_name varchar(20) not null,
Last_name varchar(20) not null,
Salary int(20),
Joining_date varchar (30),
Department varchar (30)
);

insert into Employee (Employee_id,First_name, Last_name, Salary, Joining_date, Department )
values

(1, 'John', 'Abraham', 1000000 , '01-JAN-13 12.00.00 AM', 'Banking'),
(2, 'Michael', 'Clarke', 800000 , '01-JAN-13 12.00.00 AM', 'Insurance'),
(3, 'Roy', 'Thomas', 700000 , '01-FAB-13 12.00.00', 'Banking'),
(4, 'Tom', 'Jose', 600000 , '01-FAB-13 12.00.00', 'Insurance'),
(5, 'Jerry', 'Pinto', 650000 , '01-FAB-13 12.00.00', 'insurance'),
(6, 'Philip', 'Mathew', 750000 , '01-JAN-13 12.00.00 AM', 'Services'),
(7, 'TestName1', '123', 650000 , '01-JAN-13 12.00.00 AM', 'Services'),
(8, 'TestName2', 'Lname%', 600000 , '01-FAB-13 12.00.00', 'Insurance');

create table Incentive(
Employee_ref_id varchar(20),
Incentive_Date varchar(20),
Incentive_amount varchar(20));

insert into Incentive(Employee_ref_id, Incentive_Date, Incentive_amount)
values
(1, '01-FEB-13', 5000),
(2, '01-FEB-13', 3000),
(3, '01-FEB-13', 4000),
(1, '01-JAN-13', 4500),
(2, '01-JAN-13', 3500);


-- Table :- Salesperson and Customer

create table Salesperson(
PK_SNo varchar(20),
SNAME varchar(20),
CITY  varchar(20),
COMM varchar(20));

 insert into Salesperson()
 values
(1001, 'Peel', 'London', .12),
(1002, 'Serres', 'San Jose', .13),
(1004, 'Motika', 'London', .11),
(1007, 'Rafkin', 'Barcelona', .15),
(1003, 'Axelrod', 'New York', .1);


create table customer(
PK_CNM varchar(20),
CNAME varchar(20),
CITY varchar(20),
RATING varchar(20),
FK_SNo varchar(20));

insert into customer()
values
(201, 'Hoffman', 'London', 100 ,1001 ),
(202, 'Giovanne', 'Roe', 200, 1003),
(203,'Liu','San Jose', 300, 1002),
(204,'Grass','Barcelona', 100, 1002),
(206,'Clemens','London', 300, 1007),
(207,'Pereira','Roe', 100, 1004);

SELECT firstname 'Tom' FROM Employee ;

select First_name,Salary,Joining_date  from Employee ;

select * from Employee order by First_name asc;

select * from Employee order by Salary desc;

select * from Employee where First_name like 'J%';

 select max(Salary) from  Employee order by Salary asc;
 
 SELECT Department , MAX(salary) 
FROM Employee GROUP BY Department ORDER BY Salary ASC;

SELECT First_name,Incentive_amount 
FROM Employee A 
INNER JOIN IncentiveTable B 
  ON A.Employee_id=B.Employee_id
AND Incentive_amount >3000;

create trigger paras
after delete on Employee 
for each row 
insert into backup values(old.Employee_id,old.First_name,old.Last_name,old.Salary,old.Joining_date,old.Department);

drop trigger paras;


