USE classicmodels;
INSERT INTO customers
(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit)

VALUES
(999,'ABC Company','Tran','Khanh Linh','0123456789','30A', 'Staniforth St','Birmingham','West Midlands','B4 7DR','UK',1370,22000.00
);

SELECT *
FROM customers
WHERE customerNumber = 999;

DELETE FROM customers
WHERE customerNumber = 999;

INSERT INTO customers
(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit)

VALUES
(999,'ABC Company','Tran','Khanh Linh','0123456789','30A', 'Staniforth St','Birmingham','West Midlands','B4 7DR','UK',1370,22000.00
);

UPDATE customers
SET city = 'Nottingham'
WHERE customerNumber = 999;

SELECT * FROM customers
WHERE customerNumber = 999;

SELECT 
    c.customerNumber, 
    c.customerName, 
    o.orderNumber, 
    o.orderDate, 
    o.status
FROM customers c
INNER JOIN orders o ON c.customerNumber = o.customerNumber
LIMIT 5;

SELECT 
    c.customerNumber, 
    c.customerName, 
    SUM(p.amount) AS totalpayment
FROM customers c
LEFT JOIN payments p ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY totalpayment DESC
LIMIT 7;

SELECT 
    e.employeeNumber,
    CONCAT(e.firstName, ' ', e.lastName) AS employeeName,
    COUNT(o.orderNumber) AS totalordersprocessed
FROM employees e
INNER JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
INNER JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
ORDER BY totalOrdersProcessed DESC
LIMIT 1;