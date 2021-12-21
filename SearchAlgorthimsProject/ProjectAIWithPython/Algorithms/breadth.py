from queue import Queue

#-------------------------------------------------------------
#-------------- Breadth First Search Function ----------------
#-------------------------------------------------------------

def breadthFirstSearch(start, end):

#   adj_list={
#           'Tala':         ['ShebinElkom','BerketAlseb3'],
#           'Alshohda':     ['Minouf'],
#           'BerketAlseb3': ['Quesna', 'Tala'],
#           'Quesna':       ['BerketAlseb3','ShebinElkom'],
#           'ShebinElkom':  ['Tala','Minouf','Quesna'],
#           'Minouf':       ['SirsAllyan','ShebinElkom','Alshohda'],
#           'SirsAllyan':   ['Minouf','Elbagoor'],
#           'Elbagoor':     ['SirsAllyan'],
#           'Ashmoon':      ['Elsadat'],
#           'Elsadat':      ['Minouf', 'Ashmoon']
#           }

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

path = breadthFirstSearch('Elkhankah', 'Tala')
print(path)