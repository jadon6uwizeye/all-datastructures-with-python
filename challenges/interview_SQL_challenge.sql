SELECT * FROM Customers WHERE City='Berlin';
SELECT * FROM Customers WHERE City='México D.F.';

SELECT avg(price) as `average_price` FROM Products;

SELECT count(*) as `number of Products` FROM Products where price=18;

SELECT * From orders WHERE `OrderDate` BETWEEN(1996-08-01,1996-09-06);