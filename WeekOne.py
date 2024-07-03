# LowerTriangle
def lower_triangular(n):
    for i in range(1, n + 1):
        print('*' * i)

# UpperTriangle
def upper_triangular(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Pyramid
def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# calling the Main function to print all patterns 
def main():
    n = 5
    
    print("Lower Triangular Pattern:\n" )
    lower_triangular(n)
    print("\n")  # Adding blank line for separation

    print("Upper Triangular Pattern:\n")
    upper_triangular(n)
    print("\n")  # Adding blank line for separation

    print("Pyramid Pattern:\n")
    pyramid(n)

# Calling the main function
main()