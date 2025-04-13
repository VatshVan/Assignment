import sys
import time
# your implementation for printing the list of prime numbers
def no_of_primes_in_n(num):
    """In this function, we will calculate no. of prime numbers"""
    result = []
    boolean_flag = [True]*(num+1)
    boolean_flag[:2] = [False,False]
    for i in range(2,int(num**0.5)+1):
        if boolean_flag[i]:
            for j in range(i*i,num+1,i):
                boolean_flag[j] = False
    for k in range(len(boolean_flag)):
        if boolean_flag[k] is True:
            result.append(k)
    return result
# read the parameter from command line using sys
if __name__ == "__main__":
    NUM = int(sys.argv[1])
    tw = time.perf_counter()
    primes = no_of_primes_in_n(NUM)
    print(primes)
    ts = time.perf_counter() - tw
    print(f"Total time taken to calculate: {ts}")
