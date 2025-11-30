 CREATE TABLE st (
id NUMBER,
name VARCHAR2(50),
age NUMBER 
); 

CREATE OR REPLACE FUNCTION get_age_category(age IN NUMBER) 
RETURN VARCHAR2 
IS 
    category VARCHAR2(20); 
BEGIN 
    IF age < 13 THEN 
        category := 'Child'; 
    ELSIF age BETWEEN 13 AND 19 THEN         category := 'Teenager'; 
    ELSIF age BETWEEN 20 AND 59 THEN         category := 'Adult';     ELSE 
        category := 'Senior Citizen'; 
    END IF; 
 
    RETURN category; 
END; 
/ 


SELECT get_age_category(10) AS category FROM dual; 

SELECT get_age_category(25) AS category FROM dual;


CREATE OR REPLACE PROCEDURE add_student(     p_id IN NUMBER,     p_name IN VARCHAR2,     p_age IN NUMBER 
) 
IS 
BEGIN 
    INSERT INTO st (id, name, age) 
    VALUES (p_id, p_name, p_age); 
 
    DBMS_OUTPUT.PUT_LINE('Record inserted successfully!'); END; 
/ 


BEGIN 
    add_student(101, 'Kavi', 20); 
END; 
/ 

SELECT name, age, get_age_category(age) AS age_category 
FROM st; 


SELECT * FROM st; 
