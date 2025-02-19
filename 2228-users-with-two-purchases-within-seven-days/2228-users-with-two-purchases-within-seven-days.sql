# Write your MySQL query statement below
SELECT DISTINCT p2.user_id
FROM Purchases p1
    INNER JOIN Purchases p2 ON p1.user_id = p2.user_id
        AND p1.purchase_id != p2.purchase_id
        AND ABS(DATEDIFF(p1.purchase_date, p2.purchase_date)) <= 7
ORDER BY 1;