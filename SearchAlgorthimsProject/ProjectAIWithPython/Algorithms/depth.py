#-------------------------------------------------------------
#------------- Depth First Search Function -------------------
#-------------------------------------------------------------

def depthFirstSearch(start, end):

    # Using a Python dictionary to act as an adjacency list

    """ adj_list={
            'Tala':         ['ShebinElkom','BerketAlseb3'],
            'Alshohda':     ['Minouf'],
            'BerketAlseb3': ['Quesna', 'Tala'],
            'Quesna':       ['BerketAlseb3','ShebinElkom'],
            'ShebinElkom':  ['Tala','Minouf','Quesna'],
            'Minouf':       ['SirsAllyan','ShebinElkom','Alshohda'],
            'SirsAllyan':   ['Minouf','Elbagoor'],
            'Elbagoor':     ['SirsAllyan'],
            'Ashmoon':      ['Elsadat'],
            'Elsadat':      ['Minouf', 'Ashmoon']
            } """

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

path = depthFirstSearch('ShibinElQanatir', 'Tala')
print(path)