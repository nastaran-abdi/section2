
sum = 0
min = 20
max = 0
a=int(input("please enter number of students"))
for i in range (a):
    b=float(input("please enter point"))
    sum = sum+b
    if b<min:
        min=b
    if b>max:
        max=b
average=sum/a
print(average)
print(min)
print(max)