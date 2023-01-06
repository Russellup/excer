def square_of_sum(number):
    sum = 0
    print('number:',number)
    for result in range(1, number + 1):
        #print('4sum:', sum)
        #print('result', result)
        sum = sum + result 
        #print('Aftersum:', sum)
    print(sum * sum)
    return sum * sum
#test2 second argument to range: 6, number: 5



    
#test3 second argument to range: 101, number: 100
    
    
    
#number = 1
# 1 (dont need to add extra)
# we squared 1 
# 2 : 1 + 2 = 3
#     3^2 = 9    
# 3 : 1 + 2 + 3 = 6
#     6^2 = 36
# 10 _ 4      
# 5 : 1 + 2 + 3 + 4 + 5 = 15
#     15^2 = 225 
def sum_of_squares(number):
    sum = 0
    print('number:', number)
    for n in range(1, number + 1):
        sum = sum + n * n  
    print(sum)
    return sum    
    
    
def difference_of_squares(number):
    # sum_of_squares = 0
    # square_of_sum = 0
    # for num in range(1, number + 1):
    #     sum_of_squares += num * num
    #     square_of_sum += num

    # square_of_sum = square_of_sum ** 2

    return square_of_sum(number) - sum_of_squares(number)

  

   