-- lists all records with a score of 10 or more in second_table in hbtn_0c_0 database in the mySQL server
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
