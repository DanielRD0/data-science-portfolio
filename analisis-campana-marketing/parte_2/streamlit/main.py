import streamlit as st
import pandas as pd
import plotly.express as px 
from PIL import Image
import numpy as np
import plotly.graph_objects as go
#Librerias utilizadas 


#Configuracion principal de visualizacion de pagina
st.set_page_config(layout="wide")


#Titulo principal, carga de imagen de portada
st.title("DASHBOARD VISUALIZACION DATA MARKETING")
try:
    imagen = Image.open("ingresos.jpg")
    st.image(imagen, caption="Hablemos de ingresos", use_container_width=True)
except FileNotFoundError:
    st.warning("Imagen de portada no encontrada.")

#Funcion para cargar datos con caché
@st.cache_data
def carga_data(datasets):
    if datasets == "marketing_campaign.xlsx":
        df = pd.read_excel("marketing_campaign.xlsx")
        return df
    else:
        st.error("Archivo no reconocido. Asegúrate de seleccionar 'marketing_campaign.xlsx'.")
        return None

# Limpiamos nuestro datasets , en esta ocasion solo debemos reemplazar por valores en 0.
def reemplazar_nulos(df):
    df_sin_nulos = df.fillna(0)
    return df_sin_nulos


#Barra lateral para seleccionar Dataset, ideal para cargar y navegar con 2 o más datasets
st.sidebar.header("Configuración del Dashboard")
dataset_select = st.sidebar.selectbox(
    "Selecciona un Dataset:",
    ("marketing_campaign.xlsx")
)


# Carga y limpieza de datos
df = carga_data(dataset_select)
df = reemplazar_nulos(df)

#Exploracion inicial del dataset, visualizacion de los primeros valores en formato tabla
if not df.empty:
    st.subheader(f"Explorando el Dataset: {dataset_select}")
    st.dataframe(df.head())

    st.markdown("----")

    st.subheader("Visualizaciones Basicas")

#Visualizaciones para nuestro Datasets de manera grafica y descriptiva

#Utilizamos un scatter para visualizar de manera dispersa los valores principales de nuestro analisis
if dataset_select == "marketing_campaign.xlsx":
    agrupacion_gastos = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)
    df['TotalGastos'] = agrupacion_gastos
    gastos_por_ingresos = df.groupby('Income')['TotalGastos'].sum().reset_index()
    fig_relaciongastosingresos = px.scatter(df, x="Income", y="TotalGastos",
                                            title="Ingresos vs Gastos")
    st.plotly_chart(fig_relaciongastosingresos, use_container_width=True)
    st.write("- Objetivo: Visualizar la relación directa entre ingresos y gasto.")

    #Desarrollo de texto  de datos descriptivos util para el analisis
st.write('¿Los ingresos determinan el gasto?')

st.markdown("""
La relación entre ingresos y gasto total no es tan lineal como podría suponerse.
A través de los gráficos, se revela una historia más matizada:
""")


#Linea de tendencia replicando el primer grafico y utilizando numpy para hacer un calculo de regresión lineal
fig = px.scatter(df, x="Income", y="TotalGastos", title="Ingresos vs Gastos")
x = df["Income"]
y = df["TotalGastos"]
coef = np.polyfit(x, y, 1)  # grado 1 = línea recta
poly1d_fn = np.poly1d(coef)

# Se agrega línea de tendencia
fig.add_trace(go.Scatter(
    x=x,
    y=poly1d_fn(x),
    mode='lines',
    name='Línea de tendencia',
    line=dict(color='gray', width=2, dash='dash')
))
st.plotly_chart(fig, use_container_width=True)

st.write('1. Correlación moderada: ¿Más ingreso, más gasto?')

st.markdown("""
El scatter plot muestra una correlación positiva moderada entre ingresos y gasto total.
La línea de tendencia indica que, en general, a mayor ingreso corresponde un mayor gasto. 
Sin embargo, la dispersión de los puntos sugiere que esta relación no es estricta: 
hay individuos con ingresos similares que gastan de forma muy distinta. Esto abre la puerta
a explorar factores como hábitos de consumo, prioridades personales o acceso a crédito.

""")

#Visualización mediante un histograma la distribucion de ingresos
fig_histograma_ingresos = px.histogram(df, x="Income", nbins=30,
                                       title="Distribución de ingresos")
st.plotly_chart(fig_histograma_ingresos, use_container_width=True)
st.write('- Objetivo: Entender la distribución de ingresos en la muestra.')


st.write('2. Distribución de ingresos: ¿Quiénes conforman la muestra?')

st.markdown("""
El histograma de ingresos revela si la muestra está concentrada en niveles bajos, medios o altos.
Una distribución sesgada hacia ingresos bajos podría explicar por qué algunos grupos gastan más 
proporcionalmente: podrían estar destinando una mayor parte de sus recursos a necesidades básicas,
o estar incurriendo en deuda para mantener cierto nivel de consumo.

""")


# #Visualización mediante un boxplot la comparación de niveles de ingresos y gastos 
df['Quintil_Ingreso'] = pd.qcut(df['Income'], 5, labels=[f'Q{i+1}' for i in range(5)])
fig_quintil_ingreso = px.box(df, x='Quintil_Ingreso', y='TotalGastos',
                             title='Gasto Total por Quintil de Ingreso',)
st.plotly_chart(fig_quintil_ingreso, use_container_width=True)
st.write('- Objetivo: Comparar el gasto entre distintos niveles de ingreso.')
st.markdown("""
• 	Quintil 1 (Q1): El 20%, con menores ingresos.
• 	Quintil 2 (Q2): El siguiente 20%, con ingresos bajos-medios.
• 	Quintil 3 (Q3): Ingresos medios.
• 	Quintil 4 (Q4): Ingresos medios-altos.
• 	Quintil 5 (Q5): El 20%, con mayores ingresos.

""")

st.write('3. Gasto por quintiles: ¿Gasta más quien más tiene?')

st.markdown("""
El boxplot segmentado por quintiles de ingreso permite comparar el gasto entre niveles. 
Se observa que los quintiles superiores tienden a gastar más en términos absolutos, pero 
no necesariamente de forma proporcional. En algunos casos, los quintiles bajos presentan 
gastos elevados en relación a sus ingresos, lo que podría indicar sobreendeudamiento, subsidios,
o presiones sociales de consumo.

""")

st.write('4. Segmentos que rompen la regla: ¿Quiénes son los outliers?')

st.markdown("""
Los puntos que se alejan de la línea de tendencia —individuos con ingresos bajos pero gasto alto— 
son especialmente interesantes. Estos casos podrían representar:
- Personas que reciben apoyo externo (familia, gobierno, ONGs).
- Estilos de vida que priorizan el consumo por encima del ahorro.
- Acceso a crédito informal o tarjetas de crédito con alto uso.
Estos outliers son clave para entender dinámicas ocultas en el comportamiento financiero de la población.
""")

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

st.write('Antes de culminar el analisis, probemos con nuestro datasets y busquemos otras correlaciones')
st.write('\n')

#Visualizacion mde otros valores de interes en nuestro datasets, con miras a tener una noción más amplia
opcion_segmento = st.selectbox("Filtrar por estado civil:", df['Marital_Status'].unique())
df_filtrado = df[df['Marital_Status'] == opcion_segmento]

fig_segmento = px.box(df_filtrado, x='Education', y='TotalGastos',
                      title=f"Gasto total por nivel educativo ({opcion_segmento})",)

st.plotly_chart(fig_segmento, use_container_width=True)



# Agrupamos consumidor por nivel educativoy sumar gastos
df_gasto_por_educacion = df.groupby('Education')['TotalGastos'].sum().reset_index()

# Creamos un gráfico de pie para visualizar
fig_pie = px.pie(df_gasto_por_educacion, names='Education', values='TotalGastos',
                title="Distribución de gasto por Nivel Educativo",
                color_discrete_sequence=px.colors.sequential.Blues)

st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("""
 Educación      Total de Gastos\n
 2n Cycle       100795\n
 Basic          4417\n
 Graduation     698626\n
 Master         226359\n
 PhD            326791\n
""")

# Agrupamos consumidor por situacion sentimental y sumar gastos
df_gasto_por_situacion_sentimental = df.groupby('Marital_Status')['TotalGastos'].sum().reset_index()

#gráfico de pie
fig_pie = px.pie(df_gasto_por_situacion_sentimental, names='Marital_Status', values='TotalGastos',
                title="Distribución del gasto por Situación Sentimental",
                color_discrete_sequence=px.colors.sequential.Blues)

st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("""
 Estado Civil   Total de Gastos\n
 Absurd         2385\n
 Alone          770\n
 Divorced       141666\n
 Married        510453\n
 Single         291112\n
 Together       352865\n
 Widow          56889\n
 YOLO           848\n
""")

st.title('Conclusión')

st.markdown("""
Aunque existe una relación entre ingresos y gasto, no es determinista. El análisis revela 
que el comportamiento financiero está influido por múltiples factores más allá del ingreso: 
cultura, acceso a recursos, decisiones personales y contexto económico. Identificar estos 
patrones permite diseñar estrategias de marketing más empáticas y segmentadas, enfocadas en 
necesidades reales y no solo en capacidad adquisitiva.

""")












