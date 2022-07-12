SELECT * FROM Customers WHERE City='Berlin';
SELECT * FROM Customers WHERE City='México D.F.';

SELECT avg(price) as `average_price` FROM Products;

SELECT count(*) as `number of Products` FROM Products where price=18;

SELECT * From orders WHERE `OrderDate` BETWEEN(1996-08-01,1996-09-06);

SELECT * FROM customers JOIN orders ON customers.customerId = orders.customerId;

SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Customers ON Orders.customerID = customers.CustomerID)
GROUP BY CustomerName
HAVING COUNT(Orders.OrderID) > 3;
SELECT CustomerName FROM Customers GROUP BY city HAVING COUNT(*) > 3;

select * FROM Customers where City IN (select City from Customers GROUP BY City having COUNT(City) > 1) order by city DESC;