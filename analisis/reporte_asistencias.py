import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos\estudiante.csv')

print('\t\t\tESTUDIANTES')
print(df)


df1 = pd.read_csv('datos\datos_asistencia.csv')

print('\n\n\t\t\tASISTENCIAS')
print(df1)


asistencias_completas = pd.merge(df,df1,  how="right" )

print('\n\n\t\t\tAASISTENCIAS Y ESTUDIANTES')
print(asistencias_completas)


print('\n\n\t\t\tAASISTENCIAS Y ESTUDIANTES by cedula = 01059953377')
print(asistencias_completas[asistencias_completas.cedula == 105995377])

asistencias_completas[asistencias_completas.cedula == 105995377].to_csv('datos\datos_reporte_0105995377.csv', index=True)



asistencias_completas[asistencias_completas.cedula == 105995377]['materia'].value_counts().plot(kind='bar')
plt.show()