import tkinter as tk
from tkinter import ttk
from functools import partial
import folium
import os
import sys
import webbrowser
import openrouteservice
from queue import Queue
from PIL import ImageTk, Image
import math


# Coordinates
Coordinates={
    #el menofia
    "ShebinElkom":          [30.554928799816988, 31.012393143088957],
    "Minouf":               [30.45841991481536, 30.933867041463532],
    "Tala":                 [30.683127111837056, 30.950034191578247],
    "BerketAlseb3":         [30.627495984801378, 31.07244250380298],
    "Elbagoor":             [30.43186671298956, 31.031983255977398],
    "Ashmoon":              [30.300117313578117, 30.97564036423758],
    "Quesna":               [30.56765698894867, 31.149568418149613],
    "Elsadat":              [30.362811748009076, 30.533153025293895],
    "Alshohda":             [30.59768043193886, 30.895758793318098],
    #el gharbia
    "KafrElZayat":          [30.828935887979828, 30.81468363315086],
    "Basioun":              [30.941234859668185, 30.819787152459256],
    "Tanta":                [30.78236661466976, 31.003931835360497],
    "Qutur":                [30.97124133198592, 30.952896608684792],
    "ElMahallaElKubra":     [30.969841036674914, 31.166019730570685],
    "AsSantah":             [30.749281457375343, 31.129532111290036],
    "Samannoud":            [30.96202482138702, 31.241725792395766],
    "Zefta":                [30.714483753839744, 31.240197668420624],
    #el kalubia
    "Banha":                [30.46954041758182, 31.18372798445176],
    "Qalyub":               [30.180143566835696, 31.20638419614639],
    "AlQanatirAlKhayriyyah":[30.194609758641715, 31.13391214967144],
    "ShubraAlKhaymah":      [30.124142365522676, 31.260465002556664],
    "Elkhankah":            [30.22039965655326, 31.368612270866304],
    "Kafrshokr":            [30.552839823187284, 31.255430468410704],
    "ShibinElQanatir":      [30.31214792794175, 31.32292278281032],
    "Toukh":                [30.353756127836252, 31.2014138527108],
}





#-------------------------------------------------------------
#------------ 1- Depth First Search Function -----------------
#-------------------------------------------------------------

def depthFirstSearch(start, end):

    # Using a Python dictionary to act as an adjacency list

    adj_list={
        'ShebinElkom':          ['Tala','Alshohda','Minouf','Elbagoor','Quesna','BerketAlseb3'],
        'Minouf':               ['Alshohda','ShebinElkom','Elbagoor','Ashmoon','Elsadat'],
        'Tala':                 ['BerketAlseb3','ShebinElkom','Alshohda','KafrElZayat','Tanta','AsSantah'],
        'BerketAlseb3':         ['Tala','ShebinElkom','Quesna','AsSantah','Zefta'],
        'Elbagoor':             ['Quesna','ShebinElkom','Minouf','Ashmoon','Banha','Toukh','AlQanatirAlKhayriyyah'],
        'Ashmoon':              ['Elbagoor','Minouf','Elsadat','AlQanatirAlKhayriyyah','Toukh'],
        'Quesna':               ['BerketAlseb3','ShebinElkom','Elbagoor','Zefta','Kafrshokr','Banha'],
        'Elsadat':              ['Ashmoon','Minouf'],
        'Alshohda':             ['Tala','ShebinElkom','Minouf'],
        'KafrElZayat':          ['Basioun','Tanta','Tala'],
        'Basioun':              ['Qutur','Tanta','KafrElZayat'],
        'Qutur':                ['Basioun','Tanta','ElMahallaElKubra'],
        'ElMahallaElKubra':     ['Qutur','Tanta','AsSantah','Zefta','Samannoud'],
        'Samannoud':            ['ElMahallaElKubra','AsSantah','Zefta'],
        'Zefta':                ['Samannoud','ElMahallaElKubra','AsSantah','Quesna','BerketAlseb3','Kafrshokr'],
        'AsSantah':             ['Samannoud','ElMahallaElKubra','BerketAlseb3','Tanta'],
        'Tanta':                ['Tala','KafrElZayat','Basioun','Qutur','ElMahallaElKubra','AsSantah'],
        'Kafrshokr':            ['Zefta','Quesna','Banha'],
        'Banha':                ['Kafrshokr','Quesna','Elbagoor','Toukh','ShibinElQanatir'],
        'Toukh':                ['Banha','Elbagoor','Ashmoon','AlQanatirAlKhayriyyah','Qalyub','ShibinElQanatir'],
        'AlQanatirAlKhayriyyah':['Toukh','Ashmoon','ShubraAlKhaymah','Qalyub'],
        'ShubraAlKhaymah':      ['AlQanatirAlKhayriyyah','Qalyub','Elkhankah'],
        'Qalyub':               ['Elkhankah','ShibinElQanatir','Toukh','AlQanatirAlKhayriyyah','ShubraAlKhaymah'],
        'ShibinElQanatir':      ['Banha','Toukh','Qalyub','Elkhankah'],
        'Elkhankah':            ['ShibinElQanatir','Qalyub','ShubraAlKhaymah']
    }

    visited = [] # Set to keep track of visited nodes of graph.
    allpath = []
    path = []

    def dfs(visited, adj_list, node):  #function for dfs 
        if node not in visited:
            # print (node, end = " ")
            allpath.append(node)
            visited.append(node)
            for neighbour in adj_list[node]:
                dfs(visited, adj_list, neighbour)
                    

    # Driver Code
    first = start
    last = end
    # print("Following is the Depth-First Search")
    dfs(visited, adj_list, first)
    # print(path)
    # print the path
    for point in allpath:
        # print(point)
        path.append(point);
        if point == last:
            break
    # print(allpath)
    # print(path)
    return path

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ////////////////////////////////////////////////////////////////

#-------------------------------------------------------------
#------------ 2- Breadth First Search Function ---------------
#-------------------------------------------------------------

def breadthFirstSearch(start, end):

  adj_list={
    'ShebinElkom':          ['Tala','Alshohda','Minouf','Elbagoor','Quesna','BerketAlseb3'],
    'Minouf':               ['Alshohda','ShebinElkom','Elbagoor','Ashmoon','Elsadat'],
    'Tala':                 ['BerketAlseb3','ShebinElkom','Alshohda','KafrElZayat','Tanta','AsSantah'],
    'BerketAlseb3':         ['Tala','ShebinElkom','Quesna','AsSantah','Zefta'],
    'Elbagoor':             ['Quesna','ShebinElkom','Minouf','Ashmoon','Banha','Toukh','AlQanatirAlKhayriyyah'],
    'Ashmoon':              ['Elbagoor','Minouf','Elsadat','AlQanatirAlKhayriyyah','Toukh'],
    'Quesna':               ['BerketAlseb3','ShebinElkom','Elbagoor','Zefta','Kafrshokr','Banha'],
    'Elsadat':              ['Ashmoon','Minouf'],
    'Alshohda':             ['Tala','ShebinElkom','Minouf'],
    'KafrElZayat':          ['Basioun','Tanta','Tala'],
    'Basioun':              ['Qutur','Tanta','KafrElZayat'],
    'Qutur':                ['Basioun','Tanta','ElMahallaElKubra'],
    'ElMahallaElKubra':     ['Qutur','Tanta','AsSantah','Zefta','Samannoud'],
    'Samannoud':            ['ElMahallaElKubra','AsSantah','Zefta'],
    'Zefta':                ['Samannoud','ElMahallaElKubra','AsSantah','Quesna','BerketAlseb3','Kafrshokr'],
    'AsSantah':             ['Samannoud','ElMahallaElKubra','BerketAlseb3','Tanta'],
    'Tanta':                ['Tala','KafrElZayat','Basioun','Qutur','ElMahallaElKubra','AsSantah'],
    'Kafrshokr':            ['Zefta','Quesna','Banha'],
    'Banha':                ['Kafrshokr','Quesna','Elbagoor','Toukh','ShibinElQanatir'],
    'Toukh':                ['Banha','Elbagoor','Ashmoon','AlQanatirAlKhayriyyah','Qalyub','ShibinElQanatir'],
    'AlQanatirAlKhayriyyah':['Toukh','Ashmoon','ShubraAlKhaymah','Qalyub'],
    'ShubraAlKhaymah':      ['AlQanatirAlKhayriyyah','Qalyub','Elkhankah'],
    'Qalyub':               ['Elkhankah','ShibinElQanatir','Toukh','AlQanatirAlKhayriyyah','ShubraAlKhaymah'],
    'ShibinElQanatir':      ['Banha','Toukh','Qalyub','Elkhankah'],
    'Elkhankah':            ['ShibinElQanatir','Qalyub','ShubraAlKhaymah']
    }

  #bsf code
  first=start
  last=end
  visited={}
  level={}
  parent={}
  bfs_traversal_output=[]
  queue=Queue()
  for node in adj_list.keys():
      visited[node]=False
      parent[node]=None
      level[node]=-1
  # # print(visited)
  # print(level)
  # print(parent)
  visited[first]=True
  level[first]=0
  queue.put(first)
  while not queue.empty():
      u=queue.get()
      bfs_traversal_output.append(u)
      for v in adj_list[u]:
          if not visited[v]:
              visited[v]=True
              parent[v]=u
              level[v]=level[u]+1
              queue.put(v)
  # print(bfs_traversal_output)


  # the shortest path from source node to any node
  # print(level[end])
  path=[]
  while last is not None:
      path.append(last)
      last=parent[last]
  path.reverse()
  # print(path)
  return path

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------


# ////////////////////////////////////////////////////////////////

#---------------------------------------------------------------------
#--------------------- 3- A* Search Function -------------------------
#---------------------------------------------------------------------

def aStar(start, end):


    class Graph:
        def __init__(self, adjac_lis):
            self.adjac_lis = adjac_lis
    
        def get_neighbors(self, v):
            return self.adjac_lis[v]
    
        # This is heuristic function which is having equal values for all nodes
        def h(self, n, v):

            # Cities in project
            ourCities = [
                'ShebinElkom',
                'Minouf',
                'Tala',
                'BerketAlseb3',
                'Elbagoor',
                'Ashmoon',
                'Quesna',
                'Elsadat',
                'Alshohda',
                'KafrElZayat',
                'Basioun',
                'Qutur',
                'ElMahallaElKubra',
                'Samannoud',
                'Zefta',
                'AsSantah',
                'Tanta',
                'Kafrshokr',
                'Banha',
                'Toukh',
                'AlQanatirAlKhayriyyah',
                'ShubraAlKhaymah',
                'Qalyub',
                'ShibinElQanatir',
                'Elkhankah'
            ]

            # distancies
            H = {
                'ShebinElkom':          {

                                        },

                'Minouf':               {

                                        },

                'Tala':                 {

                                        },

                'BerketAlseb3':         {

                                        },

                'Elbagoor':             {

                                        },

                'Ashmoon':              {

                                        },

                'Quesna':               {

                                        },

                'Elsadat':              {

                                        },

                'Alshohda':             {

                                        },

                'KafrElZayat':          {

                                        },

                'Basioun':              {

                                        },

                'Qutur':                {

                                        },

                'ElMahallaElKubra':     {

                                        },

                'Samannoud':            {

                                        },

                'Zefta':                {

                                        },

                'AsSantah':             {

                                        },

                'Tanta':                {

                                        },

                'Kafrshokr':            {

                                        },

                'Banha':                {

                                        },

                'Toukh':                {

                                        },

                'AlQanatirAlKhayriyyah':{

                                        },

                'ShubraAlKhaymah':      {

                                        },

                'Qalyub':               {

                                        },

                'ShibinElQanatir':      {

                                        },

                'Elkhankah':            {

                                        }
                }


            # Calculate Distance Between Two Point
            def distance(city1, city2):
    
                # radius of the Earth
                R = 6373.0

                # coordinates
                lat1 = math.radians(city1[0])
                lon1 = math.radians(city1[1])
                lat2 = math.radians(city2[0])
                lon2 = math.radians(city2[1])

                # change in coordinates
                dlon = lon2 - lon1
                dlat = lat2 - lat1

                # Haversine formula
                a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distance = R * c

                return distance

            # Fill Distances Dictionary
            for i in H:
                for j in ourCities:
                    H[i][j] = distance(Coordinates[i],Coordinates[j])
    
            return H[n][v]
    
        def a_star_algorithm(self, start, stop):
            # In this open_lst is a lisy of nodes which have been visited, but who's 
            # neighbours haven't all been always inspected, It starts off with the start 
            #node
            # And closed_lst is a list of nodes which have been visited
            # and who's neighbors have been always inspected
            open_lst = set([start])
            closed_lst = set([])
    
            # poo has present distances from start to all other nodes
            # the default value is +infinity
            poo = {}
            poo[start] = 0
    
            # par contains an adjac mapping of all nodes
            par = {}
            par[start] = start
    
            while len(open_lst) > 0:
                n = None
    
                # it will find a node with the lowest value of f() -
                for v in open_lst:
                    if n == None or poo[v] + self.h(v,stop) < poo[n] + self.h(n,stop):
                        n = v;
    
                if n == None:
                    print('Path does not exist!')
                    return None
    
                # if the current node is the stop
                # then we start again from start
                if n == stop:
                    reconst_path = []
    
                    while par[n] != n:
                        reconst_path.append(n)
                        n = par[n]
    
                    reconst_path.append(start)
    
                    reconst_path.reverse()
    
                    # print(reconst_path)
                    # print('Path found: {}'.format(reconst_path))
                    return reconst_path
    
                # for all the neighbors of the current node do
                for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                    # add it to open_lst and note n as it's par
                    if m not in open_lst and m not in closed_lst:
                        open_lst.add(m)
                        par[m] = n
                        poo[m] = poo[n] + weight
    
                    # otherwise, check if it's quicker to first visit n, then m
                    # and if it is, update par data and poo data
                    # and if the node was in the closed_lst, move it to open_lst
                    else:
                        if poo[m] > poo[n] + weight:
                            poo[m] = poo[n] + weight
                            par[m] = n
    
                            if m in closed_lst:
                                closed_lst.remove(m)
                                open_lst.add(m)
    
                # remove n from the open_lst, and add it to closed_lst
                # because all of his neighbors were inspected
                open_lst.remove(n)
                closed_lst.add(n)
    
            print('Path does not exist!')
            return None


    adj_list={
        'ShebinElkom':          [
                                    ('Tala', 18), 
                                    ('Alshohda', 16.5),
                                    ('Minouf',16.4),
                                    ('Elbagoor',14.6),
                                    ('Quesna',18.7),
                                    ('BerketAlseb3', 14)
                                ],

        'Minouf':               [
                                    ('Alshohda',18.2),
                                    ('ShebinElkom', 16.1),
                                    ('Elbagoor',11.4),
                                    ('Ashmoon',27),
                                    ('Elsadat',55.9)
                                ],

        'Tala':                 [
                                    ('BerketAlseb3',18.1),
                                    ('ShebinElkom', 18),
                                    ('Alshohda',14.4),
                                    ('KafrElZayat',25.6),
                                    ('Tanta',15.3),
                                    ('AsSantah',29.2)
                                ],

        'BerketAlseb3':         [
                                    ('Tala',18.1),
                                    ('ShebinElkom', 14),
                                    ('Quesna',13.3),
                                    ('AsSantah',16),
                                    ('Zefta',24.5)
                                ],

        'Elbagoor':             [
                                    ('Quesna',29.8),
                                    ('ShebinElkom',14.9),
                                    ('Minouf',11.5),
                                    ('Ashmoon',22.5),
                                    ('Banha',26.6),
                                    ('Toukh',39.7),
                                    ('AlQanatirAlKhayriyyah',30.8)
                                ],

        'Ashmoon':              [
                                    ('Elbagoor',23.8),
                                    ('Minouf',27.1),
                                    ('Elsadat',61.7),
                                    ('AlQanatirAlKhayriyyah',23.5),
                                    ('Toukh',56.3)
                                ],

        'Quesna':               [
                                    ('BerketAlseb3',13.9),
                                    ('ShebinElkom',18.1),
                                    ('Elbagoor',18.1),
                                    ('Zefta',21.1),
                                    ('Kafrshokr',26.8),
                                    ('Banha',15.1)
                                ],

        'Elsadat':              [
                                    ('Ashmoon',73.8),
                                    ('Minouf',54.5)
                                ],

        'Alshohda':             [
                                    ('Tala',14.4),
                                    ('ShebinElkom',17.5),
                                    ('Minouf',18.2)
                                ],

        'KafrElZayat':          [
                                    ('Basioun',20.2),
                                    ('Tanta',27.6),
                                    ('Tala',25.6)
                                ],

        'Basioun':              [
                                    ('Qutur',16.8),
                                    ('Tanta',28.8),
                                    ('KafrElZayat',20.2)
                                ],

        'Qutur':                [
                                    ('Basioun',17.1),
                                    ('Tanta',16.3),
                                    ('ElMahallaElKubra',28.8)
                                ],

        'ElMahallaElKubra':     [
                                    ('Qutur',30.8),
                                    ('tanta',31.5),
                                    ('AsSantah',30.8),
                                    ('Zefta',33.3),
                                    ('Samannoud',7.7)
                                ],

        'Samannoud':            [
                                    ('ElMahallaElKubra',7.8),
                                    ('AsSantah',46.6),
                                    ('Zefta',33.1)
                                ],

        'Zefta':                [
                                    ('Samannoud',35),
                                    ('ElMahallaElKubra',32.7),
                                    ('AsSantah',17.9),
                                    ('Quesna',21.1),
                                    ('BerketAlseb3',25.3),
                                    ('Kafrshokr',27.9)
                                ],

        'AsSantah':             [
                                    ('Samannoud',48.7),
                                    ('ElMahallaElKubra',30.3),
                                    ('BerketAlseb3',16.2),
                                    ('Tanta',25.3)
                                ],

        'Tanta':                [
                                    ('Tala',15),
                                    ('KafrElZayat',26.4),
                                    ('Basioun',28.3),
                                    ('Qutur',16),
                                    ('ElMahallaElKubra',29.2),
                                    ('AsSantah',25.9)
                                ],

        'Kafrshokr':            [
                                    ('Zefta',32.7),
                                    ('Quesna',23.1),
                                    ('Banha',13.4)
                                ],

        'Banha':                [
                                    ('Kafrshokr',17.7),
                                    ('Quesna',17.8),
                                    ('Elbagoor',29.4),
                                    ('Toukh',15.6),
                                    ('ShibinElQanatir',28.8)
                                ],

        'Toukh':                [
                                    ('Banha',17.5),
                                    ('Elbagoor',40),
                                    ('Ashmoon',57.5),
                                    ('AlQanatirAlKhayriyyah',25),
                                    ('Qalyub',22),
                                    ('ShibinElQanatir',14)
                                ],

        'AlQanatirAlKhayriyyah':[
                                    ('Toukh',24.7),
                                    ('Ashmoon',23.5),
                                    ('ShubraAlKhaymah',18.5),
                                    ('Qalyub',7.6)
                                ],

        'ShubraAlKhaymah':      [
                                    ('AlQanatirAlKhayriyyah',18.4),
                                    ('Qalyub',11.6),
                                    ('Elkhankah',22.4)
                                ],

        'Qalyub':               [
                                    ('Elkhankah',26.9),
                                    ('ShibinElQanatir',20.6),
                                    ('Toukh',22.7),
                                    ('AlQanatirAlKhayriyyah',7.6),
                                    ('ShubraAlKhaymah',12.1)
                                ],

        'ShibinElQanatir':      [
                                    ('Banha',29.8),
                                    ('Toukh',14),
                                    ('Qalyub',20.4),
                                    ('Elkhankah',17.6)
                                ],

        'Elkhankah':            [
                                    ('ShibinElQanatir',15.9),
                                    ('Qalyub',27.4),
                                    ('ShubraAlKhaymah', 24.4)
                                ],
                                
        }

    first = start
    last = end
    graph1 = Graph(adj_list)
    path = graph1.a_star_algorithm(first, last)
    return path

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# ////////////////////////////////////////////////////////////////

#---------------------------------------------------------------------
#--------------------- 4- Dijkstra Function -------------------------
#---------------------------------------------------------------------

def dijkstra(start, end):
    # Graph Object
	class Graph(object):
		def __init__(self, nodes, init_graph):
			self.nodes = nodes
			self.graph = self.construct_graph(nodes, init_graph)
			
		def construct_graph(self, nodes, init_graph):
			
			# This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
			
			graph = {}
			for node in nodes:
				graph[node] = {}
			
			graph.update(init_graph)
			
			for node, edges in graph.items():
				for adjacent_node, value in edges.items():
					if graph[adjacent_node].get(node, False) == False:
						graph[adjacent_node][node] = value
						
			return graph
		
		def get_nodes(self):
			# "Returns the nodes of the graph."
			return self.nodes
		
		def get_outgoing_edges(self, node):
			# "Returns the neighbors of a node."
			connections = []
			for out_node in self.nodes:
				if self.graph[node].get(out_node, False) != False:
					connections.append(out_node)
			return connections
		
		def value(self, node1, node2):
			# "Returns the value of an edge between two nodes."
			return self.graph[node1][node2]


	# Algorithm function
	def dijkstra_algorithm(graph, start_node):
		unvisited_nodes = list(graph.get_nodes())

		# We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
		shortest_path = {}

		# We'll use this dict to save the shortest known path to a node found so far
		previous_nodes = {}

		# We'll use max_value to initialize the "infinity" value of the unvisited nodes   
		max_value = sys.maxsize
		for node in unvisited_nodes:
			shortest_path[node] = max_value
		# However, we initialize the starting node's value with 0   
		shortest_path[start_node] = 0

		# The algorithm executes until we visit all nodes
		while unvisited_nodes:
			# The code block below finds the node with the lowest score
			current_min_node = None
			for node in unvisited_nodes: # Iterate over the nodes
				if current_min_node == None:
					current_min_node = node
				elif shortest_path[node] < shortest_path[current_min_node]:
					current_min_node = node
					
			# The code block below retrieves the current node's neighbors and updates their distances
			neighbors = graph.get_outgoing_edges(current_min_node)
			for neighbor in neighbors:
				tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
				if tentative_value < shortest_path[neighbor]:
					shortest_path[neighbor] = tentative_value
					# We also update the best path to the current node
					previous_nodes[neighbor] = current_min_node

			# After visiting its neighbors, we mark the node as "visited"
			unvisited_nodes.remove(current_min_node)

		return previous_nodes


	# Print Function
	def print_result(previous_nodes, start_node, target_node):
		path = []
		node = target_node
		
		while node != start_node:
			path.append(node)
			node = previous_nodes[node]
	
		# Add the start node manually
		path.append(start_node)

		# print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
		return path[::-1]

	# Main Code
	adj_list = {
        'ShebinElkom':                   {
                                        'Tala': 18,
                                        'Alshohda': 16.5,
                                        'Minouf':16.4,
                                        'Elbagoor':14.6,
                                        'Quesna':18.7,
                                        'BerketAlseb3': 14
                                    },

		'Minouf':                    {
                                        'Alshohda':18.2,
                                        'ShebinElkom': 16.1,
                                        'Elbagoor':11.4,
                                        'Ashmoon':27,
                                        'Elsadat':55.9
                                    },

        'Tala':                     {
                                        'BerketAlseb3':18.1,
                                        'ShebinElkom': 18,
                                        'Alshohda':14.4,
                                        'KafrElZayat':25.6,
                                        'Tanta':15.3,
                                        'AsSantah':29.2
                                    },

        'BerketAlseb3':            {
                                        'Tala':18.1,
                                        'ShebinElkom': 14,
                                        'Quesna':13.3,
                                        'AsSantah':16,
                                        'Zefta':24.5
                                    },

        'Elbagoor':                {
                                        'Quesna':29.8,
                                        'ShebinElkom':14.9,
                                        'Minouf':11.5,
                                        'Ashmoon':22.5,
                                        'Banha':26.6,
                                        'Toukh':39.7,
                                        'AlQanatirAlKhayriyyah':30.8
                                    },

        'Ashmoon':                   {
                                        'Elbagoor':23.8,
                                        'Minouf':27.1,
                                        'Elsadat':61.7,
                                        'AlQanatirAlKhayriyyah':23.5,
                                        'Toukh':56.3
                                    },

        'Quesna':                 {
                                        'BerketAlseb3':13.9,
                                        'ShebinElkom':18.1,
                                        'Elbagoor':18.1,
                                        'Zefta':21.1,
                                        'Kafrshokr':26.8,
                                        'Banha':15.1
                                    },

        'Elsadat':            {
                                        'Ashmoon':73.8,
                                        'Minouf':54.5
                                    },

        'Alshohda':               {
                                        'Tala':14.4,
                                        'ShebinElkom':17.5,
                                        'Minouf':18.2
                                    },

        'KafrElZayat':            {
                                        'Basioun':20.2,
                                        'Tanta':27.6,
                                        'Tala':25.6
                                    },

        'Basioun':                  {
                                        'Qutur':16.8,
                                        'Tanta':28.8,
                                        'KafrElZayat':20.2
                                    },

        'Qutur':                    {
                                        'Basioun':17.1,
                                        'Tanta':16.3,
                                        'ElMahallaElKubra':28.8
                                    },

        'ElMahallaElKubra':      {
                                        'Qutur':30.8,
                                        'Tanta':31.5,
                                        'AsSantah':30.8,
                                        'Zefta':33.3,
                                        'Samannoud':7.7
                                    },

        'Samannoud':                {
                                        'ElMahallaElKubra':7.8,
                                        'AsSantah':46.6,
                                        'Zefta':33.1
                                    },

        'Zefta':                    {
                                        'Samannoud':35,
                                        'ElMahallaElKubra':32.7,
                                        'AsSantah':17.9,
                                        'Quesna':21.1,
                                        'BerketAlseb3':25.3,
                                        'Kafrshokr':27.9
                                    },

        'AsSantah':                {
                                        'Samannoud':48.7,
                                        'ElMahallaElKubra':30.3,
                                        'BerketAlseb3':16.2,
                                        'Tanta':25.3
                                    },

        'Tanta':                    {
                                        'Tala':15,
                                        'KafrElZayat':26.4,
                                        'Basioun':28.3,
                                        'Qutur':16,
                                        'ElMahallaElKubra':29.2,
                                        'AsSantah':25.9
                                    },

        'Kafrshokr':               {
                                        'Zefta':32.7,
                                        'Quesna':23.1,
                                        'Banha':13.4
                                    },

        'Banha':                    {
                                        'Kafrshokr':17.7,
                                        'Quesna':17.8,
                                        'Elbagoor':29.4,
                                        'Toukh':15.6,
                                        'ShibinElQanatir':28.8
                                    },

        'Toukh':                    {
                                        'Banha':17.5,
                                        'Elbagoor':40,
                                        'Ashmoon':57.5,
                                        'AlQanatirAlKhayriyyah':25,
                                        'Qalyub':22,
                                        'ShibinElQanatir':14
                                    },

        'AlQanatirAlKhayriyyah': {
                                        'Toukh':24.7,
                                        'Ashmoon':23.5,
                                        'ShubraAlKhaymah':18.5,
                                        'Qalyub':7.6
                                    },

        'ShubraAlKhaymah':        {
                                        'AlQanatirAlKhayriyyah':18.4,
                                        'Qalyub':11.6,
                                        'Elkhankah':22.4
                                    },

        'Qalyub':                   {
                                        'Elkhankah':26.9,
                                        'ShibinElQanatir':20.6,
                                        'Toukh':22.7,
                                        'AlQanatirAlKhayriyyah':7.6,
                                        'ShubraAlKhaymah':12.1
                                    },

        'ShibinElQanatir':        {
                                        'Banha':29.8,
                                        'Toukh':14,
                                        'Qalyub':20.4,
                                        'Elkhankah':17.6
                                    },

        'Elkhankah':               {
                                        'ShibinElQanatir':15.9,
                                        'Qalyub':27.4,
                                        'ShubraAlKhaymah': 24.4
                                    },
	}

	ourCities = [
        'ShebinElkom',
        'Minouf',
        'Tala',
        'BerketAlseb3',
        'Elbagoor',
        'Ashmoon',
        'Quesna',
        'Elsadat',
        'Alshohda',
        'KafrElZayat',
        'Basioun',
        'Qutur',
        'ElMahallaElKubra',
        'Samannoud',
        'Zefta',
        'AsSantah',
        'Tanta',
        'Kafrshokr',
        'Banha',
        'Toukh',
        'AlQanatirAlKhayriyyah',
        'ShubraAlKhaymah',
        'Qalyub',
        'ShibinElQanatir',
        'Elkhankah'
    ]
	graph = Graph(ourCities, adj_list)
	previous_nodes = dijkstra_algorithm(graph, start)
	path = print_result(previous_nodes,start,end)
	return path

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------

# ////////////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#---------------------- 5- Show Function -------------------------
#-----------------------------------------------------------------

def showfunc(start, end, algo):
    start= start_city.get()
    end  = end_city.get()
    algo = Algorithm.get()
    path = []

    if start != "Start" and end != "End" and algo != "Algorithm":

        #  Check Algorithm type
        if algo == 'depth':
            path = depthFirstSearch(start, end)
        elif algo == 'breadth':
            path = breadthFirstSearch(start, end)
        elif algo == 'astar':
            path = aStar(start, end)
        elif algo == 'dijkstra':
            path = dijkstra(start, end)

        # print(path)

        # Creat Map Key
        client = openrouteservice.Client(key='5b3ce3597851110001cf62489f97821fab9b46a18afb841b2c9226af')

        # create map object
        m = folium.Map(location=[30.597246, 30.987632], zoom_start=10)

        for item in path:
            if item == start:
                folium.Marker(location=Coordinates[item], popup=item, tooltip='Start Point', icon=folium.Icon(color='green')).add_to(m),
            elif item == end:
                folium.Marker(location=Coordinates[item], popup=item, tooltip='End Point', icon=folium.Icon(color='red')).add_to(m),
            else:
                folium.Marker(location=Coordinates[item], popup=item, tooltip=item).add_to(m),


        for i in range(len(path)-1):
            coord = [Coordinates[path[i]][::-1], Coordinates[path[i+1]][::-1]]
            route = client.directions(coordinates=coord,profile='driving-car',format='geojson')
            folium.GeoJson(route, name='route').add_to(m)


        # folium.LayerControl().add_to(m)
        m.save('indexV5.html')

        #open file of html
        filename = 'file:///'+os.getcwd()+'/' + 'indexV5.html'
        webbrowser.open_new_tab(filename)

    else:
        print('Please Enter All Information')

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ////////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#---------------- Get Information From User ----------------------
#-----------------------------------------------------------------

# Declare The Window
window = tk.Tk(className=' Search Algorithm')
window.geometry('550x500+500+150')

# Set Window Style
window.configure(bg='blue')
window['background']='#856ff8'
photo = ImageTk.PhotoImage(Image.open('4.jpeg'))
logo = ttk.Label(window, image=photo)
logo.pack()

# Choose Start City
ttk.Label(text="Start City",foreground='silver',background='brown',font=('Aria', 15, 'bold')).place(x=100, y=230)
start_city= tk.StringVar()
start_city.set("Start")
start_city_Chossen = ttk.Combobox(window,width=12, textvariable=start_city)
start_city_Chossen['value']=('Tala','Alshohda','BerketAlseb3','Quesna','ShebinElkom','Minouf','Elbagoor','Ashmoon','Elsadat','KafrElZayat','Basioun','Tanta','Qutur','ElMahallaElKubra' ,'AsSantah','Samannoud','Zefta','Banha','Qalyub','AlQanatirAlKhayriyyah','ShubraAlKhaymah','Elkhankah','Kafrshokr','Toukh', 'ShibinElQanatir')
start_city_Chossen.place(x=100, y=260)


# Choose End City
ttk.Label(text="End City",foreground='silver',background='brown',font=('Aria', 15, 'bold')).place(x=200, y=230)
end_city= tk.StringVar()
end_city.set("End")
end_city_Chossen = ttk.Combobox(window,width=12, textvariable=end_city)
end_city_Chossen['value']=('Tala','Alshohda','BerketAlseb3','Quesna','ShebinElkom','Minouf','Elbagoor','Ashmoon','Elsadat','KafrElZayat','Basioun','Tanta','Qutur','ElMahallaElKubra' ,'AsSantah','Samannoud','Zefta','Banha','Qalyub','AlQanatirAlKhayriyyah','ShubraAlKhaymah','Elkhankah','Kafrshokr','Toukh', 'ShibinElQanatir')
end_city_Chossen.place(x=200, y=260)

# Choose Algorithm
ttk.Label(text="Algorithm",foreground='silver',background='brown',font=('Aria', 15, 'bold')).place(x=300, y=230)
Algorithm = tk.StringVar()
Algorithm.set("Algorithm")
Algorithm_Chossen = ttk.Combobox(window,width=12, textvariable=Algorithm)
Algorithm_Chossen['value']=('astar','breadth','depth', 'dijkstra')
Algorithm_Chossen.place(x=300, y=260)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ///////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#------------------------- Show Map ------------------------------
#-----------------------------------------------------------------

# Show Button
Enter=tk.Button(text='Enter',bg='blue', fg='white',font=('Aria', 15, 'bold'),command=partial(showfunc,start_city_Chossen, end_city_Chossen, Algorithm_Chossen))
Enter.place(x=170, y=300)

# Quite Button
quit= tk.Button(window, text='Quit',bg='grey', fg='white',font=('Aria', 15, 'bold'), command=window.quit)
quit.place(x=270, y=300)

window.mainloop()

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------