


def max_heapify(A,i,n):
    print(A)
    l = 2 * i
    r = 2*i +1
    if (l <= n) and (A[l-1] > A[i-1]):
        largest = l
    else:
        largest = i


    if (r <= n) and (A[r-1] > A[largest-1]):
        largest = r 
    
    # print("i = ", i)
    # print("largest = ", largest)
    if largest != i:
        A[i-1],A[largest-1] = A[largest-1],A[i-1]
        max_heapify(A,largest,n)


def main():
    A = [0,25,22,19,18,17,16,12,13,11,10]

    max_heapify(A,1,11)
    

if __name__ == "__main__":
    main()
