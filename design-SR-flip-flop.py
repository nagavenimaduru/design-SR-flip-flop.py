print("===== SR Flip-Flop =====")
print("S = Set, R = Reset")
print("Enter S and R as 0 or 1")

S = int(input("Enter S: "))
R = int(input("Enter R: "))

if S == 0 and R == 0:
    print("Output: Q = Previous State")
elif S == 0 and R == 1:
    print("Output: Q = 0")
elif S == 1 and R == 0:
    print("Output: Q = 1")
elif S == 1 and R == 1:
    print("Invalid State")
else:
    print("Invalid input! Enter only 0 or 1.")
