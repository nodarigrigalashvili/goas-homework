num = int(input("Enter Number: "))


print(num % 2 == 0 and num % 4 == 0)


I = 7 > 4
Q = 23 < 130
D = 392 >= 292
F = 524 <= 500
A = 100 == 100.0
C = 10.00 != 10.0

IQ = 7 > 4 and 23 < 130
QD = 23 < 130 and 392 >= 292
DF = 392 >= 292 and 524 <= 500
FA = 524 <= 500 and 100 == 100.0
AC = 100 == 100.00 and 10.00 != 10.0
IC = 7 > 4 and 10.00 != 10.0
QA = 23 < 130 and 100 == 100.0
DF = 392 >= 292 and 524 <= 500
II = 7 > 4 and 7 > 4
CC = 10.00 != 10.0 and 10.00 != 10.0