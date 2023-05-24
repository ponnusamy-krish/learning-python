if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_set = set(arr)
    new_list = list(new_set)
    new_list.sort()
    print(new_list[-2])
   
           
   