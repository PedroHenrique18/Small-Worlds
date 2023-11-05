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

  ## A rede exibe uma ampla diversidade de conexões, evidenciando uma inclinação em favor de estabelecer ligações entre nós que apresentam menor semelhança entre si, o que denota uma tendência dissortativa. Isso implica que a rede tende a preferir conexões entre nós que possuem características ou propriedades mais distintas ou heterogêneas.
  
- ## Rede Twitter
 
  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/twitter_combined.png">

  ## A rede revela uma vasta diversidade de conexões, claramente evidenciando uma predileção por estabelecer ligações entre nós que ostentam menor grau de semelhança entre si, o que aponta de maneira notável para uma tendência dissortativa. Isso significa que a rede tende a favorecer a formação de conexões entre nós que exibem características, atributos ou propriedades mais discrepantes ou heterogêneas.

- ## Rede  Wikipedia vote network

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/Wiki-Vote.png">

  ## Um gráfico que exibe uma tendência decrescente, com um coeficiente de assortatividade negativo, sugere que os nós com graus mais baixos têm uma propensão a se conectar com nós que possuem graus mais elevados. De forma mais simplificada, esse padrão de conexões pode ser descrito como característico de uma rede dissortativa, onde os nós menos conectados estabelecem ligações preferencialmente com os nós mais fortemente conectados.

- ## Rede  Slashdot social network, November 2008

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/Slashdot0811.png">

 ## Um gráfico que demonstra uma tendência decrescente, representada por um coeficiente de assortatividade negativo, sinaliza que os nós com graus mais baixos têm uma     inclinação a estabelecer conexões com nós que ostentam graus mais elevados. Resumindo, esse padrão de conexões pode ser caracterizado como pertencente a uma rede dissortativa, onde os nós menos conectados demonstram uma preferência por ligar-se aos nós mais fortemente conectados na rede.

- ## Rede  General Relativity and Quantum Cosmology collaboration network

  <img src="https://github.com/PedroHenrique18/Small-Worlds/blob/main/graph/CA-GrQc.png">

  ## Um gráfico com uma tendência ascendente indica que os nós de grau mais baixo têm uma propensão a se conectar com outros nós de grau mais baixo, enquanto os nós de grau mais alto tendem a estabelecer conexões com nós de grau mais alto. Essa configuração de conexões é claramente característica de uma rede assortativa, na qual os nós demonstram uma preferência por se ligar a outros nós com graus de conexão semelhantes. Em resumo, em uma rede assortativa, os nós com graus semelhantes tendem a se agrupar e formar conexões mais fortes entre si.

# Conclusão 

Em síntese, a análise do coeficiente de assortatividade em redes complexas fornece uma valiosa ferramenta para desvendar os padrões de conexão que definem essas estruturas intrincadas. O coeficiente de assortatividade revela se uma rede é caracterizada por conexões preferenciais entre nós semelhantes (assortativa) ou se há uma tendência à conexão entre nós mais diferentes (dissortativa), ou mesmo se a rede é relativamente neutra em relação a esse aspecto.

As implicações desses padrões são profundas e se estendem a uma variedade de campos, desde a sociologia até a biologia, passando pela informática. Uma rede assortativa, onde nós com características similares se conectam, pode criar clusters de nós mais densamente conectados, facilitando a disseminação de informações e influências dentro desses grupos. Além disso, redes assortativas podem ser mais resilientes a falhas, já que a redundância é frequentemente incorporada através das conexões entre nós semelhantes.

Por outro lado, em uma rede dissortativa, a conexão entre nós com características diferentes pode criar uma dinâmica onde os recursos ou informações fluem de maneira mais equitativa. No entanto, isso também pode tornar a rede mais vulnerável a pontos críticos, uma vez que os nós com graus mais altos, frequentemente interconectados, podem exercer um grande impacto.

A análise de redes complexas é uma disciplina em crescimento que oferece insights profundos sobre sistemas interconectados. O coeficiente de assortatividade é uma das métricas fundamentais para compreender as redes, e sua aplicação abrange diversos campos, da análise de redes sociais à biologia de sistemas. Portanto, a compreensão da natureza assortativa ou dissortativa de uma rede é crucial para desvendar suas propriedades intrínsecas e sua dinâmica, contribuindo para avanços significativos em diversas áreas do conhecimento.

# Requisito 3

Reproduzir a tabela abaixo para cada uma das redes escolhidas
Implementar a tabela no formato markdown juntamente com a interpretação dos
resultados cuja o texto deverá ter entre 500 a 1000 palavras. A tabela e o texto deverá
estar em um arquivo readme

| Rede                               | Qtd vértices | Qtd arestas | Degree Assortativity Coefficient | Qtd Componentes Conectados | Tamanho do Comp. Gigante (GCC) | Coeficiente de Clustering Médio (Avg Clustering) |
|------------------------------------|--------------|------------|----------------------------------|-----------------------------|---------------------------------|-------------------------------------------------|
| Wikipedia Vote Network             | 7115         | 103689     | -0.2749                          | 1099                        | 7066 (0.993)                    | 0.1409                                          |
| Social Circles: Twitter            | 81306        | 1768149    | 0.0739                           | 1                           | 81306 (1.000)                  | 0.5653                                          |
| Social Circles: Facebook           | 4039         | 88234      | 0.1349                           | 1                           | 4039 (1.000)                   | 0.6055                                          |
| Slashdot Social Network (Nov 2008)  | 77360        | 905468     | 0.0922                           | 1                           | 77360 (1.000)                  | 0.0555                                          |
| General Relativity and Quantum Cosmology Collaboration Network | 5242  | 14496      | 0.0812                           | 11                         | 4158 (0.793)                   | 0.5296                                          |
