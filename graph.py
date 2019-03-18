# Name: Allie Blaising

from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False 
        self.color = None 

    def get_connections(self): 
      return self.connectedTo.keys()

    # I don't think I need this? Check in office hours? 

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        
        self.numVertices = 0
        self.vertList = []
        self.vertexDict = {}
        input_file = open(filename, "r") # Reads in textfile 
        for line in input_file: 
            vertices = line.split() # Split the vertices 
            for vertex in vertices:
                self.add_vertex(vertex) # Add all vertices on the line to the graph 
            self.add_edge(vertices[0], vertices[1]) # Once added, link edges 
        input_file.close() 
        

    def in_graph(self, key):
        if key in self.vertList:   
            return True 
        else:
            return False

    # Function to check if a key is in a graph 

    def add_vertex(self, key):
        if self.vertexDict.get(key) is None: # Checks if key doesn't exist 
            newVertex = Vertex(key) # Create new vertex w/ key 
            self.numVertices += 1 # Increment 
            self.vertexDict[key] = newVertex # Assign newly created vertex to the location in the vertex dictionary  
            # that corresponds to key 
            self.vertList.append(key) # Add key to adjacency list 

        '''Add vertex to graph, only if the vertex is not already in the graph.'''


    def get_vertex(self, key):
        if key in self.vertList:
            return self.vertexDict[key]
        else:
            return None
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''


    def add_edge(self, v1, v2):
        self.vertexDict[v1].adjacent_to.append(v2)
        self.vertexDict[v2].adjacent_to.append(v1)
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''


    def get_vertices(self): 
        keys = self.vertList
        keys.sort()
        return keys
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        
## Implement w/ Stack: 

    def conn_components(self): 
        comp_stack = Stack(self.numVertices)
        return_list = []
        for i in self.vertList: 
            self.vertexDict[i].color = False
        for key in self.vertList: 
            if self.vertexDict[key].visited == False: 
                vertex_sub = []
                comp_stack.push(self.vertexDict[key])
                while not comp_stack.is_empty(): 
                    returned = comp_stack.pop()
                    if returned.visited == False: 
                        vertex_sub.append(returned.id)
                        vertex_sub.sort()
                        returned.visited = True 
                        for i in returned.adjacent_to: 
                            if self.vertexDict[i].visited == False: 
                                comp_stack.push(self.vertexDict[i])
                return_list.append(vertex_sub)
        return return_list

            # push 
            # while not empty, pull out vertex, 
            # mark vertex as visited 
            # push any vertexs in vertex adjeaceny list if unvisited 
            # stack is not empty, pop out v4, mark as visited 
            # another check, if not visited, add to list 
            # sort vertices sublists 


        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''

    # Review the logic here & comment tomorrow: 

## Implement w/ Queue: 

    def is_bipartite(self):
        bi_stack = Queue(self.numVertices)
        for i in self.vertList: 
            self.vertexDict[i].color = None 
        for key in self.vertList: 
            if self.vertexDict[key].color == None: 
                self.vertexDict[key].color = "Blue"
                bi_stack.enqueue(self.vertexDict[key])
                while not bi_stack.is_empty(): 
                    returned = bi_stack.dequeue()
                    for i in returned.adjacent_to:
                        if self.vertexDict[i].color == returned.color: 
                            return False
                        elif self.vertexDict[i].color == None: 
                            if returned.color == "Blue": 
                                new_color = "Red"
                            elif returned.color == "Red": 
                                new_color = "Blue"
                            self.vertexDict[i].color = new_color
                            bi_stack.enqueue(self.vertexDict[i])
        return True


                        # adjacent vertex is colored 
                        # adjacent vertext is uncolored 
                        # if colored, check to see if color is the other color 


        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''

        # 


'''
    def depth_first(self, temp, v, visited): 
        visited[v] = True
        temp.append(v) 
        for i in self.adj[v]: 
          if visited[i] == False: 
            temp = self.depth_first(temp, i, visited) 
        return temp 

    def conn_components(self): 
        visited_list = [] 
        connected_components = [] 
        for i in range(self.V): 
            visited_list.append(False) 
        for v in range(self.V): 
            if visited_list[v] == False: 
                temp = [] 
                connected_components.append(self.depth_first(temp, v, visited)) 
        return connected_components

        color_list = [-1] * self.V 
        color_list[0] = 1
        queue = [] 
        queue.append(self.V[0]) 
        while queue: 
            u = queue.pop() 
            if self.graph[u][u] == 1: 
                return False 
            for v in range(self.V):
                if self.graph[u][v] == 1 and colorArr[v] == -1: 
                    colorArr[v] = 1 - colorArr[u] 
                    queue.append(v) 
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]: 
                    return False
        return True

'''


