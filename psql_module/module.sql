#1
--------------------------
INSERT INTO users(name, pwd, email, gender) VALUES
('Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'),
('Alex', '21341234', 'mmm@gmail.com', 'm'),
('Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'),
('Helen', 'MarryMeeee', 'hell@gmail.com', 'f'),
('Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'),
('Lora', 'burn23', 'tpicks@gmail.com', 'f');
#2
--------------------------
SELECT CONCAT ('This is ', name, CASE WHEN gender LIKE 'm' THEN ' he' WHEN gender LIKE 'f' THEN ' she' END, ' has email', email)AS "info" FROM users;
#3
--------------------------
SELECT CONCAT('We have ', COUNT(*), CASE WHEN gender LIKE 'm' THEN ' boys!' WHEN gender LIKE 'f' THEN ' girls!' END)AS "Gender information:" FROM users GROUP BY gender;
#4
--------------------------
SELECT name, COUNT(*) AS "words" FROM vocabulary FULL JOIN word on(vocabulary.id=vocabulary_id)GROUP BY name;