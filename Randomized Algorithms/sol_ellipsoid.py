import random

random.seed(9)

def estimate_ellipsoid_volume(num_points, a, b, c):
    # Define the number of random points to generate
    num_values = num_points
    count = 0

    # Generate num_values random points and check if each point falls inside the ellipsoid
    for i in range(num_values):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        z = random.uniform(-c, c)
        
        # Check if the point falls inside the ellipsoid
        if x**2/a**2 + y**2/b**2 + z**2/c**2 <= 1:
            # If the point is inside the ellipsoid, increment the counter
            count += 1

    # Estimate the volume of the ellipsoid based on the proportion of points inside the ellipsoid
    volume = 8 * a * b * c * count / num_values

    # Return the estimated volume of the ellipsoid
    return volume


print("Estimated volume of the ellipsoid:", estimate_ellipsoid_volume(1000, 2, 3, 4))
