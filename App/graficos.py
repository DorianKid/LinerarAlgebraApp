import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import numpy as np

def polares(largo, puntos_polares, radianes=True):
    # Configurar el tamaño de la figura
    figura = plt.figure(figsize=(largo*1.5, largo*1.5))
    
    # Crear el lienzo con proyección polar
    ax = plt.subplot(111, projection='polar')
    
    # Configurar los límites radiales
    ax.set_ylim(0, largo)
    
    # Configurar las etiquetas de los ángulos en radianes
    if radianes:
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))
        ax.set_xticklabels([r'$\; 0, 2\pi$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', 
                        r'$\pi$', r'$\frac{5\pi}{4}$', r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$'], color="red")
        # Marcar el punto especificado
        for (r, (numerador, denominador)) in puntos_polares:
            ax.plot(numerador * np.pi / denominador, r, 'ko', markersize=6, zorder=3)
            texto_latex = f'({r}, $\\pi/{denominador}$)' if numerador == 1 else f'({r}, $\\frac{{{numerador}\\pi}}{{{denominador}}}$)' if denominador != 1 else f'({r}, ${int(numerador/denominador)}\\pi$)' if numerador%denominador == 0 else f'({r}, ${numerador}\\pi$)'  
            ax.text(numerador * np.pi / denominador, r, texto_latex, ha='right', va='bottom')
    else: 
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))
        # Marcar el punto especificado
        for (r, (numerador, denominador)) in puntos_polares:
            ax.plot(numerador * np.pi / denominador, r, 'ko', markersize=6, zorder=3)
            texto = f'({r}, {numerador*180/denominador:.2f}°)' if numerador*180%denominador != 0 else f'({r}, {numerador*180/denominador:.0f}°)'
            ax.text(numerador * np.pi / denominador, r, texto, fontsize="small", ha='right', va='bottom')

    # Configurar las etiquetas radiales
    ax.set_yticklabels(range(1, largo+1), color="blue")
    
    # Dibujar líneas radiales
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        ax.plot([angle, angle], [0, largo], color='#C83C2C', linestyle='--', linewidth=1)
    
    # Ajustar el diseño
    plt.close()
    return figura
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

def cuadricula_3D(largo_cuadricula, pares_ordenados):
    # Configurar el tamaño de la figura
    figura = plt.figure(figsize=(largo_cuadricula*1.5, largo_cuadricula*1.5))
    
    # Crear el lienzo 3D
    ax = figura.add_subplot(111, projection='3d')
    
    # Configurar los límites de los ejes
    ax.set_xlim(-largo_cuadricula, largo_cuadricula)
    ax.set_ylim(-largo_cuadricula, largo_cuadricula)
    ax.set_zlim(-largo_cuadricula, largo_cuadricula)
    
    # Establecer los ticks para que vayan de 1 en 1
    ax.set_xticks(range(-largo_cuadricula, largo_cuadricula+1))
    ax.set_yticks(range(-largo_cuadricula, largo_cuadricula+1))
    ax.set_zticks(range(-largo_cuadricula, largo_cuadricula+1))

    # Dibujar los ejes principales
    ax.plot([-largo_cuadricula, largo_cuadricula], [0, 0], [0, 0], color='black', linewidth=2)
    ax.plot([0, 0], [-largo_cuadricula, largo_cuadricula], [0, 0], color='black', linewidth=2)
    ax.plot([0, 0], [0, 0], [-largo_cuadricula, largo_cuadricula], color='black', linewidth=2)

    # Agregar flechas al final de los ejes
    ax.quiver(0, 0, 0, largo_cuadricula, 0, 0, color='black', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, largo_cuadricula, 0, color='black', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, largo_cuadricula, color='black', arrow_length_ratio=0.1)
    
    # Agregar etiquetas de los ejes en las partes positivas
    ax.text(largo_cuadricula + 0.6, 0, -0.1, 'X', fontsize=12)
    ax.text(0, largo_cuadricula + 0.5, -0.15, 'Y', fontsize=12)
    ax.text(0 , -0.15, largo_cuadricula + 0.5, 'Z', fontsize=12)
    
    # Agregar puntos en las posiciones deseadas
    for (letra, (x, y, z)), color in zip(pares_ordenados.items(), ["red", "blue", "green"]):
        #ax.quiver(0, 0, 0, x, y, z, color=color, arrow_length_ratio=0.075)
        ax.scatter(x, y, z, color=color, s=50, zorder=3)
        ax.text(1.15*x, 1.15*y, 1.15*z, letra, fontsize=10)
    
    # Ajustar la vista
    ax.view_init(elev=20, azim=45)
    plt.tight_layout()

    plt.close()
    return figura
    
def cuadricula_3D_interactiva(largo_cuadricula, pares_ordenados):
    # Crear la figura 3D
    figura = go.Figure()

    # Dibujar las líneas de la cuadrícula
    for i in range(-largo_cuadricula, largo_cuadricula+1):
        figura.add_trace(go.Scatter3d(x=[-largo_cuadricula, largo_cuadricula], y=[i, i], z=[0, 0],
                                   mode='lines', line=dict(color='gray', width=1, dash='dot')))
        figura.add_trace(go.Scatter3d(x=[i, i], y=[-largo_cuadricula, largo_cuadricula], z=[0, 0],
                                   mode='lines', line=dict(color='gray', width=1, dash='dot')))
        figura.add_trace(go.Scatter3d(x=[i, i], y=[0, 0], z=[-largo_cuadricula, largo_cuadricula],
                                   mode='lines', line=dict(color='gray', width=1, dash='dot')))

    # Dibujar los ejes principales
    figura.add_trace(go.Scatter3d(x=[-largo_cuadricula, largo_cuadricula], y=[0, 0], z=[0, 0],
                               mode='lines', line=dict(color='black', width=4)))
    figura.add_trace(go.Scatter3d(x=[0, 0], y=[-largo_cuadricula, largo_cuadricula], z=[0, 0],
                               mode='lines', line=dict(color='black', width=4)))
    figura.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-largo_cuadricula, largo_cuadricula],
                               mode='lines', line=dict(color='black', width=4)))

    # Agregar puntos en las posiciones deseadas
    for letra, (x, y, z) in pares_ordenados.items():
        figura.add_trace(go.Scatter3d(x=[x], y=[y], z=[z],
                                   mode='markers+text', text=[letra], textposition='top center',
                                   marker=dict(color='green', size=5)))

    # Configurar los límites de los ejes
    figura.update_layout(scene=dict(
        xaxis=dict(range=[-largo_cuadricula, largo_cuadricula], title='X'),
        yaxis=dict(range=[-largo_cuadricula, largo_cuadricula], title='Y'),
        zaxis=dict(range=[-largo_cuadricula, largo_cuadricula], title='Z')
    ))
    return figura
