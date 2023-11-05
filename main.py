import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

graphs = []  # Crie a lista 'graphs' aqui

# Second Network
graph2 = nx.read_adjlist("CA-GrQc.txt")
graphs.append(graph2)

# average degree of neighbors
degree2, avg_neigh_degree2 = zip(*nx.average_degree_connectivity(graph2).items())

# convert to list
degree2 = list(degree2)
avg_neigh_degree2 = list(avg_neigh_degree2)

# plotting the graph
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

sns.regplot(x=degree2, y=avg_neigh_degree2, ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neighbor degree") 
ax.set_xlim(0, None)
plt.show()


#twitter A rede exibe uma ampla variedade de conexões, demonstrando uma preferência por conexões entre nós que são menos semelhantes entre si, mostrando uma tendência dissortativa.

#Facebook  Os nós de grau mais baixo tendem a se conectar com nós de grau mais alto. Isso é característico de uma rede dissortativa

# Wiki-vote Um gráfico decrescente, com um coeficiente de assortatividade negativo, indica que nós com graus mais baixos tendem a se conectar a nós com graus mais altos. Em termos simples, isso descreve uma rede dissortativa.

# Slashdot0811 Os nós de grau mais baixo tendem a se conectar com nós de grau mais baixo e os nós de grau mais alto tendem a se conectar com nós de grau mais alto. Isso é característico de uma rede assortativa

# CA-GrQc Um gráfico ascendente os nós de grau mais baixo tendem a se conectar com nós de grau mais baixo e os nós de grau mais alto tendem a se conectar com nós de grau mais alto. Isso é característico de uma rede assortativa

