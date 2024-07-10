# METHOD 1

def get_max():
    grades = [9.6, 9.2, 9.7]
    max = 0
    for i in grades:
        if i > max:
            max = i
    return max

print(get_max())

# METHOD 2

def get_max2():
    grades = [9.6, 9.2, 9.7]
    grades.sort(reverse=True)
    output = f"Max: {grades[0]}, Min: {grades[-1]}"
    return output

print(get_max2())

# METHOD 3

def get_max3():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)    
    minimum = min(grades)    
    message = f"Max: {maximum}, Min: {minimum}"    
    return message
 
print(get_max3())