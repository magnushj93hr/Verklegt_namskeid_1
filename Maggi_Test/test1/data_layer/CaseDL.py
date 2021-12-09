import csv
import shutil
from tempfile import NamedTemporaryFile

from models.Case import Case

class CaseDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Case.csv"
     
    def get_all_cases(self):
        """Returns a list of all cases"""

        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                case = Case(row["id"],row["location"], row["subject"], row["description"], row["priority"], row["repeated"], row["repeat_days"], row['real_est_id'], row['emp_id'] ,row['date'], row['status'], row['closed_date'])
                ret_list.append(case)
        return ret_list

    def create_case(self, case):
        """Takes in information you need to create a case. The information will 
        be stored in a Case.csv file"""

        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "location", "subject","description","priority",'repeated', "repeat_days", "real_est_id", 'emp_id', 'date', 'status', 'closed_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': case.id,'location': case.location, 'subject': case.subject, "description": case.description, "priority": case.priority, 'repeated': case.repeated, "repeat_days": case.repeat_days, "real_est_id": case.real_est_id, 'emp_id': case.emp_id, 'date': case.date, 'status': case.status, 'closed_date': case.closed_date})

    def check_if_case_exists(self, id):
        """Takes in the case id and checks if it exists, returns true if it exists else false"""

        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == id:
                    return True
                else:
                    return False

    def edit_case(self, case):
        """Takes in case information and updates it """

        temp_file = NamedTemporaryFile(mode = 'w', newline='', encoding='utf-8', delete=False)
        
        fieldnames = ["id","location","subject","description",'priority','repeated', "repeat_days", 'real_est_id', 'emp_id', 'date', 'status', 'closed_date']
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile, temp_file:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)

            for row in reader:
                if row['id'] == case.id:
                    print('updating row', row['id'])
                    writer.writerow({'id': case.id,'location': case.location, "subject": case.subject, "description": case.description, 'priority': case.priority, 'repeated': case.repeated, "repeat_days": case.repeat_days, 'real_est_id': row['real_est_id'], 'emp_id': row['emp_id'], 'date': row['date'], "status": case.status, 'closed_date': case.closed_date})
                else:
                    row = {'id': row['id'],'location': row["location"], 'subject': row['subject'], 'description': row['description'], 'priority': row['priority'], 'repeated': row['repeated'], "repeat_days": row["repeat_days"], 'real_est_id': row['real_est_id'], 'emp_id': row['emp_id'], 'date': row['date'], "status": row['status'], 'closed_date': row['closed_date']}
                    writer.writerow(row)

        shutil.move(temp_file.name, self.filepath)