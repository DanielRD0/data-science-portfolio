--DDL - Data Definition Language
--DML - Data Manipulation Language
--DCL - Data Control Language
--TCL - Transaction Control Language

USE AdventureWorks2022;
GO

-- 1. Estructura de tablas
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'Practice')
BEGIN
    EXEC('CREATE SCHEMA Practice')
END
GO

CREATE TABLE Practice.Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Practice.Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    NombreProducto VARCHAR(100),
    Categoria VARCHAR(50),
    Precio DECIMAL(10, 2)
);

CREATE TABLE dbo.Ordenes (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT,
    ProductID INT,
    Cantidad INT,
    FechaOrden DATE,
    FOREIGN KEY (CustomerID) REFERENCES Practice.Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Practice.Products(ProductID)
);
GO

-- 2. Insertar Datos (7 registros por tabla)
INSERT INTO Practice.Customers (Nombre, Email) VALUES
('Juan Perez', 'juan@test.com'), ('Maria Lopez', 'maria@test.com'),
('Pedro Diaz', 'pedro@test.com'), ('Ana Gomez', 'ana@test.com'),
('Luis Pena', 'luis@test.com'), ('Carla Ruiz', 'carla@test.com'),
('Sofia Mota', 'sofia@test.com');

INSERT INTO Practice.Products (NombreProducto, Categoria, Precio) VALUES
('Laptop', 'Electronica', 1200.00), ('Mouse', 'Accesorios', 25.00),
('Teclado', 'Accesorios', 45.00), ('Monitor', 'Electronica', 300.00),
('Silla', 'Muebles', 250.00), ('Mesa', 'Muebles', 150.00),
('Auriculares', 'Audio', 80.00);

INSERT INTO dbo.Ordenes (CustomerID, ProductID, Cantidad, FechaOrden) VALUES
(1, 1, 1, '2026-01-10'), (2, 2, 5, '2026-01-11'),
(3, 3, 2, '2026-01-11'), (4, 1, 1, '2026-01-12'),
(5, 5, 1, '2026-01-12'), (6, 7, 3, '2026-01-13'),
(7, 4, 1, '2026-01-14');
GO

-- 3. Join Requerido
SELECT 
    c.Nombre, 
    c.Email, 
    p.NombreProducto, 
    p.Categoria, 
    o.Cantidad, 
    o.FechaOrden
FROM dbo.Ordenes o
JOIN Practice.Customers c ON o.CustomerID = c.CustomerID
JOIN Practice.Products p ON o.ProductID = p.ProductID;

-- 4. Updates Requeridos
UPDATE Practice.Customers SET Email = 'nuevo@test.com' WHERE CustomerID = 1;
UPDATE Practice.Products SET Categoria = 'Multimedia' WHERE Categoria = 'Audio';
UPDATE dbo.Ordenes SET Cantidad = 10 WHERE OrderID = 2;