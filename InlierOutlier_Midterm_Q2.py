# ===============================================
# SORU 2 - KNN ile Inlier / Outlier Tespiti
# ===============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# i) Parametreleri al
def getParameters():
    NOP = int(input("Enter number of points: "))
    thresh = float(input("Enter distance threshold: "))
    K = int(input("Enter number of neighbors (K): "))
    return NOP, thresh, K

# ii) Nokta bulutu üret
def generatePointCloud(NOP):
    return np.random.randint(100, 201, size=(NOP, 3))

# iii) K en yakın komşuyu bul
def findKNeigbors(pc_array, K):
    neighbors = {}
    for i in range(len(pc_array)):
        distances = np.sqrt(np.sum((pc_array - pc_array[i])**2, axis=1))
        sorted_indices = np.argsort(distances)
        k_nearest = distances[sorted_indices[1:K+1]]  # kendisi hariç
        neighbors[i] = k_nearest
    return neighbors

# iv) Inlier ve outlier noktaları ayır
def filterPC(pc_array, neighbors_dict, thresh):
    df = pd.DataFrame.from_dict(neighbors_dict, orient='index')
    means = df.mean(axis=1)
    mask = means < thresh

    inlier = pc_array[mask.values]
    outlier = pc_array[~mask.values]
    return inlier, outlier

# v) CSV dosyalarına yaz ( - ile ayır )
def writeToFiles(inlier, outlier):
    np.savetxt("point_cloud_inlier_name_surname.csv", inlier, delimiter='-', fmt='%d')
    np.savetxt("point_cloud_outlier_name_surname.csv", outlier, delimiter='-', fmt='%d')

# vi) 3D görselleştir
def plotFilteredPoints(inlier_file, outlier_file):
    inlier = pd.read_csv(inlier_file, delimiter='-', header=None)
    outlier = pd.read_csv(outlier_file, delimiter='-', header=None)

    inlier.columns = ["i_x", "i_y", "i_z"]
    outlier.columns = ["o_x", "o_y", "o_z"]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(inlier["i_x"], inlier["i_y"], inlier["i_z"], c='r', label='Inlier')
    ax.scatter(outlier["o_x"], outlier["o_y"], outlier["o_z"], c='g', label='Outlier')

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.legend()
    plt.show()

# vii) main fonksiyonu
def main():
    np.random.seed(42)
    NOP, thresh, K = getParameters()
    pc_array = generatePointCloud(NOP)
    neighbors_dict = findKNeigbors(pc_array, K)
    inlier, outlier = filterPC(pc_array, neighbors_dict, thresh)
    writeToFiles(inlier, outlier)
    plotFilteredPoints("point_cloud_inlier_name_surname.csv",
                       "point_cloud_outlier_name_surname.csv")

main()
