''''Este diseño incluye una clase que representa una máquina de infusión, 
con comportamientos como reabastecimiento, preparación de té con o sin azúcar, 
y verificación de ingredientes, además de pruebas unitarias y el esquema de base de datos.'''
"""import BS_MAQUINA.sql"""""
class MaquinaInfusion:
    def __init__(self):
        self.agua = 0
        self.te = 0
        self.azucar = 0

    def reabastecer(self, agua, te, azucar):
        """Reabastece la máquina de infusión con agua, té y azúcar."""
        self.agua += agua
        self.te += te
        self.azucar += azucar

    def preparar_infusion(self, tipo, cantidad_azucar):
        """Prepara una infusión (té o té con azúcar)."""
        if tipo == 'te' and self.agua >= 100 and self.te >= 5:
            self.agua -= 100
            self.te -= 5
            if cantidad_azucar > 0 and self.azucar >= cantidad_azucar:
                self.azucar -= cantidad_azucar
                return f"Té con {cantidad_azucar}g de azúcar preparado"
            return "Té preparado"
        return "Ingredientes insuficientes"

    def verificar_ingredientes(self):
        """Devuelve el estado actual de los ingredientes."""
        return f"Agua: {self.agua}ml, Té: {self.te}g, Azúcar: {self.azucar}g"

    def __str__(self):
        """Representación de los niveles actuales de ingredientes."""
        return self.verificar_ingredientes()

# Pruebas unitarias con unittest

import unittest

class TestMaquinaInfusion(unittest.TestCase):
    def setUp(self):
        self.maquina = MaquinaInfusion()

    def test_preparar_te_sin_azucar(self):
        """Test para preparar té sin azúcar."""
        self.maquina.reabastecer(200, 10, 50)
        resultado = self.maquina.preparar_infusion('te', 0)
        self.assertEqual(resultado, "Té preparado")

    def test_preparar_te_con_azucar(self):
        """Test para preparar té con azúcar."""
        self.maquina.reabastecer(200, 10, 50)
        resultado = self.maquina.preparar_infusion('te', 10)
        self.assertEqual(resultado, "Té con 10g de azúcar preparado")

    def test_ingredientes_insuficientes(self):
        """Test cuando faltan ingredientes."""
        self.maquina.reabastecer(50, 5, 10)
        resultado = self.maquina.preparar_infusion('te', 5)
        self.assertEqual(resultado, "Ingredientes insuficientes")

    def test_verificar_ingredientes(self):
        """Test para verificar el estado de los ingredientes."""
        self.maquina.reabastecer(100, 5, 5)
        estado = self.maquina.verificar_ingredientes()
        self.assertEqual(estado, "Agua: 100ml, Té: 5g, Azúcar: 5g")

if __name__ == '__main__':
    unittest.main()
///BASE DE DATOS:
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
