import csv

from models.Case import Case

class CaseDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Case.csv"
    
    def get_all_cases(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                case = Case(row["subject"], row["description"], row["priority"], row["due date"], row["repeated"])
                ret_list.append(case)
        return ret_list

    def create_case(self, case):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["subject","description","priority",'due date','repeated']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'subject': case.subject, "description": case.description, "priority": case.priority, 'due date': case.due_date, 'repeated': case.repeated})