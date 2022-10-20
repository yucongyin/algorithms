from maxheapify import max_heapify
from buildmaxheap import build_max_heap

def heapsort(A,n):
    build_max_heap(A,n)
    for i in range(n,1,-1):
        A[0],A[i-1] = A[i-1],A[0]
        max_heapify(A,1,i-1)





def main():
    A = [1,5,3,8,7,6]
    heapsort(A,6)
    print("sorted: ",A)




if __name__ == "__main__":
    main()