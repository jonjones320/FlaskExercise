"""Basic math operations."""

def add(a, b):
    """Add a and b."""
    
    return a + b

def sub(a, b):
    """Substract b from a."""

    return a - b

def mult(a, b):
    """Multiply a and b."""

    return a * b

def div(a, b):
    """Divide a by b."""

    return a / b

def math(a,b, function):
    """Add, sub, mult or divide a & b based on input"""
    math_dict = {
        "add": add(a,b),
        "sub": sub(a,b),
        "mult": mult(a,b),
        "div": div(a,b)
    }
    return f"{math_dict[function](a,b)}"