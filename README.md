### Ex3 Project 

*I will brief the project every part of the brief will get most explanation in the wiki pages.*

This illustration exhibit all the classes and their dependencies.

![image](https://user-images.githubusercontent.com/61500507/103583081-c5ed3080-4ee7-11eb-91fb-62a8e75c2138.png)

The three classes is the **DiGraph** and **GraphAlgo** and **Node**.

The **Node** represent single node in graph, for every node have special key,the neighbors, the node that direct to him, tag, info, and dictionay of all his neighbors.

The **DiGraph** class complicated from Node and Edge that represent in the node class as dictionary, in the class the node of the graph and the edges keep in two different dictionary. 

You can operate sum operation on the graph, you can removeNode, you can AddNode , you can conncet between two nodes and put weight for the edge,
the graph is directed weighted graph, in GraphAlgo class have the plot of the graph and the graph look like this:

![image](https://user-images.githubusercontent.com/61500507/103581407-a43e7a00-4ee4-11eb-9c24-3646662b38e4.png)

To read more on graph operation [Press Here!](https://github.com/EN555/ex3/wiki/The-Graph)

The **Graph Algo** class composed of graph class, you need to initial the class with graph, and you can operate on her some operation.

In this class you can find the shortestpath from src to other destination, you can found all the strongly component of the graph, you can too find tha scc of specific key,
you can export Json file of the graph that contain all the edges and the nodes of the graph, you can too read Json file and load the class with him.

To read more on graph operation [Press Here!](https://github.com/EN555/ex2/wiki/Algorithms)
