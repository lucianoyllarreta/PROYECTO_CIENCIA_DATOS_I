 PROYECTO ECONOMÍA MUNDIAL
 La primera parte de nuestro proyecto se basó en analizar cómo distintos hechos históricos impactaron en la economía mundial durante las últimas décadas. El análisis se organiza a partir de cuatro eventos clave que marcaron cambios importantes en la economía global: la caída del Muro de Berlín (1989), el milagro chino (2001), la crisis financiera internacional de 2008 y la pandemia de Covid‑19 (2019). Para cada caso, se define un período previo y posterior al evento, lo que permite comparar cómo evolucionaron las principales variables económicas antes y después de cada shock.
Además, los datos se agrupan por regiones geográficas y bloques económicos para observar diferencias en el impacto según la zona. En el caso del Covid‑19, el foco está puesto especialmente en Argentina, analizando la evolución económica antes de la pandemia y durante los gobiernos de Macri y Fernández. 

from google.colab import files
upload  = files.upload()
     
import pandas as pd
df = pd.read_csv('disuguaglianza-economica-globale-e-povert-1980-2024.csv')

### CLASIFICACIÓN GEOGRÁFICA DE LOS PAÍSES ###

# AMÉRICA
america_del_sur = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
america_central_y_caribe = ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras','Nicaragua', 'Panama', 'Bahamas', 'Barbados', 'Cuba', 'Dominica','Dominican Republic', 'Grenada', 'Haiti', 'Jamaica', 'Saint Kitts and Nevis','Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago']
america_del_norte = ['Canada', 'United States', 'Mexico']

# EUROPA
europa = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina','Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland','France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy','Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Montenegro','Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania','Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland','Ukraine', 'United Kingdom']

# ÁFRICA
africa = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde','Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Cote d\'Ivoire','Democratic Republic of Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea','Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau','Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali','Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger','Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles','Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania','Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

# ASIA
asia = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan','Brunei', 'Cambodia', 'China', 'Georgia', 'India', 'Indonesia', 'Iran','Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan','Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal','North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar','Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan','Tajikistan', 'Thailand', 'Timor', 'Turkey', 'Turkmenistan','United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']

# OCEANÍA
oceania = ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia (country)','Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa','Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']
     

### BLOQUES ECONÓMICOS ###

# MERCOSUR
mercosur = ['Argentina', 'Brazil', 'Paraguay', 'Uruguay', 'Venezuela']

# PAÍSES EMERGENTES
brics = ['Brazil', 'Russia', 'India', 'China', 'South Africa','Egypt', 'Ethiopia', 'Iran', 'United Arab Emirates']

# PETRÓLEO/ENERGÍA
medio_oriente = ['Bahrain', 'Iran', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon','Oman', 'Palestine', 'Qatar', 'Saudi Arabia', 'Syria','United Arab Emirates', 'Yemen']

# CLUB DE PAÍSES DESARROLLADOS
ocde = ['Austria', 'Belgium', 'Canada', 'Chile', 'Colombia', 'Czechia', 'Denmark','Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland','Ireland', 'Israel', 'Italy', 'Japan', 'South Korea', 'Latvia', 'Lithuania','Luxembourg', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland','Portugal', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland','Turkey', 'United Kingdom', 'United States', 'Australia']

# UNIÓN EUROPEA
union_europea = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']
     
Dividimos nuevamente Europa
### EUROPA ###

union_europea = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia','Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece','Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg','Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia','Slovenia', 'Spain', 'Sweden']

europa_no_ue = ['Albania', 'Andorra', 'Belarus', 'Bosnia and Herzegovina', 'Iceland','Moldova', 'Montenegro', 'North Macedonia', 'Norway', 'Russia','Serbia', 'Switzerland', 'Ukraine', 'United Kingdom']

# Creamos DataFrame para Caída Muro Berlín (1984-1994)
df_muro_berlin = df[(df['year'] >= 1984) & (df['year'] <= 1994)]
     

display(df_muro_berlin)
     

# Creamos DataFrame para Milagro Chino (1996-2006)
df_milagro_chino = df[(df['year'] >= 1996) & (df['year'] <= 2006)]
     

display(df_milagro_chino)
     

# Creamos DataFrame Crisis Financiera (2003-2013)
df_crisis_financiera = df[(df['year'] >= 2003) & (df['year'] <= 2013)]
     
display(df_crisis_financiera)
     

# Creamos DataFrame COVID-19 (2014-2022)
df_covid_19 = df[(df['year'] >= 2014) & (df['year'] <= 2022)]
     

display(df_covid_19)

from google.colab import files
upload  = files.upload()
import pandas as pd
df = pd.read_csv('disuguaglianza-economica-globale-e-povert-1980-2024.csv')

# Re-definimos los subconjuntos temporales para asegurar que estén disponibles
df_muro_berlin = df[(df['year'] >= 1984) & (df['year'] <= 1994)]
df_milagro_chino = df[(df['year'] >= 1996) & (df['year'] <= 2006)]
df_crisis_financiera = df[(df['year'] >= 2003) & (df['year'] <= 2013)]
df_covid_19 = df[(df['year'] >= 2014) & (df['year'] <= 2022)]
### PRESENTACIÓN DEL DATASET ###

# 1. Información general del dataset
print("--- INFORMACIÓN GENERAL ---")
df.info()

# 2. Visualización de una sola fila aleatoria de Argentina
print("\n--- FILA ALEATORIA ---")
display(df[df['country'] == 'Argentina'].sample(1))

# 4. Dimensiones del dataset original
print(f"\nDimensiones totales: El dataset tiene {df.shape[0]} filas y {df.shape[1]} columnas.")
### CREACIÓN DEL GRÁFICO DE EVOLUCIÓN DEL PBI GLOBAL ###

import matplotlib.pyplot as plt
import pandas as pd

# 1. Limpieza y preparación de datos
df_limpio = df.dropna(subset=['gdp', 'year'])
es_1983 = df_limpio['year'] == 1983
if es_1983.any():
    min_pbi_1983 = df_limpio[es_1983]['gdp'].min()
    df_limpio = df_limpio[~((es_1983) & (df_limpio['gdp'] == min_pbi_1983))]

# 2. Groupby: Agrupamos por año
pbi_por_año = df_limpio.groupby('year')['gdp'].sum().reset_index()
año_min = int(pbi_por_año['year'].min())
año_max = int(pbi_por_año['year'].max())

# 3. Configuración del Gráfico con fondo negro
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Línea del PBI en color Cian brillante para contraste
plt.plot(pbi_por_año['year'], pbi_por_año['gdp'], color='#00FFFF', linewidth=3, label='Evolución del PBI Global')

# 4. Hitos Históricos con colores vibrantes
hitos = {
    1989: 'Caída Muro de Berlín',
    2001: 'Milagro Chino',
    2008: 'Crisis Financiera',
    2020: 'COVID-19'
}

y_max = pbi_por_año['gdp'].max()

for anio, evento in hitos.items():
    # Línea vertical amarilla neón para alto contraste
    plt.axvline(x=anio, color='#FFFF00', linestyle='--', linewidth=2)

    # Texto con fondo negro y letra blanca
    plt.text(anio - 0.5, y_max * 0.90, evento,
             rotation=90, color='white', fontsize=11, fontweight='bold',
             ha='right', va='top',
             bbox=dict(facecolor='black', alpha=0.7, edgecolor='none', pad=3))

# 5. Títulos y Etiquetas
plt.title(f'EVOLUCIÓN DEL PBI GLOBAL ({año_min} - {año_max})', fontsize=16, fontweight='bold', color='white', pad=20)

plt.xlabel('Año', fontsize=12, fontweight='bold', color='white')
plt.ylabel('PBI (Billones de dólares)', fontsize=12, fontweight='bold', color='white')

plt.xticks(range(año_min, año_max + 1, 2), rotation=45, color='white')
plt.yticks(color='white')

# Grilla y leyenda
plt.grid(axis='y', linestyle='--', alpha=0.2)
plt.legend(loc='upper left', fontsize=11, facecolor='black', edgecolor='white')
plt.tight_layout()

plt.show()
plt.style.use('default')

