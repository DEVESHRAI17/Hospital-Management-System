class Patient:
    def __init__(self, pid, name, age, disease, charges=0.0):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.charges = charges

    def add_charges(self, amount):
        self.charges += amount

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
            "charges": self.charges
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            pid=data["pid"],
            name=data["name"],
            age=data["age"],
            disease=data["disease"],
            charges=data.get("charges", 0.0)
        )

    def display(self):
        print(f"{self.pid}\t{self.name}\t{self.age}\t{self.disease}\tRs. {self.charges:.2f}")