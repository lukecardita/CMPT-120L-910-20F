# Write a main function which takes a number entered by the user and calls the function, outputting the result to the user with a print statement.
def sumofnumbers(x):
    sum = 0
    for num in range(0, x+1, 1):
        sum = sum + num
    print(sum)
if __name__ == "__main__":
    sumofnumbers(10)

# Write a function which will sum a range of integers starting from one going up and including a value entered by the user. Return the sum.

n = 10
sum = 0
for num in range(0, n+1, 1):
    sum = sum + num
print(sum)