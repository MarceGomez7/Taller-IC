import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import mensaje 

class TestMensaje(unittest.TestCase):
    def test_mensaje(self):
        self.assertEqual(mensaje(), "¡Universidad Tecnológica Nacional!")

if __name__ == "__main__":
    unittest.main()
