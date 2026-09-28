from patient import Patient
from storage import load_patients, save_patients
import validation
import billing

class PatientManagement:
    def __init__(self):
        self.patients = load_patients()

    def find_patient(self, pid):
        return next((p for p in self.patients if p.pid == pid), None)

    def add_patient(self):
        pid = validation.get_positive_int("Enter patient ID: ")
        if self.find_patient(pid):
            print("Error: Patient ID already exists!")
            return
        name = validation.get_non_empty_string("Enter patient Name: ")
        age = validation.get_positive_int("Enter patient age: ")
        disease = validation.get_non_empty_string("Enter disease: ")

        self.patients.append(Patient(pid, name, age, disease))
        save_patients(self.patients)
        print("Patient Added Successfully! ✅")

    def view_patient(self):
        pid = validation.get_positive_int("Enter patient ID to view Patient: ")
        patient = self.find_patient(pid)
        if patient:
            print("\nID\tName\tAge\tDisease\tCharges")
            print("-------------------------------------------")
            patient.display()
        else:
            print("Patient Not Found ❌")

    def update_patient(self):
        pid = validation.get_positive_int("Enter Patient ID to update: ")
        patient = self.find_patient(pid)
        if patient:
            patient.name = validation.get_non_empty_string("Enter new name: ")
            patient.age = validation.get_positive_int("Enter new Age: ")
            patient.disease = validation.get_non_empty_string("Enter new disease: ")
            save_patients(self.patients)
            print("Patient Updated ✅")
        else:
            print("Patient Not Found ❌")

    def delete_patient(self):
        pid = validation.get_positive_int("Enter Patient ID to delete: ")
        patient = self.find_patient(pid)
        if patient:
            self.patients.remove(patient)
            save_patients(self.patients)
            print("Patient Deleted successfully.")
        else:
            print("Patient Not Found ❌")

    def add_charges(self):
        pid = validation.get_positive_int("Enter Patient ID to add charges: ")
        patient = self.find_patient(pid)
        if patient:
            amount = validation.get_positive_float("Enter charges amount: ")
            patient.add_charges(amount)
            save_patients(self.patients)
            print("Charges added ✅")
        else:
            print("Patient Not Found ❌")

    def generate_bill(self):
        pid = validation.get_positive_int("Enter patient ID to generate Bill: ")
        patient = self.find_patient(pid)
        if patient:
            billing.print_hospital_bill(patient)
        else:
            print("Patient Not Found ❌")

    def display_all(self):
        if not self.patients:
            print("No Records Found")
            return
        print("\nID\tName\tAge\tDisease\tCharges")
        print("-------------------------------------------")
        for p in self.patients:
            p.display()

def main():
    system = PatientManagement()
    while True:
        print("\n========= Patient Management System ==========")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Add Charges")
        print("6. Generate Bill")
        print("7. Display ALL")
        print("8. Exit")
        print("==============================================")
        try:
            choice = int(input("Enter Your choice: "))
        except ValueError:
            print("Invalid option! Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            system.add_patient()
        elif choice == 2:
            system.view_patient()
        elif choice == 3:
            system.update_patient()
        elif choice == 4:
            system.delete_patient()
        elif choice == 5:
            system.add_charges()
        elif choice == 6:
            system.generate_bill()
        elif choice == 7:
            system.display_all()
        elif choice == 8:
            print("System Closed 😇")
            break
        else:
            print("Invalid choice! Choose between 1 and 8.")

if __name__ == "__main__":
    main()