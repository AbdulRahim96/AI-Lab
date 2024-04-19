class person:


    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        # Assuming date_of_birth is in the format "DD/MM/YYYY. so i will be getting string from 6 to end string"
        birth_year = int(self.date_of_birth[6:])
        current_year = 2024  
        age = current_year - birth_year
        print("Age of ", self.name, " is", age)
    
obj = person("rahim", "Pakistan", "03/08/1996")
print(obj.age())