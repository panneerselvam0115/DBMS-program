CREATE TABLE st1 (
id NUMBER PRIMARY KEY;
name VARCHAR2(50),
dept VARCHAR2(20),
marks NUMBER
);

INSERT INTO st1 VALUES (1, 'Priya', 'CSE', 90);
INSERT INTO st1 VALUES (2, 'Arun', 'ECE', 85);
INSERT INTO st1 VALUES (3, 'Divya', 'IT', 92);
COMMIT;

CREATE OR REPLACE VIEW high_scorers AS
SELECT id, name, dept, marks
FROM st
WHERE marks > 85;

SELECT * FROM high_scorers; 


CREATE INDEX idx_marks ON st1(marks); 
SELECT index_name, table_name, column_name 
FROM user_ind_columns 
WHERE table_name = 'ST1'; 

SELECT name, dept, marks 
FROM high_scorers 
WHERE dept = 'CSE';
