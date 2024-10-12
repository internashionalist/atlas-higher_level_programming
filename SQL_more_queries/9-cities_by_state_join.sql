-- lists all California cities in database hbtn_0e_4_usa
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
