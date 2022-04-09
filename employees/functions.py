import email
from .models import EmployeeRecord
# from theme.functions import NoneValue
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def NoneValue(value):
    if value=="":
        return None
    else:
        return value

def CreateAdminUserFirst():
    try:
        if EmployeeRecord.objects.filter(user__is_superuser=True).exists():
            print("admin exists")
            return False
        else:
            print("super user not exists")
            user=User.objects.create(first_name='admin',username="admin",password=make_password('admin'),is_superuser=True,email="")
            EmployeeRecord.objects.create(
                employee_contact="1234567890",
                employee_image="default.png",
                employee_cnic=None,
                employee_address=None,
                employee_gender="Male",
                employee_dob=None,
                employee_age=None,
                employee_blood_group="",
                employee_type="Active",
                employee_pay=0,
                user=user,
            ).save()
            return True
    except Exception as e:
        print("Admin error ", e)
def addEmployee(request):
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"

        employee_data = EmployeeRecord.objects.create(employee_name=request.POST.get('emp-name'),
                    employee_contact=request.POST.get('emp-contact'),
                    employee_image=filename,
                    employee_cnic=NoneValue(request.POST.get('emp-cnic')),
                    employee_email=NoneValue(request.POST.get('emp-email')),
                    employee_address=NoneValue(request.POST.get('emp-address')),
                    employee_gender=request.POST.get('emp-gender'),
                    employee_dob=NoneValue(request.POST.get('emp-dob')),
                    employee_age=NoneValue(request.POST.get('emp-age')),
                    employee_blood_group=NoneValue(request.POST.get('emp-blood-group')),
                    employee_type=request.POST.get('emp-type'),
                    employee_username=NoneValue(request.POST.get('emp-username')),
                    employee_password=NoneValue(request.POST.get('emp-password')),
                    employee_pay= request.POST.get('emp-pay'),
                    employee_status=request.POST.get('emp-status'))

        employee_data.save()

        return employee_data
    except Exception as e:
        print("Employee error ", e)
        return False