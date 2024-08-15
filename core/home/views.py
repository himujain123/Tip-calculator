from django.shortcuts import render, redirect
from .forms import TipCalculatorForm
from .models import TipCalculation
from decimal import Decimal

def tip_calculator(request):
	if request.method == 'POST':
		form = TipCalculatorForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			
			# Get the selected tip percentage as a Decimal
			tip_percentage = Decimal(request.POST.get('tip_percentage'))
			
			instance.tip_percentage = tip_percentage
			instance.tip_amount = instance.bill_amount * (tip_percentage / Decimal(100))
			instance.total_amount_per_person = (instance.bill_amount + instance.tip_amount) / instance.num_people
			instance.save()
			return redirect('tip_calculator_result')
	else:
		form = TipCalculatorForm()

	return render(request, 'index.html', {'form': form})

def tip_calculator_result(request):
	calculations = TipCalculation.objects.last()
	return render(request, 'result.html', {'calculations': calculations})


# Create your views here.
