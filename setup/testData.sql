-- Connect to the database
\c coffee_connections_database

-- Insert Users
INSERT INTO "User" (id, username, password, email, is_admin) VALUES
('123e4567-e89b-12d3-a456-426614174000', 'john_doe', 'password123', 'john@example.com', FALSE),
('123e4567-e89b-12d3-a456-426614174001', 'jane_doe', 'password123', 'jane@example.com', FALSE),
('123e4567-e89b-12d3-a456-426614174002', 'admin_user', 'adminpassword', 'admin@example.com', TRUE);

-- Insert Menu Items
INSERT INTO "Menu" (id, name, description, price, available) VALUES
('223e4567-e89b-12d3-a456-426614174000', 'Espresso', 'Strong and bold espresso', 2.50, TRUE),
('223e4567-e89b-12d3-a456-426614174001', 'Cappuccino', 'Espresso with steamed milk and foam', 3.50, TRUE),
('223e4567-e89b-12d3-a456-426614174002', 'Latte', 'Espresso with steamed milk', 3.75, TRUE);

-- Insert Modifier Categories
INSERT INTO "ModifierCategory" (id, name) VALUES
('323e4567-e89b-12d3-a456-426614174000', 'Milk Options'),
('323e4567-e89b-12d3-a456-426614174001', 'Flavor Shots');

-- Insert Modifiers
INSERT INTO "Modifier" (id, category_id, name, additional_price) VALUES
('423e4567-e89b-12d3-a456-426614174000', '323e4567-e89b-12d3-a456-426614174000', 'Almond Milk', 0.50),
('423e4567-e89b-12d3-a456-426614174001', '323e4567-e89b-12d3-a456-426614174000', 'Soy Milk', 0.50),
('423e4567-e89b-12d3-a456-426614174002', '323e4567-e89b-12d3-a456-426614174001', 'Vanilla', 0.25),
('423e4567-e89b-12d3-a456-426614174003', '323e4567-e89b-12d3-a456-426614174001', 'Caramel', 0.25);

-- Link Modifiers to Menu Items
INSERT INTO "MenuModifier" (id, menu_id, modifier_id) VALUES
('523e4567-e89b-12d3-a456-426614174000', '223e4567-e89b-12d3-a456-426614174001', '423e4567-e89b-12d3-a456-426614174000'),
('523e4567-e89b-12d3-a456-426614174001', '223e4567-e89b-12d3-a456-426614174001', '423e4567-e89b-12d3-a456-426614174001'),
('523e4567-e89b-12d3-a456-426614174002', '223e4567-e89b-12d3-a456-426614174001', '423e4567-e89b-12d3-a456-426614174002'),
('523e4567-e89b-12d3-a456-426614174003', '223e4567-e89b-12d3-a456-426614174001', '423e4567-e89b-12d3-a456-426614174003');

-- Insert Orders
INSERT INTO "Order" (id, user_id, total_price, status, created_at, updated_at) VALUES
('623e4567-e89b-12d3-a456-426614174000', '123e4567-e89b-12d3-a456-426614174000', 3.75, 'Completed', '2024-07-01 08:30:00', '2024-07-01 08:35:00'),
('623e4567-e89b-12d3-a456-426614174001', '123e4567-e89b-12d3-a456-426614174001', 4.00, 'Pending', '2024-07-01 09:00:00', '2024-07-01 09:05:00');

-- Insert Order Items
INSERT INTO "OrderItem" (id, order_id, menu_id, quantity, price) VALUES
('723e4567-e89b-12d3-a456-426614174000', '623e4567-e89b-12d3-a456-426614174000', '223e4567-e89b-12d3-a456-426614174002', 1, 3.75),
('723e4567-e89b-12d3-a456-426614174001', '623e4567-e89b-12d3-a456-426614174001', '223e4567-e89b-12d3-a456-426614174001', 1, 3.50);

-- Insert Order Item Modifiers
INSERT INTO "OrderItemModifier" (id, order_item_id, modifier_id) VALUES
('823e4567-e89b-12d3-a456-426614174000', '723e4567-e89b-12d3-a456-426614174001', '423e4567-e89b-12d3-a456-426614174000'),
('823e4567-e89b-12d3-a456-426614174001', '723e4567-e89b-12d3-a456-426614174001', '423e4567-e89b-12d3-a456-426614174002');

-- Insert Payments
INSERT INTO "Payment" (id, order_id, amount, payment_method, status, created_at) VALUES
('923e4567-e89b-12d3-a456-426614174000', '623e4567-e89b-12d3-a456-426614174000', 3.75, 'Credit Card', 'Completed', '2024-07-01 08:35:00'),
('923e4567-e89b-12d3-a456-426614174001', '623e4567-e89b-12d3-a456-426614174001', 4.00, 'Credit Card', 'Pending', '2024-07-01 09:05:00');

-- Insert Analytics
INSERT INTO "Analytics" (id, order_id, user_id, action, timestamp) VALUES
('a23e4567-e89b-12d3-a456-426614174000', '623e4567-e89b-12d3-a456-426614174000', '123e4567-e89b-12d3-a456-426614174000', 'Order Placed', '2024-07-01 08:30:00'),
('a23e4567-e89b-12d3-a456-426614174001', '623e4567-e89b-12d3-a456-426614174000', '123e4567-e89b-12d3-a456-426614174000', 'Payment Completed', '2024-07-01 08:35:00');

-- Insert Menu Analytics
INSERT INTO "MenuAnalytics" (id, menu_id, action, count, timestamp) VALUES
('b23e4567-e89b-12d3-a456-426614174000', '223e4567-e89b-12d3-a456-426614174000', 'Item Ordered', 1, '2024-07-01 08:30:00'),
('b23e4567-e89b-12d3-a456-426614174001', '223e4567-e89b-12d3-a456-426614174001', 'Item Ordered', 1, '2024-07-01 09:00:00');
