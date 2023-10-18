l1_str = input("Enter a list of numbers:")
l = list(map(int,l1_str.split()))
double = lambda x: x **2
result = list(map(double,l))
print("Sample list:", l)
print("Triple of list Numbers:", result)