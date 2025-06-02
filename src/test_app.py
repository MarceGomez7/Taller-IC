import sys
import os
import unittest

# Ajustar el sys.path para poder importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.logic import mensaje

class TestMensaje(unittest.TestCase):
    def test_mensaje(self):
        self.assertEqual(mensaje(), "¡Hola, clickeaste en el Botón!")

if __name__ == "__main__":
    unittest.main()
