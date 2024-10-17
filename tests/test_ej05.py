import pytest
from src.ej05_def2 import calcular_iva_21
def test_calcular_iva_21():
    assert calcular_iva_21(10,21) == "El precio final con iva 21.00 es: 2.1"