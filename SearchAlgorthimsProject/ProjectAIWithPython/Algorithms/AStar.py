from collections import deque
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


#---------------------------------------------------------------------
#------------------------ A* Search Function -------------------------
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
                                    ('tanta',25.3)
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

path = aStar('ShibinElQanatir', 'AsSantah')
print(path)