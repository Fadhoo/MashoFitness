from .models import expensesData

def addExpense(request):
    try:
        add_data = expensesData.objects.create(
                date=request.POST.get('date'),
                account_head=request.POST.get('account-head'),
                paid_amount=request.POST.get('amount-paid'),
                payment_mode=request.POST.get('payment-mode'),
                expenses_for=request.POST.get('expense-for'),
                receipent_name=request.POST.get('receipent'),
                description=request.POST.get('description'),
                comments=request.POST.get('comment'),)

        add_data.save()
        print("Added expense")
        return add_data
    except Exception as e:
        print("expense error", e)
        return False

