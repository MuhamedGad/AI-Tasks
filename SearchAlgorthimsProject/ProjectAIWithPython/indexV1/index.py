import tkinter as tk
from tkinter import ttk
from functools import partial
import folium
import os
import webbrowser
import openrouteservice
from queue import Queue

#-------------------------------------------------------------
#------------ 1- Depth First Search Function -----------------
#-------------------------------------------------------------

def depthFirstSearch(start, end):

    # Using a Python dictionary to act as an adjacency list

    adj_list={
            'Tala':         ['ShebinElkom'],
            'Alshohda':     ['Minouf'],
            'BerketAlseb3': ['Quesna', 'ShebinElkom'],
            'Quesna':       ['BerketAlseb3','ShebinElkom'],
            'ShebinElkom':  ['Tala','Minouf','Quesna','BerketAlseb3'],
            'Minouf':       ['SirsAllyan','ShebinElkom','Alshohda'],
            'SirsAllyan':   ['Minouf','Elbagoor'],
            'Elbagoor':     ['SirsAllyan'],
            'Ashmoon':      ['Elsadat'],
            'Elsadat':      ['Minouf', 'Ashmoon']
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

#-----------------------------------------------------------------
#------------ 2- Breadth First Search Function -------------------
#-----------------------------------------------------------------

def breadthFirstSearch(start, end):

  adj_list={
            'Tala':         ['ShebinElkom'],
            'Alshohda':     ['Minouf'],
            'BerketAlseb3': ['Quesna', 'ShebinElkom'],
            'Quesna':       ['BerketAlseb3','ShebinElkom'],
            'ShebinElkom':  ['Tala','Minouf','Quesna','BerketAlseb3'],
            'Minouf':       ['SirsAllyan','ShebinElkom','Alshohda'],
            'SirsAllyan':   ['Minouf','Elbagoor'],
            'Elbagoor':     ['SirsAllyan'],
            'Ashmoon':      ['Elsadat'],
            'Elsadat':      ['Minouf', 'Ashmoon']
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

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ////////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#--------------------- 3- A* Search Function ---------------------
#-----------------------------------------------------------------

def aStar(start, end):


    class Graph:
        def __init__(self, adjac_lis):
            self.adjac_lis = adjac_lis
    
        def get_neighbors(self, v):
            return self.adjac_lis[v]
    
        # This is heuristic function which is having equal values for all nodes
        def h(self, n, v):
            
            H = {
                'Tala':         {
                                    'Tala': 0,
                                    'Alshohda': 13.7,
                                    'BerketAlseb3': 19.7,
                                    'Quesna': 32.8,
                                    'ShebinElkom': 16.3,
                                    'Minouf': 32,
                                    'SirsAllyan': 31.5,
                                    'Elbagoor': 31.9,
                                    'Ashmoon': 56.5,
                                    'Elsadat': 77.5
                                },

                'Alshohda':     {
                                    'Tala': 13.7,
                                    'Alshohda': 0,
                                    'BerketAlseb3': 28.9,
                                    'Quesna': 30.8,
                                    'ShebinElkom': 14.3,
                                    'Minouf': 22.8,
                                    'SirsAllyan': 27.1,
                                    'Elbagoor': 30.7,
                                    'Ashmoon': 41.6,
                                    'Elsadat': 78.9,
                                },

                'BerketAlseb3': {
                                    'Tala': 19.7,
                                    'Alshohda': 28.9,
                                    'BerketAlseb3': 0,
                                    'Quesna': 17.1,
                                    'ShebinElkom': 15.2,
                                    'Minouf': 31.6,
                                    'SirsAllyan': 30.1,
                                    'Elbagoor': 29.2,
                                    'Ashmoon': 51.5,
                                    'Elsadat': 82,
                                },

                'Quesna':       {
                                    'Tala': 32.8,
                                    'Alshohda': 30.8,
                                    'BerketAlseb3': 17.1,
                                    'Quesna': 0,
                                    'ShebinElkom': 18.3,
                                    'Minouf': 33.7,
                                    'SirsAllyan': 32.5,
                                    'Elbagoor': 33.7,
                                    'Ashmoon': 50.1,
                                    'Elsadat': 87.7,
                                },

                'ShebinElkom':  {
                                    'Tala': 16.3,
                                    'Alshohda': 14.3,
                                    'BerketAlseb3': 14.3,
                                    'Quesna': 18.3,
                                    'ShebinElkom': 0,
                                    'Minouf': 17.9,
                                    'SirsAllyan': 16.2,
                                    'Elbagoor': 16.2,
                                    'Ashmoon': 39.1,
                                    'Elsadat': 67.5,
                                },

                'Minouf':       {
                                    'Tala': 32,
                                    'Alshohda': 22.8,
                                    'BerketAlseb3': 31.6,
                                    'Quesna': 33.7,
                                    'ShebinElkom': 17.9,
                                    'Minouf': 0,
                                    'SirsAllyan': 7.2,
                                    'Elbagoor': 17.1,
                                    'Ashmoon': 24.1,
                                    'Elsadat': 57.7,
                                },

                'SirsAllyan':   {
                                    'Tala': 31.5,
                                    'Alshohda': 27.1,
                                    'BerketAlseb3': 30.1,
                                    'Quesna': 32.5,
                                    'ShebinElkom': 16.2,
                                    'Minouf': 7.2,
                                    'SirsAllyan': 0,
                                    'Elbagoor': 8.3,
                                    'Ashmoon': 22.2,
                                    'Elsadat': 62.6,
                                },

                'Elbagoor':     {
                                    'Tala': 31.9,
                                    'Alshohda': 30.7,
                                    'BerketAlseb3': 29.2,
                                    'Quesna': 33.7,
                                    'ShebinElkom': 16.2,
                                    'Minouf': 17.1,
                                    'SirsAllyan': 8.3,
                                    'Elbagoor': 0,
                                    'Ashmoon': 21,
                                    'Elsadat': 70.6,
                                },

                'Ashmoon':      {
                                    'Tala': 56.5,
                                    'Alshohda': 41.6,
                                    'BerketAlseb3': 51.5,
                                    'Quesna': 50.1,
                                    'ShebinElkom': 39.1,
                                    'Minouf': 24.1,
                                    'SirsAllyan': 22.2,
                                    'Elbagoor': 21,
                                    'Ashmoon': 0,
                                    'Elsadat': 75,
                                },

                'Elsadat':      {
                                    'Tala': 77.5,
                                    'Alshohda': 78.9,
                                    'BerketAlseb3': 82,
                                    'Quesna': 87.7,
                                    'ShebinElkom': 67.5,
                                    'Minouf': 57.6,
                                    'SirsAllyan': 62.6,
                                    'Elbagoor': 70.6,
                                    'Ashmoon': 75,
                                    'Elsadat': 0,
                                }

            }
    
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
            'Tala':         [('ShebinElkom', 16.3)],
            'Alshohda':     [('Minouf', 22.8)],
            'BerketAlseb3': [('Quesna', 17.1), ('ShebinElkom', 14.3)],
            'Quesna':       [('BerketAlseb3', 17.1),('ShebinElkom', 18.3)],
            'ShebinElkom':  [('BerketAlseb3', 14.3),('Tala', 16.3),('Minouf', 17.9),('Quesna', 18.3)],
            'Minouf':       [('SirsAllyan', 7.2),('ShebinElkom', 17.9),('Alshohda', 22.8)],
            'SirsAllyan':   [('Minouf', 7.2),('Elbagoor', 8.3)],
            'Elbagoor':     [('SirsAllyan', 3.8)],
            'Ashmoon':      [('Elsadat', 75)],
            'Elsadat':      [('Minouf', 57.6), ('Ashmoon', 75)]
            }

    first = start
    last = end
    graph1 = Graph(adj_list)
    path = graph1.a_star_algorithm(first, last)
    return path

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ////////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#---------------------- 4- Show Function -------------------------
#-----------------------------------------------------------------

def showfunc(start, end, algo):
    start= start_city.get()
    end  = end_city.get()
    algo = algorithm.get()
    path = []
    # algo = 'breadth'
    # start = 'Minouf'
    # end = 'Tala'

    #  Check Algorithm type
    if algo == 'depth':
        path = depthFirstSearch(start, end)
    elif algo == 'breadth':
        path = breadthFirstSearch(start, end)
    elif algo == 'astar':
        path = aStar(start, end)

    print(path)
    # print(path[0])


    # Coordinates of cities
    Coordinates={
    #el menofia
    "ShebinElkom":  [30.554928799816988, 31.012393143088957],
    "Minouf":       [30.45841991481536, 30.933867041463532],
    "Tala":         [30.683127111837056, 30.950034191578247],
    "BerketAlseb3": [30.627495984801378, 31.07244250380298],
    "Elbagoor":     [30.43186671298956, 31.031983255977398],
    "Ashmoon":      [30.300117313578117, 30.97564036423758],
    "Quesna":       [30.56765698894867, 31.149568418149613],
    "Elsadat":      [30.362811748009076, 30.533153025293895],
    "Alshohda":     [30.59768043193886, 30.895758793318098],
    "SirsAllyan":   [30.439229091007064, 30.96737901607289]
    }

    client = openrouteservice.Client(key='5b3ce3597851110001cf62489f97821fab9b46a18afb841b2c9226af')

    # create map object
    m = folium.Map(location=[30.597246, 30.987632], zoom_start=11)

    for item in path:
        if item == start:
            folium.Marker(location=Coordinates[item], popup=item, tooltip='Start Point', icon=folium.Icon(color='red')).add_to(m),
        elif item == end:
            folium.Marker(location=Coordinates[item], popup=item, tooltip='End Point', icon=folium.Icon(color='green')).add_to(m),
        else:
            folium.Marker(location=Coordinates[item], popup=item, tooltip=item).add_to(m),


    for i in range(len(path)-1):
        coord = [Coordinates[path[i]][::-1], Coordinates[path[i+1]][::-1]]
        route = client.directions(coordinates=coord,profile='driving-car',format='geojson')
        folium.GeoJson(route, name='route').add_to(m)


    # folium.LayerControl().add_to(m)
    m.save('index.html')

    #open file of html
    filename = 'file:///'+os.getcwd()+'/' + 'index.html'
    webbrowser.open_new_tab(filename)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ////////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#----------------- Get Variables From User -----------------------
#-----------------------------------------------------------------

window = tk.Tk()
window.geometry('500x500')

# Choose Start City
ttk.Label(text="Start City").grid(column=1,row=0)
options_list_start = ['Tala','Alshohda','BerketAlseb3','Quesna','ShebinElkom','Minouf','SirsAllyan','Elbagoor','Ashmoon','Elsadat']
start_city= tk.StringVar(window)
start_city.set("Select Start Point")
question_menu_start = tk.OptionMenu(window, start_city, *options_list_start)
# question_menu.pack()
# start_city_Chossen = ttk.Combobox(window,width=12, textvariable=start_city)
# start_city_Chossen['value']=('Tala','Alshohda','BerketAlseb3','Quesna','ShebinElkom','Minouf','SirsAllyan','Elbagoor','Ashmoon','Elsadat')
question_menu_start.grid(column=1,row=1)

# Choose Start End
ttk.Label(text="End City").grid(column=2,row=0)
options_list_end = ['Tala','Alshohda','BerketAlseb3','Quesna','ShebinElkom','Minouf','SirsAllyan','Elbagoor','Ashmoon','Elsadat']
end_city= tk.StringVar(window)
end_city.set("Select End Point")
question_menu_end = tk.OptionMenu(window, end_city, *options_list_end)
# end_city_Chossen = ttk.Combobox(window,width=12, textvariable=end_city)
# end_city_Chossen['value']=('Tala','Alshohda','BerketAlseb3','Quesna','ShebinElkom','Minouf','SirsAllyan','Elbagoor','Ashmoon','Elsadat')
question_menu_end.grid(column=2,row=1)

# Choose Algorithm
ttk.Label(text="Algorithm").grid(column=3,row=0)
options_list_algo = ['astar','breadth','depth']
algorithm = tk.StringVar(window)
algorithm.set("Select Algorithm")
question_menu_algo = tk.OptionMenu(window, algorithm, *options_list_algo)
# Algorithm_Chossen = ttk.Combobox(window,width=12, textvariable=Algorithm)
# Algorithm_Chossen['value']=('astar','breadth','depth')
question_menu_algo.grid(column=3,row=1)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# ///////////////////////////////////////////////////////////////

#-----------------------------------------------------------------
#------------------------ Show Map -------------------------------
#-----------------------------------------------------------------

# Clicked Button
button=ttk.Button(text='Enter',command=partial(showfunc,start_city, end_city, algorithm))
button.grid(column=4,row=1)

window.mainloop()

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------