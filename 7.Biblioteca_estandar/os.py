import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")



#Rename a file
os.rename('curso_de_python/6.Lectura_y_escritortura_de_archivos/cuento.txt', 
          'curso_de_python/6.Lectura_y_escritortura_de_archivos/archivo_renombrado.txt')

# List all files .txt 
txt_files = [f for f in os.listdir('curso_de_python/6.Lectura_y_escritortura_de_archivos/') if f.endswith('.txt')]
print(f"List of .txt files: {txt_files}")