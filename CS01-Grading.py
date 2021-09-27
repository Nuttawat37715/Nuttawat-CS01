A = int(input("score 1:"))
B = int(input("score 2:"))
C = int(input("score 3:"))
Score = A + B + C
if 100 >= Score >= 80:
    print("A")
elif 80 > Score >= 75:
    print("B+")
elif 75 > Score >= 70:
    print("B")
elif 70 > Score >= 65:
    print("C+")
elif 65 > Score >= 60:
    print("C")
elif 60 > Score >= 55:
    print("D+")
elif 55 > Score >= 50:
    print("D")
elif 50 > Score >= 0:
    print("F")