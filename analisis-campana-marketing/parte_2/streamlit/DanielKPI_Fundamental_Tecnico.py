# ==============================================
# DanielKPI original
# ==============================================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Analisis de Ingresos vs Gasto", layout="wide")

# Título principal
st.title("Analisis: Relacion entre Ingresos y Gasto Total")
st.markdown("---")

# Cargar datos
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("marketing_campaign.xlsx")

        # Mostrar información sobre las columnas disponibles
        st.sidebar.subheader("Columnas en el dataset")
        st.sidebar.write(list(df.columns))

        # Columnas de ingreso
        income_columns = [col for col in df.columns if 'income' in col.lower() or 'ingreso' in col.lower()]
        st.sidebar.write(f"Columnas de ingreso encontradas: {income_columns}")

        # Columnas de gasto
        mnt_columns = [col for col in df.columns if 'mnt' in col.lower() or 'amount' in col.lower() or 'gasto' in col.lower()]
        st.sidebar.write(f"Columnas de monto encontradas: {mnt_columns}")

        # Crear columna de gasto total
        if mnt_columns:
            df["GastoTotal"] = df[mnt_columns].sum(axis=1)
        else:
            common_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
            available_columns = [col for col in common_columns if col in df.columns]
            if available_columns:
                df["GastoTotal"] = df[available_columns].sum(axis=1)
                st.sidebar.write(f"Columnas usadas para GastoTotal: {available_columns}")
            else:
                st.error("No se encontraron columnas de montos en el dataset")
                return None

        return df

    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return None

df = load_data()

if df is not None:
    st.sidebar.header("Informacion del Analisis")
    st.sidebar.info(
        "Este dashboard explora la relacion entre los ingresos de los clientes "
        "y su gasto total en productos."
    )

    # Encontrar columna de ingresos
    income_col = None
    possible_income_cols = ['Income', 'income', 'Ingresos', 'ingresos', 'Annual_Income']
    for col in possible_income_cols:
        if col in df.columns:
            income_col = col
            break
    if income_col is None:
        numeric_cols = df.select_dtypes(include=['number']).columns
        st.sidebar.write("Columnas numericas disponibles:", list(numeric_cols))
        if len(numeric_cols) > 0:
            income_col = numeric_cols[0]
            st.warning(f"Usando '{income_col}' como columna de ingresos. Verifique si es correcto.")

    if income_col:
        # Checkbox mostrar datos básicos
        if st.sidebar.checkbox("Mostrar datos basicos"):
            st.sidebar.write(f"Numero de registros: {len(df)}")
            st.sidebar.write(f"Ingreso promedio: ${df[income_col].mean():,.2f}")
            st.sidebar.write(f"Gasto total promedio: ${df['GastoTotal'].mean():,.2f}")

        # Pestañas
        tab1, tab2, tab3 = st.tabs([
            "Relacion Ingresos vs Gasto",
            "Distribucion de Ingresos",
            "Gasto por Quintiles"
        ])

        # Pestaña 1
        with tab1:
            st.header("Relacion entre Ingresos y Gasto Total")
            col1, col2 = st.columns([2,1])
            with col1:
                fig, ax = plt.subplots(figsize=(10,6))
                sns.scatterplot(data=df, x=income_col, y="GastoTotal", alpha=0.6, ax=ax)
                sns.regplot(data=df, x=income_col, y="GastoTotal", scatter=False, color="red", ax=ax)
                ax.set_title("Relacion entre Ingresos y Gasto Total", fontsize=16, fontweight='bold')
                ax.set_xlabel("Ingresos ($)")
                ax.set_ylabel("Gasto Total ($)")
                st.pyplot(fig)
            with col2:
                st.subheader("Hallazgos Clave")
                st.markdown("""
                - Tendencia positiva clara: A mayor ingreso, mayor gasto
                - Variabilidad importante: No todos los clientes con altos ingresos gastan mucho
                - Oportunidad de segmentacion: Identificar clientes de ingresos medios/bajos con alto gasto
                """)
                correlacion = df[[income_col, "GastoTotal"]].corr().iloc[0,1]
                st.metric(label="Correlacion Ingresos-Gasto", value=f"{correlacion:.3f}", help="Correlacion de Pearson entre ingresos y gasto total")

        # Pestaña 2
        with tab2:
            st.header("Distribucion de Ingresos de los Clientes")
            col1, col2 = st.columns([2,1])
            with col1:
                fig, ax = plt.subplots(figsize=(10,6))
                sns.histplot(df[income_col], bins=30, kde=True, ax=ax)
                ax.set_title("Distribucion de Ingresos", fontsize=16, fontweight='bold')
                ax.set_xlabel("Ingresos ($)")
                ax.set_ylabel("Frecuencia")
                st.pyplot(fig)
            with col2:
                st.subheader("Analisis de Distribucion")
                st.markdown("""
                - Concentracion en bajos/medios ingresos: La mayoria de clientes
                - Cola larga a la derecha: Pocos clientes con ingresos muy altos
                - Distribucion asimetrica: Sesgo positivo en los ingresos
                """)
                st.metric("Ingreso Promedio", f"${df[income_col].mean():,.2f}")
                st.metric("Ingreso Mediano", f"${df[income_col].median():,.2f}")

        # Pestaña 3
        with tab3:
            st.header("Gasto Total por Quintiles de Ingreso")
            df["QuintilIngresos"] = pd.qcut(df[income_col], 5, labels=["Q1","Q2","Q3","Q4","Q5"])
            col1, col2 = st.columns([2,1])
            with col1:
                fig, ax = plt.subplots(figsize=(10,6))
                sns.boxplot(data=df, x="QuintilIngresos", y="GastoTotal", ax=ax)
                ax.set_title("Gasto Total por Quintiles de Ingreso", fontsize=16, fontweight='bold')
                ax.set_xlabel("Quintiles de Ingreso (Q1=Mas bajos, Q5=Mas altos)")
                ax.set_ylabel("Gasto Total ($)")
                st.pyplot(fig)
            with col2:
                st.subheader("Comparativa por Quintiles")
                gasto_por_quintil = df.groupby("QuintilIngresos")["GastoTotal"].mean()
                for quintil, gasto in gasto_por_quintil.items():
                    st.metric(f"Gasto Promedio {quintil}", f"${gasto:,.2f}")

        # Conclusiones y recomendaciones
        st.markdown("---")
        st.header("Conclusiones y Recomendaciones")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Hallazgos Principales")
            st.markdown("""
            1. Relacion positiva confirmada: Los ingresos son un buen predictor del gasto
            2. Segmentacion clara: Los quintiles muestran diferencias significativas en patrones de gasto
            3. Oportunidad en segmentos medios: Clientes con ingresos medios que gastan proporcionalmente mas
            4. Diversidad en altos ingresos: Comportamiento heterogeneo en el quintil superior
            """)
        with col2:
            st.subheader("Recomendaciones de Marketing")
            st.markdown("""
            - Segmentar por capacidad de gasto: No solo por nivel de ingresos
            - Personalizar ofertas: Basado en patrones de gasto reales
            - Identificar clientes valiosos: De ingresos medios con alto gasto
            - Profundizar en Q5: Entender la diversidad de comportamientos
            """)

    else:
        st.error("No se encontro una columna de ingresos en el dataset")
else:
    st.error("No se pudieron cargar los datos. Verifique que el archivo 'marketing_campaign.xlsx' exista en la misma carpeta.")

st.sidebar.markdown("---")
st.sidebar.header("Acerca del Analisis")
st.sidebar.markdown("""
**Objetivo**: Comprender como los ingresos determinan
el nivel de gasto de los clientes.

**Metricas clave**:
- Gasto Total: Suma de todas las categorias de productos
- Quintiles: 5 grupos iguales basados en ingresos

**Tecnologias**: Python, Pandas, Seaborn, Streamlit, Plotly
""")
st.sidebar.markdown("Creado por Daniel - Grupo 3")

# ==============================================
# Dashboard alternativo (main)
# ==============================================
def dashboard_main():
    st.markdown("---")
    st.header("DASHBOARD VISUALIZACION DATA MARKETING - Alternativo")
    
    # Imagen de portada con fallback
    try:
        imagen = Image.open("ingresos.jpg")
        st.image(imagen, caption="Hablemos de ingresos", use_container_width=True)
    except:
        st.warning("Imagen de portada no encontrada. Generando placeholder...")
        fig_placeholder = px.imshow(np.random.randint(0,255,(300,800,3)), title="Dashboard Alternativo", width=800, height=300)
        st.plotly_chart(fig_placeholder)
    
    # Carga de datos
    df_alt = pd.read_excel("marketing_campaign.xlsx").fillna(0)
    df_alt['TotalGastos'] = df_alt[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)

    # Scatter + línea tendencia
    fig = px.scatter(df_alt, x="Income", y="TotalGastos", title="Ingresos vs Gastos")
    x = df_alt["Income"]
    y = df_alt["TotalGastos"]
    coef = np.polyfit(x, y, 1)
    poly1d_fn = np.poly1d(coef)
    fig.add_trace(go.Scatter(x=x, y=poly1d_fn(x), mode='lines', name='Línea de tendencia',
                             line=dict(color='gray', width=2, dash='dash')))
    st.plotly_chart(fig, use_container_width=True)

    # Histograma de ingresos
    fig_hist = px.histogram(df_alt, x="Income", nbins=30, title="Distribución de ingresos")
    st.plotly_chart(fig_hist, use_container_width=True)

    # Boxplot por quintiles
    df_alt['Quintil_Ingreso'] = pd.qcut(df_alt['Income'],5, labels=[f'Q{i+1}' for i in range(5)])
    fig_box = px.box(df_alt, x='Quintil_Ingreso', y='TotalGastos', title='Gasto Total por Quintil de Ingreso')
    st.plotly_chart(fig_box, use_container_width=True)

    # Segmentación por estado civil
    opcion_segmento = st.selectbox("Filtrar por estado civil:", df_alt['Marital_Status'].unique())
    df_filtrado = df_alt[df_alt['Marital_Status']==opcion_segmento]
    fig_seg = px.box(df_filtrado, x='Education', y='TotalGastos', title=f"Gasto total por nivel educativo ({opcion_segmento})")
    st.plotly_chart(fig_seg, use_container_width=True)

    # Pie charts educación y estado civil
    df_gasto_edu = df_alt.groupby('Education')['TotalGastos'].sum().reset_index()
    fig_pie_edu = px.pie(df_gasto_edu, names='Education', values='TotalGastos', title="Distribución de gasto por Nivel Educativo", color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig_pie_edu, use_container_width=True)

    df_gasto_estado = df_alt.groupby('Marital_Status')['TotalGastos'].sum().reset_index()
    fig_pie_estado = px.pie(df_gasto_estado, names='Marital_Status', values='TotalGastos', title="Distribución del gasto por Situación Sentimental", color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig_pie_estado, use_container_width=True)

    st.title("Conclusión Alternativa")
    st.markdown("""
    Aunque existe una relación entre ingresos y gasto, no es determinista. 
    Factores como cultura, decisiones personales y contexto económico influyen.
    Identificar estos patrones permite diseñar estrategias de marketing más segmentadas.
    """)

# ----------------------------
# Sidebar opción dashboard alternativo
# ----------------------------
if st.sidebar.checkbox("Mostrar Dashboard Alternativo"):
    dashboard_main()
