print("1.")
from geographiclib.geodesic import Geodesic

# sistema espanhol
a_espanhol = 6378444.0
f_espanhol = 1 / 297.4

# Criação do elipsóide personalizado
geod_espanhol = Geodesic(a_espanhol, f_espanhol)

# Coordenadas geodésicas no Sistema Espanhol
# Cartagena
lat_cartagena = 37 + 36/60 + 57.86/3600
lon_cartagena = -(0 + 58/60 + 39.10/3600)

# Barcelona
lat_barcelona = 41 + 24/60 + 6.43/3600
lon_barcelona = 2 + 12/60 + 51.43/3600

# Resolução do problema inverso geodésico
inv_result = geod_espanhol.Inverse(lat_cartagena, lon_cartagena,
                                   lat_barcelona, lon_barcelona)

# Resultados
distance = inv_result['s12']            # distância em metros
azimuth_direct = inv_result['azi1']     # azimute direto em graus
azimuth_reverse = inv_result['azi2']    # azimute reverso em graus

# Impressão dos resultados
print("a)")
print(f"Distância geodésica: {distance:.3f} m")
print("b)")
print(f"Azimute direto (Cartagena → Barcelona): {azimuth_direct:.3f}°")
print(f"Azimute reverso (Barcelona → Cartagena): {azimuth_reverse:.3f}°")





print("2.")
import numpy as np

# Parâmetros do elipsóide Espanhol
a_espanhol = 6378444.0               # semi-eixo maior em metros
f_espanhol = 1 / 297.4               # achatamento

# Raio médio aproximado da esfera equivalente ao elipsóide
raio_medio = a_espanhol * (1 - f_espanhol / 3)

# Ângulos internos do triângulo (em graus decimais), extraídos do enunciado:
# A: Cartagena, entre Barcelona – Cartagena – Mallorca
# B: Barcelona, entre Mallorca – Barcelona – Cartagena
# C: Mallorca, entre Cartagena – Mallorca – Barcelona
A_deg = 117 + 1/60 + 5.825/3600
B_deg = 41 + 35/60 + 32.603/3600
C_deg = 21 + 26/60 + 15.598/3600

# Excesso esférico em radianos
E = np.deg2rad(A_deg + B_deg + C_deg - 180)

# Área do triângulo geodésico (aproximação esférica)
area_aproximada = E * raio_medio**2

# Resultado
print(f"Área aproximada do triângulo geodésico: {area_aproximada:.2f} m²")





print("3.")
from pyproj import CRS, Transformer

# Coordenadas cartesianas (X, Y, Z) de Argel em WGS-84
X = 5127503.301
Y = 263725.842
Z = 3772323.766

# Define os elipsóides personalizados manualmente (espanhol e africano)
crs_geocentric = CRS.from_proj4("+proj=geocent +datum=WGS84 +units=m +no_defs")

# Elipsóide Espanhol (definido manualmente)
crs_espanhol = CRS.from_proj4("+proj=latlong +a=6378444 +rf=297.4 +no_defs")

# Elipsóide Africano
crs_africano = CRS.from_proj4("+proj=latlong +a=6378245 +rf=297.5 +no_defs")

# Transforma de cartesiano para geodésico no sistema Espanhol
transformer_espanhol = Transformer.from_crs(crs_geocentric, crs_espanhol, always_xy=True)
lon_e, lat_e, h_e = transformer_espanhol.transform(X, Y, Z)

# Transforma de cartesiano para geodésico no sistema Africano
transformer_africano = Transformer.from_crs(crs_geocentric, crs_africano, always_xy=True)
lon_a, lat_a, h_a = transformer_africano.transform(X, Y, Z)

# Diferença de alturas elipsoidais
delta_h = h_e - h_a

# Resultado
print(f"Altura elipsoidal (Espanhol): {h_e:.4f} m")
print(f"Altura elipsoidal (Africano): {h_a:.4f} m")
print(f"Δh (Espanhol - Africano): {delta_h:.4f} m")
