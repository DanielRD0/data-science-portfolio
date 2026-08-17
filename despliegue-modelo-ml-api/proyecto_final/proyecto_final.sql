-- Proyecto Final - Base de datos

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS proyecto_final;

-- Usar la base de datos
USE proyecto_final;

-- Tabla 1: usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL
);

-- Tabla 2: predicciones
CREATE TABLE predicciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(500) NOT NULL,
    prediccion VARCHAR(50) NOT NULL
);

SELECT * FROM proyecto_final.usuarios;