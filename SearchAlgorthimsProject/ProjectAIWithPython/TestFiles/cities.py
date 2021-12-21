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



Coordinates={
    #el menofia
    'ShebinElkom':          [30.554928799816988, 31.012393143088957],
    'Minouf':               [30.45841991481536, 30.933867041463532],
    'Tala':                 [30.683127111837056, 30.950034191578247],
    'BerketAlseb3':         [30.627495984801378, 31.07244250380298],
    'Elbagoor':             [30.43186671298956, 31.031983255977398],
    'Ashmoon':              [30.300117313578117, 30.97564036423758],
    'Quesna':               [30.56765698894867, 31.149568418149613],
    'Elsadat':              [30.362811748009076, 30.533153025293895],
    'Alshohda':             [30.59768043193886, 30.895758793318098],
    #el gharbia
    'KafrElZayat':          [30.828935887979828, 30.81468363315086],
    'Basioun':              [30.941234859668185, 30.819787152459256],
    'Tanta':                [30.78236661466976, 31.003931835360497],
    'Qutur':                [30.97124133198592, 30.952896608684792],
    'ElMahallaElKubra':     [30.969841036674914, 31.166019730570685],
    'AsSantah':             [30.749281457375343, 31.129532111290036],
    'Samannoud':            [30.96202482138702, 31.241725792395766],
    'Zefta':                [30.714483753839744, 31.240197668420624],
    #el kalubia
    'Banha':                [30.46954041758182, 31.18372798445176],
    'Qalyub':               [30.180143566835696, 31.20638419614639],
    'AlQanatirAlKhayriyyah':[30.194609758641715, 31.13391214967144],
    'ShubraAlKhaymah':      [30.124142365522676, 31.260465002556664],
    'Elkhankah':            [30.22039965655326, 31.368612270866304],
    'Kafrshokr':            [30.552839823187284, 31.255430468410704],
    'ShibinElQanatir':      [30.31214792794175, 31.32292278281032],
    'Toukh':                [30.353756127836252, 31.2014138527108],
}




import math
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

# print(distance(Coordinates["Tala"],Coordinates["Minouf"]))




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

# H = {}
# G = {}

for i in H:
    for j in ourCities:
        H[i][j] = distance(Coordinates[i],Coordinates[j])


# print(G)
# print('-------------------------------------------------------------------------------')
print(H)