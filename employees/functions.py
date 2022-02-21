from .models import EmployeeRecord


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
                    employee_contact=request.POST.get('emp-contact'), employee_image=filename,
                    employee_cnic=request.POST.get('emp-cnic'), employee_email=request.POST.get('emp-email'),
                    employee_address=request.POST.get('emp-address'), employee_gender=request.POST.get('emp-gender'),
                    employee_dob=request.POST.get('emp-dob'), employee_age=request.POST.get('emp-age'),
                    employee_blood_group=request.POST.get('emp-blood-group'), employee_type=request.POST.get('emp-type'),
                    employee_username=request.POST.get('emp-username'), employee_password=request.POST.get('emp-password'),
                    employee_pay= request.POST.get('emp-pay'), employee_status=request.POST.get('emp-status'))

        employee_data.save()

        return employee_data
    except Exception as e:
        print("Employee error ", e)
        return False