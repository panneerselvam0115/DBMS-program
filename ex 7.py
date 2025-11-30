CREATE TABLE ss (
student_id NUMBER PRIMARY KEY,
department VARCHAR(30),
marks NUMBER(5),
email VARCHAR(50) 
); 

CREATE USER user1 IDENTIFIED BY user123; 
 
GRANT CONNECT, RESOURCE TO user1; 
 
 
INSERT INTO ss VALUES (12,  'CSE', 90, 'priya@gmail.com'); 
INSERT INTO ss VALUES (22, 'ECE', 85, 'karthik@gmail.com'); 
 
SELECT * FROM SS; 



GRANT SELECT, INSERT ON ss TO user1; 
 
SELECT grantee, table_name, privilege 
FROM user_tab_privs_made 
WHERE grantee = 'USER1'; 

UPDATE ss
SET marks = 100
WHERE student_id = 12;
REVOKE INSERT ON ss FROM user1;
INSERT INTO ss VALUES (15,  'CSE', 90, 'priya@gmail.com');
INSERT INTO ss VALUES (105, 'EEE', 82, 'anitha@gmail.com');
UPDATE ss SET marks = 85 WHERE student_id = 105;
COMMIT; 
SELECT * FROM SS;
