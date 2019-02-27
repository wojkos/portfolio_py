import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 
html = """
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
 
def pointer_color(elevation):
  if elevation < 1000:
    return "green"
  elif 100 <= elevation < 3000:
    return "orange"
  else:
    return "red"


map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln],radius=6, popup=folium.Popup(iframe),fill_color = pointer_color(el), color='grey', fill_opacity=0.6))
 
map.add_child(fg)

map.save("map.html")