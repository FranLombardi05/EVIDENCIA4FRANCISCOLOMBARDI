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