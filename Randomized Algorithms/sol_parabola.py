import random

random.seed(5678)

def estimate_area_bounded_by_p1_and_p2_using_proportion(num_points, p1, p2):
    under_parabola = 0
    # Generate num_points random points between p1 and p2
    for _ in range(num_points):
        x = random.uniform(p1[0], p2[0])
    
        # Generate a random y-coordinate between 0 and the maximum y-coordinate on the curve between p1 and p2
        max_y = max(p1[1], p2[1])
        y = random.uniform(0, max_y)
    
        if y <= x**2:
            under_parabola += 1
            
    total_area = (p2[0] - p1[0]) * max(p1[1], p2[1])
    area_under_parabola = total_area * under_parabola / num_points/ 2
    
    # Return the estimated area under the curve
    return area_under_parabola
    
p1 = (0, 0)
p2 = (2, 4)
print("Estimated area bounded by p1 and p2:", estimate_area_bounded_by_p1_and_p2_using_proportion(1000, p1, p2))
