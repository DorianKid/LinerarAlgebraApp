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

    ### OTRAS REFERENCIAS 
    # Kurosch, A. G. (1968). *Curso de álgebra superior*. Moscow: Mir Publishers (Издательство "Мир")

    # Matrix's order 
    st.subheader("Vector Columna y Vector Renglón")
    st.markdown('''
**Definición**: Un :red[vector de n componentes] se define como un conjunto ordenado de :red[n] números escritos de la siguiente manera:
''')
    st.latex('''
\\begin{bmatrix}
   a \\
   b \\
   c
\\end{bmatrix}
''')

    # Matrix's elements 
    st.subheader("Elements of the Matrix")
    st.markdown('''
    **Definition**: The elements of a matrix are the individual values that make up the matrix. If $A$ is a matrix of order $m \\times n$, then each element $a_{ij}$ of $A$ is located at the intersection of the $i$-th row and the $j$-th column.

Grossman, S. (2012). *Álgebra Lineal*. (7$^{\\textrm{ma}}$ ed., pp. 48) McGraw Hill. 
    ''')
