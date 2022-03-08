.mode column
.header on

.open employee.db

CREATE TABLE devices (
    device_id INTEGER PRIMARY KEY,
    device_name TEXT NOT NULL,
    release_date INTEGER NOT NULL
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    employee_age INTEGER NOT NULL,
    employee_device INTEGER NOT NULL,
    FOREIGN KEY(employee_device) REFERENCES devices(device_id)
);

INSERT INTO devices VALUES (1001, "Apple 1", 1979);
INSERT INTO devices VALUES (1002, "Apple 2", 1981);
INSERT INTO devices VALUES (1003, "Mac", 1982);
INSERT INTO devices VALUES (1004, "iMac", 1985);
INSERT INTO devices VALUES (1005, "MacBook", 1989);

INSERT INTO employees VALUES (1, "Steve Wozniak", 72, 1001);
INSERT INTO employees VALUES (2, "Steve Jobs", 81, 1001);
INSERT INTO employees VALUES (3, "Steve Chicken", 4, 1003);
INSERT INTO employees VALUES (4, "John Doe", 104, 1002);
INSERT INTO employees VALUES (5, "Mike Wazowksi", 48, 1004);
INSERT INTO employees VALUES (6, "Chicken Farid", 10, 1005);
