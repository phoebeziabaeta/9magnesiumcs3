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

class recordbook:
    def __init__(self, date, meeting, notes, recordAmount, records):
        self.date = date
        self.meeting = meeting
        self.notes = notes
        self.recordAmount = recordAmount
        self.records = records
