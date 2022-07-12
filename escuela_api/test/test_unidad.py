from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.lista_estudiante_cedula('0105995377') == '[{"cedula": "0105995377", "primer_apellido": "Quizhpe", "segundo_apellido": "Romero", "primer_nombre": "Boris", "segundo_nombre": "Xavier"}]'