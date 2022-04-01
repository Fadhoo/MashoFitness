from .models import RentalData, rentalPayment


def null_check(value):
    if value=="":
        return None
    else:
        return value

def addRental(request):
    try:

        add_rental = RentalData.objects.create(Full_name=request.POST.get('full-name'), contact_no=request.POST.get('contact-no'), 
                    cnic_no=null_check(request.POST.get('cnic-no')), reference=null_check(request.POST.get('reference')), 
                    shop_no=request.POST.get('shop-flat-no'), electric_bill=null_check(request.POST.get('electric-bill')),
                    gas_bill=null_check(request.POST.get('gas-bill')),
                    rent_pay_to=request.POST.get('rent-pay-to'), rent_pay_by=request.POST.get('rent-pay-from'),
                    description=null_check(request.POST.get('description')))
        add_rental.save()

        payment= rentalPayment.objects.create(rent_amount=request.POST.get('rent-amount'), payment_mode=null_check(request.POST.get('payment-mode')),
                    rent_pay_date=request.POST.get('rent-pay-date'), rent_duration=request.POST.get('rent-duration'),
                    total_rent=request.POST.get('total-rent'), rent_end_date=request.POST.get('rent-end-date'),
                    payment_status=request.POST.get('payment-status'), rental_id=add_rental)
        payment.save()
        print("successfully added")
                    
    except Exception as e:
        print("Error In Add Rental: ", e)



def editRental(request):
    try:
        print(request.POST.get('rental-id'))
        update_rental = RentalData.objects.filter(id=request.POST.get('rental-id')).update(Full_name=request.POST.get('full-name'), contact_no=request.POST.get('contact-no'), 
                    cnic_no=null_check(request.POST.get('cnic-no')), reference=null_check(request.POST.get('reference')), 
                    shop_no=request.POST.get('shop-flat-no'), electric_bill=null_check(request.POST.get('electric-bill')),
                    gas_bill=null_check(request.POST.get('gas-bill')),
                    rent_pay_to=request.POST.get('rent-pay-to'), rent_pay_by=request.POST.get('rent-pay-from'),
                    description=null_check(request.POST.get('description')))

        rentalPayment.objects.filter(rental_id=update_rental.id).update(rent_amount=request.POST.get('rent-amount'), payment_mode=null_check(request.POST.get('payment-mode')),
                    rent_pay_date=request.POST.get('rent-pay-date'), rent_duration=request.POST.get('rent-duration'),
                    total_rent=request.POST.get('total-rent'), rent_end_date=request.POST.get('rent-end-date'),
                    payment_status=request.POST.get('payment-status'))

    except Exception as e:
        print("Error In Update Rental: ", e)
