import networkx          as nx
import matplotlib.pyplot as plt

# GENERADORES DE GRAFOS:

N = 50 # NUMERO DE NODOS

# GRAFO ERDOS-RENYI
G1 = nx.erdos_renyi_graph(N,0.5) 

# GRAFO WATTS-STROGATZ
G2 = nx.watts_strogatz_graph(N,4,0.1) 

# GRAFO BARABASI-ALBERT
G3 = nx.barabasi_albert_graph(N,1) 

# GRAFO TOTALMENTE CONECTADO O COMPLETO
G4 = nx.complete_graph(10)

plt.figure(figsize=(12,15))

plt.subplot(421) 
plt.title('Grafo Erdos-Renyi',fontsize=20)
nx.draw_random(G1,node_color='blue',node_size=100,with_labels=False,alpha=0.8)

plt.subplot(422) 
plt.hist(list(dict(nx.degree(G1)).values()))
plt.xlabel('Grado de nodo')
plt.ylabel('Número de eventos')

plt.subplot(423) 
plt.title('Grafo Watts-Strogatz',fontsize=20)
nx.draw_circular(G2,node_color='green',node_size=100,with_labels=False,alpha=0.8)

plt.subplot(424) 
plt.hist(list(dict(nx.degree(G2)).values()))
plt.xlabel('Grado de nodo')
plt.ylabel('Número de eventos')

plt.subplot(425) 
plt.title('Grafo Barabasi-Albert',fontsize=20)
nx.draw_spring(G3,node_color='orange',node_size=100,with_labels=False,alpha=0.8)

plt.subplot(426) 
plt.hist(list(dict(nx.degree(G3)).values()))
plt.xlabel('Grado de nodo')
plt.ylabel('Número de eventos')

plt.subplot(427) 
plt.title('Grafo Fully connected',fontsize=20)
nx.draw_circular(G4,node_color='deeppink',node_size=100,with_labels=False,alpha=0.8)

plt.subplot(428) 
plt.hist(list(dict(nx.degree(G4)).values()))
plt.xlabel('Grado de nodo')
plt.ylabel('Número de eventos')