CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission TEXT
    );


INSERT INTO Salesman(Salesman_id, name, city, Comission ) VALUES

("5001", "James Kohog", "New York","0.15" ),
("5002", "Angelica Sales", "Paris", "0.13" ),
("5005", "Pit Alex", "London","0.12" ),
("5004", "Masri Amound", "Berlin","0.9" ),
("5003", "Ainz Matlinway", "Moscow","0.19"),
("5009", "Jozy Altidor", "Paris",   "0.21" );

CREATE TABLE IF NOT EXISTS Customer (
    Customer_id TEXT PRIMARY KEY,
    cust_nameTEXT,
    city TEXT,
    grade TEXT,
    Salesman_id TEXT
    );

INSERT INTO Customer ( Customer_id, cust_name, city, grade, Salesman_id ) VALUES
("3002", "timothy", "New York", "300", "5001" ),
("3021", "maynel", "London", "1000", "5002" ),
("3529", "Arostotle", "Paris", "200", "5005" ),
("4392", "Zane Britle", "Berlin", "500", "5004", ),
("3243", "Merry Joe", "Moscow", "880", "5003" ),
("4245", "Alistor Lays", "Paris", "932", "5009" );

CREATE TABLE IF NOT EXISTS Orders(
    ord_no TEXT PRIMARY KEY,
    purch_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders ( ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
("7001", "143.5", "2012-10-05", "3002", "5001" ),
("7002", "324.3", "2012-11-23", "3021", "5002" ),
("7004", "500", "2012-10-20", "3529", "5005" ),
("7003", "2435", "2012-09-30", "4392", "5004", ),
("7005", "112.9", "2012-12-22", "3243", "5003" ),
( "7007", "2325.5", "2012-10-15", "4245", "5009");

--Queries
SELECT customer.cust_name, Orders.customer_id, Orders.Salesman_id
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
WHERE Customer.city <> Salesman.city;

SELECT Orders.ord_no, Customer.cust_name
FROM Orders
JOIN Customer ON Orders.customer_id = Costumer.customer_id;

SELECT Customer.cust_name AS "Customer", Customer.grade AS "Grade"
FROM Orders
JOIN Salesmann ON Orders.Salesman_id = Salesman.Salesman_id
JOIN Customer ON Orders.customer_id = Customer.customer_id
WHERE Customer.grade  IS NOT NULL;

SELECT Customer.cust_name AS "Customer",
Customer.city AS "City",
Salesman.name AS "Salesman",
Salesman.Commission
FROM Customer
JOIN Saleman ON Customer.Salesman_id =   Salesman.Salesman_id
WHERE Salesman.commission BETWEEN 0.12 AND 0.14;

SELECT Orders.ord_no, Customer.cust_name, Salesman.Comission AS "Commission%",
Orders.purch_amt * Salesman.commission AS "Commission"
FROM Orders 
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
JOIN Customer ON Orders.Customer_id = Customer.Customer_id

