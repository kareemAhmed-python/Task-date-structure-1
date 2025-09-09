

def is_prime(n):
    """
    Checks if a given number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True



def calculator(a, b, operation):
    """
    Performs arithmetic operations on two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        operation (str): Operation to perform ("add", "subtract", "multiply", "divide")
        
    Returns:
        int/float: Result of the operation
        str: Error message if division by zero or invalid operation
    """
    operation = operation.lower()
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a / b
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'"
    

    # Test the prime number checker
print(is_prime(7))    
print(is_prime(10))   
print(is_prime(2))    
print(is_prime(1))    

# Test the calculator
print(calculator(10, 5, "add"))        
print(calculator(10, 5, "subtract"))   
print(calculator(10, 5, "multiply"))   
print(calculator(10, 5, "divide"))     
print(calculator(10, 0, "divide"))     
print(calculator(10, 5, "power"))     