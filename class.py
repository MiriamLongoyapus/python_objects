class Student:
    name="Mercy"
    age=21
    school="Akirachix"
    nationality="Kenyan"

    def __init__(self,name,age,nationality):
     self.name=name
     self.age=age
     self.nationality=nationality

    def greet_student(self):
     return f"Hello{Student.name}, welcome to {self.school}, proudly{self.nationality}"
    
#Update the Student Class to include these attributes - first_name, last_name, age, country
#     - Add these methods to the Student class
#             - show_full_name
#             - year_of_birth
#            - show_initials



class Student:
    first_name = "Miriam"
    last_name  = "Longoyapus"
    age = 50
    country = "Kenyan"
    

    def __init__(self,first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name  = last_name
        self.age = age
        self.country = country

    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        # current_year = datetime.datetime.now().year
        return f"{self.year_of_birth}"

    
    
    def show_initials(self):
        print(f"{self.first_name[0]},{self.last_name[0]}")



