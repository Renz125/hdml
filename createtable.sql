CREATE TABLE supplier(
SNO TEXT PRIMARY KEY,
SNAME TEXT,
STATUS  INTEGER,
CITY TEXT,
);

INSERT INTO supplier ( SNO, SNAME, STATUS, CITY ) VALUES
('S1', 'Smith' , '30', 'London',),
('S2', 'John', '20', 'Paris' ),
('S3', 'Blake', '40', 'Paris' ),
('S4', 'Clark', '10', 'Japan' );

SELECT * FROM supplier;

