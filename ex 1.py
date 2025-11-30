CREATE TABLE students(
student_id INT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE,
age INT CHECK (age >= 18)
);

INSERT INTO students(student_id, first_name, last_name, email, age) VALUES
(1, 'DOE', 'Doe', 'doe@gmail.com', 20),
(2, 'SMITH', 'Smith', 'smith@gmail.com', 22),
(3, 'JOHNSON', 'Johnson', 'johnson@gmail.com', 25);
SELECT * FROM students;

SELECT * FROM students WHERE age > 20;

 
UPDATE students 
SET email = 'jane.smith@gmail.com' 
WHERE student_id = 2; 
 
SELECT * FROM students; 

DELETE FROM students 
WHERE student_id = 1; 

 
SELECT * FROM students; 
 
 
ALTER TABLE students 
ADD department VARCHAR(50); 
 
INSERT INTO students(student_id, first_name, last_name, email, age, department) 
VALUES 
  (4, 'JOHN', 'DOE', 'johndoe@gmail.com', 20, 'computer science'); 
 
SELECT * FROM students; 
