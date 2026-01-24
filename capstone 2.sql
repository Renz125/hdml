CREATE TABLE IF NOT EXISTS nomnom (
 NAME TEXT,
 NEIGBOURHOOD TEXT,
 CUISINE TEXT,
 REVIEW REAL,
 PRICE TEXT
 );


INSERT INTO nomnom(NAME, NEIGBOURHOOD, CUISINE, REVIEW, PRICE) VALUES
    ( 'Peter', 'Brooklyn', 'Steak', 4.4, '$$$$$'),
    ( 'Vince', 'Florida', 'Korean Seafood', 3.5, '$$'),
    ( 'Jongro', 'Midtown', 'Pizza', 4, '$$$' ),
    ( 'Lightthosue', 'Queens', 'Chinese', 3.9, '$$$$$$' ),
    ( 'Minca', 'Downtown', 'Amirican', 4,6, '$$$'),
    ( 'Marea', 'Chinatown', 'Chinese', 3.0, '$$$$$$'),
    ( 'Dirty Candy', 'Uptown', 'Italian',  4.9, '$$$'),
    ( 'Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$$$' ),
    ( 'Golden  Unicorn', 'Uptiwn', 'Italian', 3.8, '$$$');




SELECT * FROM nomnom;

SELECT DISTINCT NEIGBOURHOOD FROM nomnom;

SELECT DISTINCE CUISINE FROM nomnom;

SELECT * FROM nomnom WHERE CUISINE = 'Chinese';

SELECT * FROM nomnom WHERE REVIEW = 4;

SELECT * FROM nomnom WHERE CUISINE = 'Italian' AND PRICE = '$$$';

SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';

SELECT * FROM nomnom 
WHERE NEIGBOURHOOD IN ('Midtown', 'Downtown', 'Chinatown');

-- SELECT THE TOP 4 RECORDS ORDERED BY REVIEW RATING IN DESCENDING ORDER
SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;

