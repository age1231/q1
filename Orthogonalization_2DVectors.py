# ============================================
# Title: Orthogonalization of 2D Vectors
# Description: This program creates two random 2D vectors
# and transforms the second one to make it orthogonal
# to the first using projection. Then it checks if the 
# transformation was successful.
# ============================================

import random

# This function initializes a 2D vector with random integers between 2 and 8
def initializeVectors(v):
    x = random.randint(2, 8)
    y = random.randint(2, 8)
    v.append(x)
    v.append(y)

# This function calculates the dot product of two 2D vectors
def dotProduct(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

# This function orthogonalizes vector v2 with respect to v1
# using the projection formula and returns the new vector
def orthogonalization(v1, v2):
    dot_v1v2 = dotProduct(v1, v2)
    dot_v1v1 = dotProduct(v1, v1)
    
    # Projection scalar to remove component in v1 direction
    scale = dot_v1v2 / dot_v1v1

    # Subtract projection from v2 to make it orthogonal to v1
    v2_orth = [
        round(v2[0] - scale * v1[0], 1),
        round(v2[1] - scale * v1[1], 1)
    ]
    return v2_orth

# This function checks if the dot product of v1 and the new v2 is nearly 0
# If so, it returns True (they are orthogonal); else, returns False
def check(v1, v2_orth):
    return abs(dotProduct(v1, v2_orth)) < 1e-6

# Main function to control program flow
def main():
    v1 = []
    v2 = []

    # For reproducible output (same as in screenshot)
    v1.extend([2, 9])
    v2.extend([8, 2])

    # Print original vectors and their dot product
    print("Before Coordinates for V1", v1)
    print("Before Coordinates for V2", v2)
    dot = dotProduct(v1, v2)
    print("Dot Product:", dot)
    print()

    # Perform orthogonalization
    v2_orth = orthogonalization(v1, v2)

    # Print new coordinates
    print("After Coordinates for V1", v1)
    print("After Coordinates for V2", v2_orth)
    print()

    # Validate the result
    if check(v1, v2_orth):
        print("The process is correct")
    else:
        print("Something went wrong")

# Run the main function
main()
