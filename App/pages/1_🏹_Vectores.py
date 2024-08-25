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
    st.subheader("Vector Renglón y Vector Columna")
    st.markdown('''
**Definición**: Un :red[vector de n componentes] se define como un conjunto ordenado de :red[n] números escritos de la siguiente manera:
''')
    st.latex('''
\\begin{equation}
\\begin{bmatrix}
   x_{0}, x_{1}, x_{2}, \\dots, x_{n}
\\end{bmatrix}
\\end{equation}
''')

    st.markdown('''
**Definición**: Un :red[vector columna de n componentes] se define como un conjunto ordenado de :red[n] números escritos de la siguiente manera:
''')
    st.latex('''
\\begin{equation}
\\begin{bmatrix}
   x_{0} \\\\
   x_{1} \\\\
   x_{2} \\\\
   \\vdots \\\\
   x_{n}
\\end{bmatrix}
\\end{equation}
''')

