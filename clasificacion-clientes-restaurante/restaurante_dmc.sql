-- CREAR BASE DE DATOS
CREATE DATABASE IF NOT EXISTS restaurante_dmc;
USE restaurante_dmc;

-- TABLA CLIENTES
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sexo ENUM('M','F') NOT NULL,
    fecha_registro DATE NOT NULL
);

-- TABLA PRODUCTOS (PLATOS)
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(100),
    precio DECIMAL(10,2) NOT NULL
);

-- TABLA VENTAS
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_producto INT NOT NULL,
    fecha_venta DATE NOT NULL,
    cantidad INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);


INSERT INTO clientes (nombre, sexo, fecha_registro) VALUES
('Juan Perez',   'M', '2023-08-11'),
('Ana Gomez',    'F', '2023-05-27'),
('Carlos Lopez', 'M', '2023-08-02'),
('Maria Ruiz',   'F', '2023-07-07'),
('Luis Sanchez', 'M', '2023-09-21'),
('Laura Diaz',   'F', '2024-02-27'),
('Pedro Ramirez','M', '2024-12-05'),
('Sofia Herrera','F', '2024-01-13'),
('Miguel Torres','M', '2024-11-14'),
('Lucia Morales','F', '2024-06-01');


INSERT INTO productos (nombre, categoria, precio) VALUES
('Hamburguesa clásica', 'Plato fuerte', 8.50),
('Pizza pepperoni',     'Plato fuerte', 10.00),
('Ensalada César',      'Entrada',      6.00),
('Pasta Alfredo',       'Plato fuerte', 9.50),
('Tacos de pollo',      'Plato fuerte', 7.50),
('Soda',                'Bebida',       1.50),
('Jugo natural',        'Bebida',       2.00),
('Postre del día',      'Postre',       4.00);


INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad, total) VALUES
(7, 7, '2024-01-21', 2, 4.00),
(9, 8, '2024-07-26', 2, 8.00),
(8, 6, '2024-10-25', 1, 1.50),
(9, 3, '2024-05-24', 1, 6.00),
(2, 5, '2024-09-29', 3, 22.50),
(10, 3, '2024-06-07', 1, 6.00),
(2, 6, '2024-08-29', 3, 4.50),
(2, 6, '2024-08-10', 2, 3.00),
(10, 4, '2024-10-09', 2, 19.00),
(8, 5, '2024-02-01', 3, 22.50),
(1, 2, '2024-07-23', 3, 30.00),
(1, 8, '2024-06-19', 1, 4.00),
(6, 2, '2024-04-07', 3, 30.00),
(4, 4, '2024-03-13', 3, 28.50),
(8, 2, '2024-02-11', 2, 20.00),
(6, 1, '2024-08-08', 3, 25.50),
(9, 6, '2024-02-29', 1, 1.50),
(9, 2, '2024-01-25', 1, 10.00),
(3, 1, '2024-09-07', 1, 8.50),
(1, 6, '2024-08-03', 3, 4.50),
(5, 5, '2024-04-22', 3, 22.50),
(6, 3, '2024-01-14', 2, 12.00),
(5, 3, '2024-01-28', 2, 12.00),
(7, 1, '2024-07-08', 2, 17.00),
(8, 8, '2024-12-04', 1, 4.00),
(10, 8, '2024-04-03', 1, 4.00),
(6, 4, '2024-11-04', 2, 19.00),
(3, 7, '2024-03-22', 1, 2.00),
(6, 7, '2024-03-02', 2, 4.00),
(9, 4, '2024-03-19', 2, 19.00),
(6, 2, '2024-07-25', 1, 10.00),
(1, 1, '2024-11-11', 1, 8.50),
(6, 8, '2024-05-31', 2, 8.00),
(4, 6, '2024-09-13', 1, 1.50),
(10, 1, '2024-03-30', 2, 17.00),
(3, 5, '2024-03-20', 2, 15.00),
(10, 6, '2024-08-16', 2, 3.00),
(4, 5, '2024-08-06', 3, 22.50),
(6, 6, '2024-09-15', 1, 1.50),
(9, 1, '2024-09-25', 1, 8.50),
(9, 1, '2024-05-08', 3, 25.50),
(1, 7, '2024-01-16', 2, 4.00),
(2, 7, '2024-05-21', 2, 4.00),
(9, 5, '2024-06-11', 2, 15.00),
(3, 8, '2024-11-09', 2, 8.00),
(4, 3, '2024-02-09', 1, 6.00),
(2, 2, '2024-07-04', 2, 20.00),
(8, 1, '2024-07-24', 1, 8.50),
(4, 2, '2024-09-06', 1, 10.00),
(4, 1, '2024-12-12', 1, 8.50),
(3, 6, '2024-09-28', 2, 3.00),
(2, 8, '2024-12-06', 1, 4.00),
(1, 8, '2024-12-14', 2, 8.00),
(10, 5, '2024-11-28', 2, 15.00),
(7, 5, '2024-03-19', 3, 22.50),
(1, 8, '2024-02-10', 2, 8.00),
(1, 5, '2024-03-10', 1, 7.50),
(8, 6, '2024-11-08', 2, 3.00),
(6, 3, '2024-06-07', 2, 12.00),
(7, 2, '2024-01-01', 3, 30.00),
(4, 6, '2024-03-22', 1, 1.50),
(4, 8, '2024-07-12', 3, 12.00),
(10, 7, '2024-01-17', 2, 4.00);


-- CONSULTA PARA EL DATASET MODELO DE MACHINEEE LEARNING

SELECT
    c.id_cliente,
    c.sexo,
    COUNT(v.id_venta)                AS cantidad_consumos,
    SUM(v.total)                     AS total_consumido,
    DATEDIFF(CURDATE(), MAX(v.fecha_venta)) AS dias_desde_ultimo_consumo,
    CASE
        WHEN COUNT(v.id_venta) >= 5
             OR SUM(v.total) >= 80
        THEN 1       -- cliente frecuente
        ELSE 0       -- no frecuente
    END AS es_frecuente
FROM clientes c
JOIN ventas v ON c.id_cliente = v.id_cliente
GROUP BY c.id_cliente, c.sexo
ORDER BY c.id_cliente;