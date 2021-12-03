numbers = []

with open('input.txt') as data:
    for line in data:
        numbers.append(int(line.rstrip()))
    
def depth_check(items):
    total = 0
    sum_of_three = []
    
    for i in range(0, len(items)):
        if len(items[i: i+3]) == 3:
            sum_of_three.append(sum(items[i:i+3]))
    
    for n in range(1, len(sum_of_three)):
        if sum_of_three[n] > sum_of_three[n-1]:
            total += 1

            
    print(total)

depth_check(numbers)
