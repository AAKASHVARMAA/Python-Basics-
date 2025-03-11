def num_count(num):
    if(num==-1):#base case
        return
    print(num)
    num_count(num-1)
num_count(5)