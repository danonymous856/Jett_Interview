from twisted.python.util import println

for i in range(0, 12):

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")

    # ending line after each row
    print("\r")