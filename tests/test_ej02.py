import pytest
from src.ej02_def import coste_horas 
def test_coste_horas():
    assert coste_horas(5,10) == "El importe total 50"