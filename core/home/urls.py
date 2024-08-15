from django.urls import path
from .views import tip_calculator, tip_calculator_result

urlpatterns = [
	path('tip_calculator/', tip_calculator, name='tip_calculator'),
	path('tip_calculator_result/', tip_calculator_result, name='tip_calculator_result'),
]
