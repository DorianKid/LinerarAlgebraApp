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
    
    # Agregar un puntos en las posiciones deseadas
    for letra, punto in ubicaciones_puntos.items():
        ax.plot(punto, 0, 'ko', markersize=7, zorder=3)
        ax.text(punto, 0.35, letra, ha='center', va='top', fontweight='bold', fontsize=12)
    
    # Flechas
    ax.annotate("", xy=(largo_recta + 0.5, 0), xytext=(largo_recta + 0.4, 0), arrowprops=dict(color='#C83C2C', linewidth=2, headlength=10, headwidth=8))
    ax.annotate("", xy=(-largo_recta - 0.5, 0), xytext=(-largo_recta - 0.4, 0), arrowprops=dict(color='#C83C2C', linewidth=2, headlength=10, headwidth=8))
    
    # Ajustar los límites del lienzo
    ax.set_xlim(-largo_recta - 0.5, largo_recta + 0.5)
    ax.set_ylim(-0.5, 0.5)
    plt.close()

    return figura

def cuadricula(largo_cuadricula, pares_ordenados):
    # Configurar el tamaño de la figura
    figura = plt.figure(figsize=(largo_cuadricula*1.5, largo_cuadricula*1.5))

    # Crear el lienzo
    ax = plt.axes()

    # Ocultar los ejes
    ax.set_frame_on(False)
    
    # Establecer los ticks para que vayan de 1 en 1
    ax.set_xticks(range(-largo_cuadricula, largo_cuadricula+1))
    ax.set_yticks(range(-largo_cuadricula, largo_cuadricula+1))
    
    # Cuadricula
    ax.grid(True, linewidth=.5)

    # Dibujar la línea horizontal
    ax.axhline(0, xmin=0.04, xmax=0.96, color='#0f0f0f', linewidth=3, zorder=2)
    # Dibujar la línea vertical
    ax.axvline(0, ymin=0.04, ymax=0.96, color='#0f0f0f', linewidth=3, zorder=2)

    # Ocultar las etiquetas de los ticks
    ax.xaxis.set_tick_params(labelsize=0)
    ax.yaxis.set_tick_params(labelsize=0)

    # Dibujar las líneas horizontales (ticks)
    for i in range(-largo_cuadricula, largo_cuadricula+1):
      ax.axhline(i, xmin=0.49, xmax=0.51, color='#0f0f0f', linewidth=3, zorder=2)

    # Dibujar las líneas verticales (ticks)
    for i in range(-largo_cuadricula, largo_cuadricula+1):
      ax.axvline(i, ymin=0.49, ymax=0.51, color='#0f0f0f', linewidth=3, zorder=2)

    # Agregar etiquetas numéricas horizontales
    for i in range(-largo_cuadricula, 0):
      ax.text(i - 0.05, -0.3, str(i), ha='center', va='top', fontweight='bold', fontsize=13)
    for i in range(1, largo_cuadricula+1):
      ax.text(i, -0.3, str(i), ha='center', va='top', fontweight='bold', fontsize=13)

    # Agregar etiquetas numéricas verticales
    for i in range(-largo_cuadricula, 0):
      ax.text(-0.4, i + 0.15, str(i), ha='center', va='top', fontweight='bold', fontsize=13)
    for i in range(1, largo_cuadricula+1):
      ax.text(-0.35, i + 0.15, str(i), ha='center', va='top', fontweight='bold', fontsize=13)

    # Agregar x y y en el este
    ax.text(largo_cuadricula + 0.75, 0.23, "x", ha='center', va='top', fontweight='bold', fontsize=15)
    ax.text(0, largo_cuadricula + 1.1, "y", ha='center', va='top', fontweight='bold', fontsize=15)

    # Agregar numero de cuadrantes en el este
    ax.text(largo_cuadricula - .5, largo_cuadricula - .5, "I", ha='center', va='top', fontweight='roman', fontsize=25, color="blue")
    ax.text(-largo_cuadricula + .5, largo_cuadricula - .5, "II", ha='center', va='top', fontweight='roman', fontsize=25, color="blue")
    ax.text(-largo_cuadricula + .5, -largo_cuadricula + .5, "III", ha='center', va='top', fontweight='roman', fontsize=25,color="blue")
    ax.text(largo_cuadricula - .5, -largo_cuadricula + .5, "IV", ha='center', va='top', fontweight='roman', fontsize=25,color="blue")

    # Flechas horizontales
    ax.annotate("", xy=(largo_cuadricula + 0.55, 0), xytext=(largo_cuadricula + 0.4, 0), arrowprops=dict(color='#0f0f0f', linewidth=3, headlength=10, headwidth=8))
    ax.annotate("", xy=(-largo_cuadricula - 0.55, 0), xytext=(-largo_cuadricula - 0.4, 0), arrowprops=dict(color='#0f0f0f', linewidth=3, headlength=10, headwidth=8))

    # Flechas verticales
    ax.annotate("", xy=(0, largo_cuadricula + 0.55), xytext=(0, largo_cuadricula + 0.4), arrowprops=dict(color='#0f0f0f', linewidth=3, headlength=10, headwidth=8))
    ax.annotate("", xy=(0, -largo_cuadricula - 0.55), xytext=(0, -largo_cuadricula - 0.4), arrowprops=dict(color='#0f0f0f', linewidth=3, headlength=10, headwidth=8))

    # Agregar un puntos en las posiciones deseadas
    for letra, (x, y)  in pares_ordenados.items():
        ax.plot(x, y, 'o', markersize=7, zorder=3, color="#008000")
        if x == 0:
            ax.text(x + .75, y + 0.11, letra, ha='center', va='top', fontweight='normal', fontsize=10)
        elif x != 0 and y == -1: 
            ax.text(x, y - 0.25, letra, ha='center', va='top', fontweight='normal', fontsize=10)
        elif x == 0 and y == 0: 
            ax.text(x + .75, y - 0.75, letra, ha='center', va='top', fontweight='normal', fontsize=10)
        else:
            ax.text(x, y + 0.5, letra, ha='center', va='top', fontweight='normal', fontsize=10)
    
    # Ajustar los límites del lienzo
    ax.set_xlim(-largo_cuadricula - 1, largo_cuadricula + 1)
    ax.set_ylim(-largo_cuadricula - 1, largo_cuadricula + 1)
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
''')

    st.markdown('''
###### Cuadrantes 
En un sistema de coordenadas rectangulares, el plano se divide en cuatro cuadrantes, numerados en sentido antihorario:

1. **Cuadrante I**: $x > 0, y > 0$
2. **Cuadrante II**: $x < 0, y > 0$
3. **Cuadrante III**: $x < 0, y < 0$
4. **Cuadrante IV**: $x > 0, y < 0$
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
* **Eje**
* **Coordenadas**: La posición de cualquier punto en el plano se puede describir mediante una tupla ordenada $(x, y, z)$.

**Sólo son sinónimos en el espacio euclídeo*.
''')




    
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

