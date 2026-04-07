import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head(20).to_string())


# 1. Histograma
plt.hist(df["Preço"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histograma")
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.show()

# 2. Gráfico de dispersão
plt.scatter(df["Preço"], df["Nota"], alpha=0.6, c="purple")
plt.title("Preço vs Nota")
plt.xlabel("Preço")
plt.ylabel("Nota")
plt.show()

# 3. Mapa de calor (usando seaborn)
corr = df[["Nota","N_Avaliações","Desconto","Preço","Qtd_Vendidos_Cod"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Mapa de Calor - Correlação")
plt.show()

# 4. Gráfico de barras
df["Marca"].value_counts().head(10).plot(kind="bar", color="orange")
plt.title("Produtos por Marca")
plt.xlabel("Marca")
plt.ylabel("Quantidade")
plt.show()

# 5. Gráfico de pizza
df["Material"].value_counts().head(10).plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribuição por Material")
plt.ylabel("")
plt.show()

# 6. Gráfico de densidade
df["Preço"].plot(kind="density", color="green")
plt.title("Densidade de Preços")
plt.show()

# 7. Gráfico de regressão (usando seaborn)
sns.regplot(x="Preço", y="Nota", data=df, scatter_kws={"alpha":0.5})
plt.title("Regressão Preço vs Nota")
plt.show()
