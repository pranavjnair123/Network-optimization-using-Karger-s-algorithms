import copy
import math
import random
import time

def Karger(graph, t):
    while len(graph) > t:
        
        key = random.choice(list(graph.keys()))
        value = random.choice(graph[key])

        
        for edge in graph[value]:
            if edge != key:  
                graph[key].append(edge)

        for edge in graph[value]:
            graph[edge].remove(value)
            if edge != key:  
                graph[edge].append(key)
        del graph[value]


    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)
    return graph





def graphMaker(gFile,graph):
    nEdges = 0
    edgeList = []
    for line in gFile:
        node = int(line.split()[0])
        edges = []
        for edge in line.split()[1:]:
            edges.append(int(edge))
        graph[node] = edges
        nEdges = nEdges + len(edges)
        edgeList.append(len(edges))
    gFile.close()
    
    print("Total number of edges: ", nEdges / 2)
    print("Total number of vertices: ", len(graph))
    print("Maximum degree: ", max(edgeList))
    print("Minimum degree: ", min(edgeList))

def KargerStein(graph):
    if len(graph) < 6:
        return Karger(graph, 2)
    else:
        t = 1 + int(len(graph) / math.sqrt(2))
        graph_1 = Karger(graph, t)
        graph_2 = Karger(graph, t)
        if len(graph_1) > len(graph_2):
            return KargerStein(graph_2)
        else:
            return KargerStein(graph_1)

def manualGraph():
    file=open("temp.txt",'w')
    l=[]
    while True:
        x=input()
        if x!='':
            l.append(x+'\n')
        else:
            break
    file.writelines(l)
        
    

def main():
    print("Select input method")
    print("1. Enter the name of the txt file containing the graph")
    print("2. Input a graph")
    im=int(input("Option: "))
    if im==1:
        filename=input()
    else:
        print()
        print("Input format: first element of each line is the vertex, the following elements will be vertices to which edges are formed")
        print("Enter a blank line to stop")
        print()
        manualGraph()
        filename="temp.txt"
    print("Select an option")
    print("1. Kargers algorithm for minimum cut")
    print("2. Karger-stein algorithm for minimum cut")
    opt=int(input("Option: "))
    count=int(input("Enter number of vertices in the graph: "))
    print()
    gFile = open(filename)
    graph = {}
    global cuts
    cuts = []
    
    graphMaker(gFile,graph)
    
    s=time.time()
    i = 0
    while i < count:
        graph1 = copy.deepcopy(graph)
        if opt==2:
            g = KargerStein(graph1)
        if opt==1:
            g=Karger(graph1, 2)
        i += 1
    
    e=time.time()
    gFile.close()

    
    print("The minimum number of cuts required is", min(cuts))
    print("Total runtime for the algorithm: ",e-s)


    
if __name__ == '__main__':
    main()
