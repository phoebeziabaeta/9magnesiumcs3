class attendancesheet:
    members = []
    pres = []

    def __init__(self, names, date, present, excused):
        self.names = names
        self.date = date
        self.__present = max(0, present)
        self.excused = excused

    def list_members(self):
        print("\n".join(self.names))
        return self.names

    def list_present(self):
        print(f"Amount of members present: {len(self.pres)}")
        return self.pres


memb = input("Enter list of members (separate by spaces): ")
members = memb.split()

memb2 = input("Enter list of members present separate by spaces: ")
pres = memb2.split()

