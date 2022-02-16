import collections
from .models import MembershipCategory, Member,Payment
from django.core.files.storage import FileSystemStorage
def fetchUniqueCategoryName(model):
    try:
        obj = model.objects.all()
        ls = []
        for i in obj:
            ls.append(i.category_name)
        return set(ls)
        # return obj
    except model.DoesNotExist:
        return None

def addMemberRecord(request,status):
    # if request.POST.get("photo"):
    if request.FILES:
        f=request.FILES["photo"]
        fs = FileSystemStorage()
        filename = fs.save(f.name, f)
        uploaded_file_url = fs.url(filename)
    else:
        filename="default.png"
    membership_id = MembershipCategory.objects.filter(
                    category_name=request.POST.get("membershipcategory")).filter(
                    category_class=request.POST.get("membership-class")).filter(
                    category_gender=request.POST.get("gender")
                    )[0]
    print(membership_id)
    member_data =Member.objects.create(member_name=request.POST.get("fullname"),
                    member_father_name=request.POST.get("fathername"),
                    member_cnic=request.POST.get("cnicnumber"),
                    member_contact=request.POST.get("contactnumber"),
                    member_emergency_contact=request.POST.get("alternatenumber"),
                    member_email=request.POST.get("email"),
                    member_occupation=request.POST.get("occupation"),
                    member_address=request.POST.get("address"),
                    member_gender=request.POST.get("gender"),
                    member_dob=request.POST.get("dateofbirth"),
                    member_age=request.POST.get("age"),
                    member_blood_group=request.POST.get("bloodgroup"),
                    member_height=request.POST.get("height"),
                    member_weight=request.POST.get("weight"),
                    member_card_id=request.POST.get("cardnumber"),
                    member_target=request.POST.get("target"),
                    member_image=filename,
                    member_membership_id=membership_id
                    )
    member_data.save()
    if status:
        payment=Payment.objects.create(member_id=member_data,
                                payment_amount=request.POST.get("amount"),
                                payment_discount=request.POST.get("discount"),
                                payment_payable=request.POST.get("payableamount"),
                                payment_status=request.POST.get("paymentstatus"),
                                payment_paid=0,
                                payment_remaining=0)
        payment.save()
    else:
        payment=Payment.objects.create(member_id=member_data,
                                payment_amount=request.POST.get("amount"),
                                payment_discount=request.POST.get("discount"),
                                payment_payable=request.POST.get("payableamount"),
                                payment_status=request.POST.get("paymentstatus"),
                                payment_paid=request.POST.get("paidamount"),
                                payment_remaining=request.POST.get("remainingamount"),)
        payment.save()




def CustomizeSerializer(query):
    join=Member.objects.raw(query)
    ls=[]
    for i in join:
        ship = [("name", i.member_name),
        ("father_name", i.member_father_name),
        ("cnic", i.member_cnic),
        ("contact", i.member_contact),
        ("emergency_contact", i.member_emergency_contact),
        ("email", i.member_email),
        ("occupation", i.member_occupation),
        ("address", i.member_address),
        ("gender",i.member_gender),
        ('DOB',i.member_dob),
        ("age", i.member_age),
        ("id",i.id),
        ("blood_group", i.member_blood_group),
        ("height", i.member_height),
        ("weight", i.member_weight),
        ("card_id",i.member_card_id),
        ("target",i.member_target),
        ("image",i.member_image.url),
        ("membershp_id",i.member_membership_id.id),
        ("membershp_name",i.member_membership_id.category_name),
        ("membershp_months",i.member_membership_id.category_months),
        ("membershp_gender",i.member_membership_id.category_gender),
        ("membershp_monthly_fee",i.member_membership_id.category_fee),
        ("amount",i.payment_amount),
        ("discount",i.payment_discount),
        ("payable",i.payment_payable),
        ("paid",i.payment_paid),
        ("remaining",i.payment_remaining),
        ("payment_status",i.payment_status),
        ("expiry_date",i.member_membership_expiry_date),
        ("created_at",i.member_created_at)
        ]
        
        ls.append(collections.OrderedDict(ship))
    # print(ls)
    return ls