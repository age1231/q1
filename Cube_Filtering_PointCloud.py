# ============================================
# Title: 3D Point Cloud Filtering within Cube Boundaries
# Description: This program generates a 3D point cloud and filters points that
# fall within a randomly generated cube using numpy and pandas.
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# i) Generate random min and max boundaries for x, y, z axes
def generateBoundaries():
    max_bound = np.random.randint(16, 20, 3)  # [16, 19]
    min_bound = np.random.randint(2, 6, 3)    # [2, 5]
    return max_bound, min_bound

# ii) Generate a random 3D point cloud (15 points)
def generatePointCloud():
    return np.random.randint(0, 21, size=(15, 3))  # 15x3 array, values in [0,20]

# iv) Convert numpy point cloud to pandas DataFrame
def convertPCToDataFrame(pc_array):
    df = pd.DataFrame({
        "axis_1": pc_array[:, 0],
        "axis_2": pc_array[:, 1],
        "axis_3": pc_array[:, 2]
    })
    return df

# v) Find indices of points inside the cube defined by min and max boundaries
def findIndicesOfInnerPoints(df, min_bound, max_bound):
    condition = (
        (df["axis_1"] >= min_bound[0]) & (df["axis_1"] <= max_bound[0]) &
        (df["axis_2"] >= min_bound[1]) & (df["axis_2"] <= max_bound[1]) &
        (df["axis_3"] >= min_bound[2]) & (df["axis_3"] <= max_bound[2])
    )
    return df[condition].index.tolist()

# vi) Separate inner and outer points and save to CSV
def findPoints(pc_array, inner_indices):
    inner = pc_array[inner_indices]
    outer = np.delete(pc_array, inner_indices, axis=0)

    np.savetxt("inner_points_name_surname.csv", inner, delimiter="*", fmt="%d")
    np.savetxt("outer_points_name_surname.csv", outer, delimiter="*", fmt="%d")

# vii) Plot inner and outer points using matplotlib
def plotFilteredPoints(pc_array, inner_file, outer_file):
    inner = np.loadtxt(inner_file, delimiter="*")
    outer = np.loadtxt(outer_file, delimiter="*")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot
    ax.scatter(inner[:,0], inner[:,1], inner[:,2], c='r', label='Inner Points')
    ax.scatter(outer[:,0], outer[:,1], outer[:,2], c='g', label='Outer Points')

    # Print indices over original point cloud
    for i, point in enumerate(pc_array):
        ax.text(point[0], point[1], point[2], str(i), size=8)

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.legend()
    plt.show()

# viii) Main function to run the process
def main():
    np.random.seed(50)  # To get consistent results

    # Step-by-step calls
    max_bound, min_bound = generateBoundaries()
    print("Max Boundaries:", max_bound)
    print("Min Boundaries:", min_bound)

    pc_array = generatePointCloud()
    print("Point Cloud:\n", pc_array)

    # iii) Save full point cloud to CSV with * separator
    np.savetxt("point_cloud_name_surname.csv", pc_array, delimiter="*", fmt="%d")

    df = convertPCToDataFrame(pc_array)
    print("DataFrame:\n", df)

    inner_indices = findIndicesOfInnerPoints(df, min_bound, max_bound)
    print("Inner Indices:", inner_indices)

    findPoints(pc_array, inner_indices)

    plotFilteredPoints(pc_array,
                       "inner_points_name_surname.csv",
                       "outer_points_name_surname.csv")

# Run the main function
main()
