def square_root_bisection(square_target, tolerance=0.01, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0.0
    high = max(1.0, float(square_target))
    converged = False
    
    for iteration in range(max_iterations):
        mid = (low + high) / 2.0
        
        if (high - low) <= tolerance:
            converged = True
            root = mid
            break
            
        if mid ** 2 < square_target:
            low = mid
        else:
            high = mid

    if converged:
        print(f"The square root of {square_target} is approximately {root}")
        return root
    
    print(f"Failed to converge within {max_iterations} iterations")
    return None
