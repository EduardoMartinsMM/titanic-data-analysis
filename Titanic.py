import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")

titanic = pd.read_excel("titanic.xlsx")

# Gráfico de contagem – sobrevivência
plt.figure(figsize=(10, 7), dpi=100)
ax = sns.countplot(data=titanic, x="sobreviveu", color="purple")
for container in ax.containers:
    ax.bar_label(container, fontsize=8)
plt.title("Distribuição de Sobrevivência no Titanic", fontsize=14)
plt.xlabel("Sobreviveu?", fontsize=12)
plt.ylabel("Quantidade de Passageiros", fontsize=12)
plt.show()

# Gráfico de contagem por sexo
plt.figure(figsize=(15, 9), dpi=100)
ax = sns.countplot(
    data=titanic,
    x="sobreviveu",
    hue="sexo",
    palette="viridis"
)
for container in ax.containers:
    ax.bar_label(container, fontsize=12)
plt.title("Sobrevivência por Sexo", fontsize=20)
plt.xlabel("Sobreviveu?", fontsize=15)
plt.ylabel("Quantidade de Passageiros", fontsize=15)
plt.show()

# Gráfico de barras – tarifa média por local de embarque
dados_embarque = (
    titanic[["embarque", "valor_tarifa"]]
    .groupby("embarque")
    .mean()
    .reset_index()
)

plt.figure(figsize=(15, 9), dpi=100)
ax = sns.barplot(
    data=dados_embarque,
    x="embarque",
    y="valor_tarifa",
    hue="embarque",
    palette="bright",
    legend=False
)

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f", padding=3, fontsize=12)
plt.title("Tarifa Média por Local de Embarque", fontsize=20)
plt.xlabel("Cidade de Embarque", fontsize=15)
plt.ylabel("Tarifa Média", fontsize=15)
plt.show()

# Histograma da idade
plt.figure(figsize=(15, 9), dpi=100)
sns.histplot(
    data=titanic,
    x="idade",
    bins=range(0, 85, 5),
    kde=True,
    color="lightgreen"
)
plt.title("Distribuição de Idade dos Passageiros", fontsize=20)
plt.xlabel("Idade", fontsize=15)
plt.ylabel("Frequência", fontsize=15)
plt.xticks(np.arange(0, 85, 5))
plt.show()

# Gráfico de dispersão – idade x tarifa
plt.figure(figsize=(15, 9), dpi=100)
sns.scatterplot(
    data=titanic[titanic["valor_tarifa"] < 100],
    x="idade",
    y="valor_tarifa",
    hue="classe",
    hue_order=["primeira", "segunda", "terceira"]
)
plt.title("Relação entre Idade e Valor da Tarifa", fontsize=20)
plt.xlabel("Idade", fontsize=15)
plt.ylabel("Valor da Tarifa", fontsize=15)
plt.show()

# Gráfico de barras – tarifa média por classe
dados_classe = (
    titanic[["classe", "valor_tarifa"]]
    .groupby("classe")
    .mean()
    .reset_index()
)

plt.figure(figsize=(15, 9), dpi=100)
sns.barplot(
    data=dados_classe,
    x="classe",
    y="valor_tarifa",
    color="purple"
)
plt.title("Tarifa Média por Classe", fontsize=20)
plt.xlabel("Classe", fontsize=15)
plt.ylabel("Tarifa Média", fontsize=15)
plt.show()

# Boxplot da idade
plt.figure(figsize=(15, 9), dpi=100)
sns.boxplot(y=titanic["idade"], color="orange")

minimo = titanic["idade"].min()
q1 = titanic["idade"].quantile(0.25)
q2 = titanic["idade"].median()
q3 = titanic["idade"].quantile(0.75)
maximo = titanic["idade"].max()

plt.text(0, minimo, f"Mín = {minimo}", ha="center", va="top", fontweight="bold")
plt.text(0, q1, f"Q1 = {q1:.1f}", ha="center", va="top", fontweight="bold")
plt.text(0, q2, f"Mediana = {q2:.1f}", ha="center", va="center", fontweight="bold")
plt.text(0, q3, f"Q3 = {q3:.1f}", ha="center", va="bottom", fontweight="bold")
plt.text(0, maximo, f"Máx = {maximo}", ha="center", va="bottom", fontweight="bold")

plt.title("Boxplot da Idade dos Passageiros", fontsize=20)
plt.show()
