CREATE TABLE maquina_infusion (
    id INT PRIMARY KEY,
    agua_ml INT,
    te_g INT,
    azucar_g INT
);
'''SENTENCIAS INSERT'''
INSERT INTO maquina_infusion VALUES (1, 200, 15, 50);
INSERT INTO maquina_infusion VALUES (2, 100, 10, 30);
INSERT INTO maquina_infusion VALUES (3, 150, 5, 40);
INSERT INTO maquina_infusion VALUES (4, 120, 8, 20);
INSERT INTO maquina_infusion VALUES (5, 100, 10, 10);
INSERT INTO maquina_infusion VALUES (6, 180, 15, 35);
INSERT INTO maquina_infusion VALUES (7, 90, 7, 25);
INSERT INTO maquina_infusion VALUES (8, 200, 12, 50);
INSERT INTO maquina_infusion VALUES (9, 140, 10, 30);
INSERT INTO maquina_infusion VALUES (10, 160, 8, 40);
'''CONSULTAS'''
SELECT * FROM maquina_infusion WHERE id = 1;
'''Extrae todos los campos de la fila donde el id es igual a 1.'''
SELECT agua_ml, te_g, azucar_g FROM maquina_infusion WHERE id = 2;
'''Obtiene las columnas agua_ml, te_g y azucar_g de la fila con id igual a 2'''
SELECT * FROM maquina_infusion WHERE azucar_g < 20;
'''Selecciona todas las filas donde la cantidad de azúcar (azucar_g) sea menor a 20 gramos.'''
SELECT * FROM maquina_infusion ORDER BY agua_ml DESC;
'''Extrae todos los datos y los ordena por la columna agua_ml de mayor a menor.
'''
SELECT * FROM maquina_infusion WHERE te_g BETWEEN 5 AND 15;
'''Filtra las filas donde la cantidad de té (te_g) esté entre 5 y 15 gramos.'''