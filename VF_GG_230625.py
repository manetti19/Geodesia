print("a)")

from geographiclib.geodesic import Geodesic
import math
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

# Parâmetros do elipsoide ELF-3019
a = 6376159.218  # semi-eixo maior (m)
f = 1 / 299.674  # achatamento
e2 = 2*f - f**2  # primeira excentricidade ao quadrado

# Conversão de DMS para decimal
def dms_to_decimal(deg, min, sec, direction):
    sign = -1 if direction in ['S', 'W'] else 1
    return sign * (deg + min/60 + sec/3600)

# Coordenadas iniciais - Colinas do Vento
lat0 = dms_to_decimal(38, 47, 25.3, 'N')
lon0 = dms_to_decimal(27, 18, 27.7, 'W')

# Funções de curvatura
def M(phi):  # raio de curvatura meridiano
    return a * (1 - e2) / (1 - e2 * math.sin(phi)**2)**1.5

def N(phi):  # raio de curvatura na normal
    return a / (1 - e2 * math.sin(phi)**2)**0.5

# Sistema de equações diferenciais da geodésica
def geodesic_odes(s, y):
    phi, lamb, alpha = y
    M_phi = M(phi)
    N_phi = N(phi)
    dphi_ds = math.cos(alpha) / M_phi
    dlamb_ds = math.sin(alpha) / (N_phi * math.cos(phi))
    dalpha_ds = -math.tan(phi) * math.sin(alpha) / N_phi
    return [dphi_ds, dlamb_ds, dalpha_ds]

# Função para resolver o problema direto com RK4
def solve_geodesic(phi0_deg, lamb0_deg, alpha0_deg, S):
    phi0 = math.radians(phi0_deg)
    lamb0 = math.radians(lamb0_deg)
    alpha0 = math.radians(alpha0_deg)
    s_span = (0, S)
    y0 = [phi0, lamb0, alpha0]
    sol = solve_ivp(geodesic_odes, s_span, y0, method='RK45', t_eval=[S])
    phi_f, lamb_f, alpha_f = sol.y[:, -1]
    return math.degrees(phi_f), math.degrees(lamb_f), math.degrees(alpha_f)

# Trechos da jornada
trajetos = [
    {"de": "Colinas do Vento", "para": "Bri", "S": 1155027.356, "azimute": dms_to_decimal(122, 18, 55.6142, 'N')},
    {"de": "Bri", "para": "Trollshaws", "S": 485395.180, "azimute": dms_to_decimal(177, 53, 56.4678, 'N')},
    {"de": "Trollshaws", "para": "Valfenda", "S": 927509.232, "azimute": dms_to_decimal(184, 49, 46.8629, 'N')},
]

# Cálculo dos pontos
pontos = [{"Local": "Colinas do Vento", "Latitude": lat0, "Longitude": lon0}]
phi, lamb = lat0, lon0
for trajeto in trajetos:
    phi, lamb, _ = solve_geodesic(phi, lamb, trajeto["azimute"], trajeto["S"])
    pontos.append({"Local": trajeto["para"], "Latitude": phi, "Longitude": lamb})

# Resultado final como DataFrame
df = pd.DataFrame(pontos)
print(df)



print("b)")

import math
import pandas as pd

# Função para converter DMS para decimal
def dms_to_decimal(deg, min, sec, direction):
    sign = -1 if direction in ['S', 'W'] else 1
    return sign * (deg + min / 60 + sec / 3600)

# Coordenadas dos pontos
coords = {
    "Colinas do Vento": (dms_to_decimal(38, 47, 25.3, 'N'), dms_to_decimal(27, 18, 27.7, 'W')),
    "Bri":              (33.757365, -16.072452),
    "Trollshaws":       (29.382774, -15.880378),
    "Valfenda":         (21.042035, -16.684793)
}

# Azimutes geodésicos dos trechos
azimutes_geodesicos = {
    "Colinas do Vento → Bri": dms_to_decimal(122, 18, 55.6142, 'N'),
    "Bri → Trollshaws": dms_to_decimal(177, 53, 56.4678, 'N'),
    "Trollshaws → Valfenda": dms_to_decimal(184, 49, 46.8629, 'N')
}

# Trechos a serem avaliados
trechos = [
    ("Colinas do Vento", "Bri"),
    ("Bri", "Trollshaws"),
    ("Trollshaws", "Valfenda")
]

# Cálculo dos resultados
resultados = []
for origem, destino in trechos:
    lat1, lon1 = coords[origem]
    lat2, lon2 = coords[destino]
    trecho_nome = f"{origem} → {destino}"
    delta_lambda = lon2 - lon1
    phi_m = (lat1 + lat2) / 2

    # Converter para radianos
    delta_lambda_rad = math.radians(delta_lambda)
    phi_m_rad = math.radians(phi_m)
    gamma_rad = delta_lambda_rad * math.sin(phi_m_rad)
    gamma_deg = math.degrees(gamma_rad)

    # Azimute geográfico
    az_geod = azimutes_geodesicos[trecho_nome]
    if delta_lambda > 0:
        az_geo = az_geod - gamma_deg
    else:
        az_geo = az_geod + gamma_deg

    resultados.append({
        "Trecho": trecho_nome,
        "Azimute geodésico (°)": az_geod,
        "γ (°)": gamma_deg,
        "Azimute geográfico (°)": az_geo
    })

# Apresentar em DataFrame
df = pd.DataFrame(resultados)
print(df.to_string(index=False))


print("c)")

from geographiclib.geodesic import Geodesic
import math

# --- Parâmetros do elipsoide ELF-3019 ---
a = 6376159.218
f = 1 / 299.674
geod = Geodesic(a, f)

# Conversão de coordenadas DMS para decimal
def dms(grau, minuto, segundo, direcao):
    sinal = -1 if direcao in ['S', 'W'] else 1
    return sinal * (grau + minuto / 60 + segundo / 3600)

# --- Coordenadas dos pontos ---
lat_montanhas = dms(46, 50, 0, 'N')
lon_montanhas = dms(32, 10, 0, 'W')

lat_bri = dms(35, 40, 0, 'N')
lon_bri = dms(25, 15, 0, 'W')

lat_valfenda = dms(21, 4, 30.9, 'N')
lon_valfenda = dms(16, 54, 53.6, 'W')

# --- Distância e azimute Montanhas Cinzentas → Valfenda (problema inverso) ---
linha_mont_val = geod.Inverse(lat_montanhas, lon_montanhas, lat_valfenda, lon_valfenda)
dist_mont_val = linha_mont_val["s12"]
azim_mont_val = linha_mont_val["azi1"]

# --- Distância e azimute Bri → Valfenda (problema inverso) ---
linha_bri_val = geod.Inverse(lat_bri, lon_bri, lat_valfenda, lon_valfenda)
dist_bri_val = linha_bri_val["s12"]
azim_bri_val = linha_bri_val["azi1"]

# --- Velocidades (em m/s) ---
v_dragon = 250 * 1000 / 3600      # 250 km/h
v_aguias = 350 * 1000 / 3600      # 350 km/h
atraso_aguias = 15 * 60           # 15 minutos de atraso em segundos

# --- Tempo total até interceptação (em segundos) ---
def tempo_interceptacao(d1, v1, d2, v2, atraso):
    return (d2 + v2 * atraso) / (v1 + v2)

tempo_total_s = tempo_interceptacao(dist_mont_val, v_dragon, dist_bri_val, v_aguias, atraso_aguias)

# --- Distância percorrida pelo dragão até a interceptação ---
s_intercept = v_dragon * tempo_total_s

# --- Ponto de interceptação ao longo da linha Montanhas → Valfenda ---
linha_dragon = geod.Line(lat_montanhas, lon_montanhas, azim_mont_val)
ponto_intercept = linha_dragon.Position(s_intercept)

# --- Impressão dos resultados ---
print(f"i) Distância Montanhas–Valfenda: {dist_mont_val / 1000:.2f} km")
print(f"ii) Distância Bri–Valfenda: {dist_bri_val / 1000:.2f} km")
print(f"iii) Ponto de interceptação:")
print(f"    Latitude: {ponto_intercept['lat2']:.6f}°")
print(f"    Longitude: {ponto_intercept['lon2']:.6f}°")
print(f"iv) Tempo até a interceptação: {tempo_total_s / 60:.2f} minutos")
print(f"Azimute inicial (dragão): {azim_mont_val:.4f}°")
print(f"Azimute inicial (águias): {azim_bri_val:.4f}°")


print("d)")

from geographiclib.geodesic import Geodesic
from geographiclib.polygonarea import PolygonArea

# --- Definição do elipsoide ELF-3019 ---
a = 6376159.218
f = 1 / 299.674
geod = Geodesic(a, f)

# --- Coordenadas dos vértices do polígono (latitude, longitude) ---
pontos = [
    (20, -25),
    (30, -25),
    (30, -15),
    (25, -15),
    (25, -20),
    (20, -20)
]

# --- Inicializa o objeto PolygonArea para cálculo geodésico ---
polygon = PolygonArea(geod, False)

# Adiciona os pontos ao polígono
for lat, lon in pontos:
    polygon.AddPoint(lat, lon)

# Fecha o polígono e calcula área e perímetro
num, perimetro_m, area_m2 = polygon.Compute()

# --- Conversão para unidades usuais ---
area_km2 = -1*area_m2 / 1e6
perimetro_km = perimetro_m / 1e3

# --- Exibe os resultados ---
print(f"Área do polígono: {area_km2:.2f} km²")
print(f"Perímetro do polígono: {perimetro_km:.2f} km")


print("e)")

from geographiclib.geodesic import Geodesic

# Elipsoide ELF-3019
a = 6376159.218
f = 1 / 299.674
geod = Geodesic(a, f)

# Trópico de Câncer (23°27′N)
lat_tropico = 23 + 27/60

# Ponto de partida: Bri
lat_bri = 35 + 40/60
lon_bri = -20 -15/60
azimute_aguia = 4.0

# Linha geodésica das Águias
linha = geod.Line(lat_bri, lon_bri, azimute_aguia)

# Amostragem ao longo da linha (até 40.000 km)
n = 100_000
s_total = 40_000_000
ds = s_total / n

intersec_lat = intersec_lon = None
lat_anterior = lat_bri

for i in range(1, n + 1):
    pos = linha.Position(i * ds)
    lat_atual = pos['lat2']

    if lat_atual <= lat_tropico <= lat_anterior:
        intersec_lat = pos['lat2']
        intersec_lon = pos['lon2']
        break
    lat_anterior = lat_atual

# Coordenadas de Valfenda
lat_valfenda = 21 + 4/60 + 30.9/3600
lon_valfenda = -(16 + 54/60 + 53.6/3600)

# Problema inverso
if intersec_lat is not None:
    inverso = geod.Inverse(lat_valfenda, lon_valfenda, intersec_lat, intersec_lon)
    azimute_saruman = inverso['azi1']
    print(f"Azimute de Saruman: {azimute_saruman:.2f}°")
    print(f"Ponto de encontro: ({intersec_lat:.6f}°, {intersec_lon:.6f}°)")
else:
    print("⚠️ Não foi possível encontrar a interseção.")
