import tkinter as tk
from tkinter import ttk
import requests

# Configuración de la API de Edamam
APP_ID = '8f4b5a5b'
APP_KEY = '0435e7f3de9853c676281ff1b3bab85a'

# Función para buscar recetas
def buscar_recetas():
    ingredientes = entry_ingredientes.get()
    url = f'https://api.edamam.com/search?q={ingredientes}&app_id={APP_ID}&app_key={APP_KEY}'
    response = requests.get(url)
    data = response.json()
    
    # Limpiar la lista de recetas
    listbox_recetas.delete(0, tk.END)
    
    # Agregar las recetas a la lista
    for receta in data['hits']:
        listbox_recetas.insert(tk.END, receta['recipe']['label'])

# Función para mostrar los detalles de la receta seleccionada
def mostrar_detalles():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        receta_seleccionada = listbox_recetas.get(seleccion)
        url = f'https://api.edamam.com/search?q={receta_seleccionada}&app_id={APP_ID}&app_key={APP_KEY}'
        response = requests.get(url)
        data = response.json()
        
        # Mostrar los detalles de la receta en la ventana emergente
        ventana_detalles = tk.Toplevel(ventana)
        ventana_detalles.title(receta_seleccionada)
        
        label_ingredientes = tk.Label(ventana_detalles, text='Ingredientes:')
        label_ingredientes.pack()
        
        listbox_ingredientes = tk.Listbox(ventana_detalles, width=50)
        listbox_ingredientes.pack()
        
        for ingrediente in data['hits'][0]['recipe']['ingredientLines']:
            listbox_ingredientes.insert(tk.END, ingrediente)
        
        label_instrucciones = tk.Label(ventana_detalles, text='Instrucciones:')
        label_instrucciones.pack()
        
        text_instrucciones = tk.Text(ventana_detalles, height=10, width=50)
        text_instrucciones.pack()
        
        text_instrucciones.insert(tk.END, data['hits'][0]['recipe']['instructions'])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('App de Recetas')

# Crear los widgets
label_ingredientes = tk.Label(ventana, text='Ingredientes:')
label_ingredientes.pack()

entry_ingredientes = tk.Entry(ventana)
entry_ingredientes.pack()

boton_buscar = tk.Button(ventana, text='Buscar', command=buscar_recetas)
boton_buscar.pack()

listbox_recetas = tk.Listbox(ventana, width=50)
listbox_recetas.pack()

boton_detalles = tk.Button(ventana, text='Ver Detalles', command=mostrar_detalles)
boton_detalles.pack()

# Ejecutar la aplicación
ventana.mainloop()