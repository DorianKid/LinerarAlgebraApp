import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="🤝🏼",
    layout="wide",    
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)

st.write("# ¡Bienvenido! 🤝🏼")

st.markdown(
    """
    #### ¡Bienvenido a *Pracphy*, tu plataforma de estudio y práctica para la licenciatura en Física en la Universidad de Guadalajara!
    ### ¿Qué es Álgebra Lineal I?
    #### Álgebra Lineal I es una unidad de aprendizaje fundamental para la carrera. Este curso te introducirá a conceptos clave como: 
    - Vectores
    - Independencia Lineal
    - Matriz Escalonada
    - Eigenvalues
    
    Estos conocimientos son esenciales para comprender y modelar una amplia gama de fenómenos físicos y matemáticos.**
    ## ¿Qué aprenderás?
    #### A lo largo de esta página web, explorarás seis unidades temáticas principales:

    1. [Vectores](https://algebralinear.streamlit.app/Vectores)
    2. [Matrices y Determinantes](https://algebralinear.streamlit.app/Matrices_y_Determinantes)
    3. [Espacios Vectoriales](https://algebralinear.streamlit.app/Espacios_Vectoriales)
    4. [Sistemas de Ecuaciones Lineales](https://algebralinear.streamlit.app/Sistemas_de_Ecuaciones_Lineales)
    5. [Transformaciones Lineales](https://algebralinear.streamlit.app/Transformaciones_Lineales)
    6. [Diagonalización](https://algebralinear.streamlit.app/Diagonalizacion)

    Cada unidad te proporcionará las herramientas necesarias para desarrollar tu pensamiento lógico-matemático y aplicar estos conceptos en diversos ámbitos de la física y las matemáticas.
    ### ¿Cómo usar esta plataforma?
    Pracphy está diseñada para complementar tus clases presenciales. Aquí encontrarás:

    - **Resúmenes teóricos de cada unidad**
    - **Ejercicios prácticos con soluciones paso a paso**
    - **Colección de videos explicativos**
    - **Descarga de ejercicios prácticos**
    - **Recursos adicionales para profundizar en los temas**
    
    Nuestro objetivo es ayudarte a desarrollar las competencias necesarias para comprender y aplicar los métodos del Álgebra Lineal en tu carrera universitaria.
    
    ¡Descubre cómo estas herramientas matemáticas pueden ayudarte a entender mejor el universo que nos rodea pero hasta que hayas entendido esto! 
"""
)
