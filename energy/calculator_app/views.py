import requests

from django.shortcuts import render
from validate_docbr import CPF, CNPJ

from .forms import EnergyCalculatorForm, ClienteCalculatorForm
from .models import ClienteCalculator
from .calculator import calculator


def energy_calculator_view(request):
    if request.method == 'POST':
        form = EnergyCalculatorForm(request.POST)

        if form.is_valid():
            # Get the form data
            consumption_month1 = form.cleaned_data['consumption_month1']
            consumption_month2 = form.cleaned_data['consumption_month2']
            consumption_month3 = form.cleaned_data['consumption_month3']
            tariff = form.cleaned_data['tariff']
            tariff_type = form.cleaned_data['tariff_type']

            result_calculator = calculator(
                    [consumption_month1, consumption_month2, consumption_month3],
                     tariff, tariff_type)

            # Render the results template
            return render(request, 'result.html', {'result_calculator': result_calculator})
    else:
        form = EnergyCalculatorForm()

    return render(request, 'index.html', {'form': form})


def create_cliente(request):

    if request.method == 'POST':
        form = ClienteCalculatorForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            document = form.cleaned_data['document']
            code_zip = form.cleaned_data['code_zip']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            consumption = form.cleaned_data['consumption']
            tariff = form.cleaned_data['tariff']
            tariff_type = form.cleaned_data['tariff_type']
            tariff_type_consumption = form.cleaned_data['tariff_type_consumption']

            # Validate document
            document_validator = CPF() if len(document) == 11 else CNPJ()
            if not document_validator.validate(document):
                form.add_error('document', 'Invalid document number.')

            # Validate ZIP code
            try:
                response = requests.get(f'https://viacep.com.br/ws/{code_zip}/json/')
                data = response.json()

                if 'erro' in data:
                    raise ValueError()
            except:
                form.add_error('code_zip', 'Invalid or nonexistent ZIP code.')

            if form.is_valid():
                # Save form data to database
                cliente = ClienteCalculator(
                    name=name,
                    document=document,
                    code_zip=code_zip,
                    city=city,
                    state=state,
                    consumption=consumption,
                    tariff=tariff,
                    tariff_type=tariff_type,
                    tariff_type_consumption=tariff_type_consumption
                )
                cliente.assert_consumption_value()
                cliente.save()

                return render(request, 'create_cliente_success.html', {'cliente': cliente})

    else:
        form = ClienteCalculatorForm()

    return render(request, 'create_cliente.html', {'form': form})


def cliente_filter(request):
    if request.method == 'GET':
        clientes = ClienteCalculator.objects.all()
        return render(request, 'cliente_filter.html', {'clientes': clientes})

    elif request.method == 'POST':
        document = request.POST.get('document')
        code_zip = request.POST.get('code_zip')
        city = request.POST.get('city')
        state = request.POST.get('state')
        tariff_type = request.POST.get('tariff_type')
        tariff_type_consumption = request.POST.get('tariff_type_consumption')

        clientes = ClienteCalculator.objects.all()

        if request.POST.get('name'):
            clientes = clientes.filter(name__icontains=request.POST.get('name'))
        if document:
            clientes = clientes.filter(document__icontains=document)
        if code_zip:
            clientes = clientes.filter(code_zip__icontains=code_zip)
        if city:
            clientes = clientes.filter(city__icontains=city)
        if state:
            clientes = clientes.filter(state__icontains=state)
        if tariff_type:
            clientes = clientes.filter(tariff_type__icontains=tariff_type)
        if tariff_type_consumption:
            clientes = clientes.filter(tariff_type_consumption__icontains=tariff_type_consumption)

        context = {'clientes': clientes}

        return render(request, 'cliente_list.html', context)