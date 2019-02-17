## Name: Allie Blaising 


import random
import time



def selection_sort(alist):
    count = 0
    for i in range(len(alist)):
        for j in range(i + 1,len(alist)):
            count += 1 
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    return count 
           


def insertion_sort(alist):
    count = 0
    for index in range(1,len(alist)):
         count += 1 
         currentvalue = alist[index]
         position = index
         while position > 0 and alist[position - 1] > currentvalue:
             alist[position] = alist[position-1]
             position = position - 1
             count += 1 
         alist[position] = currentvalue    
    return count 


def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 500000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

