SELECT
    c.login AS courier_login,
    COUNT(o.id) AS orders_count
FROM "Couriers" c
JOIN "Orders" o
    ON o."courierId" = c.id
WHERE o."inDelivery" = true
GROUP BY c.login;
