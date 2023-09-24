CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE parks (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    address TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    comment TEXT,
    points INTEGER,
    park_id INTEGER REFERENCES parks,
    user_id INTEGER REFERENCES users
);
