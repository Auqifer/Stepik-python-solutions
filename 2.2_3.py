#Дана последовательность натуральных чисел от 1 до n.
#Напишите программу, которая сначала располагает в обратном порядке часть элементов этой последовательности от элемента с номером 

# X до элемента с номером 
# �
# Y, а затем от элемента с номером 
# �
# A до элемента с номером 
# �
# B.
n, x, y, a, b = input().split()
res = [i for i in range(1, int(n) + 1)]
res[int(x) - 1:int(y)] = res[int(x) - 1:int(y)][::-1]
res[int(a) - 1:int(b)] = res[int(a) - 1:int(b)][::-1]
print(*res)
#Fdsafasfasfasdfas
