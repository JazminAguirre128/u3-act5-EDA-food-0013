import pandas as pd
import matplotlib.pyplot as plt
# Meredith Aguirre NC 0013
# 1. Leer el archivo CSV desde el archivo de indian food
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV Meredith Aguirre 0013---")
print(df_food_india)
print("\n--- MOSTRAR NOMBRE COMIDA + INGREDIENTES Meredith Aguirre 0013---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- TIEMPO DE COCINADO MOSTRAR 10 REGISTROS CON HEAD Meredith Aguirre 0013---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)