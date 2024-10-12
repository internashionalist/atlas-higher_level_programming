-- lists all records of second_table in hbtn_0c_0 in mySQL
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
