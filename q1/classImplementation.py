class attendancesheet:
    def __init__(self, names, date, present, excused):
        self.names = [name.strip() for name in names.split(",")] if isinstance(names, str) else list(names)
        self.date = date
        self.__present__ = min(len(self.names), max(0, present))
        self.excused = max(0, excused)

    def __str__(self):
        return (f"Attendance sheet ({self.date}): "
                f"{self.__present__}/{len(self.names)} present, "
                f"{self.excused} excused")

    def list_members(self):
        print(f"List of members:\n{'\n'.join(self.names)}")
        print("")
        return self.names

    def list_present(self, pres):
        print(f"Amount of members present: {len(pres)}")
        print("")
        return len(pres)

    def updatePresent(self, updated_present):
        self.__present__ = min(len(self.names), max(0, updated_present))
        return self.__present__

rec_at1 = attendancesheet("Roffee, Zia, Thumper, Bob", "2024-06-15", 3, 0)
rec_at2 = attendancesheet("Rom, CJ, Six", "2024-06-15", 2, 1)

print("---BEFORE---")
print(" ")
print(f"recorded attendance 1: {rec_at1}")
print(f"recorded attendance 2: {rec_at2}")
rec_at1.updatePresent(4)

print(" ")
print("---AFTER---")
print(" ")

print(f"data of recorded attendance 1: {rec_at1}")
print(f"data of recorded attendance 2: {rec_at2}")
print(" ")
print("---END---")
