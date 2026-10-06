"""
Week -3: Fibonacci Series Generator
A program to print the Fibonacci series for n terms.
"""

def fibonacci(n):
    """
    Generate Fibonacci series for n terms.
    
    Args:
        n (int): Number of terms in the Fibonacci series
        
    Returns:
        list: List containing the Fibonacci series
        
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("Number of terms must be at least 1")
    
    series = []
    a, b = 0, 1
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series


def main():
    """Main function to get input and display Fibonacci series."""
    try:
        n = int(input("Enter the number of terms: "))
        if n < 1:
            print("Error: Please enter a positive integer")
            return
        
        series = fibonacci(n)
        print("Fibonacci Series:")
        print(" ".join(map(str, series)))
    except ValueError:
        print("Error: Please enter a valid integer")


if __name__ == "__main__":
    main()
