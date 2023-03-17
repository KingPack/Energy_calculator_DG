from django import forms
from .models import ClienteCalculator

class EnergyCalculatorForm(forms.Form):
    consumption_month1 = forms.FloatField(label='Consumption Month 1 (kWh)')
    consumption_month2 = forms.FloatField(label='Consumption Month 2 (kWh)')
    consumption_month3 = forms.FloatField(label='Consumption Month 3 (kWh)')
    tariff = forms.FloatField(label='Tariff')
    tariff_type = forms.ChoiceField(label='Tariff Type',
        choices=[
            ('Residencial', 'Residencial'),
            ('Comercial', 'Comercial'),
            ('industrial', 'Industrial')])


class ClienteCalculatorForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    document = forms.CharField(label='Document', max_length=18)
    consumption = forms.DecimalField(label='Energy Consumption', decimal_places=2)
    tariff = forms.DecimalField(label='Tariff', decimal_places=2)
    code_zip = forms.CharField(label='ZIP Code', max_length=9)
    city = forms.CharField(label='City', max_length=100, disabled=False)
    state = forms.CharField(label='State', max_length=2, disabled=False)
    tariff_type = forms.ChoiceField(label='Tariff Type', 
                choices=[('Residencial', 'Residential'),
                         ('Comercial', 'Commercial'),
                         ('Industrial', 'Industrial')])
    tariff_type_consumption = forms.ChoiceField(label='Tariff Type Consumption', 
                choices=[('low', 'Low'),
                         ('median', 'Median'),
                         ('high', 'High')])


    class Meta:
        model = ClienteCalculator
        fields = ['name', 'document', 'consumption', 'tariff', 'tariff_type',
                  'tariff_type_consumption', 'code_zip', 'city', 'state']
