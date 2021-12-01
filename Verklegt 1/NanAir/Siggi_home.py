from data_layer.EmployeeDL import EmployeeDL


class HomeSiggi:
    def __init__(self):
        self.options = """
\t- 1\t\t//list all employees
\t- 2\t\t//create a new employee
"""

    def options_print(self):
        print(self.options)
        self.input_prompt()

    def input_prompt(self):
        command = input("Go to: ")
        while True:
            if command == "1":
                emp = EmployeeDL()
                emp.load_employee_from_file()
            elif command == "2":
                pass
            elif command == "q":
                return
            else:
                print("Invalid menu")