l1 = int(input("Enter a Number:"))
sum = lambda x: x + 25
result = sum( l1)
print(f"The result of adding 25 to {l1} is {result}")

#
def triple(n):
    return n**3
l1 = [1,2,3,4,5,6,7]
l = list(map(triple,l1))
print(l)