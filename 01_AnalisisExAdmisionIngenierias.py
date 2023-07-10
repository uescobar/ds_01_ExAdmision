import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


# cargar el dataset
df = pd.read_csv('../data/dataset_ExAdmisionIngenierias2020_2022.csv')
#st.write(df.shape)
#eliminar del dataset los registros con na
#df.dropna(inplace=True)


# Titulo

img = Image.open("getlogocabecera.png")
st.image(img, width=200)
st.write("")
st.markdown("<h1 style='text-align: center; color: red;'>Resultados Examen Admisión Ingenierías <br> 2020-2022</h1>", unsafe_allow_html=True)

st.subheader("Introducción")
st.markdown("""
            En esta página se muestra un breve análisis de los resultados del examen de 
            admisión que fue llevado a cabo en los años 2020 al 2022, aplicado
            en línea.
            """)

st.subheader("Características de la información")
st.markdown(f"""
    - El examen de admisión aplicado constó de **30 preguntas**, todas ellas del área de Matemáticas.
    - El dataset limpio cuenta con: **{df.shape[0]}** registros de aspirantes al área de Ingenierías.
    - Solo una porción tiene identificada la carrera, por lo que, al seleccionar la carrera se realizará estimaciones.
    - Es posible seleccionar el año de aplicación para conocer los resultados.

    """)





selecion_carrera = st.radio("Seleccione la carrera: ", ('Todas', 'Sistemas Computacionales', 'Civil'))
seleccion_periodo = st.radio("Seleccione el año: ", ('Todos', '2020', '2021', '2022'))

#if (seleccion_carrera != 'Todas'):
#    st.success("Filtrar por carrera")
#else:
#    st.success("Otros")

#if (seleccion_periodo != 'Todos'):
#    st.success("Filtrar por periodo")

st.markdown("""
    - ¿Qué variables tiene nuestro dataset?
    - ¿Cuál fue la distribución de los aciertos del examen de admisión?
    - ¿Cuánto se tardaron los aspirantes en contestar el examen?
    - ¿Influye el tiempo ocupado para contestar con el resultado del examen?
""")
questions = ['p01', 'p02', 'p03', 'p04',
       'p05', 'p06', 'p07', 'p08', 'p09', 'p10', 'p11', 'p12', 'p13', 'p14',
       'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24',
       'p25', 'p26', 'p27', 'p28', 'p29', 'p30']


st.write(df.info(verbose=True))

df['Aciertos'] = df[questions].sum(axis=1) 

# 
with st.echo(code_location="above"):
     st.write(df.head())
     fig1 = px.histogram(df['Aciertos'],
         
        template='gridon', 
        title="Aciertos Examen Admisión"
        )
     #fig1.update_layout(width=900,height=500)
     #fig1.update_xaxes(title_text='Barrio', title_font_color= 'black')
     #fig1.update_yaxes(title_text='Cantidad de Disturbios', title_font_color= 'b')
     #fig1.update_layout({
     #       'font_color' : '#2C3E50',
            #'font_color' : 'black',
     #       'plot_bgcolor': color,
     #       'paper_bgcolor': color,
     #   })
     fig1

     st.write(df['Aciertos'].mean())

