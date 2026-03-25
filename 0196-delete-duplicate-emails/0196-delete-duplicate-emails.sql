DELETE FROM Person
WHERE id NOT IN (select * from(
    SELECT MIN(id)
    FROM Person
    GROUP BY email)
    as temp
);
