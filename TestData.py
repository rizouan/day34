import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lesson4prj.settings')
import django
django.setup()

#Faker
import random
from faker import Faker
from lesson4app.models import Employee

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name =fakegen.first_name()
        fake_dob= fakegen.date()
        fake_email=fakegen.email()
        fake_salary=fakegen.random_int()


        st = Employee.objects.get_or_create(name=fake_name, dob= fake_dob, email = fake_email, salary = fake_salary)[0]
        st.save()
    return st

if __name__ == "__main__":
    print('Populate Records')
    populate(20)
    print('Populate Complete')
