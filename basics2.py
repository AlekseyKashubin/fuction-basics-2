#1
def countdown(x):
        for y in range(x, 0-1, -1):
                print(y)
countdown(5)

#2
def problem2(x,y):
        print(x)
        return(y)
problem2(5,10)

#3
def problem3(a):
    sum = a[0] + len(a)
    print(sum)
problem3([1,2,3,4,5,6,7,8,9])

#4
new_list = []
def problem4(list):
    if len(list) < 2:
        return False
    for i in range(0, len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
problem4([5,2,3,2,1,4])
problem4([3])

#5
def problem5(size, val):
    for i in range(0, size):
        if i <= size:
                print(val)
problem5(4,7)
problem5(6,2)