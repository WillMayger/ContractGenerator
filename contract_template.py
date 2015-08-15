from docx import Document
from datetime import datetime


class ContractGenerator:

    def __init__(self, client_name, client_address, client_town, client_country, client_postcode,
                 service_provider_name, service_provider_address, service_provider_town,
                 service_provider_country, service_provider_postcode):

        # date time
        now = datetime.now()
        if 4 <= now.day.__int__() <= 20 or 24 <= now.day.__int__() <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][now.day.__int__() % 10 - 1]

        self.date = now.day.__str__() + suffix
        self.month = now.month.__str__()
        self.year = now.year.__str__()

        # client info
        self.client_name = client_name
        self.client_address = client_address
        self.client_town = client_town
        self.client_country = client_country
        self.client_postcode = client_postcode

        # service provider info
        self.service_provider_name = service_provider_name
        self.service_provider_address = service_provider_address
        self.service_provider_town = service_provider_town
        self.service_provider_country = service_provider_country
        self.service_provider_postcode = service_provider_postcode

        # new instance of Document
        self.contract = Document()

    def heading(self):
        self.contract.add_heading('GENERAL SERVICE AGREEMENT', 0)
        self.contract.add_heading(
            'THIS GENERAL SERVICE AGREEMENT (the "Agreement") dated this {0} day of {1}, {2}'.format(
                self.date, self.month, self.year
            ), 1)

    def agreement(self):

        self.contract.add_heading(
            'BETWEEN', 2)

        p = self.contract.add_paragraph(
            '{0} of {1}, {2}, {3},\n {4} \n (the "Customer")'.format(
                self.client_name, self.client_address, self.client_town, self.client_country,
                self.client_postcode
            ))

        self.contract.add_heading(
            '- AND -', 2)

        self.contract.add_paragraph(
            '{0} of {1}, {2}, {3},\n {4} \n (the "Service Provider")'.format(
                self.service_provider_name, self.service_provider_address,
                self.service_provider_town, self.service_provider_country,
                self.service_provider_postcode
            ))

    def save(self):

        self.contract.save('contract.docx')


cg = ContractGenerator("Mr Example", "93 london drive", "camden", "london", "LON DON",
                       "Mr Company Example", "93 Company drive", "Regents Place", "London", "LON DON")
cg.heading()
cg.agreement()
cg.save()
