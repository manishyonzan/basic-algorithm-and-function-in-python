# Practical Example: Custom Error Class
# Let's create a custom error class that provides better debugging information. 
# This example shows how you can use __str__ and __repr__ to make your error messages more helpful:

class ValidationError(Exception):
    def __init__(self, field, message, value=None):
        self.field = field
        self.message = message
        self.value = value
        super().__init__(self.message)
        
    def __str__(self):
        if self.value is not None:
            return f"Error in field '{self.field}':{self.message} (got:{repr(self.value)})"
        return f"Error in field '{self.field}', message='{self.message}'"
    
    def __repr__(self):
        if self.value is not None:
            return f"ValidationError(field='{self.field}', message='{self.message}', value='{repr(self.value)}')"
        return f"ValidationError(field='{self.field}', message='{self.message}')"
    
    
try:
    age = -5
    if age < 0:
        raise ValidationError("age","age must be positive",age)
except ValidationError as e:
    print(e)