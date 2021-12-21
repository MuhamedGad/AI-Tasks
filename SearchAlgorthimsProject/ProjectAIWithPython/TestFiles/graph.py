import tkinter as tk
from tkinter import ttk
from functools import partial
import folium
import os
import webbrowser
import openrouteservice
from queue import Queue
from PIL import ImageTk, Image

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
    "SirsAllyan":   [30.439229091007064, 30.96737901607289],
    #el gharbia
    "KafrElZayat":[30.828935887979828, 30.81468363315086],
    "Basioun":[30.941234859668185, 30.819787152459256],
    "Tanta":[30.78236661466976, 31.003931835360497],
    "Qutur":[30.97124133198592, 30.952896608684792],
    "ElMahallaElKubra":[30.969841036674914, 31.166019730570685],
    "AsSantah":[30.749281457375343, 31.129532111290036],
    "Samannoud":[30.96202482138702, 31.241725792395766],
    "Zefta":[30.714483753839744, 31.240197668420624],
    #el kalubia
    "Banha":[30.46954041758182, 31.18372798445176],
    "Qalyub":[30.180143566835696, 31.20638419614639],
    "qaha":[30.284328474135044, 31.208016001570982],
    "AlQanatirAlKhayriyyah":[30.194609758641715, 31.13391214967144],
    "ShubraAlKhaymah":[30.124142365522676, 31.260465002556664],
    "Elkhankah":[30.22039965655326, 31.368612270866304],
    "Kafrshokr":[30.552839823187284, 31.255430468410704],
    "ShibinElQanatir":[30.31214792794175, 31.32292278281032],
    "Toukh":[30.353756127836252, 31.2014138527108],
    "el khosous":[30.16001719965362, 31.312695529441243]
    }

client = openrouteservice.Client(key='5b3ce3597851110001cf62489f97821fab9b46a18afb841b2c9226af')

    # create map object
m = folium.Map(location=[30.597246, 30.987632], zoom_start=9)

for item in Coordinates:
    folium.Marker(location=Coordinates[item], popup=item, tooltip=item).add_to(m),


# for i in range(len(path)-1):
#     coord = [Coordinates[path[i]][::-1], Coordinates[path[i+1]][::-1]]
#     route = client.directions(coordinates=coord,profile='driving-car',format='geojson')
#     folium.GeoJson(route, name='route').add_to(m)


folium.LayerControl().add_to(m)
m.save('indexV3.html')

#open file of html
filename = 'file:///'+os.getcwd()+'/' + 'indexV3.html'
webbrowser.open_new_tab(filename)