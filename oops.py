#Class
"""A class is a blueprint for creating objects.
 It defines the attributes and methods that objects of that class will have."""
# Example
class Student():
    def __init__(self,name,roll_no,father_name,ph_number): # Initialiazes the Student object
        self.name=name
        self.roll_no=roll_no             
        self.father_name=father_name
        self.ph_number=ph_number
    def student_details(self):
        print(f"name of the student:{self.name}")
        print(f"roll_no:{self.roll_no}")
        print(f"father's name:{self.father_name}")
        print(f"student phone number:{self.ph_number}")
#Object
""" an object is a fundamental unit of data
 that combines both data (attributes) and behavior (methods). """
# Creating Student Objects
student1=Student("Ram",123,"krishna",1234567890)
student2=Student("seetha",321,"Siva",1235674908)
#Display Student Details
student1.student_details()
student2.student_details()

        
    
    
