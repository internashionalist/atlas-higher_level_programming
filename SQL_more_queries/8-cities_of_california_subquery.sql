-- lists all California cities from the cities table
SELECT cities.id, cities.name 
FROM cities 
WHERE cities.state_id = (
    SELECT states.id 
    FROM states 
    WHERE states.name = 'California'
) 
ORDER BY cities.id;
