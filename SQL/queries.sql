-- Create Table
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    marks INT
);

-- Insert Data
INSERT INTO students VALUES (1, 'Sanjana', 85);
INSERT INTO students VALUES (2, 'Rahul', 70);
INSERT INTO students VALUES (3, 'Anita', 90);
INSERT INTO students VALUES (4, 'Karan', 60);
INSERT INTO students VALUES (5, 'Neha', 75);

-- Select
SELECT * FROM students;

-- Where
SELECT * FROM students
WHERE marks > 70;

-- Average
SELECT AVG(marks) FROM students;

-- Subquery
SELECT name
FROM students
WHERE marks > (SELECT AVG(marks) FROM students);

-- Group By
SELECT marks, COUNT(*)
FROM students
GROUP BY marks;

-- Having
SELECT marks, COUNT(*)
FROM students
GROUP BY marks
HAVING COUNT(*) > 1;


-- INNER JOIN
SELECT students.name, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.id;

-- LEFT JOIN
SELECT students.name, marks.marks
FROM students
LEFT JOIN marks
ON students.id = marks.id;

-- RIGHT JOIN
SELECT students.name, marks.marks
FROM students
RIGHT JOIN marks
ON students.id = marks.id;
