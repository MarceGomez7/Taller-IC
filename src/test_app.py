import sys
import os
import unittest

# Agregar la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import mensaje

class TestApp(unittest.TestCase):
    def test_mensaje(self):
        # Este test espera que la función mensaje() devuelva ¡Hola, CI!
        self.assertEqual(mensaje(), "¡Hola, clickeaste el Botón!")

if __name__ == "__main__":
    unittest.main()
