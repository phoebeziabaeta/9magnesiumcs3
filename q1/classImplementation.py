class attendancesheet:
    members = []
    pres = []

    def __init__(self, names, date, present, excused):
        self.names = names
        self.date = date
        self.__present__ = max(0, present)
        self.excused = excused

    def list_members(self):
        print(f"List of members:\n{'\n'.join(self.names)}")
        print("")
        return self.names

    def list_present(self, pres):
        print(f"Amount of members present: {len(pres)}")
        print("")
        return len(pres)

    def updatePresent(self, present):
        self.__present__ = present
        update = input("Do you want to update the amount of members present? (yes/no): ")
        if update.lower() == "yes":
            new_present = int(input("Enter the new amount of members present: "))
            self.__present__ = max(0, new_present)
        else:
            print("No one has left or arrived.")
        print(f"Updated amount of members present: {self.__present__}")
        return self.__present__


memb = input("Enter list of members (separate by spaces): ")
members = memb.split()

memb2 = input("Enter list of members present separate by spaces: ")
pres = memb2.split()
      
exc = input("Enter list of members excused separate by spaces: ")
excused = exc.split()

sheet = attendancesheet(members, "2023-10-01", len(pres), len(excused))
sheet.list_members()
sheet.list_present(pres)
sheet.updatePresent(len(pres))
