from faker import Faker


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


def create_contact(type_of_contact,number_of_contacts):

    match type_of_contact.lower():
        case  "basic":
            for _ in range(number_of_contacts):
                print((BaseContact(fake.first_name(),fake.last_name(), fake.email(), fake.phone_number())))
        case "business":
            for _ in range(number_of_contacts):
                print((BusinessContact(fake.company(),fake.job(),fake.phone_number(),
                        fake.first_name(),fake.last_name(),fake.email(), fake.phone_number())))
        case '_':
            print("Wrong choice please choose from 'basic' or 'business'")






create_contact("business",3)


