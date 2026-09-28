import unittest
from patient import Patient

class TestPatientManagement(unittest.TestCase):
    def test_patient_creation(self):
        p = Patient(101, "Alice", 30, "Flu")
        self.assertEqual(p.pid, 101)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.charges, 0)

    def test_add_charges(self):
        p = Patient(101, "Alice", 30, "Flu")
        p.add_charges(150.50)
        self.assertEqual(p.charges, 150.50)

    def test_serialization(self):
        p = Patient(102, "Bob", 45, "Fever", 200.0)
        d = p.to_dict()
        p2 = Patient.from_dict(d)
        self.assertEqual(p2.pid, 102)
        self.assertEqual(p2.charges, 200.0)

if __name__ == "__main__":
    unittest.main()