from maxheapify import max_heapify


def build_max_heap(A,n):
    print(A)
    for i in range (((int)(n/2)),0,-1):
        print(i)
        max_heapify(A,i,n)




def main():
    A = [2,8,5,3,9,1]
    build_max_heap(A,6)












if __name__ == "__main__":
    main()