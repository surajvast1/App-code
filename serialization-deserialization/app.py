import pickle

class Employee:
    def __init__(self, name, age, salary, married, has_kid):
        self.name = name
        self.age = age
        self.salary = salary
        self.married = married
        self.has_kid = has_kid

    def __str__(self):
        return (f"Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary}, "
                f"Married: {self.married}, Has Kid: {self.has_kid})")

# Step 2: Serialize the Employee object
def serialize_employee(employee, filename):
    with open(filename, "wb") as file:
        pickle.dump(employee, file)
    print(f"Employee object has been serialized and saved to {filename}.")

# Step 3: Deserialize the Employee object
def deserialize_employee(filename):
    with open(filename, "rb") as file:
        employee = pickle.load(file)
    print(f"Employee object has been loaded from {filename}.")
    return employee

# Example usage
if __name__ == "__main__":
    # Create an instance of the Employee class
    employee = Employee("John Doe", 30, 50000, True, True)
    filename = "employee.pkl"

    # Serialize the employee object
    serialize_employee(employee, filename)

    # Deserialize the employee object
    loaded_employee = deserialize_employee(filename)
    print(loaded_employee)



# Explanation of What We're Doing:

# Class Definition: We define the Employee
#  class to encapsulate the employee's details.
# Object Instantiation: We create an instance 
# of Employee with specific details.
# Serialization: We use pickle.dump() to serialize the 
#  Employee object and save it to a file.
# Deserialization: We use pickle.load() to read the
#  serialized object from the file and convert it back into an Employee object.
# Output: We print the deserialized object to ensure
#  it has been correctly restored.
# This process allows us to save and load complex Python 
# objects (like instances of custom classes) to and from files, which is useful for various applications such as saving user settings, game states, or any other type of persistent data.