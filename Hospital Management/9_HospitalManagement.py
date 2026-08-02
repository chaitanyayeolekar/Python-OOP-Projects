# class Patient:
#     def __init__(self,id, disease):
#         self.id = id
#         self.disease = disease
#         self.assign = True

# class Doctor:
#     def Add_patient(self, disease):
#         disease = ["cough","cold"]
#         if disease == disease.disease:
#             print("go to medcial and told")
#             if disease[1]:
#                 print("tell the medical i want paracitamol")
#             elif disease[2]:
#                 print("tell the medical store , i want minoxidol")
#             else:
#                 print("cough syrup")
#         else:
#             print("serious condition")

#     def Asisgn_doctor(self,disease):
#         if self.disease == disease.disease:
#             self.Assign = True
#             print("doctor coming ")

#     def Dis


# p1 = Patient(1,"cough")
# p2 = Patient(2, "fracture")


# d1 = Doctor()
# d1.Add_patient(p1)


#********************************reattempt*************************************

# class Patient:

#     def __init__(self,patient_id, name, disease):
#         self.patient_id = patient_id
#         self.name = name
#         self.disease = disease

# class Doctor:
#     def __init__(self,doctor_id, name, specialiazation):
#         self.doctor_id = doctor_id
#         self.name = name
#         self.specialization = specialiazation


#     def add_patient(self, patient):
#         print(patient.name,"Added successfully")

#     def assign_doctor(self,patient):
#         print(patient.name , "is assignment to Dr.",self.name)

#     def display_record(self, patient):
#         print("\n-------Patient Record---------")
#         print("Patient Id :",patient.patient_id)
#         print("patient Name :",patient.name)
#         print("Disease:",patient.disease)
#         print("Doctor:",self.name)
#         print("specialiation:",self.specialization)


# p1 = Patient(101,"Chaitanya","Fever")
# p2 = Patient(102, "maggie","constipation")


# d1 = Doctor(1,"Sharma","General Physician")
# d2 = Doctor(2,"yeolekar","stomach specilist")

# d1.add_patient(p2)
# d1.assign_doctor(d2)
# d2.display_record(p2)


#****************************this is my 2nd attempt***********************




class Patient:

    print("--------------Welcome To Maggie hospital-----------")
    def __init__(self,id, name , disease):
        self.id = id
        self.name = name
        self.disease = disease


class Doctor:

    def __init__(self, id , name, specialization):
        self.list = ["cough","fever","cold"]
        self.doctor_list["stomach","heart"]
        self.id = id
        self.name = name
        self.specialization = specialization


    def add_patient(self, patient):
        if patient.disease in self.list:
            print("no need doctor purchase this medicine")

        else:
            print(patient.name,"is listed......")


    def add_doctor(self, patient):

        if patient.disease not in self.list:
            print(patient.name , "is assigned to Dr",self.name)
        else:
            print("no need doctor")


    def display_record(self,patient):
        print("\n--------patient details")
        print("patient id :",patient.id)
        print("patient name :",patient.name)
        print("patient disease :",patient.disease)
        print("Doctor :",self.name)
        print("Specialization",self.specialization)


c1 = Patient(101,"chaitanya","stomach")

d1 = Doctor(1,"maggie","heart")
d2 = Doctor(2,"sharma","stomach")

d1.add_patient(c1)
d1.add_doctor(c1)
d1.display_record(c1)
        

