from faker import Faker
import time

fake=Faker()



class BaseContact:
    def __init__(self, first_name,last_name, mail, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.phone_number = phone_number


    def introduce(self):
        print(f"Name: {self.first_name}, last name:{self.last_name} E-mail: {self.mail} company: {self.company}")


    @property
    def label_length(self):
        len_of_full_name = len(self.first_name)+len(self.last_name)+1
        return len_of_full_name
    def contact(self):
        return f"We,re calling {self.phone_number} - {self.first_name} {self.last_name},  e-mail:{self.mail}"
    @property


    def __str__(self):
        return f"{self.first_name} {self.last_name} e-mail:{self.mail} phone number: {self.phone_number} "



class BusinessContact(BaseContact):
    def __init__(self,company, job, business_phone_number, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.company = company
        self.job = job
        self.business_phone_number = business_phone_number


    def contact(self):
        return f"We,re contact with {self.first_name} {self.last_name} business phone number: {self.phone_number} the {self.job} of the company: {self.company} " \
               f"e-mail:{self.mail}"


    def __str__(self):
        return f"{self.first_name} {self.last_name} the {self.job} of the {self.company}, " \
               f"business phone number: {self.business_phone_number} e-mail:{self.mail}"




def function_performance(func):
    def time_of_one_performance():
        total_performance_time = 0
        start_performance = time.perf_counter()
        print(func())
        end_performance = time.perf_counter()
        total_performance_time = total_performance_time + (end_performance - start_performance)
        print (total_performance_time)
    return time_of_one_performance



def create_contact(type_of_contact : str):
    list_of_contacts = []
    match type_of_contact.lower():
        case  "basic":
                contact = BaseContact(fake.first_name(),fake.last_name(), fake.email(), fake.phone_number())
        case  "business":
                contact = BusinessContact(fake.company(),fake.job(),fake.phone_number(),
                        fake.first_name(),fake.last_name(),fake.email(), fake.phone_number())
        case '_':
            return "Wrong choice please choose from 'basic' or 'business'"
    return contact



first_id = BusinessContact(fake.company(),fake.job(),fake.phone_number(),
                        fake.first_name(),fake.last_name(),fake.email(), fake.phone_number())

print(type(first_id))


print(create_contact("business"))




contacts = [create_contact("basic") for _ in range(1000)]
print (contacts)






#styl dwie linij