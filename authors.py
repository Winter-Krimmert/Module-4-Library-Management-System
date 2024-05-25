class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

# accessor methods, commonly known as getters, return the value of the private attributes.
# Getters provide a controlled way to access the attributes.
# This preserves the integrity of the data from outside.
    def get_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography
    

    # For user convenience. For clear summary of the user details. For debugging.
def __str__(self):
    return f"Name: {self.__name}, Biography: {self.__biography} "