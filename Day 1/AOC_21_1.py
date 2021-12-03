numbers = []

with open('input.txt') as data:
    for line in data:
        numbers.append(int(line.rstrip()))
    
def depth_check(items):
    total = 0
    for i in range(1, len(items)):
        if items[i] > items[i-1]:
            total += 1
            
    print(total)

depth_check(numbers)
