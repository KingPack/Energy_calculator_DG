from django.db import models


class ClienteCalculator(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    code_zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    consumption = models.DecimalField(max_digits=14, decimal_places=2)
    tariff = models.DecimalField(max_digits=14, decimal_places=2)
    tariff_type = models.CharField(max_length=20)
    applied_discount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    coverage = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    tariff_type_consumption = models.CharField(
        max_length=10,
        default='',
        choices=[
            ('low', 'Low'),
            ('median', 'Median'),
            ('high', 'High')
        ]
    )

    def __str__(self):
        return self.name

    def assert_consumption_value(self):
        if self.tariff_type_consumption == 'low':
            self.coverage = 0.90
            if self.tariff_type_consumption == 'Residencial':
                self.applied_discount = 0.18
            elif self.tariff_type_consumption == 'Comercial':
                self.applied_discount = 0.16
            elif self.tariff_type_consumption == 'Industrial':
                self.applied_discount = 0.12
        elif self.tariff_type_consumption == 'median':
            self.coverage = 0.95
            if self.tariff_type_consumption == 'Residencial':
                self.applied_discount = 0.22
            elif self.tariff_type_consumption == 'Comercial':
                self.applied_discount = 0.18
            elif self.tariff_type_consumption == 'Industrial':
                self.applied_discount = 0.15
        else:
            self.coverage = 0.99
            if self.tariff_type_consumption == 'Residencial':
                self.applied_discount = 0.25
            elif self.tariff_type_consumption == 'Comercial':
                self.applied_discount = 0.22
            elif self.tariff_type_consumption == 'Industrial':
                self.applied_discount = 0.18


# class Tariff(models.Model):
#     """
#     TODO: Escrever regra de negocio sobre a tarifa
#     1. valor low, median e high vao receber os valores de desconto
#     """

#     tariff_type = models.CharField(
#         max_length=20,
#         choices=[
#         ('Residencial', 'Residential'),
#         ('Comercial', 'Commercial'),
#         ('Industrial', 'Industrial'),
#     ],
#         default='')
#     tariff_type_consumption = models.CharField(
#         max_length=10,
#         choices=[('low', 'Low'),
#                  ('median', 'Median'),
#                  ('high', 'High'),
#     ],
#         default='')
#     coverage = models.DecimalField(max_digits=5, decimal_places=2)
#     low_consumption_tariff = models.DecimalField(max_digits=5, decimal_places=2)
#     median_consumption_tariff = models.DecimalField(max_digits=5, decimal_places=2)
#     high_consumption_tariff = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"{self.tariff_type} {self.tariff_type_consumption}"
