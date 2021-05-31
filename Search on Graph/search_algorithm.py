import pygame
import graphUI
from node_color import white, yellow, black, red, blue, purple, orange, green
import numpy as np

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""


def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    # TODO: your code

    visited = ['false'] * len(graph) #khoi tao tap cac dinh danh dau chua dc di qua
    visited[start] = 'true'
    path = [-1] * len(graph) #mang luu vet duong di
    queue = []
    queue.append(start)
    
    while (queue != []):
        
        u = queue.pop(0)
        #print(u)
        graph[u][3] = yellow #dinh dang xet

        if (u == goal):
            print("Finish!")
            break
        ok = 0 #bien ok kiem tra xem trong ds dinh ke voi u co dinh goal hay khong
        for i in graph[u][1]:
            if (visited[i] == 'false'):
                visited[i] = 'true'
                queue.append(i)
                path[i] = u
                if (i == goal):
                    ok = 1
                    break
                graph[i][3] = red #dinh ke voi dinh dang xet
                graph[i][2] = white #vien cua dinh dang xet
                edges[edge_id(u,i)][1] = white #to mau cac canh dang xet
                graphUI.updateUI()
        
        if ok == 1:
             break

        graph[u][3] = blue #danh dau dinh da xet
        graphUI.updateUI()

        if (queue == []):
            print("Cannot find the path from ", start, " to ", goal)
            return

    graph[start][3] = orange #to mau dinh bat dau
    graph[goal][3] = purple #to mau dinh dich
    i = goal
    while (path[i] != -1):
        edges[tuple(np.sort([path[i], i]))][1] = green
        i = path[i]
    graphUI.updateUI()

    print("Implement BFS algorithm.")
    pass


def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    visited = ['false'] * len(graph) #khoi tao tap cac dinh danh dau chua dc di qua    
    path = [-1] * len(graph) #mang luu vet duong di
    stack = []
    stack.append(start)
    
    while (stack != []):        
        u = stack.pop()
        visited[u] = 'true'
        #print(u)
        graph[u][3] = yellow #dinh dang xet

        if (u == goal):
            print("Finish!")
            break

        for i in graph[u][1]:
            if (visited[i] == 'false'):                
                stack.append(i)
                path[i] = u               
                graph[i][3] = red #dinh ke voi dinh dang xet
                graph[i][2] = white #vien cua dinh dang xet
                edges[edge_id(u,i)][1] = white #to mau cac canh dang xet
                graphUI.updateUI()

        graph[u][3] = blue #danh dau dinh da xet
        graphUI.updateUI()

        if (stack == []):
            print("Cannot find the path from ", start, " to ", goal)
            return

    graph[start][3] = orange #to mau dinh bat dau
    graph[goal][3] = purple #to mau dinh dich
    i = goal
    while (path[i] != -1):
        edges[tuple(np.sort([path[i], i]))][1] = green
        i = path[i]
    graphUI.updateUI()

    print("Implement DFS algorithm.")
    pass


def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code

    #them mang weight luu trong so bang cach tinh khoang cach cua 2 dinh
    weight = []
    for i in range(0, len(graph)):
        temp = []
        for j in graph[i][1]:
            a = graph[i][0] #toa do dinh i
            b = graph[j][0] #toa do dinh j
            d = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
            temp.append(d)
        weight.append(temp)
           
    visited = ['false'] * len(graph) #khoi tao tap cac dinh danh dau chua dc di qua
    visited[start] = 'true'
    path = [-1] * len(graph) #mang luu vet duong di
    queue = []
    queue.append((start,0))
    
    while (queue != []):
        queue.sort(key = lambda tup: tup[1]) #sap xep queue dua theo chi phi        
        put = queue.pop(0) #lay ra dinh co chi phi nho nhat
        u = put[0]
        value = put[1] #chi phi cua dinh hien tai
       # print(u)
        graph[u][3] = yellow #dinh dang xet
        cost = weight[u] #chi phi tu dinh dang xet toi cac dinh ke

        if (u == goal):
            print("Finish!")
            break
        
        j = 0 #bien dem cho mang cost
        for i in graph[u][1]:                      
            if visited[i] == 'true':                
                ok = 'false'
                for k in range(0,len(queue)): #tim xem dinh dang xet co trong queue hay khong, neu co thi ok=true
                    if queue[k][0] == i:
                        ok = 'true'
                        break
                if ok == 'true' and queue[k][1] > cost[j] + value: #neu dinh da di qua nhung chi phi lon hon chi phi hien tai thi:
                    queue.remove(queue[k]) #xoa dinh do trong queue
                else:
                   continue #neu dinh dang xet khong co trong queue thi bo qua
            else:
                visited[i] = 'true'
                
            queue.append((i, cost[j] + value)) #cap nhat lai gia tri moi   
            j = j + 1
            path[i] = u
            graph[i][3] = red #dinh ke voi dinh dang xet
            graph[i][2] = white #vien cua dinh dang xet
            edges[edge_id(u,i)][1] = white #to mau cac canh dang xet
            graphUI.updateUI()
              
        graph[u][3] = blue #danh dau dinh da xet
        graphUI.updateUI()

        if (queue == []):
            print("Cannot find the path from ", start, " to ", goal)
            return

    graph[start][3] = orange #to mau dinh bat dau
    graph[goal][3] = purple #to mau dinh dich
    i = goal
    while (path[i] != -1):
        edges[tuple(np.sort([path[i], i]))][1] = green
        i = path[i]
    graphUI.updateUI()
    
    print("Implement Uniform Cost Search algorithm.")
    pass

def GBFS(graph, edges, edge_id, start, goal):
    """
    Greedy Best-First search
    """
    # TODO: your code
    
    #them mang h(x) = heuristic luu khoang cach tu dinh do toi goal 
    heuristic = []
    g = graph[goal][0] #toa do dinh goal
    for i in range(0, len(graph)):
        a = graph[i][0] #toa do dinh i
        heuristic.append(np.sqrt((a[0]-g[0])**2 + (a[1]-g[1])**2))

    #print(heuristic)
           
    visited = ['false'] * len(graph) #khoi tao tap cac dinh danh dau chua dc di qua
    visited[start] = 'true'
    path = [-1] * len(graph) #mang luu vet duong di
    queue = []
    queue.append((start, heuristic[start])) # (dinh, h(x))
    
    while (queue != []):
        queue.sort(key = lambda tup: tup[1]) #sap xep queue dua theo h(x)        
        put = queue.pop(0) #lay ra dinh co h(x) nho nhat
        u = put[0] #ten dinh        
        
        graph[u][3] = yellow #dinh dang xet
        
        if (u == goal):
            print("Finish!")
            break
        
        ok = 0 #bien ok kiem tra xem trong ds dinh ke voi u co dinh goal hay khong
        for i in graph[u][1]:  
            if visited[i] == 'false': #tranh lap lai chu trinh
                visited[i] = 'true'
                queue.append((i, heuristic[i])) 
                path[i] = u       
                if (i == goal):
                    ok = 1
                    break
                graph[i][3] = red #dinh ke voi dinh dang xet
                graph[i][2] = white #vien cua dinh dang xet
                edges[edge_id(u,i)][1] = white #to mau cac canh dang xet
                graphUI.updateUI()
        
        if ok == 1:
            break

        graph[u][3] = blue #danh dau dinh da xet
        graphUI.updateUI()

        if (queue == []):
            print("Cannot find the path from ", start, " to ", goal)
            return
    
    graph[start][3] = orange #to mau dinh bat dau
    graph[goal][3] = purple #to mau dinh dich
    i = goal
    while (path[i] != -1):
        edges[tuple(np.sort([path[i], i]))][1] = green
        i = path[i]
       
    graphUI.updateUI()
    print("Implement Greedy Best-first search algorithm.")
    pass

def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    
    #them mang g(x) = weight luu trong so bang cach tinh khoang cach cua 2 dinh
    #va h(x) = heuristic luu khoang cach tu dinh do toi goal 
    weight = []
    heuristic = []
    g = graph[goal][0] #toa do dinh goal
    for i in range(0, len(graph)):
        temp = []
        a = graph[i][0] #toa do dinh i
        for j in graph[i][1]:            
            b = graph[j][0] #toa do dinh j
            d = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
            temp.append(d)
        weight.append(temp)
        heuristic.append(np.sqrt((a[0]-g[0])**2 + (a[1]-g[1])**2))
           
    visited = ['false'] * len(graph) #khoi tao tap cac dinh danh dau chua dc di qua
    visited[start] = 'true'
    path = [] #mang luu vet duong di
    queue = []
    queue.append((start, 0, heuristic[start], 0 + heuristic[start])) # (dinh, g(x), h(x), f(x) = g(x) + h(x))
    
    while (queue != []):
        queue.sort(key = lambda tup: tup[3]) #sap xep queue dua theo f(x) 
        put = queue.pop(0) #lay ra dinh co chi phi nho nhat
        u = put[0] #ten dinh
        visited[u] = 'true' #dinh nao da lay ra thi danh dau lai
        value = put[1] #chi phi cua dinh dang xet
        path.append(u)

        graph[u][3] = yellow #dinh dang xet
        cost = weight[u] #chi phi tu dinh dang xet toi cac dinh ke
      
        if (u == goal):
            print("Finish!")
            break
        
        queue = [] #xoa du lieu cua tap dinh truoc de chuan bi cho lan duyet tiep theo
        j = 0 #bien dem cho mang cost
        for i in graph[u][1]:  
            if visited[i] == 'false': #tranh lap lai chu trinh
                queue.append((i, cost[j] + value, heuristic[i], cost[j] + value + heuristic[i])) #cap nhat lai gia tri moi                       
                graph[i][3] = red #dinh ke voi dinh dang xet
                graph[i][2] = white #vien cua dinh dang xet
                edges[edge_id(u,i)][1] = white #to mau cac canh dang xet
                graphUI.updateUI()
            j = j + 1
        
        graph[u][3] = blue #danh dau dinh da xet
        graphUI.updateUI()

        if (queue == []):
            print("Cannot find the path from ", start, " to ", goal)
            return

    graph[start][3] = orange #to mau dinh bat dau
    graph[goal][3] = purple #to mau dinh dich
    for i in range(1, len(path)):
        edges[tuple(np.sort([path[i-1], path[i]]))][1] = green
       
    graphUI.updateUI()
    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
