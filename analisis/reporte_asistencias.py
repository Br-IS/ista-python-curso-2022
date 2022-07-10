import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos\estudiante.csv')

print('\t\tESTUDIANTES')
print()
print(df)


df1 = pd.read_csv('datos\sistencia.csv')

print('\n\t\tASISTENCIAS')
print()
print(df1)


asistencias_completas = pd.merge(df,df1,  how="left" )

print('\n\t\tASISTENCIAS Y ESTUDIANTES')
print()
print(asistencias_completas)

print('\n\t\tASISTENCIAS Y ESTUDIANTES by cedula = 105995377')
print()
print(asistencias_completas[asistencias_completas.cedula == 105995377])

asistencias_completas[asistencias_completas.cedula == 105995377].to_csv('datos\eporte_105995377.csv', index=False)

asistencias_completas[asistencias_completas.cedula == 105995377]['materia'].value_counts().plot(kind='bar')

plt.show()
