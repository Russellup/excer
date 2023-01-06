def equilateral(sides):
    # step one sum of sides
    # step two calculate expected side length for equalateral triangle
    # step three compare each side length with expected 
    sum = 0
    print('sides', sides)
    for side in sides:
        new_sum = sum + side  
        print(side)
        sum = new_sum 
        
    print(sum) 
    expected_side = sum/3  
    print(expected_side)

    for side in sides:
        if side != expected_side:
            return False
    
    for side in sides:
        if side == sum:
            return False
    
    return True

    

def isosceles(sides):
    #triangle inequality violation check
    # if not (sides[0] + sides[1] >= sides[2]):
    #    return False
    # if not (sides[1] + sides[2] >= sides[0]):
    #    return False
    # if not (sides[0] + sides[2] >= sides[1]):
    #    return False 
    if inequality_violation(sides):
        return False
    # actual isosceles check    
    if sides[0] == sides[1]:
       return True    
    if sides[1] == sides[2]:
       return True
    if sides[0] == sides[2]:
       return True
   
    return False        


    
    #step one compar the first two sides if same then it is isoce
    #else if the third side is the same ae ither the first or 
    #second then it is an isoseles return true
    
    #step two calculate how to isolate one of the sides
    
    
    
   


def scalene(sides):
    if inequality_violation(sides):
      return False
    if sides[0] == sides[1]:
      return False  
    if sides[1] == sides[2]:
      return False
    if sides[0] == sides[2]:
      return False 
    

    return True
def inequality_violation(sides):
    result = False
    if not (sides[0] + sides[1] >= sides[2]):
       result = True
    if not (sides[1] + sides[2] >= sides[0]):
       result = True
    if not (sides[0] + sides[2] >= sides[1]):
       result = True 
        

    return result

    
        