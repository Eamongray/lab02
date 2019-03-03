
def find_reverse(numbers):
    #TODO: find the reverse of the list
    numbers = numbers[::-1]
    return numbers

    pass

def find_max(numbers):
    #TODO: find the maximum of the list
    return max(numbers)
    pass

def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)
    pass

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    return sum(numbers)
    pass

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    return sum(numbers)/len(numbers)
    pass

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    numbers.sort(reverse = True)
    return numbers
    pass

def second_smallest(numbers):
    #TODO: find the second smallest
    numbers.sort()
    small = numbers[0]
    for i in numbers:
       if i == small:continue
       else:
          if i > small:
             small = i
             break;

    return small
    pass

def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    #numbers.sort()
    #small= [numbers[0]]
    #for i in range(1,len(numbers)-1):
    #    if(numbers[i] != numbers[i-1]):small.append(numbers[i])
    #    else: continue

    #return small[k-1]

    numbers.sort()
    if k==1:
        return numbers[0]
    n = 1
    num = numbers[0]
    for i in numbers:
        if i != num:
            num = i
            n += 1
        if n == k:
           return num


    pass

if __name__ == '__main__':
    # If you are testing, place your print statements here
    print(numbers)
    pass
