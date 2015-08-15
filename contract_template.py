from docx import Document
from datetime import datetime


class ContractGenerator:

    def __init__(self, client_name, client_address, client_town, client_country, client_postcode,
                 service_provider_name, service_provider_address, service_provider_town,
                 service_provider_country, service_provider_postcode, service_provided, currency,
                 cost):

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

        # currency
        self.currency_letters = currency

        # cost
        self.cost = cost

        # service provider info
        self.service_provider_name = service_provider_name
        self.service_provider_address = service_provider_address
        self.service_provider_town = service_provider_town
        self.service_provider_country = service_provider_country
        self.service_provider_postcode = service_provider_postcode
        self.service_provided = service_provided

        # new instance of Document
        self.contract = Document()

    def heading(self):
        self.contract.add_heading('GENERAL SERVICE AGREEMENT', 0)
        self.contract.add_heading(
            'THIS GENERAL SERVICE AGREEMENT (the "Agreement") dated this {0} day of {1}, {2}'.format(
                self.date, self.month, self.year
            ), 1)

    # first part of the contract document adding the addresses
    def client_and_service_info(self):

        self.contract.add_heading(
            'BETWEEN', 2)

        self.contract.add_paragraph(
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

    def background(self):
        self.contract.add_heading(
            'BACKGROUND:', 2)

        self.contract.add_paragraph(
            '1. The Customer is of the opinion that the Service Provider has the necessary qualifications,' +
            ' experience and abilities to provide services to the Customer.'
            )
        self.contract.add_paragraph(
            '2. The Service Provider is agreeable to providing such services to the Customer on the terms' +
            ' and conditions set out in this Agreement.'
            )

    def in_consideration_of(self):

        self.contract.add_heading(
            'IN CONSIDERATION OF:', 2)

        self.contract.add_paragraph(
            'IN CONSIDERATION OF the matters described above and of the mutual benefits and obligations set' +
            ' forth in this Agreement, the receipt and sufficiency of which consideration is hereby acknowledged,' +
            ' the Customer and the Service Provider (individually the "Party" and collectively the "Parties" to ' +
            'this Agreement) agree as follows:'
            )

        self.contract.add_heading(
            '1. Services Provided\n',
            6)

        self.contract.add_paragraph(
            '2. The Customer hereby agrees to engage the Service Provider to provide the Customer with services'
            ' (the "Services") consisting of:'
            )

        self.contract.add_paragraph(
            '  2.1 ' + self.service_provided
        )

        self.contract.add_paragraph(
            '3. The Services will also include any other tasks which the Parties may agree on.' +
            ' The Service Provider hereby agrees to provide such Services to the Customer.'
        )

    def terms_of_agreement(self):

        self.contract.add_heading(
            'Term of Agreement:\n', 3)

        self.contract.add_paragraph(
            '1. The term of this Agreement (the "Term") will begin on the date of this Agreement and will remain ' +
            'in full force and effect until the completion of the Services, subject to earlier termination as ' +
            'provided in this Agreement. The Term of this Agreement may be extended by mutual written agreement ' +
            'of the Parties.'
            )

        self.contract.add_paragraph(
            '2. In the event that either Party wishes to terminate this Agreement, that Party will be required ' +
            'to provide 3 days notice to the other Party.'
            )

    def performance(self):

        self.contract.add_heading(
            'Performance:\n', 3)

        self.contract.add_paragraph(
            '1. The Parties agree to do everything necessary to ensure that the terms of this Agreement take effect.'
            )

    def currency(self):

        self.contract.add_heading(
            'Currency:\n', 3
        )

        self.contract.add_paragraph(
            '1. Except as otherwise provided in this Agreement, all monetary amounts referred' +
            ' to in this Agreement are in {0}.'.format(self.currency)
        )

    def compensation(self):

        self.contract.add_heading(
            'Compensation:\n', 3
        )

        self.contract.add_paragraph(
            '1. For the services rendered by the Service Provider as required by this Agreement, ' +
            'the Customer will provide compensation (the "Compensation") to the Service Provider ' +
            'of a fixed amount of ' +
            '163'.encode() +
            ' {0}.'.format(self.cost)
        )

    def save(self):

        self.contract.save('contract.docx')


cg = ContractGenerator("Mr Example", "93 london drive", "camden", "london", "LON DON",
                       "Mr Company Example", "93 Company drive", "Regents Place", "London", "LON DON",
                       "Responsive Website Development with up to date responsive devices to work across all devices.",
                       "GBP", "100000.00")
cg.heading()
cg.client_and_service_info()
cg.background()
cg.in_consideration_of()
cg.terms_of_agreement()
cg.performance()
cg.currency()
cg.compensation()
cg.save()
