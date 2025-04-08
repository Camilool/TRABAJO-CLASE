CREATE DATABASE if not exists libreria;
USE libreria;
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    numero VARCHAR(15) NOT NULL
);
CREATE TABLE IF NOT EXISTS libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    fecha_publicacion YEAR NOT NULL
);
CREATE TABLE IF NOT EXISTS ejemplares (
    id INT AUTO_INCREMENT PRIMARY KEY,
    libro_id INT NOT NULL,
    estado ENUM('available', 'borrowed') NOT NULL DEFAULT 'available',
    FOREIGN KEY (libro_id) REFERENCES libros(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ejemplar_id INT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE NOT NULL,
    estado ENUM('activo', 'finalizado') NOT NULL,
    FOREIGN KEY (ejemplar_id) REFERENCES ejemplares(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS devoluciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prestamo_id INT NOT NULL,
    fecha_real_devolucion DATE,
    estado_libro VARCHAR(50),
    estado ENUM('Pendiente', 'Completado') NOT NULL DEFAULT 'Pendiente',
    FOREIGN KEY (prestamo_id) REFERENCES prestamos(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    ejemplar_id INT NOT NULL,
    fecha_recibir DATE NOT NULL,
    fecha_limite_recibir DATE NOT NULL,
    puesto_reserva INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (ejemplar_id) REFERENCES ejemplares(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS historial_prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ejemplar_id INT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE NOT NULL,
    fecha_real_devolucion DATE,
    estado_libro VARCHAR(50),
    estado ENUM('Completado') NOT NULL DEFAULT 'Completado',
    FOREIGN KEY (ejemplar_id) REFERENCES ejemplares(id) ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
INSERT IGNORE INTO usuarios (nombre, email, numero) VALUES
('Feid Cáceres', 'feidcaceres@gmail.com', '3126714981'),
('Messi Alberto', 'messialberto@gmail.com', '3112345678');

INSERT INTO libros (nombre, autor, fecha_publicacion) VALUES
('Vidas de papel', 'Pablo Escobar', 1976),
('Arepa', 'Colombia', 1976);

INSERT INTO ejemplares (libro_id, estado) VALUES
(1, 'available'),
(2, 'borrowed');



SELECT * FROM usuarios;
