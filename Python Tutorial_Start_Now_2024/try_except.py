# Error handling for your programing 
try:
    n = int(input("Enter the number : "))
    print(n + 12)
except Exception as e:
    print("Some error occurred: ",e)


