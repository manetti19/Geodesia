from pyproj import Transformer

# Criar transformador de WGS84 (lat/lon) para UTM zona 23S
# EPSG:32723 → WGS84 / UTM zone 23S
transformer = Transformer.from_crs("EPSG:4326", "EPSG:32723", always_xy=True)

# Lista de coordenadas (lon, lat) - exemplo
coords = [
    (-43.1665207 ,-22.9560316), 
    (-43.1665495 ,-22.9560372), 
    (-43.1665013 ,-22.9560421), 
    (-43.1664838 ,-22.9560421), 
    (-43.1665210 ,-22.9560424), 
    (-43.1665227 ,-22.9560841), 
    (-43.1665123 ,-22.9560798), 
    (-43.1665120 ,-22.9560903), 
    (-43.1665261 ,-22.9560714), 
    (-43.1665174 ,-22.956047), 
    (-43.1665224 ,-22.9560591)
]

# Converter e imprimir
print(f"{'Lon':>10} {'Lat':>10} {'Easting':>12} {'Northing':>12}")
for lon, lat in coords:
    easting, northing = transformer.transform(lon, lat)
    print(f"{lon:10.6f} {lat:10.6f} {easting:12.3f} {northing:12.3f}")
