-- \c cc_db

-- CREATE TABLE "User" (
--     id UUID PRIMARY KEY,
--     username VARCHAR NOT NULL,
--     password VARCHAR NOT NULL,
--     email VARCHAR NOT NULL,
--     is_admin BOOLEAN NOT NULL
-- );

-- CREATE TABLE "Order" (
--     id UUID PRIMARY KEY,
--     user_id UUID REFERENCES "User"(id),
--     total_price DECIMAL NOT NULL,
--     status VARCHAR NOT NULL,
--     created_at TIMESTAMP NOT NULL,
--     updated_at TIMESTAMP NOT NULL
-- );

-- CREATE TABLE "Analytics" (
--     id UUID PRIMARY KEY,
--     order_id UUID REFERENCES "Order"(id),
--     user_id UUID REFERENCES "User"(id),
--     action VARCHAR NOT NULL,
--     timestamp TIMESTAMP NOT NULL
-- );

-- CREATE TABLE "Payment" (
--     id UUID PRIMARY KEY,
--     order_id UUID REFERENCES "Order"(id),
--     amount DECIMAL NOT NULL,
--     payment_method VARCHAR NOT NULL,
--     status VARCHAR NOT NULL,
--     created_at TIMESTAMP NOT NULL
-- );

-- CREATE TABLE "Menu" (
--     id UUID PRIMARY KEY,
--     name VARCHAR NOT NULL,
--     description TEXT,
--     price DECIMAL NOT NULL,
--     available BOOLEAN NOT NULL
-- );

-- CREATE TABLE "OrderItem" (
--     id UUID PRIMARY KEY,
--     order_id UUID REFERENCES "Order"(id),
--     menu_id UUID REFERENCES "Menu"(id),
--     quantity INTEGER NOT NULL,
--     price DECIMAL NOT NULL
-- );

-- CREATE TABLE "MenuAnalytics" (
--     id UUID PRIMARY KEY,
--     menu_id UUID REFERENCES "Menu"(id),
--     action VARCHAR NOT NULL,
--     count INTEGER NOT NULL,
--     timestamp TIMESTAMP NOT NULL
-- );

-- CREATE TABLE "ModifierCategory" (
--     id UUID PRIMARY KEY,
--     name VARCHAR NOT NULL
-- );

-- CREATE TABLE "Modifier" (
--     id UUID PRIMARY KEY,
--     category_id UUID REFERENCES "ModifierCategory"(id),
--     name VARCHAR NOT NULL,
--     additional_price DECIMAL NOT NULL
-- );

-- CREATE TABLE "MenuModifier" (
--     id UUID PRIMARY KEY,
--     menu_id UUID REFERENCES "Menu"(id),
--     modifier_id UUID REFERENCES "Modifier"(id)
-- );

-- CREATE TABLE "OrderItemModifier" (
--     id UUID PRIMARY KEY,
--     order_item_id UUID REFERENCES "OrderItem"(id),
--     modifier_id UUID REFERENCES "Modifier"(id)
-- );

CREATE TABLE "User" (
    id UUID PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    is_admin BOOLEAN NOT NULL
);

CREATE TABLE "Order" (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    total_price DECIMAL NOT NULL,
    status VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "User" (id)
);

CREATE TABLE "Payment" (
    id UUID PRIMARY KEY,
    order_id UUID NOT NULL,
    amount DECIMAL NOT NULL,
    payment_method VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (order_id) REFERENCES "Order" (id)
);

CREATE TABLE "OrderItem" (
    id UUID PRIMARY KEY,
    order_id UUID NOT NULL,
    item_id UUID NOT NULL,
    quantity INTEGER NOT NULL,
    price DECIMAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES "Order" (id),
    FOREIGN KEY (item_id) REFERENCES "Item" (id)
);

CREATE TABLE "ModifierCategory" (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE "Modifier" (
    id UUID PRIMARY KEY,
    category_id UUID NOT NULL,
    name VARCHAR NOT NULL,
    additional_price DECIMAL NOT NULL,
    FOREIGN KEY (category_id) REFERENCES "ModifierCategory" (id)
);

CREATE TABLE "Item" (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL,
    description TEXT,
    price DECIMAL NOT NULL,
    available BOOLEAN NOT NULL
);

CREATE TABLE "ItemModifier" (
    id UUID PRIMARY KEY,
    item_id UUID NOT NULL,
    modifier_id UUID NOT NULL,
    FOREIGN KEY (item_id) REFERENCES "Item" (id),
    FOREIGN KEY (modifier_id) REFERENCES "Modifier" (id)
);

CREATE TABLE "OrderItemModifier" (
    id UUID PRIMARY KEY,
    order_item_id UUID NOT NULL,
    modifier_id UUID NOT NULL,
    FOREIGN KEY (order_item_id) REFERENCES "OrderItem" (id),
    FOREIGN KEY (modifier_id) REFERENCES "Modifier" (id)
);

CREATE TABLE "Analytics" (
    id UUID PRIMARY KEY,
    order_id UUID NOT NULL,
    user_id UUID NOT NULL,
    action VARCHAR NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (order_id) REFERENCES "Order" (id),
    FOREIGN KEY (user_id) REFERENCES "User" (id)
);

CREATE TABLE "ItemAnalytics" (
    id UUID PRIMARY KEY,
    item_id UUID NOT NULL,
    action VARCHAR NOT NULL,
    count INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (item_id) REFERENCES "Item" (id)
);

-- Creating the "Menu" table that stores all Items
CREATE TABLE "Menu" (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL,
    item_id UUID NOT NULL,
    FOREIGN KEY (item_id) REFERENCES "Item" (id)
);
