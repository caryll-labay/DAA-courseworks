import random

random.seed(1234)

def estimate_pi(num_points):
    #number of random points to generate
    NUM_POINTS = num_points
    inside_circle = 0

    for _ in range(NUM_POINTS):
        # Generate random x and y coordinates between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        #distance of the point from the origin
        distance = x**2 + y**2

        # Check if the point falls inside the circle
        if distance <= 1:
            # If the point is inside the circle, increment the counter
            inside_circle += 1

    #Estimate pi as the ratio of the number of points inside the circle to the total number of points generated
    pi = 4 * inside_circle / NUM_POINTS

    # Return the estimated value of pi
    return pi


print("Estimated value of pi with 1000 points:", estimate_pi(1000))
