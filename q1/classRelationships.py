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
        self.records = []
        self.related_objects = []
            
    def __str__(self):
        if self.records is None or len(self.records) == 0:
            return f"Record book ({self.date}): Meeting: {self.meeting}, Notes: {self.notes}, No records available."
        else:
            return f"Record book ({self.date}): Meeting: {self.meeting}, Notes: {self.notes}, Record: {len(self.records)} records available."

    def findRecord(self, records):
        rec = input("Enter the record to find: ")
        if rec in self.records:
            print(f"Record found: {rec}")
        else:
            print("Record not found.")
        return self.records

    def addRecord(self, new_record):
        self.records.append(new_record)
        return self.records


print("---BEFORE RELATIONSHIP---")
print("")
record1 = attendancesheet("Alice, Bob, Charlie", "2001-10-01", 2, 1)
record2 = attendancesheet("David, Eve, Frank", "2015-10-02", 3, 0)
record3 = attendancesheet("Grace, Heidi, Ivan", "2023-10-03", 1, 2)
rbook = recordbook("2023-10-01","5th","incomplete members",3,None)
rbook2 = recordbook("2023-05-20","9th","incomplete members",8,None)
print(f"recorded attendance sheet 1: {record1}")
print(f"recorded attendance sheet 2: {record2}")
print(f"recorded attendance sheet 3: {record3}")
print(f"record book 1: {rbook}")
print(f"record book 2: {rbook2}")
print("")

print("---BUILDING RELATIONSHIP ---")
print("")

for record in [record1, record2, record3]:
    rbook.records = rbook.addRecord(record)
    rbook2.records = rbook2.addRecord(record)
    rbook.related_objects.append(record)
    rbook2.related_objects.append(record)

print(f"Updated record book 1: {rbook}")
print(f"Updated record book 2: {rbook2}")
print("")

print("---AFTER RELATIONSHIP---")
print("")
for obj in rbook.related_objects:
    print(obj)
print("")

print("Related object(s):")
print("")
for obj in rbook.related_objects:
    print(obj)
print("")
print("---END---")
