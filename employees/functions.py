from optparse import check_choice
from .models import EmployeeRecord
from theme.functions import null_check
from django.core.files.storage import FileSystemStorage

def check_admin():
    if EmployeeRecord.objects.filter(super_user=True).exists():
        print("admin exists")
        return False
    else:
        print("super user not exists")
        EmployeeRecord.objects.create(
            employee_name="Admin",
            employee_contact="1234567890",
            employee_image="default.png",
            employee_cnic=None,
            employee_email=None,
            employee_address=None,
            employee_gender="Male",
            employee_dob=None,
            employee_age=None,
            employee_blood_group="",
            employee_type="Active",
            employee_username="Admin",
            employee_password="Admin123",
            employee_pay=0,
            super_user=True,
        ).save()
        return True
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
                    employee_cnic=null_check(request.POST.get('emp-cnic')),
                    employee_email=null_check(request.POST.get('emp-email')),
                    employee_address=null_check(request.POST.get('emp-address')),
                    employee_gender=request.POST.get('emp-gender'),
                    employee_dob=null_check(request.POST.get('emp-dob')),
                    employee_age=null_check(request.POST.get('emp-age')),
                    employee_blood_group=null_check(request.POST.get('emp-blood-group')),
                    employee_type=request.POST.get('emp-type'),
                    employee_username=null_check(request.POST.get('emp-username')),
                    employee_password=null_check(request.POST.get('emp-password')),
                    employee_pay= request.POST.get('emp-pay'),
                    employee_status=request.POST.get('emp-status'))

        employee_data.save()

        return employee_data
    except Exception as e:
        print("Employee error ", e)
        return False