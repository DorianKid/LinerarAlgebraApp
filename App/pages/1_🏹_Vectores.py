import streamlit as st
import random
import matplotlib.pyplot as plt
from graficos import recta, cuadricula, cuadricula_3D, polares

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
    st.header("Sistemas de Coordenadas")
    with st.expander("Ver"):
    
        largo = 8
        ubicaciones = [random.randint(-largo, largo) for _ in range(4)]
        while len(set(ubicaciones)) != 4: 
            ubicaciones = [random.randint(-largo, largo) for _ in range(4)]
            
        st.markdown(f'''
    **Definición**: Un sistema de coordenadas es un :blue[sistema de referencia] que utiliza uno o más números (coordenadas) para determinar unívocamente la posición
    de un punto u objeto geométrico. El orden en que se escriben las coordenadas es significativo y a veces se las identifica por su posición en una tupla ordenada 
    $(0,0,0)$; también se las puede representar con letras, como por ejemplo «la coordenada-x». [1](https://es.wikipedia.org/wiki/Sistema_de_coordenadas)
    
    #### Diferentes Sistemas de Coordenadas
    ##### Sistema de Coordenadas Lineal (Recta Real)
    Para representar un número de la recta real se emplean las letras mayúsculas y sus coordenadas correspondientes, por ejemplo: 
    **A({ubicaciones[0]})**, **B({ubicaciones[1]})**, **C({ubicaciones[2]})**, **D({ubicaciones[3]})**. 
    ''')
    
        ubicaciones = {"A":ubicaciones[0], "B":ubicaciones[1], "C":ubicaciones[2], "D":ubicaciones[3]}
        figura_recta = recta(largo, ubicaciones)
        st.pyplot(fig= figura_recta, use_container_width=True)
    
        st.markdown(f'''
    ##### Sistema de Coordenadas Rectangulares (Cartesianas 2-D) 
    Un sistema de coordenadas rectangulares se define por dos ejes ortogonales (perpendiculares*), también conocido como sistema de coordenadas cartesianas en 2-D, 
    que se intersectan en un punto llamado origen. 
    
    **Características principales**:
    * **Eje horizontal**: Comúnmente llamado eje de abscisas o eje $X$.
    * **Eje vertical**: Conocido como eje de ordenadas o eje $Y$.
    * **Perpendicularidad**: Los ejes $X$ e $Y$ son perpendiculares entre sí, formando un ángulo recto ($90^{{\\circ}}$) en el punto de intersección.
    * **Origen**: El punto donde los ejes se cruzan se denomina origen y se representa como $(0, 0)$.
    * **Escala**: Ambos ejes están igualmente escalados, lo que significa que una unidad en el eje $X$ representa la misma distancia que una unidad en el eje $Y$.
    * **Coordenadas**: La posición de cualquier punto en el plano se puede describir mediante un par ordenado $(x, y)$.
    
    **Sólo son sinónimos en el espacio euclídeo*.
    ###### Cuadrantes:
    En un sistema de coordenadas rectangulares, el plano se divide en cuatro cuadrantes, numerados en sentido antihorario:
    ''')
    
        largo_2D = 5
        pares = [(random.randint(-largo_2D, largo_2D), random.randint(-largo_2D, largo_2D)) for _ in range(3)]
        while len(set(pares)) != 3: 
            pares = [(random.randint(-largo_2D, largo_2D), random.randint(-largo_2D, largo_2D)) for _ in range(3)]
        pares = {f"{pares[0]}":pares[0], f"{pares[1]}":pares[1], f"{pares[2]}":pares[2]}
        figura_2D = cuadricula(largo_2D, pares)
        
        # Crear una columna central
        col1, col2, col3 = st.columns([1, 2, 1])
            
        with col2:  # Usar la columna central para el contenido
            st.pyplot(fig= figura_2D, use_container_width=True)
    
        st.markdown('''
    ##### Sistema de Coordenadas Cartesianas (3-D)
    Al igual que el sistema anterior, este sistema se define por tres ejes perependiculares entre sí (también se puede extender a $\\mathbb{R}^{n}$), 
    que se intersectan en un punto llamado origen. 
    
    **Características principales**:
    * **Eje horizontal**: Comúnmente llamado eje de abscisas o eje $X$.
    * **Eje vertical**: Conocido como eje de ordenadas o eje $Y$.
    * **Eje altura**: Conocido como el eje perpendicular al plano $XY$ o eje $Z$.
    * **Coordenadas**: La posición de cualquier punto en el plano se puede describir mediante una tupla ordenada $(x, y, z)$.
    ''')

        largo_3D = 5
        pares_3D = [(random.randint(-largo_3D, largo_3D), random.randint(-largo_3D, largo_3D), random.randint(-largo_3D, largo_3D)) for _ in range(3)]
        while len(set(pares_3D)) != 3: 
            pares_3D = [(random.randint(-largo_3D, largo_3D), random.randint(-largo_3D, largo_3D), random.randint(-largo_3D, largo_3D)) for _ in range(3)]
        pares_3D = {f"{pares_3D[0]}":pares_3D[0], f"{pares_3D[1]}":pares_3D[1], f"{pares_3D[2]}":pares_3D[2]}
        figura_3D = cuadricula_3D(largo_3D, pares_3D)

            # Crear una columna central
        col1, col2, col3 = st.columns([1, 2, 1])
            
        with col2:  # Usar la columna central para el contenido
            st.pyplot(fig= figura_3D, use_container_width=True)

        st.markdown('''
    ##### Sistema de Coordenadas Polares 
    Es un sistema de coordenadas bidimensional en el que cada punto del plano se determina por una distancia y un ángulo. 
    De manera más precisa, como sistema de referencia se toma: 

    Caracteristicas principales:
    * **Origen**: Un punto *O* del plano, al que se llama origen o polo; 
    * **Eje radial**: Una recta dirigida (o rayo, o segmento *OL*) que pasa por *O*, llamada eje polar (equivalente al eje x del sistema cartesiano).
    * **Coordenadas**: Todo punto *P* del plano corresponde a un par ordenado $(r, \\theta)$ donde $r$ es la distancia de *P* al origen y $\\theta$ es el ángulo formado entre el eje polar y la recta dirigida *OP*. Se conoce a $r$ como la «coordenada radial» mientras que el ángulo es la «coordenada angular» 
    * **Crecimiento**: El valor de $\\theta$ crece en sentido antihorario y decrece en sentido horario.     
    ''')

        largo_polar = 5
        puntos_polares = [(random.randint(0, largo_polar), (random.randint(1, largo_polar*2), random.randint(1, largo_polar*2))) for _ in range(3)]  
        while True: 
            denominadores = [den for (r, (num, den)) in puntos_polares] 
            numeradores = [den for (r, (num, den)) in puntos_polares] 
            if len(set(numeradores)) == len(numeradores) and len(set(denominadores)) == len(denominadores):
                break
            else:
                puntos_polares = [(random.randint(0, largo_polar), (random.randint(1, largo_polar*2), random.randint(1, largo_polar*2))) for _ in range(3)]  
                
        figura_polar = polares(largo_polar, puntos_polares)
        figura_polar_360 = polares(largo_polar, puntos_polares, radianes=False)
        
            # Crear una columna central
        col1, col2, col3 = st.columns([3, 1, 3])
            
        with col1:  # Usar la columna central para el contenido
            st.pyplot(fig= figura_polar, use_container_width=True)

        with col3:  # Usar la columna central para el contenido
            st.pyplot(fig= figura_polar_360, use_container_width=True)

    
    st.header("Vector Renglón y Vector Columna")
    with st.expander("Ver"):
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




        #figura_3D_int = cuadricula_3D_interactiva(largo_3D, pares_3D)
        
        # Crear una columna central
        #col1, col2, col3 = st.columns([1, 2, 1])
            
        #with col2:  # Usar la columna central para el contenido
            #st.plotly_chart(figura_3D_int)
