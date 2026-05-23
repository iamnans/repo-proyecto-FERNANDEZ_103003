
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/dataset.csv", sep=";")

# Total de ventas
total_ventas = df["total_ventas"].sum()

print(f"Total de ventas: ${total_ventas:,.0f}")

# Productos más vendidos
ventas_producto = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)

print("\nCantidad vendida por producto:")
print(ventas_producto)

# Generar gráfico
ventas_producto.plot(kind="bar")

plt.title("Cantidad vendida por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")

# Guardar gráfico
plt.savefig("resultados/grafico_productos.png")

plt.show()
