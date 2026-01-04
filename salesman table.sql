CREATE TABLE IF NOT EXISTS Salesman (
Salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
Commisions REAL
);

INSERT INTO Salesman ( Salesman_id, name, city, Commisions ) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002',  'Nail Kaite', 'Africa', 0.20),
('5006', 'Pit Skate', 'Canada', 0.25),
('5007', 'John Pork', 'USA', 0.31),
('5009', 'Mail Storm', 'Japan' , 0.40);

SELECT * FROM Salesman;


