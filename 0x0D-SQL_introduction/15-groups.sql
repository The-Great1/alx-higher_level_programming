-- script that list the number of records with the same sourcein t-- he table

SELECT `score`, COUNT(*) AS 'number'
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
