import numpy as np
Lenght = []
Row = []
m = int(input("Enter your Row: "))
n = int(input("Enter your Lenght: "))
x = m*n
print("Input Number First Array: ")
for i in range(x):
    Lenght+=[int(input(""))]
NewRow = np.asarray(Row)
print("Input Second Array: ")
for a in range(x):
    Row+=[int(input(""))]
NewRow = np.asarray(Row)
NewLenght = np.asarray(Lenght)
NewRowNumpy = NewLenght.reshape(int(m),n)
print(NewRowNumpy)
NewLenghtNumpy = NewLenght.reshape(int(n),m)
print(NewLenghtNumpy)
 y = np.add(NewRowNumpy,NewLenghtNumpy)
print(y)
