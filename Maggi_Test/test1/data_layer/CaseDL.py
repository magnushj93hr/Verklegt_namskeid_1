import csv
import shutil
from tempfile import NamedTemporaryFile

from models.Case import Case

class CaseDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Case.csv"
    
    def get_all_cases(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                case = Case(row["id"],row["location"], row["subject"], row["description"], row["priority"], row["due date"], row["repeated"], row['date'])
                ret_list.append(case)
        return ret_list

    def create_case(self, case):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "location", "subject","description","priority",'due date','repeated','date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': case.id,'location': case.location, 'subject': case.subject, "description": case.description, "priority": case.priority, 'due date': case.due_date, 'repeated': case.repeated, 'date': case.date})
            
    def check_if_case_exists(self, id):
            with open(self.filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['id'] == id:
                        return True
                    else:
                        return False

    def edit_case(self, case):
        temp_file = NamedTemporaryFile(mode = 'w', delete=False)
        
        fieldnames = ["id","location","subject","description",'priority','due date','repeated','date']
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile, temp_file:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            #fieldnames = ["name","id","address",'homeline','email','location','phone']
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            # writer.writeheader()

            for row in reader:
                if row['id'] == case.id:
                    print('updating row', row['id'])
                    writer.writerow({'id': case.id,'location': case.location, "subject": case.subject, "description": case.description, 'priority': case.priority, 'due date': case.due_date, 'repeated': case.repeated, 'date': case.date})
                else:
                    row = {'id': row['id'],'location': row["location"], 'subject': row['subject'], 'description': row['description'], 'priority': row['priority'], 'due date': row['due date'], 'repeated': row['repeated'], 'date': row['date']}
                    writer.writerow(row)

        shutil.move(temp_file.name, self.filepath)