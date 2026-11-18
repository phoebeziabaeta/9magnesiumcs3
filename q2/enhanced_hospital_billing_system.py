class  Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print("Patient Name: ", self.name)
        return self.name

    def set_bill_amount(self, bill_amount): 
        self.bill_amount = bill_amount
        float(self.bill_amount)

    def get_bill_amount(self):
        print(f"Original Bill: ₱{self.bill_amount:,.2f}")
        return self.bill_amount

    def calculate_bill(self):
        print(f"Final Bill: ₱{self.bill_amount:,.2f}")
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.2
        discount_amount = self.bill_amount * (1 - discount)
        print(f"Final Bill: ₱{discount_amount:,.2f}")
        return discount_amount

    def display_patient_type(self):
        print("Patient Type: Senior Patient")

class PhilHealthMember(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = self.bill_amount * 0.15
        final_amount = self.bill_amount - discount
        print(f"Final Bill: ₱{final_amount:,.2f}")
        return final_amount

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print("-----------------------")
ob1 = Patient("Juan Dela Cruz", 15000)
ob2 = SeniorPatient("Maria Santos", 15000)
ob3 = PhilHealthMember("Pedro Reyes", 15000)

ob1.get_name()
ob1.display_patient_type()
ob1.get_bill_amount()
ob1.calculate_bill()
print("")

ob2.get_name()
ob2.display_patient_type()
ob2.get_bill_amount()
ob2.calculate_bill()
print("")

ob3.get_name()
ob3.display_patient_type()
ob3.get_bill_amount()
ob3.calculate_bill()
