-- script that lists number of records with same score in second_table in hbtn_0c_0 database in mySQL server
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
