### Ex3 Project 

*I will brief the project every part of the brief will get most explanation in the wiki pages.*

This illustration exhibit all the classes and their dependencies.

![diagram](https://user-images.githubusercontent.com/61500507/104128284-5ce63c80-536f-11eb-8a8e-0cda54ca715e.png)

The project composed of two abstract class GraphInterface and GraphAlgoInTnterface, The three classes is the **DiGraph** and **GraphAlgo** and **Node**.

The **Node** represent single node in graph, for every node have special key,the neighbors, the node that direct to him, tag, info, and dictionay of all his neighbors.

The **DiGraph** inherit from GraphInterface (e.g. in python we havn't interfaces so we use abstract inheritance), The class composed from Node and Edge that represent in the node class as dictionary,we have some different dictionary, on one for the neighbors, one for the nodes that direct to him and one for the node weight. 

You can operate sum operations on the graph, you can removeNode, you can AddNode , you can conncet between two nodes and put weight for the edge,
the graph is directed weighted graph, in GraphAlgo class have the plot of the graph and the graph look like this:

![image](https://user-images.githubusercontent.com/61500507/103581407-a43e7a00-4ee4-11eb-9c24-3646662b38e4.png)

To read more on graph operation [Press Here!](https://github.com/EN555/ex3/wiki/The-Graph)

The **Graph Algo** class composed of graph class, you need to initial the class with graph, and you can operate on her some operation.

In this class you can find the shortestpath from src to other destination, you can found all the strongly component of the graph, you can too find tha scc of specific key,
you can export Json file of the graph that contain all the edges and the nodes of the graph, you can too read Json file and load the class with him.

To read more on graph operation [Press Here!](https://github.com/EN555/ex3/wiki/The-Algo)
