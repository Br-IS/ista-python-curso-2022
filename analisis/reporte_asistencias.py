import pandas as pd
import matplotlib.pyplot as plt

# analisis punto numero 19
datos_estudiante = pd.read_csv('datos\estudiante.csv')

# analisis punto numero 20
datos_asistencia = pd.read_csv('datos\datos_asistencia.csv')

# analisis punto numero 21
asistencias_completas = pd.merge(datos_estudiante,datos_asistencia,  how="right" )
print('\n\n\t\t\tESTUDIANTES CON ASISTENCIAS')

# analisis punto numero 22
print(asistencias_completas)

# analisis punto numero 23
print('\n\n\t\t\tAASISTENCIAS Y ESTUDIANTES by cedula = 01059953377')
print(asistencias_completas[asistencias_completas.cedula == 105995377])

# analisis punto numero 24
asistencias_completas[asistencias_completas.cedula == 105995377].to_csv('datos\datos_reporte_0105995377.csv', index=True)

# analisis punto numero 25
asistencias_completas[asistencias_completas.cedula == 105995377]['materia'].value_counts().plot(kind='bar')
plt.show()