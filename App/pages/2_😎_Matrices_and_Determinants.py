import streamlit as st
import random

### Funciones basicas principales ###
def get_scalar(min_value,max_value):
    return random.randint(min_value,max_value)

def get_colors(index):
    colors = ["red", "blue", "green", "orange", "purple", 
          "black", "pink", "brown", "gray", "maroon",
          "scarlet", "crimson", "burgundy", "navy", "teal",
          "indigo", "gold", "lemon", "mustard",
          "violet", "orchid", "plum", "turquoise", "magenta",
          "salmon", "peach", "baby pink", "sky blue", "mint green",
          "sienna", "umber", "ochre", "silver", "bronze",
          "neon pink", "neon green", "neon blue"]
    return colors[:index]

def get_colors_matrix(matrix):
    matrix_height, matrix_width = len(matrix), len(matrix[0])
    num_colors = matrix_height * matrix_width
    colors = get_colors(num_colors)
    color_matrix = []

    index = 0
    for row in matrix:
        color_row = []
        for _ in row:
            color_row.append(colors[index])
            index += 1
        color_matrix.append(color_row)

    return color_matrix

def generate_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix

### Funciones para ejercicios ###
def matrix_addition(A, B):
    new_matrix = []
    for i in range(len(A)):
        new_row = []
        for j in range(len(A[0])):
            new_row.append(A[i][j] + B[i][j])
        new_matrix.append(new_row)
    return new_matrix

def matrix_scalar_multiplication(scalar, A):
    new_matrix = []
    for i in range(len(A)):
        new_row = []
        for j in range(len(A[0])):
            new_row.append(scalar * A[i][j])
        new_matrix.append(new_row)
    return new_matrix

def matrix_multiplication(A, B):
    new_matrix = []
    for i in range(len(A)):
        new_row = []
        for j in range(len(B[0])):
            new_value = 0
            for k in range(len(B)):
                new_value += A[i][k] * B[k][j]
                #print(A[i][k] * B[k][j], new_value)
            new_row.append(new_value)
        new_matrix.append(new_row)
    return new_matrix

def matrix_transpose(A):
    new_matrix = []
    for i in range(len(A[0])):
        new_row = []
        for j in range(len(A)):
            new_row.append(A[j][i])
        new_matrix.append(new_row)
    return new_matrix

def determinant(matrix):
    # Base case for a 1x1 matrix:
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case for a 2x2 matrix:
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c+1:] for row in (matrix[1:])]
        print('\n'.join([str(sublista) for sublista in sub_matrix]))
        print(det)
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    
    return det

def cofactor(matrix, i, j):
    sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    return ((-1) ** (i + j)) * determinant(sub_matrix)

def attached_matrix(matrix):
    adj_matrix = []
    for i in range(len(matrix)):
        adj_row = []
        for j in range(len(matrix)):
            adj_row.append(cofactor(matrix, i, j))
        adj_matrix.append(adj_row)
    return adj_matrix

def inverse_matrix(matrix):
    det = determinant(matrix)
    adj = attached_matrix(matrix)
    transpose_adj = matrix_transpose(adj)
    return matrix_scalar_multiplication(1/det, transpose_adj)

### Funciones para escritura latex ###
def matrix_to_latex(matrix):
    latex = r'\begin{bmatrix}'
    for row in matrix:
        latex += ' & '.join(map(str, row)) + r'\\'
    latex += r'\end{bmatrix}'
    return latex

def determinant_to_latex(matrix):
    latex = r'\begin{vmatrix}'
    for row in matrix:
        latex += ' & '.join(map(str, row)) + r'\\'
    latex += r'\end{vmatrix}'
    return latex

def colored_matrix_to_latex(matrix):
    index = len(matrix[0]) * len(matrix)
    colors = get_colors(index) 

    latex = r'\begin{bmatrix}'
    color_index = 0
    for row in matrix:
        row_latex = " "
        for col in row:
            row_latex += f"\\textcolor{{{colors[color_index]}}}{{{col}}} & "
            color_index += 1
        row_latex = row_latex[:-2]
        latex += f"{row_latex} \\\\"
    latex += r'\end{bmatrix}'
    return latex

def matrix_addition_procedure(A, B):
    index = len(A[0]) * len(A)
    colors = get_colors(index)

    colored_A_plus_B = r'\begin{bmatrix}'
    color_index = 0
    for row_A, row_B in zip(A, B):
        row_latex = " "
        for x, y in zip(row_A, row_B):
            row_latex += f"\\textcolor{{{colors[color_index]}}}{{{x} + {y}}} & "
            color_index += 1
        row_latex = row_latex[:-3]
        colored_A_plus_B += f"{row_latex} \\\\"
    colored_A_plus_B += r'\end{bmatrix}'
    colored_A_plus_B  = colored_A_plus_B.replace('+ -', '- ')

    latex = colored_A_plus_B
    return latex

def matrix_scalar_multiplication_procedure(scalar, A):
    index = len(A[0]) * len(A)
    colors = get_colors(index)

    colored_n_times_A = r'\begin{bmatrix}'
    color_index = 0
    for row_A in A:
        row_latex = " "
        for y in row_A:
            if scalar < 0: 
                if y < 0:
                    row_latex += f"({scalar}) \cdot (\\textcolor{{{colors[color_index]}}}{{{y}}}) & "
                else:
                    row_latex += f"({scalar}) \cdot \\textcolor{{{colors[color_index]}}}{{{y}}} & "
            else:
                if y < 0:
                    row_latex += f"{scalar} \cdot (\\textcolor{{{colors[color_index]}}}{{{y}}}) & "
                else:
                    row_latex += f"{scalar} \cdot \\textcolor{{{colors[color_index]}}}{{{y}}} & "
            color_index += 1
        row_latex = row_latex[:-3]
        colored_n_times_A += f"{row_latex} \\\\"
    colored_n_times_A += r'\end{bmatrix}'

    latex = colored_n_times_A
    return latex

def matrix_multiplication_procedure(A, B):
    index_A, index_B = len(A) * len(A[0]), len(B) * len(B[0])
    colors_A, colors_B = get_colors_matrix(A), get_colors_matrix(B)

    colored_A_times_B = r'\begin{bmatrix}'
    for i in range(len(A)):
        row_latex = " "
        for j in range(len(B[0])):
            for k in range(len(B)):  
                if A[i][k] < 0 and B[k][j] < 0:
                    row_latex += f"(\\textcolor{{{colors_A[i][k]}}}{{{A[i][k]}}}) \\cdot (\\textcolor{{{colors_B[k][j]}}}{{{B[k][j]}}}) + "
                elif A[i][k] < 0 and B[k][j] >= 0:
                    row_latex += f"(\\textcolor{{{colors_A[i][k]}}}{{{A[i][k]}}}) \\cdot \\textcolor{{{colors_B[k][j]}}}{{{B[k][j]}}} + "
                elif A[i][k] >= 0 and B[k][j] < 0:
                    row_latex += f"\\textcolor{{{colors_A[i][k]}}}{{{A[i][k]}}} \\cdot (\\textcolor{{{colors_B[k][j]}}}{{{B[k][j]}}}) + "
                else:
                    row_latex += f"\\textcolor{{{colors_A[i][k]}}}{{{A[i][k]}}} \\cdot \\textcolor{{{colors_B[k][j]}}}{{{B[k][j]}}} + "
            row_latex = row_latex[:-2]
            row_latex += " & "
        colored_A_times_B += f"{row_latex} \\\\"
    colored_A_times_B += r'\end{bmatrix}'

    latex = colored_A_times_B
    return latex

def matrix_transpose_procedure(A):
    index = len(A[0]) * len(A)
    colors = get_colors(index)

    colored_A_T = r'\begin{bmatrix}'
    for i in range(len(A[0])):
        row_latex = " "	
        color_index = i
        for j in range(len(A)):
            print(color_index)
            row_latex += f"\\textcolor{{{colors[color_index]}}}{{{A[j][i]}}} & "
            color_index += len(A[0])
        row_latex = row_latex[:-2]
        colored_A_T += f"{row_latex} \\\\"
    colored_A_T += r'\end{bmatrix}'
    return colored_A_T

def determinant_procedure(matrix):
    def determinant_step(matrix, step):
        n = len(matrix)
        if n == 2:
            elements = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
            a, b, c, d = elements
            if step == 1:
                al, bl, cl, dl = [f"({i})" if i < 0 else f"{i}" for i in elements]
                return f"[{al} \\cdot {dl} - ({bl} \\cdot {cl})]"
            elif step == 2:
                ad, bc = [f"({i*j})" if i*j < 0 else f"{i*j}" for i, j in zip([a,b],[d,c])]
                return f"[{ad} - {bc}]"
            else:
                return f"{a*d - b*c}" if a*d - b*c >= 0 else f"({a*d - b*c})"
        
        latex = ""
        for c in range(n):
            sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            sign = (-1) ** (1 + c + 1)
            element = matrix[0][c]
            
            if step == 1:
                term = f"(-1)^{{1+{c+1}}}" + (f" \\cdot ({element})" if element < 0 else f" \\cdot {element}")
            elif step == 2:
                term = f"(-1)^{{{1+c+1}}}" + (f" \\cdot ({element})" if element < 0 else f" \\cdot {element}")
            elif step == 3:
                term = f"{sign * element}" if sign * element >= 0 else f"({sign * element})"
            
            latex += f"{term} \\cdot {determinant_step(sub_matrix, step)} + "
        
        return latex[:-3]  # Remove the last " + "

    return [determinant_step(matrix, i) for i in range(1, 4)]

def cofactor_procedure(matrix, step):
    """Genera los pasos para calcular los cofactores de una matriz."""
    n = len(matrix)
    steps = []
    
    for i in range(n):
        for j in range(n):
            sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            sign = (-1) ** (i + j)
            det_steps = determinant_procedure(sub_matrix)
            
            if step == 1:
                term = f"(-1)^{{{i+1}+{j+1}}} \\cdot {determinant_to_latex(sub_matrix)}"	
                steps.append(term)
            elif step == 2:
                term = f"(-1)^{{{i+1+j+1}}} \\cdot {det_steps[1]}"
                steps.append(term)
            elif step == 3:
                term = f"{sign}" if len(det_steps[2]) == 1 else f"{sign} \\cdot {det_steps[2]}" 
                steps.append(term)
    
    return steps

def attached_matrix_procedure(matrix):
    """Genera los pasos para calcular la matriz adjunta de una matriz."""
    n = len(matrix)
    adj_steps = []
    
    for step in range(1, 4):
        cofactor_steps = cofactor_procedure(matrix, step)
        adj_matrix = []
        
        for i in range(n):
            adj_row = []
            for j in range(n):
                adj_row.append(cofactor_steps[i*n + j])
            adj_matrix.append(" & ".join(adj_row))
        
        adj_steps.append("\\begin{bmatrix} " + " \\\\ ".join(adj_matrix) + " \\end{bmatrix}")
    adj_steps = [latex.replace("\\cdot  \\end", " \\end").replace("\\cdot  &","  &").replace("\\cdot  \\\\", "  \\\\") for latex in adj_steps]
    return adj_steps

def display_matrix(matrix):
    st.latex(matrix_to_latex(matrix))

def get_user_matrix(rows, cols):
    st.markdown("#### Enter your answer:")
    user_matrix = []
    
    # Crear una columna central
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  # Usar la columna central para el contenido
        for i in range(rows):
            row = []
            cols_input = st.columns(cols)
            for j in range(cols):
                with cols_input[j]:
                    value = st.number_input(
                        "",
                        key=f"matrix_{i}_{j}",
                        min_value=None,
                        max_value=None,
                        step=1,
                        value=None,
                        format="%d"
                    )
                    row.append(value)
            user_matrix.append(row)
    
    return user_matrix

def matrices_are_equal(A, B):
    return all(all(A[i][j] == B[i][j] for j in range(len(A[0]))) for i in range(len(A)))

def is_matrix_complete(matrix):
    return all(all(val is not None for val in row) for row in matrix)

def check_matrix_answer(correct_answer, user_matrix):
    if is_matrix_complete(user_matrix):
        if matrices_are_equal(correct_answer, user_matrix):
            st.success("Correct!")
        else:
            st.error("Incorrect. Try again!")
        return "Bien"
    else:
        st.error("Please fill in all the fields before submitting your answer.")
        return None

def check_numeric_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        st.success("Correct!")
    else:
        st.error("Incorrect. Try again!")

def display_matrix_answer(user_matrix, correct_answer):
    col1, col2, col3 = st.columns(3) 
    with col1:    
        st.markdown("##### Your answer:")
        display_matrix(user_matrix)
    with col3:
        st.markdown("##### Correct answer:")
        display_matrix(correct_answer)

def display_answer(user_answer, correct_answer):
    col1, col2, col3 = st.columns(3) 
    with col1:    
        st.markdown("##### Your answer:")
        st.markdown(f"###### $${user_answer}$$")
    with col3:
        st.markdown("##### Correct answer:")
        st.markdown(f"###### $${correct_answer}$$")

st.set_page_config(
    page_title="Matrices and Determinants",
    page_icon="😎",
)

# Inicializar el estado de la sesión si no existe
if 'page' not in st.session_state:
    st.session_state.page = 'generate'

if st.session_state.page == 'generate':
    st.title("Linear Algebra Matrix Practice")
    st.header("Definitions")

    ### OTRAS REFERENCIAS 
    # Kurosch, A. G. (1968). *Curso de álgebra superior*. Moscow: Mir Publishers (Издательство "Мир")

    # Matrix's order 
    st.subheader("Order of the Matrix")
    st.markdown('''
**Definition**: The :red[order of a matrix] refers to its :red[dimensions], specified by the number of rows and columns it has. If a :blue[matrix $A$] has :blue[$m$ rows] and :blue[$n$ columns], then :blue[$A$ is] said to be of order :blue[$m \\times  n$].

Grossman, S. (2012). *Álgebra Lineal*. (7$^{\\textrm{ma}}$ ed., pp. 48) McGraw Hill. 
    ''')

    # Matrix's elements 
    st.subheader("Elements of the Matrix")
    st.markdown('''
    **Definition**: The elements of a matrix are the individual values that make up the matrix. If $A$ is a matrix of order $m \\times n$, then each element $a_{ij}$ of $A$ is located at the intersection of the $i$-th row and the $j$-th column.

Grossman, S. (2012). *Álgebra Lineal*. (7$^{\\textrm{ma}}$ ed., pp. 48) McGraw Hill. 
    ''')

    ## Barra Lateral
    st.sidebar.title("Matrix Generation")
    exercise = st.sidebar.selectbox("Choose an exercise", ["Matrix Addition", "Matrix Scalar Multiplication", "Matrix Multiplication", "Transposed Matrix",  "Determinant of a Matrix", "Attached Matrix", "Inverse Matrix"])

    if exercise == "Matrix Addition":
        rows_A = rows_B = st.sidebar.slider("Rows in Matrix A and B", 2, 5, 3)
        cols_A = cols_B = st.sidebar.slider("Columns in Matrix A and B", 2, 5, 3)
    elif exercise == "Matrix Scalar Multiplication":
        rows_A = st.sidebar.slider("Rows in Matrix A", 2, 5, 3)
        cols_A = st.sidebar.slider("Columns in Matrix A", 2, 5, 3) 
        scalar_range = st.sidebar.slider("Range for the value of the scalar", value=[0,20], min_value=-100, max_value=100)
    elif exercise in ["Inverse Matrix", "Determinant of a Matrix", "Attached Matrix"]:
        rows_A = st.sidebar.slider("Rows and Columns in Matrix A", 2, 5, 3)
        cols_A = rows_A
    elif exercise == "Transposed Matrix":
        rows_A = st.sidebar.slider("Rows in Matrix A", 2, 5, 3)
        cols_A = st.sidebar.slider("Columns in Matrix A", 2, 5, 3)
    else: 
        rows_A = st.sidebar.slider("Rows in Matrix A", 2, 5, 3)
        cols_A = st.sidebar.slider("Columns in Matrix A", 2, 5, 3)
        rows_B = cols_A
        cols_B = st.sidebar.slider("Columns in Matrix B", 2, 5, 3)

    if st.sidebar.button("Generate"):
        st.session_state.matrix_A = generate_matrix(rows_A, cols_A)
        if exercise == "Matrix Scalar Multiplication":
            st.session_state.scalar = get_scalar(scalar_range[0], scalar_range[1])
        if exercise == "Matrix Addition" or exercise == "Matrix Multiplication":
            st.session_state.matrix_B = generate_matrix(rows_B, cols_B)

    # Asegurarse de que las matrices y el escalar existan en el estado de la sesión
    if 'matrix_A' not in st.session_state:
        st.session_state.matrix_A = generate_matrix(rows_A, cols_A)
    if 'matrix_B' not in st.session_state:  
        st.session_state.matrix_B = generate_matrix(rows_B, cols_B)
    if exercise == "Matrix Scalar Multiplication" and "scalar" not in st.session_state:
        st.session_state.scalar = get_scalar(scalar_range[0], scalar_range[1])

    if st.sidebar.button("Resolve"):
        st.session_state.page = 'resolve'

    # Mostrar matrices y escalar
    if exercise == "Matrix Scalar Multiplication":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Scalar")
            col1_1, col1_2 = st.columns(2) 
            with col1_1:
                for _ in range(rows_A//2):
                    st.write("")
                st.subheader(st.session_state.scalar)
        with col3:
            st.header("Matrix A")
            col3_1, col3_2 = st.columns(2) 
            with col3_1:
                display_matrix(st.session_state.matrix_A)
    elif exercise in ["Matrix Addition", "Matrix Multiplication"]:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Matrix A")
            col1_1, col1_2 = st.columns(2) 
            with col1_1:
                display_matrix(st.session_state.matrix_A)
        with col3:
            st.header("Matrix B")
            col3_1, col3_2 = st.columns(2) 
            with col3_1:
                display_matrix(st.session_state.matrix_B)

    else:
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            col2_1, col2_2 = st.columns([1,2])
            with col2_2:
                st.header("Matrix A")
            display_matrix(st.session_state.matrix_A)

 
# Página de resolución
elif st.session_state.page == 'resolve':
    st.header("Exercise")

    ## Barra Lateral
    st.sidebar.title("Matrix Generation")
    exercise = st.sidebar.selectbox("Choose an exercise", ["Matrix Addition", "Matrix Scalar Multiplication", "Matrix Multiplication", "Transposed Matrix",  "Determinant of a Matrix", "Attached Matrix", "Inverse Matrix"])

    if exercise == "Matrix Addition":
        rows_A = rows_B = st.sidebar.slider("Rows in Matrix A and B", 2, 5, 3)
        cols_A = cols_B = st.sidebar.slider("Columns in Matrix A and B", 2, 5, 3)
    elif exercise == "Matrix Scalar Multiplication":
        rows_A = st.sidebar.slider("Rows in Matrix A", 2, 5, 3)
        cols_A = st.sidebar.slider("Columns in Matrix A", 2, 5, 3) 
        scalar_range = st.sidebar.slider("Range for the value of the scalar", value=[0,20], min_value=-100, max_value=100)
    elif exercise in ["Inverse Matrix", "Determinant of a Matrix", "Attached Matrix"]:
        rows_A = st.sidebar.slider("Rows and Columns in Matrix A", 2, 5, 3)
        cols_A = rows_A
    elif exercise == "Transposed Matrix":
        rows_A = st.sidebar.slider("Rows in Matrix A", 2, 5, 3)
        cols_A = st.sidebar.slider("Columns in Matrix A", 2, 5, 3)
    else: 
        rows_A = st.sidebar.slider("Rows in Matrix A", 2, 5, 3)
        cols_A = st.sidebar.slider("Columns in Matrix A", 2, 5, 3)
        rows_B = cols_A
        cols_B = st.sidebar.slider("Columns in Matrix B", 2, 5, 3)

    if st.sidebar.button("Generate"):
        st.session_state.matrix_A = generate_matrix(rows_A, cols_A)
        if exercise == "Matrix Scalar Multiplication":
            st.session_state.scalar = get_scalar(scalar_range[0], scalar_range[1])
        if exercise == "Matrix Addition" or exercise == "Matrix Multiplication":
            st.session_state.matrix_B = generate_matrix(rows_B, cols_B)

    # Asegurarse de que las matrices y el escalar existan en el estado de la sesión
    if 'matrix_A' not in st.session_state:
        st.session_state.matrix_A = generate_matrix(rows_A, cols_A)
    if 'matrix_B' not in st.session_state:  
        st.session_state.matrix_B = generate_matrix(rows_B, cols_B)
    if exercise == "Matrix Scalar Multiplication" and "scalar" not in st.session_state:
        st.session_state.scalar = get_scalar(scalar_range[0], scalar_range[1])

    if st.sidebar.button("Regresar"):
        st.session_state.page = 'generate'

    if exercise == "Matrix Addition":
        st.markdown("### Matrix Addition $$(A + B)$$")
        st.latex(f"{matrix_to_latex(st.session_state.matrix_A)} + {matrix_to_latex(st.session_state.matrix_B)}")
        result_rows, result_cols = len(st.session_state.matrix_A), len(st.session_state.matrix_A[0])
        user_matrix = get_user_matrix(result_rows, result_cols)
        if st.button("Check Answer"):
            correct_answer = matrix_addition(st.session_state.matrix_A, st.session_state.matrix_B)
            fields_unfilled = check_matrix_answer(correct_answer, user_matrix)
            if fields_unfilled != None:            
                display_matrix_answer(user_matrix, correct_answer)
                st.markdown("##### Procedure:")
                st.latex(f"""
                         \\begin{{gather*}}
                         {colored_matrix_to_latex(st.session_state.matrix_A)} + {colored_matrix_to_latex(st.session_state.matrix_B)} = \\\\
                         {matrix_addition_procedure(st.session_state.matrix_A,st.session_state.matrix_B)} = {colored_matrix_to_latex(correct_answer)}
                         \\end{{gather*}}
                         """)

    elif exercise == "Matrix Scalar Multiplication":
        st.markdown("### Matrix Scalar Multiplication $$(a \\cdot M_{n \\times m})$$")
        st.latex(f"{st.session_state.scalar} \cdot {matrix_to_latex(st.session_state.matrix_A)}")
        result_rows, result_cols = len(st.session_state.matrix_A), len(st.session_state.matrix_A[0])
        user_matrix = get_user_matrix(result_rows, result_cols)
        if st.button("Check Answer"):
            correct_answer = matrix_scalar_multiplication(st.session_state.scalar, st.session_state.matrix_A)
            fields_unfilled = check_matrix_answer(correct_answer, user_matrix)
            if fields_unfilled != None:            
                display_matrix_answer(user_matrix, correct_answer)
                st.markdown("##### Procedure:")
                st.latex(f"""
                          \\begin{{gather*}} 
                          {st.session_state.scalar} \\cdot {colored_matrix_to_latex(st.session_state.matrix_A)} = \\\\
                          {matrix_scalar_multiplication_procedure(st.session_state.scalar,st.session_state.matrix_A)} = \\\\
                          {colored_matrix_to_latex(matrix_scalar_multiplication(st.session_state.scalar, st.session_state.matrix_A))}
                          \\end{{gather*}}
                          """)

    elif exercise == "Matrix Multiplication":
        st.markdown("### MAtrix Multiplication $$(A_{n \\times m}\\cdot B_{m \\times l})$$")
        st.latex(f"{matrix_to_latex(st.session_state.matrix_A)} \\cdot {matrix_to_latex(st.session_state.matrix_B)}")
        result_rows, result_cols = len(st.session_state.matrix_A), len(st.session_state.matrix_B[0])
        user_matrix = get_user_matrix(result_rows, result_cols)
        if st.button("Check Answer"):
            correct_answer = matrix_multiplication(st.session_state.matrix_A, st.session_state.matrix_B)
            fields_unfilled = check_matrix_answer(correct_answer, user_matrix)
            if fields_unfilled != None:  
                display_matrix_answer(user_matrix, correct_answer)
                st.markdown("##### Procedure:")
                st.latex(f"""
                         \\begin{{gather*}}
                         {colored_matrix_to_latex(st.session_state.matrix_A)} \\cdot {colored_matrix_to_latex(st.session_state.matrix_B)} = \\\\
                         {matrix_multiplication_procedure(st.session_state.matrix_A,st.session_state.matrix_B)} \\\\
                          = {matrix_to_latex(correct_answer)}
                         \\end{{gather*}} 
                         """)

    elif exercise == "Transposed Matrix":
        st.markdown("### Transposed Matrix $$((M_{n \\times m})^{T})$$")
        st.latex(f"{matrix_to_latex(st.session_state.matrix_A)}^{{T}}")
        result_rows, result_cols = len(st.session_state.matrix_A[0]), len(st.session_state.matrix_A)
        user_matrix = get_user_matrix(result_rows, result_cols)
        if st.button("Check Answer"):
            correct_answer = matrix_transpose(st.session_state.matrix_A)
            fields_unfilled = check_matrix_answer(correct_answer, user_matrix)
            if fields_unfilled != None:  
                display_matrix_answer(user_matrix, correct_answer)
                st.markdown("##### Procedure:")
                st.latex(f"{colored_matrix_to_latex(st.session_state.matrix_A)}^{{T}} = {matrix_transpose_procedure(st.session_state.matrix_A)} = {matrix_to_latex(correct_answer)}")

    elif exercise == "Determinant of a Matrix":
        st.subheader("Determinant of a Matrix $$(M_{n \\times n})$$")
        st.latex(determinant_to_latex(st.session_state.matrix_A))
        user_answer = st.number_input("Valor del determinante:", step=1)
        if st.button("Check Answer"):
            correct_answer = determinant(st.session_state.matrix_A)
            display_answer(user_answer, correct_answer)
            st.markdown("##### Procedure:")
            if len(st.session_state.matrix_A) == 2:
                steps = determinant_procedure(st.session_state.matrix_A)
                st.latex(f"""\\begin{{gather*}}
                      {determinant_to_latex(st.session_state.matrix_A)} = \\\\ {steps[0]} \\\\ = {steps[1]} \\\\ = {correct_answer} 
                      \\end{{gather*}}
                      """)
            else:
                steps = determinant_procedure(st.session_state.matrix_A)
                st.latex(f"""\\begin{{gather*}}
                      {determinant_to_latex(st.session_state.matrix_A)} = \\\\ {steps[0]} \\\\ = {steps[1]} \\\\ = {steps[2]} \\\\ = {correct_answer}
                      \\end{{gather*}}
                      """)

    elif exercise == "Attached Matrix":
        st.markdown("### Attached Matrix $$((M_{n \\times n})^{*})$$")
        st.latex(f"{matrix_to_latex(st.session_state.matrix_A)}^{{*}}")
        result_rows, result_cols = len(st.session_state.matrix_A[0]), len(st.session_state.matrix_A)
        user_matrix = get_user_matrix(result_rows, result_cols)
        if st.button("Check Answer"):
            correct_answer = attached_matrix(st.session_state.matrix_A)
            fields_unfilled = check_matrix_answer(correct_answer, user_matrix)
            if fields_unfilled != None:  
                display_matrix_answer(user_matrix, correct_answer)
                st.markdown("##### Procedure:")
                st.latex(f"""\\begin{{gather*}}
                        {matrix_to_latex(st.session_state.matrix_A)}^{{*}} = {attached_matrix_procedure(st.session_state.matrix_A)[0]} \\\\     
                        = {attached_matrix_procedure(st.session_state.matrix_A)[1]} \\\\ 
                        = {attached_matrix_procedure(st.session_state.matrix_A)[2]} \\\\
                        = {matrix_to_latex(correct_answer)}
                        \\end{{gather*}}
                        """)

    elif exercise == "Inverse Matrix":
        st.markdown("### Inverse Matrix $$((M_{n \\times n})^{-1})$$")
        st.latex(f"{matrix_to_latex(st.session_state.matrix_A)}^{{-1}}")
        result_rows, result_cols = len(st.session_state.matrix_A[0]), len(st.session_state.matrix_A)
        user_matrix = get_user_matrix(result_rows, result_cols)
        if st.button("Check Answer"):
            correct_answer = matrix_transpose(st.session_state.matrix_A)
            fields_unfilled = check_matrix_answer(correct_answer, user_matrix)
            if fields_unfilled != None:  
                display_matrix_answer(user_matrix, correct_answer)
                st.markdown("##### Procedure:")
                #st.latex(f"{colored_matrix_to_latex(st.session_state.matrix_A)}^{{T}} = {matrix_transpose_procedure(st.session_state.matrix_A)} = {matrix_to_latex(correct_answer)}")