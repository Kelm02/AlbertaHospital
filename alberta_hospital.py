""" The funtions that aren't hashtagged out work but I couldnt get the program to run while having two classes.
    My submittion has two different sets of classes because I started with the Doctors option
    but when I realized i wouldnt be able to finish the full set after spending ten hours trying
    to fiure out searchDoctorById."""

class Main:

    while True:
        
            main_menu = int(input("""
        Welcome to Alberta Hospital (AH) Managment system 
        Select from the following options, or select 0 to stop: 
        1 - 	Doctors
        2 - 	Facilities
        3 - 	Laboratories
        4 - 	Patients

        > """))
            if main_menu == 1:
                
                doctor_menu = int(input("""
        Doctors Menu:
        1 - Display Doctors list
        2 - Search for doctor by ID
        3 - Search for doctor by name
        4 - Add doctor
        5 - Edit doctor info
        6 - Back to the Main Menu

        > """))
        


            if main_menu == 3:
                lab_menu = int(input("""
        Laboratories Menu:
        1 - Display laboratories list
        2 - Add laboratory
        3 - Back to the Main Menu
                """))



                break


    class Doctor: 
        Doctors_list = []
    
        def __init__(self, id="", name="", specilist="", timing="", qualification="", roomNb=""):
            self.__id = id
            self.__name = name 
            self.__specilist = specilist
            self.__timing = timing
            self.__qualification = qualification
            self.__roomNb = roomNb

        def getId(self):
            return self.__id

        def setId(self, id):
            self.__id = id

        def getName(self):
            return self.__name

        def setName(self, name):
            self.__name = name

        def getSpecilist(self):
            return self.__specilist

        def setSpecilist(self, specilist):
            self.__specilist = specilist

        def getTiming(self):
            return self.__timing

        def setTiming(self, timing):
            self.__timing = timing

        def getQualification(self):
            return self.__qualification

        def setQualification(self, qualification):
            self.__qualification = qualification

        def getRoomNb(self):
            return self.__roomNb

        def setRoomNb(self, roomNb):
            self.__roomNb = roomNb
        
        

        if doctor_menu == 1:

            def readDoctorsFile(self):
                f = open("doctors.list.txt", "r")
                lines = f.readlines()
                for l in lines:
                    inst = l.split("_")
                    doctorObject = Doctor(inst[0], inst[1], inst[2], inst[3], inst[4], inst[5])
                    self.Doctors_list.append(doctorObject)

            def displayDoctorsList(self):
                for i in range(len(self.Doctors_list)):
                    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(self.Doctors_list[i].__id, self.Doctors_list[i].__name, self.Doctors_list[i].__specilist, self.Doctors_list[i].__timing, self.Doctors_list[i].__qualification, self.Doctors_list[i].__roomNb))
        
    class Laboratories: 
        laboratories_list = []
    
        def __init__(self, lab="", cost=""):
            self.__lab = lab
            self.__cost = cost 

        def getLab(self):
            return self.__lab

        def setLab(self, lab):
            self.__lab = lab

        def getCost(self):
            return self.__cost

        def setAgCost(self, cost):
            self.__cost = cost
        while True:
            if lab_menu == 1:
                # 1 - Display labroratories list
                def readLaboratoriesFile(self):
                    file = open("laboratories.txt", "r")
                    lines = file.readlines()
                    for l in lines:
                        inst = l.split("_")
                        labObject = Laboratories(inst[0], inst[1])
                        self.laboratories_list.append(labObject)

                def displayLabsList(self):
                    for i in range(len(self.laboratories_list)):
                        labsList = print("{:<15} {:<15}".format(self.laboratories_list[i].__lab, self.laboratories_list[i].__cost))
                
            if lab_menu == 2:
                def enterLaboratoryInfo(self):
                    facility_num = input("Enter a Facility Number: ")
                    facility_cost = input("Enter the cost of facility"f"{facility_num}: ")
                    underscore = "_"
                    userFacility_entry = (f"Facility{facility_num + underscore + facility_cost}") 
                    file = open("laboratories.txt", "a")
                    file.write(userFacility_entry)

            if lab_menu == 3:
                main_menu
            
            else:
                break

"""Failed attempts. Many of these turned into abominations"""
# THIS IS THE CLOSEST TO WORKING 
    # Not sure why anytime i specify the indexs i need, the program tells me that it isnt. and for some reason if i dont have the or statment with the second set of indexs, the output will fail, regardless of which one i leave in. 
    # def searchDoctorById(self):
    #     id = input("Enter a Dr ID number: ")
    #     file = open("doctors.list.txt", "r")
    #     dr_list = []
    #     for line in file:
    #         line_strip = line.strip()
    #         line_split = line_strip.split("_")
    #         dr_list.append(line_split)
    #     drList_full = []
    #     for i in dr_list:
    #         for j in i:
    #             drList_full.append(j)
    #         print(drList_full)
    #         for lists in drList_full:
    #             if drList_full[2][6] or drList_full[3][12] == id:
    #                 print("true")
    #             else:
    #                 print("false")
    #     print(drList_full[6])


 # def searchDoctorById(self):
    #     id = input("Enter a Dr ID number: ")
    #     f = open("doctors.list.txt", "r")
    #     lines = f.readlines()
    #     index = ([0])
    #     index = ([1])
    #     index = ([2])
    #     index = ([3])
    #     index = ([4])
    #     index = ([5])
        
    #     if index.startswith(id):
    #         print(True)


# def searchDoctorById(self):
    #     idNum = input("Enter an ID number: ")
    #     file = open("doctors.list.txt", "r")
    #     return(file.read([0]))
    #     if idnum == index(0):
    #     for line in "doctors.list.txt":
    #         id = line.split("_")[0]
    #     if find_id == id:
    #     print(line)
    

    # def searchDoctorById(self):
    #     id = input("Enter a Dr ID number: ")
    #     file = open("doctors.list.txt", "r")
    #     lines = file.readlines()
    #     for l in lines: 
    #         inst = l.split("_")
    #         doctorObject = Doctor(inst[0], inst[1], inst[2], inst[3], inst[4], inst[5])
    #         self.Doctors_list.append(doctorObject)

    #     for i in range(len(self.Doctors_list)):
    #         print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(self.Doctors_list[i].__id, self.Doctors_list[i].__name, self.Doctors_list[i].__specilist, self.Doctors_list[i].__timing, self.Doctors_list[i].__qualification, self.Doctors_list[i].__roomNb))
        
    #     for id in lines:
            
    #         if str(id) == lines[:2]:
    #             print("ID True.")
    #         else:
    #             print("ID False.")


    # def searchDoctorById(self):
    #     id = input("Enter a Dr ID number: ")
    #     with open("doctors.list.txt") as f:
    #         lines = [line.rstrip().split("_") for line in f]
    #         print(lines)
    #         if str(id) == lines[0]:
    #             print("TRUE")
    #         else:
    #             print("FALSE")


    # def searchDoctorById(self):
    #         id = input("Enter a Dr ID number: ")
    #         f = open("doctors.list.txt", "r")
    #         for line in "doctors.list.txt":
    #             if id in line:
    #                 print("yes")
    #             else: 
    #                 print("No")