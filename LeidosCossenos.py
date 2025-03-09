import math

def degrees_to_radians(deg, min, sec):
    return math.radians(deg + min / 60 + sec / 3600)

def radians_to_dms(rad):
    degrees_total = math.degrees(rad)
    deg = int(degrees_total)
    minutes_total = (degrees_total - deg) * 60
    min = int(minutes_total)
    sec = (minutes_total - min) * 60
    return deg, min, sec

def solve_spherical_triangle(A, B, C):
    # Aplicando a Lei dos Cossenos para encontrar os lados
    a = math.acos((math.cos(A) + math.cos(B) * math.cos(C)) / (math.sin(B) * math.sin(C)))
    b = math.acos((math.cos(B) + math.cos(A) * math.cos(C)) / (math.sin(A) * math.sin(C)))
    c = math.acos((math.cos(C) + math.cos(A) * math.cos(B)) / (math.sin(A) * math.sin(B)))
    
    return a, b, c

# def solve_spherical_triangle_dois(a, b, c):
    # Aplicando a Lei dos Cossenos para encontrar os lados
    A = math.acos((math.cos(a) - math.cos(b) * math.cos(c)) / (math.sin(b) * math.sin(c)))
    B = math.acos((math.cos(b) - math.cos(a) * math.cos(c)) / (math.sin(a) * math.sin(c)))
    C = math.acos((math.cos(c) - math.cos(a) * math.cos(b)) / (math.sin(a) * math.sin(b)))
    
    return A, B, C

def main():
    # Convertendo ângulos para radianos
    A = degrees_to_radians(117, 22, 48)
    B = degrees_to_radians(72, 38, 36)
    C = degrees_to_radians(58, 21, 12)
    
    a, b, c = solve_spherical_triangle(A, B, C)

    # a = degrees_to_radians( , , )
    # b = degrees_to_radians( , , )
    # c = degrees_to_radians( , , )
    
    # A, B, C = solve_spherical_triangle_dois(a, b, c)
    
    # Convertendo os resultados para grau, minuto e segundo
    a_deg, a_min, a_sec = radians_to_dms(a)
    b_deg, b_min, b_sec = radians_to_dms(b)
    c_deg, c_min, c_sec = radians_to_dms(c)

    # Convertendo os resultados para grau, minuto e segundo
    # A_deg, A_min, A_sec = radians_to_dms(A)
    # B_deg, B_min, B_sec = radians_to_dms(B)
    # C_deg, C_min, C_sec = radians_to_dms(C)
    
    print("\nResultados:")
    print(f"a: {a_deg}° {a_min}' {a_sec:.2f}\"")
    print(f"b: {b_deg}° {b_min}' {b_sec:.2f}\"")
    print(f"c: {c_deg}° {c_min}' {c_sec:.2f}\"")

    # print("\nResultados:")
    # print(f"A: {A_deg}° {A_min}' {A_sec:.2f}\"")
    # print(f"B: {B_deg}° {B_min}' {B_sec:.2f}\"")
    # print(f"C: {C_deg}° {C_min}' {C_sec:.2f}\"")


if __name__ == "__main__":
    main()
