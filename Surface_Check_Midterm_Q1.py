# ===============================================
# SORU 1 - Aynı yüzeyde olup olmadıklarını kontrol et
# ===============================================

import random
import math

# ii) Koordinatları belirleme
def initalizeCoordinates(p1, p2, p3):
    for p in (p1, p2, p3):
        p.append(random.randint(7, 15))
        p.append(random.randint(7, 15))
        p.append(random.randint(7, 15))

# iii) Normal vektör hesaplama
def calculateNormals(p1, p2, p3):
    nx = (p2[1] - p1[1]) * (p3[2] - p1[2]) - (p2[2] - p1[2]) * (p3[1] - p1[1])
    ny = (p2[2] - p1[2]) * (p3[0] - p1[0]) - (p2[0] - p1[0]) * (p3[2] - p1[2])
    nz = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return [nx, ny, nz]

# v) Açılar hesaplama
def calculateAngles(n):
    norm = math.sqrt(n[0]**2 + n[1]**2 + n[2]**2)
    angleX = math.degrees(math.acos(n[0] / norm))
    angleY = math.degrees(math.acos(n[1] / norm))
    angleZ = math.degrees(math.acos(n[2] / norm))
    return [angleX, angleY, angleZ]

# vii) Yüzey kontrolü
def isSameSurface(angles, thresh):
    return (abs(angles[0] - angles[1]) < thresh and
            abs(angles[0] - angles[2]) < thresh and
            abs(angles[1] - angles[2]) < thresh)

# i, iv, vi, viii) main fonksiyonu
def main():
    random.seed(10)
    p1, p2, p3 = [], [], []
    initalizeCoordinates(p1, p2, p3)

    print("P1:", p1)
    print("P2:", p2)
    print("P3:", p3)

    n = calculateNormals(p1, p2, p3)
    print("Normal Vector:", n)

    angles = calculateAngles(n)
    print("Angles:", angles)

    result = isSameSurface(angles, 5)
    print("Are the points on the same surface?", result)

main()
