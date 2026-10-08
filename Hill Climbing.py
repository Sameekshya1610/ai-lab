#objective function
def objective_function(x):
    return -(x **2) + 10 #emaple function

#hill climbing function
def hill_climbing(start,step_size,max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        left = current-step_size
        right =  current+step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        # move to better neighbour
        if left_value > current_value:
            current = left
            current_value = left_value 
        elif right_value > current_value:
            current = right
            current_value = right_value    
        else:
            break

    return current,current_value

    # Main programa
start = float(input("enter the string value:"))       
step_size = float(input("enter the step size:"))   
max_iterations = int(input("enter the maximum iterations:"))

best_position ,best_value = hill_climbing (start,step_size,max_iterations)

print("\nBest position =", best_position)
print("maximum value =", best_value)