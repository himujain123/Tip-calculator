from django import forms
from .models import TipCalculation

class TipCalculatorForm(forms.ModelForm):
	class Meta:
		model = TipCalculation
		fields = ['bill_amount', 'num_people']

	tip_percentage = forms.ChoiceField(choices=[(5, '5%'), (10, '10%'), (15, '15%'), (25, '25%')], widget=forms.RadioSelect)
