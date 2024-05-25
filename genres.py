class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category


        # For user convenience. For clear summary of the genre details. For debugging.
    def __str__(self):
        return f"Name: {self.__name}, Description: {self.__description}, Category: {self.__category}"
