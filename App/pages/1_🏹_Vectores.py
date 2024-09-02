import streamlit as st

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
El orden en que se escriben las coordenadas es significativo y a veces se las identifica por su posición en una tupla ordenada (0,0,0); también se las puede representar con letras, como por ejemplo «la coordenada-x». [1](https://es.wikipedia.org/wiki/Sistema_de_coordenadas)
''')
    st.latex('''
\\begin{equation}
   (x_{0}, x_{1}, x_{2}, \\dots, x_{n})
\\end{equation}
''')
    # VECTOR COLUMNA Y VECTOR RENGLON
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

