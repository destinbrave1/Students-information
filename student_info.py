class Students(object):
    def __init__(self):
        print("\nADVENTIST UNIVERSITY OF CENTRAL AFRICA\n")
        self.Roll_no = 0
        self.First_name = ""
        self.Last_name = ""
        self.Gender = ""
        self.Age = 0
        self.Department = ""
        self.Faculty = ""
        self.Registration_date = ""
    def students_info(self):
        print("// Students Information\n")
        self.Roll_no = int(input("Student's Roll_number : ...\n"))
        self.First_name = input("Student's first_name :\n")
        self.Last_name = input("student's last_name :\n")
        print("Student's Gender ? 'MALE / FEMALE' \n")
        self.Gender = input("Gender : \n")
        self.Age = int(input("Student's Age :\n"))
        self.Faculty = input("Student's faculty : \n")
        self.Department = input("Student's department : \n")
        self.Registration_date = input("Student's registration date ('DD/MM/YYYY') : \n")
    def display_students(self):
        print("Student's ID : ",self.Roll_no)
        print("Student's first name : ",self.First_name)
        print("Student's last name : ",self.Last_name)
        print("Student's Gender ",self.Gender)
        print("Student's Age : ",self.Age)
        print("Student's Department : ",self.Department)
        print("Student's Faculty : ",self.Faculty)
        print("Student's Registration date : ",self.Registration_date)
L = []
for i in range(3):
    a = Students()
    a.students_info()
    L.append(a)
for i in range(3):
    print("................................")
    L[i].display_students()
    print("................................")
