# exception_handling/06_custom_exceptions.py
"""
CUSTOM EXCEPTIONS
=================

What is it?
-----------
Creating your own exception types for specific error conditions.

When to use it?
---------------
Use custom exceptions when:
1. Built-in exceptions don't adequately describe the error
2. You need to include additional information with the error
3. You want to create a hierarchy of related exceptions

How to identify it?
-------------------
Look for application-specific error conditions that need special handling.
"""

# Example 1: Basic custom exception
print("=== BASIC CUSTOM EXCEPTION ===")

class InvalidAgeError(Exception):
    """Exception raised for invalid ages"""
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}: {self.age}"

def set_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    print(f"Age set to {age}")

try:
    set_age(150)
except InvalidAgeError as e:
    print(f"Error: {e}")

# Example 2: Exception hierarchy
print("\n=== EXCEPTION HIERARCHY ===")

class BankError(Exception):
    """Base class for bank-related errors"""
    pass

class InsufficientFundsError(BankError):
    """Exception raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: {balance} available, {amount} requested")

class AccountClosedError(BankError):
    """Exception raised when account is closed"""
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.is_open = True
    
    def withdraw(self, amount):
        if not self.is_open:
            raise AccountClosedError()
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance
    
    def close(self):
        self.is_open = False

# Test the exceptions
account = BankAccount(100)
try:
    account.withdraw(150)
except BankError as e:
    print(f"Bank error: {e}")

account.close()
try:
    account.withdraw(50)
except BankError as e:
    print(f"Bank error: {e}")

# Example 3: Adding custom methods
print("\n=== CUSTOM METHODS IN EXCEPTIONS ===")

class ConfigurationError(Exception):
    """Exception for configuration errors"""
    def __init__(self, key, value, message="Invalid configuration"):
        self.key = key
        self.value = value
        self.message = message
        super().__init__(self.message)
    
    def get_details(self):
        return f"Key: {self.key}, Value: {self.value}, Problem: {self.message}"

def validate_config(key, value):
    if key == "timeout" and value < 0:
        raise ConfigurationError(key, value, "Timeout must be positive")
    # Other validations...

try:
    validate_config("timeout", -5)
except ConfigurationError as e:
    print(f"Configuration error: {e}")
    print(f"Details: {e.get_details()}")

"""
Key Points:
- Custom exceptions make error handling more specific
- You can create hierarchies of related exceptions
- Add custom methods to provide more error information
- Use them for application-specific error conditions
"""
