-- all customers in Berlin
SELECT * FROM Customers WHERE City='Berlin';

-- all customers in Mexico City
SELECT * FROM Customers WHERE City='México D.F.';


-- avg price of all products
SELECT avg(price) as `average_price` FROM Products;

-- number of products that Have price = 18
SELECT count(*) as `number of Products` FROM Products where price=18;


-- orders between 1996-08-01 and 1996-09-06
SELECT * From orders WHERE `OrderDate` BETWEEN(1996-08-01,1996-09-06);

-- customers with more than 3 orders
SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM (Orders
INNER JOIN Customers ON Orders.customerID = customers.CustomerID)
GROUP BY CustomerName
HAVING COUNT(Orders.OrderID) > 3;
SELECT CustomerName FROM Customers GROUP BY city HAVING COUNT(*) > 3;


-- all customers that are from the same city
select * FROM Customers where City IN (
        select City from Customers GROUP BY City having COUNT(City) > 1
    ) 
    order by city DESC;