import streamlit as st
import random
import matplotlib.pyplot as plt

def recta(largo_recta, ubicaciones_puntos):
    # Configurar el tamaño de la figura
    figura = plt.figure(figsize=(largo_recta*1.5, 1.5))
    
    
    # Crear el lienzo 
    ax = plt.axes()
    
    # Ocultar los ejes
    ax.set_axis_off()
    
    # Dibujar la línea horizontal
    ax.axhline(0, color='#C83C2C', linewidth=2, zorder=1)
    
    # Dibujar las líneas verticales (ticks)
    for i in range(-largo_recta, largo_recta + 1):
        ax.axvline(i, ymin=0.35, ymax=0.65, color='#C83C2C', linewidth=2, zorder=1)
    
    # Agregar etiquetas numéricas
    for i in range(-largo_recta, largo_recta + 1):
        ax.text(i, -0.3, str(i), ha='center', va='top', fontweight='bold', fontsize=12)
    
    # Agregar un punto en la posición deseada
    for punto in ubicaciones_puntos:
        ax.plot(punto, 0, 'ko', markersize=7, zorder=3)
    
    # Flechas
    ax.annotate("", xy=(largo_recta + 0.5, 0), xytext=(largo_recta + 0.4, 0), arrowprops=dict(color='#C83C2C', linewidth=2, headlength=10, headwidth=8))
    ax.annotate("", xy=(-largo_recta - 0.5, 0), xytext=(-largo_recta - 0.4, 0), arrowprops=dict(color='#C83C2C', linewidth=2, headlength=10, headwidth=8))
    
    # Ajustar los límites del lienzo
    ax.set_xlim(-largo_recta - 0.5, largo_recta + 0.5)
    ax.set_ylim(-0.5, 0.5)
    plt.close()

    return figura

st.set_page_config(
    page_title="Vectores",
    page_icon="🏹",  
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Todo bien, ¡suerte!"}
)

# Inicializar el estado de la sesión si no existe
if 'page' not in st.session_state:
    st.session_state.page = 'generate'
    
if st.session_state.page == 'generate':
    st.title("Vectores")
    st.header("Definiciones")
    st.subheader("Sistemas de Coordenadas")
    st.markdown('''
**Definición**: Un sistema de coordenadas es un :blue[sistema de referencia] que utiliza uno o más números (coordenadas) para determinar unívocamente la posición de un punto u objeto geométrico. 
El orden en que se escriben las coordenadas es significativo y a veces se las identifica por su posición en una tupla ordenada $(0,0,0)$; también se las puede representar con letras, como por ejemplo «la coordenada-x». 

#### Diferentes Sistemas de Coordenadas
##### Recta Real
Para representar un número de la recta real se emplean las letras mayúsculas y sus coordenadas correspondientes, por ejemplo, los puntos A(5), B(3), C(-3), D(-5), etc. [1](https://es.wikipedia.org/wiki/Sistema_de_coordenadas)

''')
    punto = random.randint(5, 10)
    ubicaciones = [random.randint(-punto, punto) for _ in range(4)]
    figura_recta = recta(punto, ubicaciones)
    st.pyplot(fig= figura_recta, use_container_width=True)
    
    st.subheader("Vector Renglón y Vector Columna")
    st.markdown('''
**Definición**: Un :red[vector de n componentes] se define como un conjunto ordenado de :red[n] números escritos de la siguiente manera:
''')
    st.latex('''
\\begin{equation}
   (x_{0}, x_{1}, x_{2}, \\dots, x_{n})
\\end{equation}
''')

    st.markdown('''
**Definición**: Un :red[vector columna de n componentes] se define como un conjunto ordenado de :red[n] números escritos de la siguiente manera:
''')
    st.latex('''
\\begin{equation}
\\begin{pmatrix}
   x_{0} \\\\
   x_{1} \\\\
   x_{2} \\\\
   \\vdots \\\\
   x_{n}
\\end{pmatrix}
\\end{equation}
''')

