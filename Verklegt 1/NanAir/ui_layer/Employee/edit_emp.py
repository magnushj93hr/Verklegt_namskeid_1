class EditEmp:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
        
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - n               //Change name                                - g            //Change GSM                    |
|   - h               //Change home address                        - em           //Change email                  |
|   - p               //Change the home phonenumber                - l            //Change location               |
|   - b               //Go back                                                                                   |
|                                                 (can´t change ID)                                               |
|_________________________________________________________________________________________________________________|
"""

#Hvernig viljum við fá þetta uppsett til að geta breytt 