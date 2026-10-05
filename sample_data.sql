INSERT INTO categories (category_name)
VALUES
('Electronics'),
('Accessories'),
('Furniture'),
('Stationery');


INSERT INTO suppliers
(supplier_name, phone, email, address)
VALUES
('ABC Suppliers', '9876543210', 'abc@gmail.com', 'Hyderabad'),
('XYZ Suppliers', '9876543211', 'xyz@gmail.com', 'Bangalore'),
('Global Traders', '9876543212', 'global@gmail.com', 'Chennai');

INSERT INTO suppliers
(supplier_name, phone, email, address)
VALUES
('Ramu Suppliers', '9876543210', 'ramu@gmail.com', 'Hyderabad'),
('lalitha Suppliers', '9876543211', 'lalitha@gmail.com', 'Bangalore'),
('People  Traders', '9876543212', 'people@gmail.com', 'Chennai');


INSERT INTO products
(product_name, category_id, supplier_id, price)
VALUES
('Laptop', 1, 1, 55000),
('Mouse', 2, 2, 800),
('Keyboard', 2, 2, 1500),
('Office Chair', 3, 3, 7500),
('Notebook', 4, 1, 100);


INSERT INTO inventory
(product_id, quantity)
VALUES
(1, 20),
(2, 50),
(3, 30),
(4, 15),
(5, 100);