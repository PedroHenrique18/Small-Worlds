# Small Worlds

# Objetivo

O objetivo desta análise é explorar e compreender aspectos fundamentais das redes, com foco nas semanas 7 e 8 do curso. Vamos investigar quatro conceitos-chave: assortatividade, distâncias, componentes conectados e coeficientes de clustering. Para isso, usaremos diferentes redes e geraremos gráficos bipartidos para avaliar a assortatividade em relação ao grau dos nós nas redes.

# Conteúdo

1. Assortatividade
2. Distâncias
3. Componentes Conectados
4. Coeficientes de Clustering

# Requisito 1 

## Escolha 5 redes:

1. Social circles: Facebook
2. Social circles: Twitter
3. Wikipedia vote network
4. Slashdot social network, November 2008
5. General Relativity and Quantum Cosmology collaboration network

# Requisito 2

Para cada uma das redes escolhidas, fazer um gráfico bipartido
sobre a assortatividade em relação ao grau dos nós da rede. Faça
as figuras em um layout de grid.
Como você interpreta os resultados comparando as diferentes
redes? 

- ## Rede Facebook

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/facebook_combined.png">

  ## A medida que o grau do nó aumenta, o grau médio do vizinho também tende a aumentar,assortatividade tende a zero.
  
- ## Rede Twitter
 
  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/twitter_combined.png">

  ## A rede exibe uma ampla variedade de conexões, demonstrando uma preferência por conexões entre nós que são menos semelhantes entre si, mostrando uma tendência dissortativa.

- ## Rede  Wikipedia vote network

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/Wiki-Vote.png">

  ## Um gráfico decrescente, com um coeficiente de assortatividade negativo, indica que nós com graus mais baixos tendem a se conectar a nós com graus mais altos. Em termos simples, isso descreve uma rede dissortativa.

- ## Rede  Slashdot social network, November 2008

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/Slashdot0811.png">

 ## Gráfico decrescente, significando coeficiente de assortatividade negativo, ou seja, nós de grau mais baixo se conectam com nós de grau mais alto. Em resumo, é uma rede dissortativa

- ## Rede  General Relativity and Quantum Cosmology collaboration network

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/CA-GrQc.png">

  ## Um gráfico ascendente os nós de grau mais baixo tendem a se conectar com nós de grau mais baixo e os nós de grau mais alto tendem a se conectar com nós de grau mais alto. Isso é característico de uma rede assortativa
