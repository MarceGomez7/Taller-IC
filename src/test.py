import unittest
from src.app import mensaje

class TestApp(unittest.TestCase):
    def test_mensaje(self):
        self.assertEqual(mensaje(), "¡Hola, CI!")

if __name__ == "__main__":
    unittest.main()
