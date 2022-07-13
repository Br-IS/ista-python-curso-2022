from calendar import c
from cmath import pi
from doctest import OutputChecker
from flask import Flask, request
import csv
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/lista_estudiante')
def lista_estudiante():
    with open('datos\estudiante.csv') as archivo:
        reader = csv.reader(archivo)
        next(reader)
        lista = []
        for fila in reader:
            lista.append({
                'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
            })
    return json.dumps(sorted(lista, key=lambda x: x['cedula']))


@app.route('/lista_estudiante/<cedula>')
def lista_estudiante_cedula(cedula):
    with  open('datos\estudiante.csv') as archivo:
        reader = csv.reader(archivo)
        next(reader)
        lista = []
        for fila in reader:
            if fila[0] == cedula:
                lista.append({
                    'cedula': fila[0],
                    'primer_apellido': fila[1],
                    'segundo_apellido': fila[2],
                    'primer_nombre': fila[3],
                    'segundo_nombre': fila[4]
                })

    return json.dumps(lista)



@app.route('/registro_asistencia', methods=['POST'])
def registro_asistencia():
    
    with open('datos\datos_asistencia.csv', 'a' , newline='') as archivo:
        escritor = csv.writer(archivo,delimiter=',')
        escritor.writerow([request.json['cedula'],request.json['materia'],request.json['fecha_anio'],request.json['fecha_mes'],request.json['fecha_dia']])
    return 'Registro exitoso'

if __name__ == '__main__':
    app.run(debug=True)