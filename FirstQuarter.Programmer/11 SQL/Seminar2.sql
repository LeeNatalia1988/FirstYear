USE seminar_2;
DROP TABLE IF EXISTS sales;
CREATE TABLE seminar_2.sales 
(
id SERIAL PRIMARY KEY,
order_date DATE NOT NULL,
count_product INT NOT NULL
);

INSERT INTO sales (order_date, count_product)
VALUES
('2022-01-01', 156),
('2022-01-02', 180),
('2022-01-03', 21),
('2022-01-04', 124),
('2022-01-05', 341);

SELECT * FROM sales;

SELECT id AS "Номер заказа", count_product AS "Количество продукта",
	CASE 
		WHEN count_product < 100 THEN "Маленький заказ"
		WHEN count_product BETWEEN 100 AND 300 THEN "Средний заказ"
		WHEN count_product < 100 THEN "Большой заказ"
		ELSE "Неопределен"
		END
		AS "Тип"
FROM seminar_2.sales; 

DROP TABLE IF EXISTS orders;
CREATE TABLE orders
(
	employee_id VARCHAR(20),
    amount DECIMAL(5,2) NOT NULL,
    order_status VARCHAR(20) NOT NULL
);

INSERT INTO orders (employee_id, amount, order_status)
VALUES
('e03', 15.00, 'OPEN'),
('e01', 25.50, 'OPEN'),
('e05', 100.70, 'CLOSED'),
('e02', 22.18, 'OPEN'),
('e04', 9.50, 'CANCELLED'); 

SELECT * FROM orders;

SELECT employee_id, amount, order_status,
CASE 
WHEN order_status = 'OPEN' THEN "Order is in open state"
WHEN order_status = 'CLOSED' THEN "Order is closed"
WHEN order_status = 'CANCELLED' THEN "Order is cancelled"
ELSE "Not mentioned"
END
AS full_order_status
FROM orders;
