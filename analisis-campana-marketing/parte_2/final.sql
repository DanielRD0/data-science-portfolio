-- Crear la base de datos
CREATE DATABASE DB_NovaCruz;
USE DB_NovaCruz;

-- Crear tablas
CREATE TABLE Clientes (
    Id_cliente INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    Telefono VARCHAR(20) NOT NULL,
    Direccion VARCHAR(150),
    Fecha_registro DATE NOT NULL
);

CREATE TABLE Empleados (
    Id_empleado INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Cargo VARCHAR(50) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    Telefono VARCHAR(20) NOT NULL,
    Fecha_contratacion DATE NOT NULL
);

CREATE TABLE Servicios (
    Id_servicio INT PRIMARY KEY NOT NULL,
    Nombre_servicio VARCHAR(100) NOT NULL,
    Descripcion VARCHAR(200),
    Precio DECIMAL(10,2) NOT NULL
);

CREATE TABLE Ventas (
    Id_venta INT PRIMARY KEY NOT NULL,
    Id_cliente INT NOT NULL,
    Id_empleado INT NOT NULL,
    Fecha_venta DATE NOT NULL,
    Total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (Id_cliente) REFERENCES Clientes(Id_cliente),
    FOREIGN KEY (Id_empleado) REFERENCES Empleados(Id_empleado)
);

CREATE TABLE Detalle_Venta (
    Id_detalle INT PRIMARY KEY NOT NULL,
    Id_venta INT NOT NULL,
    Id_servicio INT NOT NULL,
    Cantidad INT NOT NULL,
    Subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (Id_venta) REFERENCES Ventas(Id_venta),
    FOREIGN KEY (Id_servicio) REFERENCES Servicios(Id_servicio)
);

CREATE TABLE Departamento (
    Id_departamento INT PRIMARY KEY NOT NULL,
    Nombre_departamento VARCHAR(100) NOT NULL,
    Id_empleado INT NOT NULL,
    FOREIGN KEY (Id_empleado) REFERENCES Empleados(Id_empleado)
);

-- Insertar datos
INSERT INTO Clientes (Id_cliente, Nombre, Apellido, Correo, Telefono, Direccion, Fecha_registro) VALUES
(1, 'Juan', 'Perez', 'juan.perez@gmail.com', '809-312-4567', 'Av. Central 123', '2020-01-15'),
(2, 'Maria', 'Gomez', 'maria.gomez@gmail.com', '829-456-7890', 'Calle Sur 456', '2021-03-22'),
(3, 'Carlos', 'Lopez', 'carlos.lopez@gmail.com', '849-876-5432', 'Av. Norte 789', '2022-07-10'),
(4, 'Ana', 'Martinez', 'ana.martinez@gmail.com', '809-432-1987', 'Calle Este 321', '2021-05-18'),
(5, 'Luis', 'Ramirez', 'luis.ramirez@gmail.com', '829-246-3579', 'Av. Oeste 654', '2022-09-25'),
(6, 'Sofia', 'Fernandez', 'sofia.fernandez@gmail.com', '849-135-7924', 'Calle Central 111', '2023-02-14'),
(7, 'Pedro', 'Santos', 'pedro.santos@gmail.com', '809-975-3146', 'Av. Libertad 222', '2020-11-30'),
(8, 'Lucia', 'Diaz', 'lucia.diaz@gmail.com', '829-864-2097', 'Calle Paz 333', '2021-08-05'),
(9, 'Miguel', 'Torres', 'miguel.torres@gmail.com', '849-753-1864', 'Av. Esperanza 444', '2022-12-01'),
(10, 'Elena', 'Mendez', 'elena.mendez@gmail.com', '809-159-7538', 'Calle Progreso 555', '2023-04-20');

INSERT INTO Empleados (Id_empleado, Nombre, Apellido, Cargo, Correo, Telefono, Fecha_contratacion) VALUES
(1, 'Juan', 'De la Cruz', 'CEO', 'juan.delacruz@empresa.com', '829-312-9045', '2020-01-10'),
(2, 'Crismar', 'Justina', 'Administrador de Servicios y Financiero', 'crismar.justina@empresa.com', '809-456-7821', '2020-03-15'),
(3, 'Ian', 'Arias', 'Administrador de Desarrollo y TI / DBA', 'ian.arias@empresa.com', '849-227-5638', '2020-06-12'),
(4, 'Aura', 'Lopez', 'Finanzas / Ventas / Servicios', 'aura.lopez@empresa.com', '809-678-1245', '2021-07-22'),
(5, 'Moises', 'Perez', 'Operaciones / Reportes', 'moises.perez@empresa.com', '829-543-2198', '2022-11-05'),
(6, 'Jose', 'Fernandez', 'Soporte / Desarrollo', 'jose.fernandez@empresa.com', '849-315-6720', '2020-06-30'),
(7, 'Miguel', 'Santos', 'Seguridad TI / Infraestructura', 'miguel.santos@empresa.com', '809-234-9817', '2022-04-18');

INSERT INTO Servicios (Id_servicio, Nombre_servicio, Descripcion, Precio) VALUES
(1, 'Software de gestión empresarial (ERP)', 'Desarrollo, implementación y mantenimiento de sistemas ERP para optimizar procesos empresariales.', 5000.00),
(2, 'Soluciones en la nube para almacenamiento seguro de datos', 'Implementación de servicios en la nube para almacenamiento y respaldo seguro de información empresarial.', 2000.00),
(3, 'Desarrollo de aplicaciones móviles y web', 'Diseño y desarrollo de aplicaciones móviles y web personalizadas según las necesidades del cliente.', 3500.00),
(4, 'Consultoría tecnológica para optimización de procesos internos', 'Asesoría especializada para mejorar y automatizar procesos internos mediante tecnología.', 1500.00),
(5, 'Diseño y desarrollo de bases de datos', 'Creación, optimización y mantenimiento de bases de datos eficientes y seguras.', 1200.00);

INSERT INTO Ventas (Id_venta, Id_cliente, Id_empleado, Fecha_venta, Total) VALUES
(1, 1, 2, '2022-08-15', 10000.00),
(2, 4, 4, '2023-01-20', 2000.00),
(3, 6, 3, '2023-07-05', 3500.00),
(4, 2, 1, '2023-04-10', 1500.00),
(5, 9, 7, '2024-02-18', 1200.00),
(6, 3, 5, '2023-09-12', 2400.00),
(7, 7, 6, '2023-11-03', 5000.00),
(8, 8, 2, '2024-01-15', 3500.00),
(9, 10, 3, '2024-03-22', 2000.00),
(10, 5, 4, '2024-04-10', 1500.00);

INSERT INTO Detalle_Venta (Id_detalle, Id_venta, Id_servicio, Cantidad, Subtotal) VALUES
(1, 1, 1, 2, 10000.00),
(2, 2, 2, 1, 2000.00),
(3, 3, 3, 1, 3500.00),
(4, 4, 4, 1, 1500.00),
(5, 5, 5, 1, 1200.00),
(6, 6, 2, 2, 2400.00),
(7, 7, 1, 1, 5000.00),
(8, 8, 3, 1, 3500.00),
(9, 9, 2, 1, 2000.00),
(10, 10, 4, 1, 1500.00);

INSERT INTO Departamento (Id_departamento, Nombre_departamento, Id_empleado) VALUES
(1, 'Dirección General', 1),
(2, 'Servicios y Finanzas', 2),
(3, 'Servicios y Finanzas', 4),
(4, 'Servicios y Finanzas', 5),
(5, 'Desarrollo y TI', 3),
(6, 'Desarrollo y TI', 6),
(7, 'Desarrollo y TI', 7);

-- CONSULTAS COMUNES

-- 1. Total de ventas por cliente
SELECT Id_cliente, SUM(Total) AS TotalGastado FROM Ventas GROUP BY Id_cliente;

-- 2. Total de ventas por empleado
SELECT Id_empleado, SUM(Total) AS TotalVendido FROM Ventas GROUP BY Id_empleado;

-- 3. Cantidad de ventas por empleado
SELECT Id_empleado, COUNT(*) AS VentasRealizadas FROM Ventas GROUP BY Id_empleado;

-- 4. Promedio de ventas por cliente
SELECT Id_cliente, AVG(Total) AS PromedioGastado FROM Ventas GROUP BY Id_cliente;

-- 5. Venta máxima y mínima por empleado
SELECT Id_empleado, MAX(Total) AS VentaMaxima, MIN(Total) AS VentaMinima FROM Ventas GROUP BY Id_empleado;

-- 6. Total de servicios vendidos por tipo
SELECT Id_servicio, SUM(Cantidad) AS TotalServiciosVendidos FROM Detalle_Venta GROUP BY Id_servicio;

-- 7. Clientes que han gastado más de 200
SELECT Id_cliente, SUM(Total) AS TotalGastado FROM Ventas GROUP BY Id_cliente HAVING SUM(Total) > 200;

-- 8. Empleados con más de 1 venta
SELECT Id_empleado, COUNT(*) AS VentasRealizadas FROM Ventas GROUP BY Id_empleado HAVING COUNT(*) > 1;

-- 9. Promedio de cantidad de servicios por venta
SELECT AVG(Cantidad) AS PromedioServiciosPorVenta FROM Detalle_Venta;

-- 10. Total de ventas y cantidad de clientes registrados por año
SELECT 
COUNT(C.Id_cliente) AS ClientesRegistrados,
SUM(V.Total) AS TotalVentas
FROM Clientes C LEFT JOIN 
Ventas V ON C.Id_cliente = V.Id_cliente;

-- VISTAS, JOINS Y UNION

-- Vista: Resumen de ventas por cliente
CREATE VIEW 
Vista_VentasPorCliente AS
SELECT c.Id_cliente, c.Nombre, c.Apellido, COUNT(v.Id_venta) AS CantidadVentas, SUM(v.Total) AS TotalGastado
FROM Clientes c
JOIN Ventas v ON c.Id_cliente = v.Id_cliente
GROUP BY c.Id_cliente, c.Nombre, c.Apellido;

-- Vista: Detalle de ventas con cliente y empleado
CREATE VIEW Vista_DetalleVentas AS
SELECT v.Id_venta, c.Nombre AS Cliente, e.Nombre AS Empleado, v.Fecha_venta, v.Total
FROM Ventas v
JOIN Clientes c ON v.Id_cliente = c.Id_cliente
JOIN Empleados e ON v.Id_empleado = e.Id_empleado;

-- Consulta JOIN: Listar cada venta con su cliente y empleado
SELECT v.Id_venta, c.Nombre AS Cliente, e.Nombre AS Empleado, v.Fecha_venta, v.Total
FROM Ventas v
JOIN Clientes c ON v.Id_cliente = c.Id_cliente
JOIN Empleados e ON v.Id_empleado = e.Id_empleado;

-- Consulta JOIN: Detalle de servicios vendidos en cada venta
SELECT v.Id_venta, c.Nombre AS Cliente, s.Nombre_servicio, dv.Cantidad, dv.Subtotal
FROM Ventas v
JOIN Clientes c ON v.Id_cliente = c.Id_cliente
JOIN Detalle_Venta dv ON v.Id_venta = dv.Id_venta
JOIN Servicios s ON dv.Id_servicio = s.Id_servicio;

-- UNION: Clientes y empleados registrados (nombre, correo, tipo)
SELECT Nombre, Correo, 'Cliente' AS Tipo FROM Clientes
UNION
SELECT Nombre, Correo, 'Empleado' AS Tipo FROM Empleados;

-- UNION: Listar todos los nombres y teléfonos de clientes y empleados
SELECT Nombre, Telefono FROM Clientes
UNION
SELECT Nombre, Telefono FROM Empleados;
