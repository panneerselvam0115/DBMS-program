CREATE TABLE Ott_platforms ( 
platform_id INT PRIMARY KEY,
platform_name VARCHAR(50) 
); 
INSERT INTO Ott_platforms VALUES (1, 'Netflix'); 
INSERT INTO Ott_platforms VALUES (2, 'Amazon Prime'); 
INSERT INTO Ott_platforms VALUES (3, 'Disney+ Hotstar'); 
 
SELECT * FROM Ott_platforms; 

CREATE TABLE Movie (
movie_id INT PRIMARY KEY,
movie_name VARCHAR(100),
release_year INT,
platform_id INT, 
FOREIGN KEY (platform_id) 
REFERENCES Ott_platforms(platform_id) 
ON UPDATE CASCADE 
ON DELETE SET NULL 
); 
 
 
INSERT INTO Movie VALUES (101, 'Inception', 2010, 1); 
INSERT INTO Movie VALUES (102, 'KGF', 2022, 2); 
INSERT INTO Movie VALUES (103, 'Avengers', 2019, 3); 
INSERT INTO Movie VALUES (104, 'Dangal', 2016, 2); 
 
SELECT * FROM Movie; 


UPDATE Ott_platforms 
SET platform_id = 5 
WHERE platform_id = 2; 
 
SELECT * FROM Ott_platforms; 


SELECT * FROM Movie; 


 
UPDATE Movie 
SET platform_id = 3 
WHERE movie_id = 101; 



DELETE FROM Ott_platforms WHERE platform_id = 3; 
 
SELECT * FROM Ott_platforms; 
 
SELECT * FROM Movie; 


DELETE FROM Ott_platforms WHERE platform_id = 3; 
 
SELECT * FROM Ott_platforms; 
 
SELECT * FROM Movie; 

DELETE FROM Ott_platforms WHERE platform_id = 3; 
 
SELECT * FROM Ott_platforms; 
 
SELECT * FROM Movie; 
