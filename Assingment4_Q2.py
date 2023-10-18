l1_str = input("Enter a list of numbers:")
l = list(map(int,l1_str.split()))
triple = lambda x: x * 3
result = list(map(triple,l))
print("Sample list:", l)
print("Triple of list Numbers:", result)