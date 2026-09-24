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
        self.related_objects = []

    def findRecord(self, record):
        input_find = input("Do you want to find a record? (yes/no): ")
        if input_find == "yes":
            rec = input("Enter the record to find: ")
            if rec in self.records:
                print(f"Record found: {rec}")
            else:
                print("Record not found.")
        return self.records

    def addRecord(self, new_record):
        input_record = input("Do you want to add a record? (yes/no): ")
        if input_record == "yes":
            new_record = input("Enter the new record: ")
            self.records.append(new_record)
            self.recordAmount += 1
        else:
            print("Record book unchanged.")
        return self.records


print("---BEFORE RELATIONSHIP---")
print("")
record1 = attendancesheet("Alice, Bob, Charlie", "2001-10-01", 2, 1)
record2 = attendancesheet("David, Eve, Frank", "2015-10-02", 3, 0)
record3 = attendancesheet("Grace, Heidi, Ivan", "2023-10-03", 1, 2)
rbook = [recordbook
("2023-10-01", "Meeting 1", "Notes for meeting 1", 0, []),
         recordbook("2023-10-02", "Meeting 2", "Notes for meeting 2", 0, []),
         recordbook("2023-10-03", "Meeting 3", "Notes for meeting 3", 0, [])]
print("")

print("---BUILDING RELATIONSHIP ---")
print("")
print("")
...
print("---AFTER RELATIONSHIP---")
print("")
print("")
...
print("Related object(s):")
print("")
print("")
...
