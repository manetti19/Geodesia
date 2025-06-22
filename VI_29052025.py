from geographiclib.geodesic import Geodesic

# Coordenadas (φ, λ) convertidas para decimais
wellington = {
    "lat": -(41 + 12/60 + 24.83/3600),  # S → negativo
    "lon":  174 + 43/60 + 54.15/3600    # E → positivo
}

chatham = {
    "lat": -(43 + 47/60 + 35.17/3600),  # S → negativo
    "lon": -(176 + 37/60 + 36.72/3600)  # W → negativo
}

# WGS84
geod = Geodesic.WGS84

# Cálculo geodésico direto
result = geod.Inverse(wellington["lat"], wellington["lon"],
                      chatham["lat"], chatham["lon"])

# Resultados
distancia_m = result['s12']
azimute_graus = result['azi1'] % 360
contraazimute_graus = result['azi2'] % 360
contraazimute_graus_f = contraazimute_graus + 180

# Impressão
print("a)")
print(f"Distância: {distancia_m:.2f} m")
print(f"Azimute: {azimute_graus:.4f}°")
print(f"Contra-azimute: {contraazimute_graus_f:.4f}°")



print("b) Considera que a Terra não é uma esfera perfeita, mas sim um elipsoide oblato, o que permite maior precisão nos cálculos de distâncias e azimutes. Mas a altitude sobre o nível do mar foi desprezada, assumindo que ambos os pontos estão sobre o elipsoide.")


print("c)")

# Coordenadas de partida (Ilha Chatham) em graus decimais
lat_chatham = -(43 + 47/60 + 35.17/3600)
lon_chatham = -(176 + 37/60 + 36.72/3600)

# Azimute em graus decimais
azimute = 15 + 30/60 + 18.27/3600  # já em graus

# Velocidade e tempo
velocidade_ms = 30 * 1852 / 3600  # converter nós para m/s
tempo_horas = 50.64
distancia_m = 30 * 1852 * tempo_horas  # distância total em metros

# Elipsoide WGS84
geod = Geodesic.WGS84

# Cálculo do ponto final
destino = geod.Direct(lat_chatham, lon_chatham, azimute, distancia_m)

# Resultados
lat_final = destino['lat2']
lon_final = destino['lon2']

print(f"Coordenadas da Ilha Niue (WGS84):")
print(f"Latitude: {lat_final:.6f}°")
print(f"Longitude: {lon_final:.6f}°")



print("d)")

# Coordenadas Ilha Chatham
lat_chatham = -(43 + 47/60 + 35.17/3600)
lon_chatham = -(176 + 37/60 + 36.72/3600)

# Coordenadas Ilha Niue (obtidas anteriormente na questão c)
lat_niue = -18.935007
lon_niue = -169.866038

# Trópico de Capricórnio (latitude)
lat_tropico = -23.43722

# Linha geodésica
geod = Geodesic.WGS84
line = geod.InverseLine(lat_chatham, lon_chatham, lat_niue, lon_niue)

# Resolução: percorrer a linha geodésica até cruzar o trópico
n = 1000
ds = line.s13 / n

for i in range(n + 1):
    s = i * ds
    pos = line.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)
    lat = pos['lat2']
    if lat >= lat_tropico:
        print(f"Latitude no cruzamento: {lat:.6f}°")
        print(f"Longitude no cruzamento: {pos['lon2']:.6f}°")
        print(f"Azimute geodésico no Trópico de Capricórnio: {pos['azi2']:.6f}°")
        break


print("e)")
print("Para determinar o azimute geodésico da embarcação ao cruzar o Trópico de Capricórnio, foi empregada a solução do problema geodésico inverso elipsoidal, utilizando o elipsoide WGS-84. Inicialmente, determinou-se a linha geodésica entre a Ilha Chatham e a Ilha Niue, com base em suas coordenadas geográficas. Em seguida, foram amostrados pontos intermediários dessa linha até identificar o instante em que a latitude atingiu −23° 26′ (Trópico de Capricórnio). O azimute no ponto correspondente foi extraído diretamente da trajetória geodésica, refletindo a variação do rumo ao longo da superfície elipsoidal.")


print("f)")

# Dados do ponto inicial (Chatham)
lat_chatham = -(43 + 47/60 + 35.17/3600)
lon_chatham = -(176 + 37/60 + 36.72/3600)

# Azimute de navegação
azimute = 15 + 30/60 + 18.27/3600  # graus

# Tempo até o acidente e velocidade
tempo_horas = 44.5
velocidade_m_h = 30 * 1852  # em metros por hora
distancia_m = velocidade_m_h * tempo_horas

# Cálculo com elipsoide WGS-84
geod = Geodesic.WGS84
ponto_acidente = geod.Direct(lat_chatham, lon_chatham, azimute, distancia_m)

# Resultado
lat_final = ponto_acidente['lat2']
lon_final = ponto_acidente['lon2']

print(f"Coordenadas do local do acidente (WGS-84):")
print(f"Latitude: {lat_final:.6f}°")
print(f"Longitude: {lon_final:.6f}°")


print("g)")


from math import radians, sin, cos, sqrt

def geodetic_to_ecef(phi_deg, lambda_deg, h, a, f):
    phi = radians(phi_deg)
    lam = radians(lambda_deg)
    e2 = 2*f - f**2
    N = a / sqrt(1 - e2 * sin(phi)**2)
    
    X = (N + h) * cos(phi) * cos(lam)
    Y = (N + h) * cos(phi) * sin(lam)
    Z = ((1 - e2) * N + h) * sin(phi)
    
    return X, Y, Z

# Coordenadas em graus decimais
phi = -(19 + 6/60 + 11.906/3600)
lam = 169 + 41/60 + 33.815/3600
h = -106.87

# Elipsoide WGS-84
a_wgs = 6378137.0
f_wgs = 1/298.257223563

# Elipsoide AGD84 (Australian National Spheroid)
a_agd = 6378160.0
f_agd = 1/298.25

# Conversão
X_wgs, Y_wgs, Z_wgs = geodetic_to_ecef(phi, lam, h, a_wgs, f_wgs)
X_agd, Y_agd, Z_agd = geodetic_to_ecef(phi, lam, h, a_agd, f_agd)

# Diferenças (parâmetros de conversão)
dX = X_wgs - X_agd
dY = Y_wgs - Y_agd
dZ = Z_wgs - Z_agd

print("Parâmetros de conversão (WGS-84 → AGD84):")
print(f"ΔX = {dX:.3f} m")
print(f"ΔY = {dY:.3f} m")
print(f"ΔZ = {dZ:.3f} m")


print("h)")

from math import radians, sin, cos, sqrt

def geodetic_to_ecef(phi_deg, lambda_deg, h, a, f):
    phi = radians(phi_deg)
    lam = radians(lambda_deg)
    e2 = 2*f - f**2
    N = a / sqrt(1 - e2 * sin(phi)**2)
    
    X = (N + h) * cos(phi) * cos(lam)
    Y = (N + h) * cos(phi) * sin(lam)
    Z = ((1 - e2) * N + h) * sin(phi)
    return X, Y, Z

def ecef_to_geodetic(X, Y, Z, a, f):
    # Transformação reversa de ECEF para geodésico (iteração simples de Bowring)
    e2 = 2*f - f**2
    lon = atan2(Y, X)
    p = sqrt(X**2 + Y**2)
    phi = atan2(Z, p*(1 - e2))  # primeira estimativa
    for _ in range(5):
        N = a / sqrt(1 - e2 * sin(phi)**2)
        h = p / cos(phi) - N
        phi = atan2(Z, p*(1 - e2 * N / (N + h)))
    return degrees(phi), degrees(lon), h

# Coordenadas AGD84
phi_agd = -22.522900
lam_agd = 169.610850
h_agd = -95.59

# Elipsoides
a_agd = 6378160.0
f_agd = 1 / 298.25
a_wgs = 6378137.0
f_wgs = 1 / 298.257223563

# Conversão AGD84 → ECEF
X_agd, Y_agd, Z_agd = geodetic_to_ecef(phi_agd, lam_agd, h_agd, a_agd, f_agd)

# Parâmetros de transformação (aproximados)
dX = -117.276
dY = -51.724
dZ = +137.892

# Conversão ECEF → WGS84 (aplicando os deltas)
X_wgs = X_agd + dX
Y_wgs = Y_agd + dY
Z_wgs = Z_agd + dZ

# Reverter para geodésico WGS84
from math import atan2, degrees
lat_wgs, lon_wgs, h_wgs = ecef_to_geodetic(X_wgs, Y_wgs, Z_wgs, a_wgs, f_wgs)

print("Coordenadas dos náufragos em WGS-84:")
print(f"Latitude: {lat_wgs:.6f}°")
print(f"Longitude: {lon_wgs:.6f}°")
print(f"Altura elipsoidal: {h_wgs:.2f} m")


print("i)")

from geographiclib.geodesic import Geodesic

# Coordenadas do acidente (obtidas na questão f)
lat_acidente = -23.433267  # exemplo
lon_acidente = -172.549280

# Coordenadas atuais dos náufragos (obtidas acima)
geod = Geodesic.WGS84
res = geod.Inverse(lat_acidente, lon_acidente, lat_wgs, lon_wgs)

distancia_m = res['s12']
azimute_corrente = res['azi1'] % 360
velocidade_m_s = distancia_m / (19 * 3600)

print(f"Distância percorrida: {distancia_m:.2f} m")
print(f"Direção da corrente: {azimute_corrente:.2f}°")
print(f"Velocidade média da corrente: {velocidade_m_s:.3f} m/s")
