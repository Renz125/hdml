CREATE TABLE IF NOT EXISTS PRO (
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT,
    PRO_PRICE TEXT,
    PRO_COM TEXT;
);
 
INSERT INTO PRO( PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM) VALUES
    ("101", "MOTHER BOARD", "3200", "15"),
    ("102", "KEY BOARD", "450", "16"),
    ("103", "ZIP DRIVE", "250",  "14"),
    ("104", "SPEAKER", "650", "19" );

SELECT * FROM PRO

SELECT pro_name, pro_price 
    FROM PRO
    WHERE pro_price =
        (SELECT MIN(pro_price) FROM PRODUCT);
SELECT pro_name, pro_price
    FROM PRO
    WHERE pro_price =
        (SELECT MAX(pro_price) FROM PRODUCT);
