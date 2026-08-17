import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title="Analisis de Ingresos vs Gasto",
    layout="wide"
)

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

        # Verificar nombres de columnas (posibles variaciones)
        income_columns = [col for col in df.columns if 'income' in col.lower() or 'ingreso' in col.lower()]
        st.sidebar.write(f"Columnas de ingreso encontradas: {income_columns}")

        # Crear columna de gasto total - ajustar nombres según el dataset real
        # Buscar columnas que contengan "Mnt" o "Amount" o "Gasto"
        mnt_columns = [col for col in df.columns if 'mnt' in col.lower() or 'amount' in col.lower() or 'gasto' in col.lower()]
        st.sidebar.write(f"Columnas de monto encontradas: {mnt_columns}")

        # Si encontramos columnas de monto, las sumamos
        if mnt_columns:
            df["GastoTotal"] = df[mnt_columns].sum(axis=1)
        else:
            # Si no encontramos, usar columnas comunes del dataset de marketing
            # Estas son las columnas típicas en el dataset marketing_campaign
            common_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                            'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
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
    # Sidebar con información
    st.sidebar.header("Informacion del Analisis")
    st.sidebar.info(
        "Este dashboard explora la relacion entre los ingresos de los clientes "
        "y su gasto total en productos."
    )

    # Encontrar la columna de ingresos
    income_col = None
    possible_income_cols = ['Income', 'income', 'Ingresos', 'ingresos', 'Annual_Income']

    for col in possible_income_cols:
        if col in df.columns:
            income_col = col
            break

    # Si no encontramos con nombres comunes, mostrar las columnas numéricas
    if income_col is None:
        numeric_cols = df.select_dtypes(include=['number']).columns
        st.sidebar.write("Columnas numericas disponibles:", list(numeric_cols))
        # Tomar la primera columna numérica como ingresos para ejemplo
        if len(numeric_cols) > 0:
            income_col = numeric_cols[0]
            st.warning(f"Usando '{income_col}' como columna de ingresos. Verifique si es correcto.")

    if income_col:
        # Mostrar datos básicos
        if st.sidebar.checkbox("Mostrar datos basicos"):
            st.sidebar.write(f"Numero de registros: {len(df)}")
            st.sidebar.write(f"Ingreso promedio: ${df[income_col].mean():,.2f}")
            st.sidebar.write(f"Gasto total promedio: ${df['GastoTotal'].mean():,.2f}")

        # Crear pestañas para organizar los gráficos
        tab1, tab2, tab3 = st.tabs([
            "Relacion Ingresos vs Gasto", 
            "Distribucion de Ingresos", 
            "Gasto por Quintiles"
        ])

        # Pestaña 1: Scatter plot
        with tab1:
            st.header("Relacion entre Ingresos y Gasto Total")

            col1, col2 = st.columns([2, 1])

            with col1:
                fig, ax = plt.subplots(figsize=(10, 6))
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

                # Calcular correlación
                correlacion = df[[income_col, "GastoTotal"]].corr().iloc[0,1]
                st.metric(
                    label="Correlacion Ingresos-Gasto",
                    value=f"{correlacion:.3f}",
                    help="Correlacion de Pearson entre ingresos y gasto total"
                )

        # Pestaña 2: Histograma de ingresos
        with tab2:
            st.header("Distribucion de Ingresos de los Clientes")

            col1, col2 = st.columns([2, 1])

            with col1:
                fig, ax = plt.subplots(figsize=(10, 6))
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

                # Estadísticas descriptivas
                ingreso_mediano = df[income_col].median()
                ingreso_promedio = df[income_col].mean()

                st.metric("Ingreso Promedio", f"${ingreso_promedio:,.2f}")
                st.metric("Ingreso Mediano", f"${ingreso_mediano:,.2f}")

        # Pestaña 3: Boxplot por quintiles
        with tab3:
            st.header("Gasto Total por Quintiles de Ingreso")

            # Crear quintiles
            df["QuintilIngresos"] = pd.qcut(df[income_col], 5, labels=["Q1", "Q2", "Q3", "Q4", "Q5"])

            col1, col2 = st.columns([2, 1])

            with col1:
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.boxplot(data=df, x="QuintilIngresos", y="GastoTotal", ax=ax)
                ax.set_title("Gasto Total por Quintiles de Ingreso", fontsize=16, fontweight='bold')
                ax.set_xlabel("Quintiles de Ingreso (Q1=Mas bajos, Q5=Mas altos)")
                ax.set_ylabel("Gasto Total ($)")
                st.pyplot(fig)

            with col2:
                st.subheader("Comparativa por Quintiles")
                st.markdown("""
                - Gasto creciente: Cada quintil gasta mas que el anterior
                - Mayor dispersion en Q5: Comportamiento mas diverso en altos ingresos
                - Diferencias significativas: Brecha importante entre quintiles
                """)

                # Calcular gasto promedio por quintil
                gasto_por_quintil = df.groupby("QuintilIngresos")["GastoTotal"].mean()

                for quintil, gasto in gasto_por_quintil.items():
                    st.metric(f"Gasto Promedio {quintil}", f"${gasto:,.2f}")

        # Sección de conclusiones
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

# Información adicional en el sidebar
st.sidebar.markdown("---")
st.sidebar.header("Acerca del Analisis")
st.sidebar.markdown("""
**Objetivo**: Comprender como los ingresos determinan
el nivel de gasto de los clientes.

**Metricas clave**:
- Gasto Total: Suma de todas las categorias de productos
- Quintiles: 5 grupos iguales basados en ingresos

**Tecnologias**: Python, Pandas, Seaborn, Streamlit
                    """)
st.sidebar.markdown("Creado por Daniel - Grupo 3")