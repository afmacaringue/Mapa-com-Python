import folium

center = [-25.966444, 32.583055]
ponto = [-25.966444, 32.583055]

map = folium.Map(location=center, zoom_start=16)

folium.Marker(ponto, popup="Macaringue").add_to(map)

map.save('index.html')