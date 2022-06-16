from faker import Faker
from faker.providers import company
from faker.providers import job
from faker.providers import person
from faker.providers import phone_number

fake=Faker()



class BaseContact:
    def __init__(self, first_name,last_name, mail, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
    def introduce(self):
        print(f"Name: {self.first_name}, last name:{self.last_name} E-mail: {self.mail} company: {self.company}")
    @property
    def lenght_of_full_name(self):
        len_of_full_name = len(self.first_name)+len(self.last_name)+1
        return
    def contact(self):
        print(f"We,re contact with {self.first_name} {self.last_name}  the {self.job} of {self.company} e-mail:{self.mail}")
    def __repr__(self):
        return f"Name: {self.first_name}, last name:{self.last_name} E-mail: {self.mail}"



class BussinesContact(BaseContact):
    def __init__(self, company,job):
        super.__init__(self,*args, **kwargs)
        self.company = company
        self.job = job


person_one = 


