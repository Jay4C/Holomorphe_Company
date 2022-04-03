from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'contents/index.html')


def international_energy(request):
    return render(request, "contents/international_energy.html")


def international_free_trade_agreements(request):
    return render(request, "contents/international_free_trade_agreements.html")


def international_lands_for_injecting_gas(request):
    return render(request, "contents/international_lands_for_injecting_gas.html")


def international_electricity_generation_without_license(request):
    context = {
        "dataEurope": [
            {'k1': 'Albania', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Germany', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Andorra', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Austria', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Belgium', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 5 Mws / Hydrogen', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Bielorussia / Belarus', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Bosnia Herzegovine', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Bulgarie', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 5 MW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Chyprus', 'k2': '90000,00 €', 'k3': '3', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Croatia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Danmark', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Spain', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 250 kW / any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Estonia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 100 kW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Finland', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'France', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 50 Mws / Hydrogen', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Greece', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 20 kW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Hungary', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 50 MW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Ireland', 'k2': '100000,00 €', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Iceland', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Hydrogen', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Italy', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Lettonie', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'Yes'},
            {'k1': 'Liechtenstein', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Lithuania', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'Yes'},
            {'k1': 'Luxembourg', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 50 kW / Hydrogen', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'North Macedoine', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Malta', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Moldova', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 20 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Monaco', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Montenegro', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited powers / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Norway', 'k2': '?', 'k3': '1', 'k4': 'No', 'k5': 'Yes', 'k6': 'Yes'},
            {'k1': 'The Netherlands', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 500 Mws / Hydrogen', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Poland', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Portugal', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'Yes'},
            {'k1': 'Republic Tcheque', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Roumania', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'England', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 100 Mws / Hydrogen', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Russia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'San Marino', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Serbia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Slovakia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Slovenia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Sweden', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Switzerland', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'Yes'},
            {'k1': 'Ukraine', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 5 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Vatican', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'Yes'},
            {'k1': 'Guernesey', 'k2': '2500000,00 €', 'k3': '5', 'k4': '?', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Isle of Man', 'k2': '5000,00 €', 'k3': '0', 'k4': '?', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Jersey island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Kosovo', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited powers / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Ile Aland', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Faroe Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Gibraltar', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Svalbard', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Akrotiri and Dhekelia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'North Chyprus', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Transnistria', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'}
                    ],
        "dataAsia": [
            {'k1': 'Afghanistan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Saudi Arabia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Armenia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Azerbaïdjan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Bahrain', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Bangladesh', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Bhutan', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 500 kW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Myanmar', 'k2': 'Three hundred thousand kyats to a maximum of one million kyats', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Brunei', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Cambodia', 'k2': '400,000 Riels to 4,000,000 Riels per day for every day ', 'k3': '1 to 3 years', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'China', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'North Korea', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'South Korea', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'United Arab Emirates', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Georgia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'India', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Indonesia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Iraq', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Iran', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Israel', 'k2': '?', 'k3': '3', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Japan', 'k2': '1 million yen', 'k3': '5', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Jordan', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Kazakhstan', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Kyrgyzstan', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Kuwait', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Laos', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Lebanon', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Malaysia', 'k2': '100 thousand ringgit', 'k3': '5', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'The Maldives', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Mongolia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1,5 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Nepal', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Oman', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 25 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Uzbekistan', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Pakistan', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Palestine', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Philippines', 'k2': 'Fifty million pesos ', 'k3': '2', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Qatar', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Singapore', 'k2': '$500,000', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Sri Lanka', 'k2': 'A fine not less than one hundred thousand rupees and not exceeding ten million rupees', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Syria', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Tajikistan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Thailand', 'k2': '0,00 €', 'k3': '2', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Timor Leste', 'k2': 'a fine of US$ 500 to US$ 5,000 or of US$ 5,000 to US$ 50,000,', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Turkmenistan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Vietnam', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Yemen', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Kurdistan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Tibet', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Ryūkyū', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Christmas island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Cocos island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Hong Kong', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Macao', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Abkhazie', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Haut-Karabagh', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'South Ossetia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Taiwan', 'k2': 'NT$200,000 to NT$2,000,000', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'}
        ],
        "dataAfrica": [
            {'k1': 'South Africa', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Algeria', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 25 MW with declaration / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Angola', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Benin', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Botswana', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 25 kW / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Burkina Faso', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Burundi', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Cameroon', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 100 kW / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Cape Verde', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Central African Republic', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Comoros', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Republic of Congo', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Democratic Republic Of The Congo', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Ivory coast', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Djibouti', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Egypt', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Eritrea', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Ethiopia', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Eswatini', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Gabon', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Gambia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Ghana', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Guinea', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Guinea Bissau', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Equatorial Guinea', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Kenya', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Lesotho', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Liberia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Libya', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Madagascar', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Malawi', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Mali', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Morocco', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Mauritius', 'k2': '100,000 rupees', 'k3': '5', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Mauritania', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Mozambique', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Namibia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Niger', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Nigeria', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Uganda', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 0,5 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Rwanda', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Sao Tome And Principe', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Senegal', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Sierra Leone', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Somalia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Sudan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'South Sudan', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Tanzania', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Tchad', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Togo', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Tunisia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Zambia', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Zimbabwe', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 100 kW / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Seychelles', 'k2': 'SCR 200,000', 'k3': '2', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'}
        ],
        "dataAmerica": [
            {'k1': 'Antigua And Barbuda', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Argentina', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Bahamas', 'k2': '2000,00 €', 'k3': '2', 'k4': 'Yes up to 250 kW / any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Barbados', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 5 kW / any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Belize', 'k2': '5000,00 €', 'k3': '1', 'k4': 'Yes up to 75 kW / any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Bolivia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Brazil', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 50 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Canada', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Chile', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Colombia', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to 1 MW / Any devices', 'k5': 'No', 'k6': 'No'},
            {'k1': 'Costa Rica', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Cuba', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Dominican Republic', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Dominique', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Ecuador', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Usa', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Grenada', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Guatemala', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Guyana', 'k2': '50000,00 €', 'k3': '5', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Haiti', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Honduras', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Jamaica', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Mexcio', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Panama', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Nicaragua', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Paraguay', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Peru', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Saint Kitts And Nevis', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Saint Lucia', 'k2': '5000,00 €', 'k3': '1', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Saint Vincent And The Grenadines', 'k2': '750,00 €', 'k3': '1', 'k4': 'No', 'k5': 'Yes',
             'k6': 'No'},
            {'k1': 'El Salvador', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Suriname', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Trinidad And Tobago', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Uruguay', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Venezuela', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Puerto Rico', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'American Virgin Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Galápagos island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Archipel of San Andrés, Providencia and Santa Catalina', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?',
             'k6': 'No'},
            {'k1': 'Navasse island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Cayman Islands', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Greenland', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Turks And Caicos Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'British Virgin Islands', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Caribbean Netherlands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Anguilla', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Aruba', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Montserrat', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Clipperton island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Bermuda', 'k2': '50000,00 €', 'k3': '5', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Curaçao', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Bonaire', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Malouines island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Saba', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'San Eustache', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'}
        ],
        "dataOceania": [
            {'k1': 'Australia', 'k2': '20000,00 €', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Fiji', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Kiribati', 'k2': '?', 'k3': '?', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Marshall Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Federated States Of Micronesia', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Nauru', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'New Zealand', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices',
             'k5': 'No', 'k6': 'No'},
            {'k1': 'Palau', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Papua New Guinea',
             'k2': 'Penalty: A fine not exceeding K10,000,000.00. Default penalty: A fine not exceeding K1,000,000', 'k3': '0', 'k4': 'No', 'k5': 'Yes', 'k6': 'No'},
            {'k1': 'Solomon Islands', 'k2': '50 euros per day of offences', 'k3': '0', 'k4': 'No', 'k5': 'Yes',
             'k6': 'No'},
            {'k1': 'Samoa', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Tonga', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Vanuatu', 'k2': '0,00 €', 'k3': '0', 'k4': 'Yes up to unlimited power / Any devices', 'k5': 'No',
             'k6': 'No'},
            {'k1': 'Tuvalu', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Cook Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Niue', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Northern Mariana Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Norfolk Island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Guam', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Hawaï', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Atoll Johnston', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Atoll Palmyra', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Gambier island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Midway island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Pitcairn Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Chatham island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Tuamotu island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'American Samoa', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Tokelau', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Paques island', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Falkland Islands', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?', 'k6': 'No'},
            {'k1': 'Saint Helena  Ascension And Tristan Da Cunha', 'k2': '?', 'k3': '?', 'k4': '?', 'k5': '?',
             'k6': 'No'}
        ]
    }
    return render(request, "contents/international_electricity_generation_without_license.html", context)


def countries_with_gas_networks(request):
    context = {
        'data': [
            {'k1': 'Albania', 'k2': 'Yes'},
            {'k1': 'Andorra', 'k2': 'No'},
            {'k1': 'Armenia', 'k2': 'Yes'},
            {'k1': 'Austria', 'k2': 'Yes'},
            {'k1': 'Azerbaïdjan', 'k2': 'Yes'},
            {'k1': 'Bielorussia / Belarus', 'k2': 'Yes'},
            {'k1': 'Bosnia Herzegovine', 'k2': 'Yes'},
            {'k1': 'Bulgaria', 'k2': 'Yes'},
            {'k1': 'Croatia', 'k2': 'Yes'},
            {'k1': 'Cyprus', 'k2': 'No'},
            {'k1': 'Republic of Tcheque', 'k2': 'Yes'},
            {'k1': 'Danemark', 'k2': 'Yes'},
            {'k1': 'Estonia', 'k2': 'Yes'},
            {'k1': 'Finland', 'k2': 'Yes'},
            {'k1': 'Georgia', 'k2': 'Yes'},
            {'k1': 'Germany', 'k2': 'Yes'},
            {'k1': 'Hungary', 'k2': 'Yes'},
            {'k1': 'Iceland', 'k2': 'No'},
            {'k1': 'Ireland', 'k2': 'Yes'},
            {'k1': 'Italy', 'k2': 'Yes'},
            {'k1': 'Kazakhstan', 'k2': 'Yes'},
            {'k1': 'Lettonie', 'k2': 'No'},
            {'k1': 'Liechtenstein', 'k2': 'Yes'},
            {'k1': 'Lithuania', 'k2': 'Yes'},
            {'k1': 'North Macedoine', 'k2': 'Yes'},
            {'k1': 'Malta', 'k2': 'No'},
            {'k1': 'Moldova', 'k2': 'Yes'},
            {'k1': 'Montenegro', 'k2': 'No'},
            {'k1': 'The Netherlands', 'k2': 'Yes'},
            {'k1': 'Norway', 'k2': 'Yes'},
            {'k1': 'Poland', 'k2': 'Yes'},
            {'k1': 'Roumania', 'k2': 'Yes'},
            {'k1': 'San Marino', 'k2': 'No'},
            {'k1': 'Serbia', 'k2': 'Yes'},
            {'k1': 'Slovakia', 'k2': 'Yes'},
            {'k1': 'Slovenia', 'k2': 'Yes'},
            {'k1': 'Spain', 'k2': 'Yes'},
            {'k1': 'Sweden', 'k2': 'Yes'},
            {'k1': 'Switzerland', 'k2': 'Yes'},
            {'k1': 'Turkey', 'k2': 'Yes'},
            {'k1': 'Ukraine', 'k2': 'Yes'},
            {'k1': 'England', 'k2': 'Yes'},
            {'k1': 'Abkhazie', 'k2': 'No'},
            {'k1': 'Kosovo', 'k2': 'No'},
            {'k1': 'Faroe Islands', 'k2': 'No'},
            {'k1': 'Gibraltar', 'k2': 'No'},
            {'k1': 'Guernesey', 'k2': 'No'},
            {'k1': 'Isle of Man', 'k2': 'No'},
            {'k1': 'Jersey island', 'k2': 'No'},
            {'k1': 'Afghanistan', 'k2': 'Yes'},
            {'k1': 'Bahrain', 'k2': 'Yes'},
            {'k1': 'Bangladesh', 'k2': 'Yes'},
            {'k1': 'Bhutan', 'k2': 'No'},
            {'k1': 'Brunei', 'k2': 'Yes'},
            {'k1': 'Cambodia', 'k2': 'No'},
            {'k1': 'China', 'k2': 'Yes'},
            {'k1': 'India', 'k2': 'Yes'},
            {'k1': 'Indonesia', 'k2': 'Yes'},
            {'k1': 'Iraq', 'k2': 'Yes'},
            {'k1': 'Israel', 'k2': 'Yes'},
            {'k1': 'Jordan', 'k2': 'Yes'},
            {'k1': 'Kuwait', 'k2': 'Yes'},
            {'k1': 'Kyrgyzstan', 'k2': 'Yes'},
            {'k1': 'Lebanon', 'k2': 'Yes'},
            {'k1': 'Malaysia', 'k2': 'Yes'},
            {'k1': 'Maldives', 'k2': 'No'},
            {'k1': 'Mongolia', 'k2': 'No'},
            {'k1': 'Myanmar', 'k2': 'No'},
            {'k1': 'Nepal', 'k2': 'No'},
            {'k1': 'Oman', 'k2': 'Yes'},
            {'k1': 'Palestine', 'k2': 'No'},
            {'k1': 'Philippines', 'k2': 'Yes'},
            {'k1': 'Qatar', 'k2': 'Yes'},
            {'k1': 'Russia', 'k2': 'Yes'},
            {'k1': 'Saudi Arabia', 'k2': 'Yes'},
            {'k1': 'Singapore', 'k2': 'Yes'},
            {'k1': 'South Korea', 'k2': 'Yes'},
            {'k1': 'Sri Lanka', 'k2': 'No'},
            {'k1': 'Syria', 'k2': 'Yes'},
            {'k1': 'Taiwan', 'k2': 'Yes'},
            {'k1': 'Tajikistan', 'k2': 'Yes'},
            {'k1': 'Thailand', 'k2': 'Yes'},
            {'k1': 'Timor Leste', 'k2': 'No'},
            {'k1': 'Turkmenistan', 'k2': 'Yes'},
            {'k1': 'United Arab Emirates', 'k2': 'Yes'},
            {'k1': 'Uzbekistan', 'k2': 'Yes'},
            {'k1': 'Vietnam', 'k2': 'Yes'},
            {'k1': 'Cayman Islands', 'k2': 'No'},
            {'k1': 'Usa', 'k2': 'Yes'},
            {'k1': 'Guatemala', 'k2': 'No'},
            {'k1': 'Dominican Republic', 'k2': 'No'},
            {'k1': 'Nicaragua', 'k2': 'No'},
            {'k1': 'Panama', 'k2': 'No'},
            {'k1': 'Puerto Rico', 'k2': 'No'},
            {'k1': 'Jamaica', 'k2': 'No'},
            {'k1': 'Trinidad And Tobago', 'k2': 'Yes'},
            {'k1': 'Bahamas', 'k2': 'No'},
            {'k1': 'Belize', 'k2': 'No'},
            {'k1': 'Barbados', 'k2': 'Yes'},
            {'k1': 'Saint Lucia', 'k2': 'No'},
            {'k1': 'Saint Vincent And The Grenadines', 'k2': 'No'},
            {'k1': 'Grenada', 'k2': 'No'},
            {'k1': 'Antigua And Barbuda', 'k2': 'No'},
            {'k1': 'Greenland', 'k2': 'No'},
            {'k1': 'Saint Kitts And Nevis', 'k2': 'No'},
            {'k1': 'Turks And Caicos Islands', 'k2': 'No'},
            {'k1': 'British Virgin Islands', 'k2': 'No'},
            {'k1': 'Caribbean Netherlands', 'k2': 'No'},
            {'k1': 'Anguilla', 'k2': 'No'},
            {'k1': 'Aruba', 'k2': 'No'},
            {'k1': 'Montserrat', 'k2': 'No'},
            {'k1': 'Colombia', 'k2': 'Yes'},
            {'k1': 'Brazil', 'k2': 'Yes'},
            {'k1': 'Peru', 'k2': 'Yes'},
            {'k1': 'Uruguay', 'k2': 'Yes'},
            {'k1': 'Guyana', 'k2': 'No'},
            {'k1': 'Suriname', 'k2': 'No'},
            {'k1': 'French Guiana', 'k2': 'No'},
            {'k1': 'Falkland Islands', 'k2': 'No'},
            {'k1': 'Nigeria', 'k2': 'Yes'},
            {'k1': 'Ethiopia', 'k2': 'No'},
            {'k1': 'Egypt', 'k2': 'Yes'},
            {'k1': 'Democratic Republic Of The Congo', 'k2': 'Yes'},
            {'k1': 'South Africa', 'k2': 'Yes'},
            {'k1': 'Tanzania', 'k2': 'Yes'},
            {'k1': 'Kenya', 'k2': 'No'},
            {'k1': 'Algeria', 'k2': 'Yes'},
            {'k1': 'Sudan', 'k2': 'Yes'},
            {'k1': 'Morocco', 'k2': 'Yes'},
            {'k1': 'Uganda', 'k2': 'No'},
            {'k1': 'Mozambique', 'k2': 'Yes'},
            {'k1': 'Ghana', 'k2': 'Yes'},
            {'k1': 'Angola', 'k2': 'Yes'},
            {'k1': 'Ivory Coast', 'k2': 'Yes'},
            {'k1': 'Madagascar', 'k2': 'No'},
            {'k1': 'Cameroon', 'k2': 'Yes'},
            {'k1': 'Burkina_Faso', 'k2': 'No'},
            {'k1': 'Mali', 'k2': 'No'},
            {'k1': 'Malawi', 'k2': 'No'},
            {'k1': 'Zambia', 'k2': 'No'},
            {'k1': 'Somalia', 'k2': 'No'},
            {'k1': 'Senegal', 'k2': 'Yes'},
            {'k1': 'Chad', 'k2': 'No'},
            {'k1': 'Zimbabwe', 'k2': 'No'},
            {'k1': 'Rwanda', 'k2': 'No'},
            {'k1': 'Tunisia', 'k2': 'Yes'},
            {'k1': 'Benin', 'k2': 'No'},
            {'k1': 'Togo', 'k2': 'No'},
            {'k1': 'Eritrea', 'k2': 'No'},
            {'k1': 'Sierra Leone', 'k2': 'No'},
            {'k1': 'Central African Republic', 'k2': 'No'},
            {'k1': 'Liberia', 'k2': 'No'},
            {'k1': 'Mauritania', 'k2': 'No'},
            {'k1': 'Namibia', 'k2': 'No'},
            {'k1': 'Botswana', 'k2': 'No'},
            {'k1': 'Lesotho', 'k2': 'No'},
            {'k1': 'Gambia', 'k2': 'No'},
            {'k1': 'Gabon', 'k2': 'Yes'},
            {'k1': 'Guinea Bissau', 'k2': 'No'},
            {'k1': 'Mauritius', 'k2': 'No'},
            {'k1': 'Equatorial Guinea', 'k2': 'Yes'},
            {'k1': 'Eswatini', 'k2': 'No'},
            {'k1': 'Djibouti', 'k2': 'No'},
            {'k1': 'Comoros', 'k2': 'No'},
            {'k1': 'Cape Verde', 'k2': 'No'},
            {'k1': 'Seychelles', 'k2': 'No'},
            {'k1': 'Australia', 'k2': 'Yes'},
            {'k1': 'Papua New Guinea', 'k2': 'No'},
            {'k1': 'New Zealand', 'k2': 'Yes'},
            {'k1': 'Solomon Islands', 'k2': 'No'},
            {'k1': 'Vanuatu', 'k2': 'No'},
            {'k1': 'New Caledonia', 'k2': 'No'},
            {'k1': 'Samoa', 'k2': 'No'},
            {'k1': 'Kiribati', 'k2': 'No'},
            {'k1': 'Tonga', 'k2': 'No'},
            {'k1': 'American Samoa', 'k2': 'No'},
            {'k1': 'Marshall Islands', 'k2': 'No'},
            {'k1': 'Cook Islands', 'k2': 'No'},
            {'k1': 'Tuvalu', 'k2': 'No'},
            {'k1': 'Norfolk Island', 'k2': 'No'},
            {'k1': 'Niue', 'k2': 'No'},
            {'k1': 'Pitcairn Islands', 'k2': 'No'},
            {'k1': 'Luxembourg', 'k2': 'Yes'},
            {'k1': 'Belgium', 'k2': 'Yes'},
            {'k1': 'France', 'k2': 'Yes'},
            {'k1': 'Grece', 'k2': 'Yes'},
            {'k1': 'Monaco', 'k2': 'No'},
            {'k1': 'Portugal', 'k2': 'Yes'},
            {'k1': 'Vatican', 'k2': 'No'},
            {'k1': 'Haut Karabagh', 'k2': 'No'},
            {'k1': 'North cyprus', 'k2': 'No'},
            {'k1': 'Transnistria', 'k2': 'No'},
            {'k1': 'South Ossetia', 'k2': 'No'},
            {'k1': 'Akrotiri and Dhekelia', 'k2': 'No'},
            {'k1': 'Aland island', 'k2': 'No'},
            {'k1': 'Svalbard', 'k2': 'No'},
            {'k1': 'Latvia', 'k2': 'Yes'},
            {'k1': 'Iran', 'k2': 'Yes'},
            {'k1': 'Japan', 'k2': 'Yes'},
            {'k1': 'Laos', 'k2': 'No'},
            {'k1': 'North Korea', 'k2': 'No'},
            {'k1': 'Pakistan', 'k2': 'Yes'},
            {'k1': 'Yemen', 'k2': 'Yes'},
            {'k1': 'Mexico', 'k2': 'Yes'},
            {'k1': 'Canada', 'k2': 'Yes'},
            {'k1': 'Cuba', 'k2': 'Yes'},
            {'k1': 'Haiti', 'k2': 'No'},
            {'k1': 'Honduras', 'k2': 'No'},
            {'k1': 'El Salvador', 'k2': 'No'},
            {'k1': 'Costa Rica', 'k2': 'No'},
            {'k1': 'United States Virgin Islands', 'k2': 'No'},
            {'k1': 'Bermuda', 'k2': 'No'},
            {'k1': 'Sint Maarten', 'k2': 'No'},
            {'k1': 'Saint Barthelemy', 'k2': 'No'},
            {'k1': 'Saint Pierre And Miquelon', 'k2': 'No'},
            {'k1': 'Argentina', 'k2': 'Yes'},
            {'k1': 'Venezuela', 'k2': 'Yes'},
            {'k1': 'Ecuador', 'k2': 'Yes'},
            {'k1': 'Chile', 'k2': 'Yes'},
            {'k1': 'Bolivia', 'k2': 'Yes'},
            {'k1': 'Paraguay', 'k2': 'No'},
            {'k1': 'Niger', 'k2': 'No'},
            {'k1': 'Guinea', 'k2': 'No'},
            {'k1': 'Burundi', 'k2': 'No'},
            {'k1': 'Libya', 'k2': 'Yes'},
            {'k1': 'Western Sahara', 'k2': 'No'},
            {'k1': 'Sao Tome And Principe', 'k2': 'No'},
            {'k1': 'Saint Helena  Ascension And Tristan Da Cunha', 'k2': 'No'},
            {'k1': 'Fiji', 'k2': 'No'},
            {'k1': 'Guam', 'k2': 'No'},
            {'k1': 'Federated States Of Micronesia', 'k2': 'No'},
            {'k1': 'Northern Mariana Islands', 'k2': 'No'},
            {'k1': 'Palau', 'k2': 'No'},
            {'k1': 'Wallis And Futuna', 'k2': 'No'},
            {'k1': 'Nauru', 'k2': 'No'},
            {'k1': 'Tokelau', 'k2': 'No'}
        ]
    }
    return render(request, "contents/countries_with_gas_networks.html", context)


def international_energy_needs_for_abundance(request):
    context = {
        'data': [
            {'k1': 'Afghanistan', 'k2': '1147339923'},
            {'k1': 'Åland Islands', 'k2': '976278'},
            {'k1': 'Albania', 'k2': '95217638'},
            {'k1': 'Algeria', 'k2': '1367899068'},
            {'k1': 'American Samoa', 'k2': '1840688'},
            {'k1': 'Andorra', 'k2': '2558503'},
            {'k1': 'Angola', 'k2': '953912913'},
            {'k1': 'Anguilla', 'k2': '488784'},
            {'k1': 'Antarctica', 'k2': '36616'},
            {'k1': 'Antigua and Barbuda', 'k2': '3342532'},
            {'k1': 'Argentina', 'k2': '1451634941'},
            {'k1': 'Armenia', 'k2': '96830421'},
            {'k1': 'Aruba', 'k2': '3470290'},
            {'k1': 'Australia', 'k2': '801535148'},
            {'k1': 'Austria', 'k2': '289068445'},
            {'k1': 'Azerbaijan', 'k2': '323047003'},
            {'k1': 'Bahamas', 'k2': '12952322'},
            {'k1': 'Bahrain', 'k2': '47182424'},
            {'k1': 'Bangladesh', 'k2': '5394755821'},
            {'k1': 'Barbados', 'k2': '9435220'},
            {'k1': 'Belarus', 'k2': '314562535'},
            {'k1': 'Belgium', 'k2': '375377256'},
            {'k1': 'Belize', 'k2': '12148563'},
            {'k1': 'Benin', 'k2': '359943734'},
            {'k1': 'Bermuda', 'k2': '2164371'},
            {'k1': 'Bhutan', 'k2': '26411207'},
            {'k1': 'Bolivia (Plurinational State of)', 'k2': '360459665'},
            {'k1': 'Bonaire, Sint Eustatius and Saba', 'k2': '828292'},
            {'k1': 'Bosnia and Herzegovina', 'k2': '116429469'},
            {'k1': 'Botswana', 'k2': '74498233'},
            {'k1': 'Bouvet Island', 'k2': ''},
            {'k1': 'Brazil', 'k2': '6874659575'},
            {'k1': 'British Indian Ocean Territory', 'k2': '132426'},
            {'k1': 'United States Minor Outlying Islands', 'k2': '9932'},
            {'k1': 'Virgin Islands (British)', 'k2': '1015078'},
            {'k1': 'Virgin Islands (U.S.)', 'k2': '3551268'},
            {'k1': 'Brunei Darussalam', 'k2': '14010538'},
            {'k1': 'Bulgaria', 'k2': '235977239'},
            {'k1': 'Burkina Faso', 'k2': '617318134'},
            {'k1': 'Burundi', 'k2': '348416679'},
            {'k1': 'Cambodia', 'k2': '521836902'},
            {'k1': 'Cameroon', 'k2': '775989511'},
            {'k1': 'Canada', 'k2': '1200594112'},
            {'k1': 'Cabo Verde', 'k2': '17862943'},
            {'k1': 'Cayman Islands', 'k2': '2038003'},
            {'k1': 'Central African Republic', 'k2': '152111820'},
            {'k1': 'Chad', 'k2': '478473115'},
            {'k1': 'Chile', 'k2': '592929271'},
            {'k1': 'China', 'k2': '45642772823'},
            {'k1': 'Christmas Island', 'k2': '46415'},
            {'k1': 'Cocos (Keeling) Islands', 'k2': '19731'},
            {'k1': 'Colombia', 'k2': '1610744416'},
            {'k1': 'Comoros', 'k2': '26339565'},
            {'k1': 'Congo', 'k2': '2606678449'},
            {'k1': 'Congo (Democratic Republic of the)', 'k2': '2692882710'},
            {'k1': 'Cook Islands', 'k2': '575358'},
            {'k1': 'Costa Rica', 'k2': '160807342'},
            {'k1': 'Croatia', 'k2': '138198085'},
            {'k1': 'Cuba', 'k2': '380216102'},
            {'k1': 'Curaçao', 'k2': '5330610'},
            {'k1': 'Cyprus', 'k2': '39050805'},
            {'k1': 'Czech Republic', 'k2': '350641635'},
            {'k1': 'Denmark', 'k2': '191011362'},
            {'k1': 'Djibouti', 'k2': '31682424'},
            {'k1': 'Dominica', 'k2': '2447398'},
            {'k1': 'Dominican Republic', 'k2': '356457619'},
            {'k1': 'Ecuador', 'k2': '550390861'},
            {'k1': 'Egypt', 'k2': '3229643394'},
            {'k1': 'El Salvador', 'k2': '210051539'},
            {'k1': 'Equatorial Guinea', 'k2': '40439259'},
            {'k1': 'Eritrea', 'k2': '216389911'},
            {'k1': 'Estonia', 'k2': '43561202'},
            {'k1': 'Ethiopia', 'k2': '3390211408'},
            {'k1': 'Falkland Islands (Malvinas)', 'k2': '112496'},
            {'k1': 'Faroe Islands', 'k2': '1626092'},
            {'k1': 'Fiji', 'k2': '29754798'},
            {'k1': 'Finland', 'k2': '181930249'},
            {'k1': 'France', 'k2': '2214566785'},
            {'k1': 'French Guiana', 'k2': '9823063'},
            {'k1': 'French Polynesia', 'k2': '9276706'},
            {'k1': 'French Southern Territories', 'k2': '6489'},
            {'k1': 'Gabon', 'k2': '65543785'},
            {'k1': 'Gambia', 'k2': '67487633'},
            {'k1': 'Georgia', 'k2': '123133005'},
            {'k1': 'Germany', 'k2': '2737742018'},
            {'k1': 'Ghana', 'k2': '933826041'},
            {'k1': 'Gibraltar', 'k2': '1139128'},
            {'k1': 'Greece', 'k2': '356574253'},
            {'k1': 'Greenland', 'k2': '1860122'},
            {'k1': 'Grenada', 'k2': '3552890'},
            {'k1': 'Guadeloupe', 'k2': '13100242'},
            {'k1': 'Guam', 'k2': '5392916'},
            {'k1': 'Guatemala', 'k2': '548987510'},
            {'k1': 'Guernsey', 'k2': '2086570'},
            {'k1': 'Guinea', 'k2': '410385658'},
            {'k1': 'Guinea-Bissau', 'k2': '60111406'},
            {'k1': 'Guyana', 'k2': '25601356'},
            {'k1': 'Haiti', 'k2': '359117263'},
            {'k1': 'Holy See', 'k2': '33107'},
            {'k1': 'Honduras', 'k2': '301695131'},
            {'k1': 'Hong Kong', 'k2': '242889148'},
            {'k1': 'Hungary', 'k2': '324907952'},
            {'k1': 'Iceland', 'k2': '11105211'},
            {'k1': 'India', 'k2': '44335566875'},
            {'k1': 'Indonesia', 'k2': '8644618844'},
            {'k1': 'Ivory coast', 'k2': '784488942'},
            {'k1': 'Iran (Islamic Republic of)', 'k2': '2657704670'},
            {'k1': 'Iraq', 'k2': '1231646950'},
            {'k1': 'Ireland', 'k2': '157248492'},
            {'k1': 'Isle of Man', 'k2': '2772239'},
            {'k1': 'Israel', 'k2': '282928149'},
            {'k1': 'Italy', 'k2': '2007164263'},
            {'k1': 'Jamaica', 'k2': '95391579'},
            {'k1': 'Japan', 'k2': '4204343778'},
            {'k1': 'Jersey', 'k2': '3535774'},
            {'k1': 'Jordan', 'k2': '321199263'},
            {'k1': 'Kazakhstan', 'k2': '589110204'},
            {'k1': 'Kenya', 'k2': '1604392868'},
            {'k1': 'Kiribati', 'k2': '3787218'},
            {'k1': 'Kuwait', 'k2': '134166872'},
            {'k1': 'Kyrgyzstan', 'k2': '201270967'},
            {'k1': 'Laos', 'k2': '223745414'},
            {'k1': 'Latvia', 'k2': '64873412'},
            {'k1': 'Lebanon', 'k2': '198859754'},
            {'k1': 'Lesotho', 'k2': '72960800'},
            {'k1': 'Liberia', 'k2': '152747531'},
            {'k1': 'Libya', 'k2': '208347580'},
            {'k1': 'Liechtenstein', 'k2': '1246989'},
            {'k1': 'Lithuania', 'k2': '94957090'},
            {'k1': 'Luxembourg', 'k2': '19268446'},
            {'k1': 'Macao', 'k2': '20266707'},
            {'k1': 'Macedonia', 'k2': '68901446'},
            {'k1': 'Madagascar', 'k2': '824171453'},
            {'k1': 'Malawi', 'k2': '598948728'},
            {'k1': 'Malaysia', 'k2': '1032501189'},
            {'k1': 'Maldives', 'k2': '14161504'},
            {'k1': 'Mali', 'k2': '595746071'},
            {'k1': 'Malta', 'k2': '14481379'},
            {'k1': 'Marshall Islands', 'k2': '1756830'},
            {'k1': 'Martinique', 'k2': '12463935'},
            {'k1': 'Mauritania', 'k2': '142391652'},
            {'k1': 'Mauritius', 'k2': '41829169'},
            {'k1': 'Mayotte', 'k2': '8951071'},
            {'k1': 'Mexico', 'k2': '4222417014'},
            {'k1': 'Micronesia (Federated States of)', 'k2': '3474097'},
            {'k1': 'Moldova (Republic of)', 'k2': '117592765'},
            {'k1': 'Monaco', 'k2': '1274567'},
            {'k1': 'Mongolia', 'k2': '100226552'},
            {'k1': 'Montenegro', 'k2': '20602274'},
            {'k1': 'Montserrat', 'k2': '172650'},
            {'k1': 'Morocco', 'k2': '1167890916'},
            {'k1': 'Mozambique', 'k2': '954443047'},
            {'k1': 'Myanmar', 'k2': '1750844635'},
            {'k1': 'Namibia', 'k2': '82094618'},
            {'k1': 'Nauru', 'k2': '432007'},
            {'k1': 'Nepal', 'k2': '959518108'},
            {'k1': 'Netherlands', 'k2': '563814090'},
            {'k1': 'New Caledonia', 'k2': '9170501'},
            {'k1': 'New Zealand', 'k2': '155375426'},
            {'k1': 'Nicaragua', 'k2': '203602591'},
            {'k1': 'Niger', 'k2': '684410244'},
            {'k1': 'Nigeria', 'k2': '6157466017'},
            {'k1': 'Niue', 'k2': '53765'},
            {'k1': 'Norfolk Island', 'k2': '71808'},
            {'k1': 'South Korea', 'k2': '1703991555'},
            {'k1': 'Northern Mariana Islands', 'k2': '1821619'},
            {'k1': 'Norway', 'k2': '173350633'},
            {'k1': 'Oman', 'k2': '146488383'},
            {'k1': 'Pakistan', 'k2': '6396290878'},
            {'k1': 'Palau', 'k2': '711889'},
            {'k1': 'Palestine, State of', 'k2': '159474011'},
            {'k1': 'Panama', 'k2': '133555561'},
            {'k1': 'Papua New Guinea', 'k2': '267665755'},
            {'k1': 'Paraguay', 'k2': '222651409'},
            {'k1': 'Peru', 'k2': '1051920601'},
            {'k1': 'Philippines', 'k2': '3420570930'},
            {'k1': 'Pitcairn', 'k2': '1655'},
            {'k1': 'Poland', 'k2': '1257056685'},
            {'k1': 'Portugal', 'k2': '341839577'},
            {'k1': 'Puerto Rico', 'k2': '112936435'},
            {'k1': 'Qatar', 'k2': '85077216'},
            {'k1': 'Republic of Kosovo', 'k2': '60618002'},
            {'k1': 'Réunion', 'k2': '33106500'},
            {'k1': 'Romania', 'k2': '652175273'},
            {'k1': 'Russian Federation', 'k2': '4778671533'},
            {'k1': 'Rwanda', 'k2': '394546979'},
            {'k1': 'Saint Barthélemy', 'k2': '318650'},
            {'k1': 'Saint Helena, Ascension and Tristan da Cunha', 'k2': '186489'},
            {'k1': 'Saint Kitts and Nevis', 'k2': '1814931'},
            {'k1': 'Saint Lucia', 'k2': '5893454'},
            {'k1': 'Saint Martin (French part)', 'k2': '1057720'},
            {'k1': 'Saint Pierre and Miquelon', 'k2': '198904'},
            {'k1': 'Saint Vincent and the Grenadines', 'k2': '3629896'},
            {'k1': 'Samoa', 'k2': '6459906'},
            {'k1': 'San Marino', 'k2': '1099235'},
            {'k1': 'Sao Tome and Principe', 'k2': '6618320'},
            {'k1': 'Saudi Arabia', 'k2': '1068535032'},
            {'k1': 'Senegal', 'k2': '510224599'},
            {'k1': 'Serbia', 'k2': '233676337'},
            {'k1': 'Seychelles', 'k2': '3134424'},
            {'k1': 'Sierra Leone', 'k2': '244861964'},
            {'k1': 'Singapore', 'k2': '185637515'},
            {'k1': 'Sint Maarten (Dutch part)', 'k2': '1323234'},
            {'k1': 'Slovakia', 'k2': '179794714'},
            {'k1': 'Slovenia', 'k2': '68366313'},
            {'k1': 'Solomon Islands', 'k2': '19844665'},
            {'k1': 'Somalia', 'k2': '474018735'},
            {'k1': 'South Africa', 'k2': '1850946839'},
            {'k1': 'South Georgia and the South Sandwich Islands', 'k2': '993'},
            {'k1': 'Korea (Republic of)', 'k2': '1696565999'},
            {'k1': 'South Sudan', 'k2': '404916663'},
            {'k1': 'Spain', 'k2': '1538940192'},
            {'k1': 'Sri Lanka', 'k2': '701957120'},
            {'k1': 'Sudan', 'k2': '1310316469'},
            {'k1': 'Suriname', 'k2': '18485610'},
            {'k1': 'Svalbard and Jan Mayen', 'k2': '85150'},
            {'k1': 'Swaziland', 'k2': '44465274'},
            {'k1': 'Sweden', 'k2': '328518614'},
            {'k1': 'Switzerland', 'k2': '277181291'},
            {'k1': 'Syrian Arab Republic', 'k2': '610167792'},
            {'k1': 'Taiwan', 'k2': '787272570'},
            {'k1': 'Tajikistan', 'k2': '289183655'},
            {'k1': 'Tanzania, United Republic of', 'k2': '1839801072'},
            {'k1': 'Thailand', 'k2': '2279829926'},
            {'k1': 'Timor-Leste', 'k2': '42906024'},
            {'k1': 'Togo', 'k2': '251820421'},
            {'k1': 'Tokelau', 'k2': '49627'},
            {'k1': 'Tonga', 'k2': '3546434'},
            {'k1': 'Trinidad and Tobago', 'k2': '45189114'},
            {'k1': 'Tunisia', 'k2': '377521630'},
            {'k1': 'Turkey', 'k2': '2632378131'},
            {'k1': 'Turkmenistan', 'k2': '187467013'},
            {'k1': 'Turks and Caicos Islands', 'k2': '1155417'},
            {'k1': 'Tuvalu', 'k2': '367383'},
            {'k1': 'Uganda', 'k2': '1373521313'},
            {'k1': 'Ukraine', 'k2': '1489946280'},
            {'k1': 'United Arab Emirates', 'k2': '306884410'},
            {'k1': 'United Kingdom of Great Britain and Northern Ireland', 'k2': '2171639573'},
            {'k1': 'United States of America', 'k2': '10697621009'},
            {'k1': 'Uruguay', 'k2': '114018985'},
            {'k1': 'Uzbekistan', 'k2': '1054372501'},
            {'k1': 'Vanuatu', 'k2': '8952064'},
            {'k1': 'Venezuela', 'k2': '1045111918'},
            {'k1': 'VietNam', 'k2': '3069008967'},
            {'k1': 'Wallis and Futuna', 'k2': '382645'},
            {'k1': 'Western Sahara', 'k2': '16983635'},
            {'k1': 'Yemen', 'k2': '913216748'},
            {'k1': 'Zambia', 'k2': '549282853'},
            {'k1': 'Zimbabwe', 'k2': '534681960'},
            {'k1': 'Total', 'k2': '250550977481'}
        ]
    }
    return render(request, "contents/international_energy_needs_for_abundance.html", context)


def forecast_of_worldwide_ammonia_production(request):
    context = {
        'data': [
            {'k1': '1994', 'k2': '92000', 'k3': '211'},
            {'k1': '1995', 'k2': '96000', 'k3': '230'},
            {'k1': '1996', 'k2': '96000', 'k3': '225'},
            {'k1': '1997', 'k2': '96000', 'k3': '192'},
            {'k1': '1998', 'k2': '106000', 'k3': '121'},
            {'k1': '1999', 'k2': '101000', 'k3': '110'},
            {'k1': '2000', 'k2': '109000', 'k3': '169'},
            {'k1': '2001', 'k2': '105000', 'k3': '150'},
            {'k1': '2002', 'k2': '109000', 'k3': '137'},
            {'k1': '2003', 'k2': '108000', 'k3': '240'},
            {'k1': '2004', 'k2': '117000', 'k3': '274'},
            {'k1': '2005', 'k2': '115000', 'k3': '295'},
            {'k1': '2006', 'k2': '124000', 'k3': '201'},
            {'k1': '2007', 'k2': '125000', 'k3': '200'},
            {'k1': '2008', 'k2': '136000', 'k3': '500'},
            {'k1': '2009', 'k2': '133000', 'k3': '250'},
            {'k1': '2010', 'k2': '131000', 'k3': '390'},
            {'k1': '2011', 'k2': '136000', 'k3': '520'},
            {'k1': '2012', 'k2': '137000', 'k3': '575'},
            {'k1': '2013', 'k2': '139500', 'k3': '595'},
            {'k1': '2014', 'k2': '142000', 'k3': '615'},
            {'k1': '2015', 'k2': '144500', 'k3': '636'},
            {'k1': '2016', 'k2': '147000', 'k3': '656'},
            {'k1': '2017', 'k2': '149500', 'k3': '676'},
            {'k1': '2018', 'k2': '152000', 'k3': '696'},
            {'k1': '2019', 'k2': '154500', 'k3': '717'},
            {'k1': '2020', 'k2': '157000', 'k3': '737'},
            {'k1': '2021', 'k2': '159500', 'k3': '757'},
            {'k1': '2022', 'k2': '162000', 'k3': '777'},
            {'k1': '2023', 'k2': '164500', 'k3': '797'},
            {'k1': '2024', 'k2': '167000', 'k3': '818'},
            {'k1': '2025', 'k2': '169500', 'k3': '838'},
            {'k1': '2026', 'k2': '172000', 'k3': '858'},
            {'k1': '2027', 'k2': '174500', 'k3': '878'},
            {'k1': '2028', 'k2': '177000', 'k3': '899'},
            {'k1': '2029', 'k2': '179500', 'k3': '919'},
            {'k1': '2030', 'k2': '182000', 'k3': '939'},
            {'k1': '2031', 'k2': '184500', 'k3': '959'},
            {'k1': '2032', 'k2': '187000', 'k3': '979'},
            {'k1': '2033', 'k2': '189500', 'k3': '1000'},
            {'k1': '2034', 'k2': '192000', 'k3': '1020'},
            {'k1': '2035', 'k2': '194500', 'k3': '1040'},
            {'k1': '2036', 'k2': '197000', 'k3': '1060'},
            {'k1': '2037', 'k2': '199500', 'k3': '1081'},
            {'k1': '2038', 'k2': '202000', 'k3': '1101'},
            {'k1': '2039', 'k2': '204500', 'k3': '1121'},
            {'k1': '2040', 'k2': '207000', 'k3': '1141'},
            {'k1': '2041', 'k2': '209500', 'k3': '1161'},
            {'k1': '2042', 'k2': '212000', 'k3': '1182'},
            {'k1': '2043', 'k2': '214500', 'k3': '1202'},
            {'k1': '2044', 'k2': '217000', 'k3': '1222'},
            {'k1': '2045', 'k2': '219500', 'k3': '1242'},
            {'k1': '2046', 'k2': '222000', 'k3': '1263'},
            {'k1': '2047', 'k2': '224500', 'k3': '1283'},
            {'k1': '2048', 'k2': '227000', 'k3': '1303'},
            {'k1': '2049', 'k2': '229500', 'k3': '1323'},
            {'k1': '2050', 'k2': '232000', 'k3': '1343'},
            {'k1': '2051', 'k2': '234500', 'k3': '1364'},
            {'k1': '2052', 'k2': '237000', 'k3': '1384'},
            {'k1': '2053', 'k2': '239500', 'k3': '1404'},
            {'k1': '2054', 'k2': '242000', 'k3': '1424'},
            {'k1': '2055', 'k2': '244500', 'k3': '1445'},
            {'k1': '2056', 'k2': '247000', 'k3': '1465'},
            {'k1': '2057', 'k2': '249500', 'k3': '1485'},
            {'k1': '2058', 'k2': '252000', 'k3': '1505'},
            {'k1': '2059', 'k2': '254500', 'k3': '1525'},
            {'k1': '2060', 'k2': '257000', 'k3': '1546'},
            {'k1': '2061', 'k2': '259500', 'k3': '1566'},
            {'k1': '2062', 'k2': '262000', 'k3': '1586'},
            {'k1': '2063', 'k2': '264500', 'k3': '1606'},
            {'k1': '2064', 'k2': '267000', 'k3': '1627'},
            {'k1': '2065', 'k2': '269500', 'k3': '1647'},
            {'k1': '2066', 'k2': '272000', 'k3': '1667'},
            {'k1': '2067', 'k2': '274500', 'k3': '1687'},
            {'k1': '2068', 'k2': '277000', 'k3': '1707'},
            {'k1': '2069', 'k2': '279500', 'k3': '1728'},
            {'k1': '2070', 'k2': '282000', 'k3': '1748'},
            {'k1': '2071', 'k2': '284500', 'k3': '1768'},
            {'k1': '2072', 'k2': '287000', 'k3': '1788'},
            {'k1': '2073', 'k2': '289500', 'k3': '1809'},
            {'k1': '2074', 'k2': '292000', 'k3': '1829'},
            {'k1': '2075', 'k2': '294500', 'k3': '1849'},
            {'k1': '2076', 'k2': '297000', 'k3': '1869'},
            {'k1': '2077', 'k2': '299500', 'k3': '1889'},
            {'k1': '2078', 'k2': '302000', 'k3': '1910'},
            {'k1': '2079', 'k2': '304500', 'k3': '1930'},
            {'k1': '2080', 'k2': '307000', 'k3': '1950'},
            {'k1': '2081', 'k2': '309500', 'k3': '1970'},
            {'k1': '2082', 'k2': '312000', 'k3': '1991'},
            {'k1': '2083', 'k2': '314500', 'k3': '2011'},
            {'k1': '2084', 'k2': '317000', 'k3': '2031'},
            {'k1': '2085', 'k2': '319500', 'k3': '2051'},
            {'k1': '2086', 'k2': '322000', 'k3': '2071'},
            {'k1': '2087', 'k2': '324500', 'k3': '2092'},
            {'k1': '2088', 'k2': '327000', 'k3': '2112'},
            {'k1': '2089', 'k2': '329500', 'k3': '2132'},
            {'k1': '2090', 'k2': '332000', 'k3': '2152'},
            {'k1': '2091', 'k2': '334500', 'k3': '2173'},
            {'k1': '2092', 'k2': '337000', 'k3': '2193'},
            {'k1': '2093', 'k2': '339500', 'k3': '2213'},
            {'k1': '2094', 'k2': '342000', 'k3': '2233'},
            {'k1': '2095', 'k2': '344500', 'k3': '2253'},
            {'k1': '2096', 'k2': '347000', 'k3': '2274'},
            {'k1': '2097', 'k2': '349500', 'k3': '2294'},
            {'k1': '2098', 'k2': '352000', 'k3': '2314'},
            {'k1': '2099', 'k2': '354500', 'k3': '2334'},
            {'k1': '2100', 'k2': '357000', 'k3': '2355'}
        ]
    }
    return render(request, "contents/forecast_of_worldwide_ammonia_production.html", context)


def forecast_of_worldwide_natural_gas_reserves(request):
    context = {
        'data': [
            {'k1': '2017', 'k2': '197393692700000'}, {'k1': '2018', 'k2': '187524008065000'},
            {'k1': '2019', 'k2': '178147807661750'}, {'k1': '2020', 'k2': '169240417278663'},
            {'k1': '2021', 'k2': '160778396414729'}, {'k1': '2022', 'k2': '152739476593993'},
            {'k1': '2023', 'k2': '145102502764293'}, {'k1': '2024', 'k2': '137847377626079'},
            {'k1': '2025', 'k2': '130955008744775'}, {'k1': '2026', 'k2': '124407258307536'},
            {'k1': '2027', 'k2': '118186895392159'}, {'k1': '2028', 'k2': '112277550622551'},
            {'k1': '2029', 'k2': '106663673091424'}, {'k1': '2030', 'k2': '101330489436852'},
            {'k1': '2031', 'k2': '96263964965010'}, {'k1': '2032', 'k2': '91450766716759'},
            {'k1': '2033', 'k2': '86878228380921'}, {'k1': '2034', 'k2': '82534316961875'},
            {'k1': '2035', 'k2': '78407601113782'}, {'k1': '2036', 'k2': '74487221058092'},
            {'k1': '2037', 'k2': '70762860005188'}, {'k1': '2038', 'k2': '67224717004928'},
            {'k1': '2039', 'k2': '63863481154682'}, {'k1': '2040', 'k2': '60670307096948'},
            {'k1': '2041', 'k2': '57636791742101'}, {'k1': '2042', 'k2': '54754952154996'},
            {'k1': '2043', 'k2': '52017204547246'}, {'k1': '2044', 'k2': '49416344319883'},
            {'k1': '2045', 'k2': '46945527103889'}, {'k1': '2046', 'k2': '44598250748695'},
            {'k1': '2047', 'k2': '42368338211260'}, {'k1': '2048', 'k2': '40249921300697'},
            {'k1': '2049', 'k2': '38237425235662'}, {'k1': '2050', 'k2': '36325553973879'},
            {'k1': '2051', 'k2': '34509276275185'}, {'k1': '2052', 'k2': '32783812461426'},
            {'k1': '2053', 'k2': '31144621838355'}, {'k1': '2054', 'k2': '29587390746437'},
            {'k1': '2055', 'k2': '28108021209115'}, {'k1': '2056', 'k2': '26702620148659'},
            {'k1': '2057', 'k2': '25367489141226'}, {'k1': '2058', 'k2': '24099114684165'},
            {'k1': '2059', 'k2': '22894158949957'}, {'k1': '2060', 'k2': '21749451002459'},
            {'k1': '2061', 'k2': '20661978452336'}, {'k1': '2062', 'k2': '19628879529719'},
            {'k1': '2063', 'k2': '18647435553233'}, {'k1': '2064', 'k2': '17715063775572'},
            {'k1': '2065', 'k2': '16829310586793'}, {'k1': '2066', 'k2': '15987845057453'},
            {'k1': '2067', 'k2': '15188452804581'}, {'k1': '2068', 'k2': '14429030164352'},
            {'k1': '2069', 'k2': '13707578656134'}, {'k1': '2070', 'k2': '13022199723327'},
            {'k1': '2071', 'k2': '12371089737161'}, {'k1': '2072', 'k2': '11752535250303'},
            {'k1': '2073', 'k2': '11164908487788'}, {'k1': '2074', 'k2': '10606663063398'},
            {'k1': '2075', 'k2': '10076329910229'}, {'k1': '2076', 'k2': '9572513414717'},
            {'k1': '2077', 'k2': '9093887743981'}, {'k1': '2078', 'k2': '8639193356782'},
            {'k1': '2079', 'k2': '8207233688943'}, {'k1': '2080', 'k2': '7796872004496'},
            {'k1': '2081', 'k2': '7407028404271'}, {'k1': '2082', 'k2': '7036676984058'},
            {'k1': '2083', 'k2': '6684843134855'}, {'k1': '2084', 'k2': '6350600978112'},
            {'k1': '2085', 'k2': '6033070929206'}, {'k1': '2086', 'k2': '5731417382746'},
            {'k1': '2087', 'k2': '5444846513609'}, {'k1': '2088', 'k2': '5172604187928'},
            {'k1': '2089', 'k2': '4913973978532'}, {'k1': '2090', 'k2': '4668275279605'},
            {'k1': '2091', 'k2': '4434861515625'}, {'k1': '2092', 'k2': '4213118439844'},
            {'k1': '2093', 'k2': '4002462517852'}, {'k1': '2094', 'k2': '3802339391959'},
            {'k1': '2095', 'k2': '3612222422361'}, {'k1': '2096', 'k2': '3431611301243'},
            {'k1': '2097', 'k2': '3260030736181'}, {'k1': '2098', 'k2': '3097029199372'},
            {'k1': '2099', 'k2': '2942177739403'}, {'k1': '2100', 'k2': '2795068852433'}
        ]
    }
    return render(request, "contents/forecast_of_worldwide_natural_gas_reserves.html", context)


def international_real_estate_price(request):
    context = {
        'data': [
            {'k1': 'Abou Dabi', 'k2': 'United Arab Emirates', 'k3': '3074 €', 'k4': '307 €'},
            {'k1': 'Abuja', 'k2': 'Nigeria', 'k3': '3280 €', 'k4': '328 €'},
            {'k1': 'Accra', 'k2': 'Ghana', 'k3': '1585 €', 'k4': '159 €'},
            {'k1': 'Achgabat', 'k2': 'Turkmenistan', 'k3': '1943 €', 'k4': '194 €'},
            {'k1': 'Addis-Abeba', 'k2': 'Ethiopia', 'k3': '1381 €', 'k4': '138 €'},
            {'k1': 'Alger', 'k2': 'Algeria', 'k3': '1827 €', 'k4': '183 €'},
            {'k1': 'Amman', 'k2': 'Jordan', 'k3': '1164 €', 'k4': '116 €'},
            {'k1': 'Amsterdam', 'k2': 'Netherlands', 'k3': '7284 €', 'k4': '728 €'},
            {'k1': 'Ankara', 'k2': 'Turkey', 'k3': '706 €', 'k4': '71 €'},
            {'k1': 'Antananarivo', 'k2': 'Madagascar', 'k3': '732 €', 'k4': '73 €'},
            {'k1': 'Asmara', 'k2': 'Eritrea', 'k3': '935 €', 'k4': '94 €'},
            {'k1': 'Asuncion', 'k2': 'Paraguay', 'k3': '1086 €', 'k4': '109 €'},
            {'k1': 'Athens', 'k2': 'Greece', 'k3': '1597 €', 'k4': '160 €'},
            {'k1': 'Bagdad', 'k2': 'Irak', 'k3': '1768 €', 'k4': '177 €'},
            {'k1': 'Bakou', 'k2': 'Azerbaijan', 'k3': '1371 €', 'k4': '137 €'},
            {'k1': 'Bamako', 'k2': 'Mali', 'k3': '360 €', 'k4': '36 €'},
            {'k1': 'Bandar Seri Begawan', 'k2': 'Brunei', 'k3': '1163 €', 'k4': '116 €'},
            {'k1': 'Bangkok', 'k2': 'Thailand', 'k3': '4604 €', 'k4': '460 €'},
            {'k1': 'Banjul', 'k2': 'Gambia', 'k3': '5396 €', 'k4': '540 €'},
            {'k1': 'Basse-terre', 'k2': 'Saint Kitts and Nevis', 'k3': '4326 €', 'k4': '433 €'},
            {'k1': 'Belgrade', 'k2': 'Serbia', 'k3': '2378 €', 'k4': '238 €'},
            {'k1': 'Belmopan', 'k2': 'Belize', 'k3': '2425 €', 'k4': '242 €'},
            {'k1': 'Berlin', 'k2': 'Germany', 'k3': '5960 €', 'k4': '596 €'},
            {'k1': 'Berne', 'k2': 'Switzerland', 'k3': '7202 €', 'k4': '720 €'},
            {'k1': 'Beyrouth', 'k2': 'Lebanon', 'k3': '3747 €', 'k4': '375 €'},
            {'k1': 'Bichkek', 'k2': 'Kyrgyzstan', 'k3': '808 €', 'k4': '81 €'},
            {'k1': 'Bissau', 'k2': 'Guinea-Bissau', 'k3': '685 €', 'k4': '68 €'},
            {'k1': 'Bloemfontein', 'k2': 'South Africa', 'k3': '640 €', 'k4': '64 €'},
            {'k1': 'Bogota', 'k2': 'Colombia', 'k3': '1561 €', 'k4': '156 €'},
            {'k1': 'Brasilia', 'k2': 'Brazil', 'k3': '2127 €', 'k4': '213 €'},
            {'k1': 'Bratislava', 'k2': 'Slovakia', 'k3': '2953 €', 'k4': '295 €'},
            {'k1': 'Brazzaville', 'k2': 'Republic of Congo', 'k3': '6502 €', 'k4': '650 €'},
            {'k1': 'Bridgetown', 'k2': 'Barbade', 'k3': '2312 €', 'k4': '231 €'},
            {'k1': 'Bruxelles', 'k2': 'Belgium', 'k3': '3194 €', 'k4': '319 €'},
            {'k1': 'Bucarest', 'k2': 'Romania', 'k3': '1709 €', 'k4': '171 €'},
            {'k1': 'Budapest', 'k2': 'Hungary', 'k3': '2819 €', 'k4': '282 €'},
            {'k1': 'Buenos Aires', 'k2': 'Argentina', 'k3': '2550 €', 'k4': '255 €'},
            {'k1': 'Bujumbura', 'k2': 'Burundi', 'k3': '8126 €', 'k4': '813 €'},
            {'k1': 'Cairo', 'k2': 'Egypt', 'k3': '632 €', 'k4': '63 €'},
            {'k1': 'Canberra', 'k2': 'Australia', 'k3': '3754 €', 'k4': '375 €'},
            {'k1': 'Caracas', 'k2': 'Venezuela', 'k3': '685 €', 'k4': '69 €'},
            {'k1': 'Castries', 'k2': 'St. LUCIA', 'k3': '222 €', 'k4': '22 €'},
            {'k1': 'Chisinau', 'k2': 'Moldova', 'k3': '862 €', 'k4': '86 €'},
            {'k1': 'Sri Jayawardenapura Kotte', 'k2': 'Sri Lanka', 'k3': '30 €', 'k4': '3 €'},
            {'k1': 'Copenhague', 'k2': 'Denmark', 'k3': '6456 €', 'k4': '646 €'},
            {'k1': 'Dakar', 'k2': 'Senegal', 'k3': '9716 €', 'k4': '972 €'},
            {'k1': 'Damas', 'k2': 'Syria', 'k3': '1832 €', 'k4': '183 €'},
            {'k1': 'Dar es Salam', 'k2': 'Tanzanie', 'k3': '784 €', 'k4': '78 €'},
            {'k1': 'Dili', 'k2': 'East Timor', 'k3': '1802 €', 'k4': '180 €'},
            {'k1': 'Djibouti', 'k2': 'Djibouti', 'k3': '608 €', 'k4': '61 €'},
            {'k1': 'Doha', 'k2': 'Qatar', 'k3': '3870 €', 'k4': '387 €'},
            {'k1': 'Douchanbé', 'k2': 'Tajikistan', 'k3': '603 €', 'k4': '60 €'},
            {'k1': 'Dublin', 'k2': 'Ireland', 'k3': '5734 €', 'k4': '573 €'},
            {'k1': 'Erevan', 'k2': 'Armenia', 'k3': '1314 €', 'k4': '131 €'},
            {'k1': 'Gaborone', 'k2': 'Botswana', 'k3': '1022 €', 'k4': '102 €'},
            {'k1': 'Georgetown', 'k2': 'Guyana', 'k3': '4541 €', 'k4': '454 €'},
            {'k1': 'Guatemala', 'k2': 'Guatemala', 'k3': '1446 €', 'k4': '145 €'},
            {'k1': 'Hanoï', 'k2': 'Vietnam', 'k3': '1907 €', 'k4': '191 €'},
            {'k1': 'Harare', 'k2': 'Zimbabwe', 'k3': '5 €', 'k4': ' €'},
            {'k1': 'Havana', 'k2': 'Cuba', 'k3': '327 €', 'k4': '33 €'},
            {'k1': 'The Hague', 'k2': 'Netherlands', 'k3': '3554 €', 'k4': '355 €'},
            {'k1': 'Helsinki', 'k2': 'Finland', 'k3': '7133 €', 'k4': '713 €'},
            {'k1': 'Honiara', 'k2': 'Salomon', 'k3': '2812 €', 'k4': '281 €'},
            {'k1': 'Islamabad', 'k2': 'Pakistan', 'k3': '611 €', 'k4': '61 €'},
            {'k1': 'Jakarta', 'k2': 'Indonesia', 'k3': '1905 €', 'k4': '190 €'},
            {'k1': 'Jerusalem', 'k2': 'Israel', 'k3': '8524 €', 'k4': '852 €'},
            {'k1': 'Kaboul', 'k2': 'Afghanistan', 'k3': '669 €', 'k4': '67 €'},
            {'k1': 'Kampala', 'k2': 'Uganda', 'k3': '2443 €', 'k4': '244 €'},
            {'k1': 'Katmandou', 'k2': 'Nepal', 'k3': '1417 €', 'k4': '142 €'},
            {'k1': 'Khartoum', 'k2': 'Sudan', 'k3': '578 €', 'k4': '58 €'},
            {'k1': 'Kiev', 'k2': 'Ukraine', 'k3': '1655 €', 'k4': '166 €'},
            {'k1': 'Kigali', 'k2': 'Rwanda', 'k3': '3443 €', 'k4': '344 €'},
            {'k1': 'Kingston', 'k2': 'Jamaica', 'k3': '979 €', 'k4': '98 €'},
            {'k1': 'Kingstown', 'k2': 'Saint Vincent and the Grenadines', 'k3': '1067 €', 'k4': '107 €'},
            {'k1': 'Kinshasa', 'k2': 'Democratic Republic of Congo', 'k3': '7661 €', 'k4': '766 €'},
            {'k1': 'Koweït', 'k2': 'Koweït', 'k3': '6244 €', 'k4': '624 €'},
            {'k1': 'Kuala Lumpur', 'k2': 'Malaysia', 'k3': '2623 €', 'k4': '262 €'},
            {'k1': 'Libreville', 'k2': 'Gabon', 'k3': '10764 €', 'k4': '1076 €'},
            {'k1': 'Lilongwe', 'k2': 'Malawi', 'k3': '368 €', 'k4': '37 €'},
            {'k1': 'Lima', 'k2': 'Peru', 'k3': '1597 €', 'k4': '160 €'},
            {'k1': 'Lisbon', 'k2': 'Portugal', 'k3': '4346 €', 'k4': '435 €'},
            {'k1': 'Ljubljana', 'k2': 'Slovenia', 'k3': '3400 €', 'k4': '340 €'},
            {'k1': 'Lomé', 'k2': 'Togo', 'k3': '381 €', 'k4': '38 €'},
            {'k1': 'London', 'k2': 'UK', 'k3': '14277 €', 'k4': '1428 €'},
            {'k1': 'Luanda', 'k2': 'Angola', 'k3': '6188 €', 'k4': '619 €'},
            {'k1': 'Lusaka', 'k2': 'Zambia', 'k3': '32713 €', 'k4': '3271 €'},
            {'k1': 'Luxembourg', 'k2': 'Luxembourg', 'k3': '8698 €', 'k4': '870 €'},
            {'k1': 'Madrid', 'k2': 'Spain', 'k3': '5255 €', 'k4': '525 €'},
            {'k1': 'Malabo', 'k2': 'Equatorial Guinea', 'k3': '688 €', 'k4': '69 €'},
            {'k1': 'Male', 'k2': 'Maldives', 'k3': '3359 €', 'k4': '336 €'},
            {'k1': 'Managua', 'k2': 'Nicaragua', 'k3': '883 €', 'k4': '88 €'},
            {'k1': 'Manama', 'k2': 'Bahreïn', 'k3': '2584 €', 'k4': '258 €'},
            {'k1': 'Manila', 'k2': 'Philippines', 'k3': '2406 €', 'k4': '241 €'},
            {'k1': 'Maputo', 'k2': 'Mozambique', 'k3': '1301 €', 'k4': '130 €'},
            {'k1': 'Mascate', 'k2': 'Oman', 'k3': '3005 €', 'k4': '300 €'},
            {'k1': 'Maseru', 'k2': 'Lesotho', 'k3': '32178 €', 'k4': '3218 €'},
            {'k1': 'Mbabane', 'k2': 'Eswatini', 'k3': '416 €', 'k4': '42 €'},
            {'k1': 'Mexico', 'k2': 'Mexico', 'k3': '2076 €', 'k4': '208 €'},
            {'k1': 'Minsk', 'k2': 'Belarus', 'k3': '1479 €', 'k4': '148 €'},
            {'k1': 'Mogadiscio', 'k2': 'Somalia', 'k3': '25576 €', 'k4': '2558 €'},
            {'k1': 'Monaco', 'k2': 'Monaco', 'k3': '50333 €', 'k4': '5033 €'},
            {'k1': 'Monrovia', 'k2': 'Liberia', 'k3': '6161 €', 'k4': '616 €'},
            {'k1': 'Montevideo', 'k2': 'Uruguay', 'k3': '2408 €', 'k4': '241 €'},
            {'k1': 'Moscou', 'k2': 'Russia', 'k3': '4601 €', 'k4': '460 €'},
            {'k1': 'Nairobi', 'k2': 'Kenya', 'k3': '1883 €', 'k4': '188 €'},
            {'k1': 'Nassau', 'k2': 'Bahamas', 'k3': '1263 €', 'k4': '126 €'},
            {'k1': 'New Delhi', 'k2': 'India', 'k3': '1657 €', 'k4': '166 €'},
            {'k1': 'Nicosia', 'k2': 'Cyprus', 'k3': '1700 €', 'k4': '170 €'},
            {'k1': 'Nouakchott', 'k2': 'Mauritania', 'k3': '7235 €', 'k4': '723 €'},
            {'k1': 'Astana', 'k2': 'Kazakhstan', 'k3': '845 €', 'k4': '84 €'},
            {'k1': 'Nukualofa', 'k2': 'Tonga', 'k3': '1307 €', 'k4': '131 €'},
            {'k1': 'Oslo', 'k2': 'Norway', 'k3': '7942 €', 'k4': '794 €'},
            {'k1': 'Ottawa', 'k2': 'Canada', 'k3': '3275 €', 'k4': '327 €'},
            {'k1': 'Ouagadougou', 'k2': 'Burkina Faso', 'k3': '13720 €', 'k4': '1372 €'},
            {'k1': 'Oulan-Bator', 'k2': 'Mongolia', 'k3': '1084 €', 'k4': '108 €'},
            {'k1': 'Panama', 'k2': 'Panama', 'k3': '1967 €', 'k4': '197 €'},
            {'k1': 'Paramaribo', 'k2': 'Suriname', 'k3': '418 €', 'k4': '42 €'},
            {'k1': 'Paris', 'k2': 'France', 'k3': '10889 €', 'k4': '1089 €'},
            {'k1': 'La Paz', 'k2': 'Bolivia', 'k3': '1101 €', 'k4': '110 €'},
            {'k1': 'Pekin', 'k2': 'China', 'k3': '13550 €', 'k4': '1355 €'},
            {'k1': 'Phnom Penh', 'k2': 'Cambodia', 'k3': '1956 €', 'k4': '196 €'},
            {'k1': 'Podgorica', 'k2': 'Montenegro', 'k3': '1338 €', 'k4': '134 €'},
            {'k1': 'Port Moresby', 'k2': 'Papua New Guinea', 'k3': '9974 €', 'k4': '997 €'},
            {'k1': 'Port-au-Prince', 'k2': 'Haïti', 'k3': '2257 €', 'k4': '226 €'},
            {'k1': 'Port of Spain', 'k2': 'Trinidad and Tobago', 'k3': '1049 €', 'k4': '105 €'},
            {'k1': 'Port-Louis', 'k2': 'Mauritius', 'k3': '839 €', 'k4': '84 €'},
            {'k1': 'Port-Vila', 'k2': 'Vanuatu', 'k3': '1371 €', 'k4': '137 €'},
            {'k1': 'Prague', 'k2': 'Czech republic', 'k3': '4848 €', 'k4': '485 €'},
            {'k1': 'Praia', 'k2': 'Green cap', 'k3': '725 €', 'k4': '73 €'},
            {'k1': 'Pretoria', 'k2': 'South Africa', 'k3': '492 €', 'k4': '49 €'},
            {'k1': 'Putrajaya', 'k2': 'Malaysia', 'k3': '1678 €', 'k4': '168 €'},
            {'k1': 'Quito', 'k2': 'Ecuador', 'k3': '1451 €', 'k4': '145 €'},
            {'k1': 'Rabat', 'k2': 'Morocco', 'k3': '1750 €', 'k4': '175 €'},
            {'k1': 'Ramallah', 'k2': 'Palestine', 'k3': '812 €', 'k4': '81 €'},
            {'k1': 'Reykjavik', 'k2': 'Iceland', 'k3': '4293 €', 'k4': '429 €'},
            {'k1': 'Riga', 'k2': 'Latvia', 'k3': '1804 €', 'k4': '180 €'},
            {'k1': 'Riyad', 'k2': 'Saudi Arabia', 'k3': '1153 €', 'k4': '115 €'},
            {'k1': 'Roma', 'k2': 'Italy', 'k3': '6661 €', 'k4': '666 €'},
            {'k1': 'Roseau', 'k2': 'Dominica', 'k3': '109 €', 'k4': '11 €'},
            {'k1': 'Santo Domingo', 'k2': 'Dominican Republic', 'k3': '23811 €', 'k4': '2381 €'},
            {'k1': 'San jose', 'k2': 'Costa Rica', 'k3': '1197 €', 'k4': '120 €'},
            {'k1': 'San Salvador', 'k2': 'Salvador', 'k3': '1151 €', 'k4': '115 €'},
            {'k1': 'Sanaa', 'k2': 'Yemen', 'k3': '1323 €', 'k4': '132 €'},
            {'k1': 'Santiago', 'k2': 'Chile', 'k3': '2150 €', 'k4': '215 €'},
            {'k1': 'Sarajevo', 'k2': 'Bosnia and Herzegovina', 'k3': '1703 €', 'k4': '170 €'},
            {'k1': 'Seoul', 'k2': 'South Korea', 'k3': '11828 €', 'k4': '1183 €'},
            {'k1': 'Singapour', 'k2': 'Singapore', 'k3': '16224 €', 'k4': '1622 €'},
            {'k1': 'Skopje', 'k2': 'North Macedonia', 'k3': '115 €', 'k4': '11 €'},
            {'k1': 'Sofia', 'k2': 'Bulgaria', 'k3': '1491 €', 'k4': '149 €'},
            {'k1': 'Stockholm', 'k2': 'Sweden', 'k3': '8631 €', 'k4': '863 €'},
            {'k1': 'Sucre', 'k2': 'Bolivia', 'k3': '1085 €', 'k4': '109 €'},
            {'k1': 'Suva', 'k2': 'Fiji', 'k3': '1344 €', 'k4': '134 €'},
            {'k1': 'Tachkent', 'k2': 'Uzbekistan', 'k3': '799 €', 'k4': '80 €'},
            {'k1': 'Tallinn', 'k2': 'Estonia', 'k3': '2573 €', 'k4': '257 €'},
            {'k1': 'Tbilissi', 'k2': 'Georgia', 'k3': '872 €', 'k4': '87 €'},
            {'k1': 'Tegucigalpa', 'k2': 'Honduras', 'k3': '36 €', 'k4': '4 €'},
            {'k1': 'Tehran', 'k2': 'Iran', 'k3': '2368 €', 'k4': '237 €'},
            {'k1': 'Tel Aviv-Jaffa', 'k2': 'Israel', 'k3': '10698 €', 'k4': '1070 €'},
            {'k1': 'Thimphou', 'k2': 'Bhutan', 'k3': '629 €', 'k4': '63 €'},
            {'k1': 'Tirana', 'k2': 'Albania', 'k3': '1546 €', 'k4': '155 €'},
            {'k1': 'Tokyo', 'k2': 'Japan', 'k3': '9538 €', 'k4': '954 €'},
            {'k1': 'Tripoli', 'k2': 'Libya', 'k3': '1804 €', 'k4': '180 €'},
            {'k1': 'Tunis', 'k2': 'Tunisia', 'k3': '680 €', 'k4': '68 €'},
            {'k1': 'Vaduz', 'k2': 'Liechtenstein', 'k3': '1382 €', 'k4': '138 €'},
            {'k1': 'Valletta', 'k2': 'Malta', 'k3': '3925 €', 'k4': '393 €'},
            {'k1': 'Warsaw', 'k2': 'Poland', 'k3': '2944 €', 'k4': '294 €'},
            {'k1': 'Victoria', 'k2': 'Seychelles', 'k3': '1028 €', 'k4': '103 €'},
            {'k1': 'Vienna', 'k2': 'Austria', 'k3': '6254 €', 'k4': '625 €'},
            {'k1': 'Vientiane', 'k2': 'Laos', 'k3': '1083 €', 'k4': '108 €'},
            {'k1': 'Vilnius', 'k2': 'Lithuania', 'k3': '2660 €', 'k4': '266 €'},
            {'k1': 'Washington D.C.', 'k2': 'United States', 'k3': '5658 €', 'k4': '566 €'},
            {'k1': 'Wellington', 'k2': 'New Zealand', 'k3': '3840 €', 'k4': '384 €'},
            {'k1': 'Windhoek', 'k2': 'Namibia', 'k3': '1171 €', 'k4': '117 €'},
            {'k1': 'Abidjan', 'k2': 'Ivory Coast', 'k3': '1026 €', 'k4': '103 €'},
            {'k1': 'Yaounde', 'k2': 'Cameroon', 'k3': '114 €', 'k4': '11 €'},
            {'k1': 'Zagreb', 'k2': 'Croatia', 'k3': '2560 €', 'k4': '256 €'},
            {'k1': 'Average [€]', 'k2': '', 'k3': '3885 €', 'k4': '389 €'},
            {'k1': 'Lowest [€]', 'k2': 'Zimbabwe', 'k3': '5 €', 'k4': ' €'},
            {'k1': 'Highest [€]', 'k2': 'Monaco', 'k3': '50333 €', 'k4': '5033 €'}
        ]
    }
    return render(request, "contents/international_real_estate_price.html", context)


def international_plastic_waste(request):
    context = {
        'data': [
            {'k1': 'China', 'k2': '0,12', 'k3': '61570980638,26'},
            {'k1': 'United States', 'k2': '0,34', 'k3': '40581114388,15'},
            {'k1': 'Germany', 'k2': '0,49', 'k3': '14700551650,88'},
            {'k1': 'Brazil', 'k2': '0,17', 'k3': '12665413317,98'},
            {'k1': 'Nigeria', 'k2': '0,10', 'k3': '8002898215,28'},
            {'k1': 'Pakistan', 'k2': '0,10', 'k3': '7998753855,26'},
            {'k1': 'Japan', 'k2': '0,17', 'k3': '7884905799,33'},
            {'k1': 'Egypt', 'k2': '0,18', 'k3': '6356243859,37'},
            {'k1': 'Turkey', 'k2': '0,21', 'k3': '6345460389,16'},
            {'k1': 'Russia', 'k2': '0,11', 'k3': '6000411163,60'},
            {'k1': 'Indonesia', 'k2': '0,06', 'k3': '5589778277,78'},
            {'k1': 'United Kingdom', 'k2': '0,22', 'k3': '5215891177,48'},
            {'k1': 'South Africa', 'k2': '0,24', 'k3': '5056763085,60'},
            {'k1': 'India', 'k2': '0,01', 'k3': '4958191269,55'},
            {'k1': 'Spain', 'k2': '0,28', 'k3': '4721458818,75'},
            {'k1': 'France', 'k2': '0,19', 'k3': '4694848345,92'},
            {'k1': 'Iran', 'k2': '0,14', 'k3': '4305753568,80'},
            {'k1': 'Mexico', 'k2': '0,09', 'k3': '4042986646,56'},
            {'k1': 'Vietnam', 'k2': '0,10', 'k3': '3623971942,35'},
            {'k1': 'Thailand', 'k2': '0,14', 'k3': '3619472340,24'},
            {'k1': 'Éthiopie', 'k2': '0,10', 'k3': '3606292819,50'},
            {'k1': 'Argentina', 'k2': '0,18', 'k3': '2972010261,09'},
            {'k1': 'Italy', 'k2': '0,13', 'k3': '2958799934,35'},
            {'k1': 'Philippines', 'k2': '0,08', 'k3': '2944418344,88'},
            {'k1': 'Venezuela', 'k2': '0,25', 'k3': '2927549557,80'},
            {'k1': 'Sri Lanka', 'k2': '0,36', 'k3': '2823803299,91'},
            {'k1': 'Pays-Bas', 'k2': '0,42', 'k3': '2659157819,12'},
            {'k1': 'Colombia', 'k2': '0,14', 'k3': '2622333191,04'},
            {'k1': 'Malaisie', 'k2': '0,20', 'k3': '2352345282,54'},
            {'k1': 'Algeria', 'k2': '0,14', 'k3': '2260277993,52'},
            {'k1': 'Taiwan', 'k2': '0,25', 'k3': '2169335882,70'},
            {'k1': 'Bangladesh', 'k2': '0,03', 'k3': '2153734427,82'},
            {'k1': 'South Korea', 'k2': '0,11', 'k3': '2102286376,96'},
            {'k1': 'Saudi Arabia', 'k2': '0,16', 'k3': '1902573800,40'},
            {'k1': 'Trinidad and Tobago', 'k2': '3,60', 'k3': '1785979602,00'},
            {'k1': 'Guatemala', 'k2': '0,28', 'k3': '1771854890,40'},
            {'k1': 'Peru', 'k2': '0,14', 'k3': '1690444391,04'},
            {'k1': 'Syria', 'k2': '0,18', 'k3': '1643565321,12'},
            {'k1': 'Kurdistan', 'k2': '0,10', 'k3': '1606000000,00'},
            {'k1': 'Ukraine', 'k2': '0,10', 'k3': '1587291878,28'},
            {'k1': 'Sudan', 'k2': '0,10', 'k3': '1557764314,14'},
            {'k1': 'Democratic Republic of Congo', 'k2': '0,05', 'k3': '1523006794,58'},
            {'k1': 'Myanmar', 'k2': '0,08', 'k3': '1460285922,75'},
            {'k1': 'Ouganda', 'k2': '0,10', 'k3': '1445851797,00'},
            {'k1': 'Iraq', 'k2': '0,10', 'k3': '1433278622,29'},
            {'k1': 'Poland', 'k2': '0,10', 'k3': '1360017363,32'},
            {'k1': 'Yemen', 'k2': '0,10', 'k3': '1286964145,59'},
            {'k1': 'Canada', 'k2': '0,09', 'k3': '1274981226,62'},
            {'k1': 'Ouzbékistan', 'k2': '0,10', 'k3': '1191866802,50'},
            {'k1': 'Kuwait', 'k2': '0,69', 'k3': '1183760039,35'},
            {'k1': 'Afghanistan', 'k2': '0,10', 'k3': '1152488157,00'},
            {'k1': 'Népal', 'k2': '0,10', 'k3': '1084214286,50'},
            {'k1': 'Hong Kong', 'k2': '0,40', 'k3': '1082099523,95'},
            {'k1': 'Australia', 'k2': '0,11', 'k3': '1026312962,64'},
            {'k1': 'Portugal', 'k2': '0,27', 'k3': '995399586,58'},
            {'k1': 'Israël', 'k2': '0,30', 'k3': '976588123,50'},
            {'k1': 'Morocco', 'k2': '0,07', 'k3': '945413839,96'},
            {'k1': 'Cote Ivoire', 'k2': '0, 10', 'k3': '944304029, 36'},
            {'k1': 'Ecuador', 'k2': '0,15', 'k3': '901573013,25'},
            {'k1': 'Chile', 'k2': '0,12', 'k3': '829921926,96'},
            {'k1': 'Niger', 'k2': '0,10', 'k3': '786450717,50'},
            {'k1': 'Greece', 'k2': '0,20', 'k3': '784944180,00'},
            {'k1': 'Ireland', 'k2': '0,43', 'k3': '762337226,10'},
            {'k1': 'Mali', 'k2': '0,10', 'k3': '715189066,50'},
            {'k1': 'Burkina Faso', 'k2': '0,10', 'k3': '700435000,00'},
            {'k1': 'United Arab Emirates', 'k2': '0,20', 'k3': '693055205,53'},
            {'k1': 'Kazakhstan', 'k2': '0,10', 'k3': '673065876,50'},
            {'k1': 'Angola', 'k2': '0,06', 'k3': '659234892,08'},
            {'k1': 'Malawi', 'k2': '0,10', 'k3': '654008788,50'},
            {'k1': 'Honduras', 'k2': '0,19', 'k3': '624497819,09'},
            {'k1': 'Zambie', 'k2': '0,10', 'k3': '616401780,00'},
            {'k1': 'Sénégal', 'k2': '0,10', 'k3': '609382054,38'},
            {'k1': 'Tunisia', 'k2': '0,14', 'k3': '608753862,00'},
            {'k1': 'Nouvelle-Zélande', 'k2': '0,33', 'k3': '593584754,37'},
            {'k1': 'Tchad', 'k2': '0,10', 'k3': '553414606,00'},
            {'k1': 'Norway', 'k2': '0,28', 'k3': '542921454,60'},
            {'k1': 'Jordan', 'k2': '0,14', 'k3': '541660233,60'},
            {'k1': 'Zimbabwé', 'k2': '0,10', 'k3': '511947722,50'},
            {'k1': 'North Korea', 'k2': '0,05', 'k3': '504927646,11'},
            {'k1': 'Finland', 'k2': '0,23', 'k3': '472272630,57'},
            {'k1': 'Costa Rica', 'k2': '0,26', 'k3': '471170366,34'},
            {'k1': 'Soudan du Sud', 'k2': '0,10', 'k3': '469557462,00'},
            {'k1': 'Tanzania', 'k2': '0,02', 'k3': '455001973,39'},
            {'k1': 'Kenya', 'k2': '0,03', 'k3': '453825726,21'},
            {'k1': 'Ghana', 'k2': '0,04', 'k3': '442099840,60'},
            {'k1': 'Rwanda', 'k2': '0,10', 'k3': '441274816,50'},
            {'k1': 'Burundi', 'k2': '0,10', 'k3': '429232882,50'},
            {'k1': 'Bolivie', 'k2': '0,10', 'k3': '414724132,50'},
            {'k1': 'Cambodge', 'k2': '0,07', 'k3': '403626432,33'},
            {'k1': 'Cameroon', 'k2': '0,05', 'k3': '399585579,38'},
            {'k1': 'Singapore', 'k2': '0,19', 'k3': '399274859,99'},
            {'k1': 'Bulgarie', 'k2': '0,15', 'k3': '396282411,14'},
            {'k1': 'Tchéquie', 'k2': '0,10', 'k3': '388717700,00'},
            {'k1': 'Croatia', 'k2': '0,25', 'k3': '377623246,14'},
            {'k1': 'Haiti', 'k2': '0,09', 'k3': '375072430,50'},
            {'k1': 'Cuba', 'k2': '0,09', 'k3': '365113370,83'},
            {'k1': 'Azerbaïdjan', 'k2': '0,10', 'k3': '363822145,00'},
            {'k1': 'Hongrie', 'k2': '0,10', 'k3': '356910541,50'},
            {'k1': 'Salvador', 'k2': '0,15', 'k3': '356368032,51'},
            {'k1': 'Belarus', 'k2': '0,10', 'k3': '345915427,50'},
            {'k1': 'Libya', 'k2': '0,14', 'k3': '344236569,12'},
            {'k1': 'Papua New Guinea', 'k2': '0,10', 'k3': '338682753,21'},
            {'k1': 'Nicaragua', 'k2': '0,14', 'k3': '337191652,66'},
            {'k1': 'Belgium', 'k2': '0,08', 'k3': '332181244,00'},
            {'k1': 'Tadjikistan', 'k2': '0,10', 'k3': '325999604,00'},
            {'k1': 'Uruguay', 'k2': '0,25', 'k3': '322480500,30'},
            {'k1': 'Autriche', 'k2': '0,10', 'k3': '322012745,50'},
            {'k1': 'Suisse', 'k2': '0,10', 'k3': '311794789,50'},
            {'k1': 'Turkménistan', 'k2': '0,10', 'k3': '309563800,00'},
            {'k1': 'Roumanie', 'k2': '0,04', 'k3': '299304836,25'},
            {'k1': 'Puerto Rico', 'k2': '0,25', 'k3': '293890172,94'},
            {'k1': 'Somalia', 'k2': '0,05', 'k3': '268282073,70'},
            {'k1': 'Laos', 'k2': '0,10', 'k3': '263919272,50'},
            {'k1': 'Paraguay', 'k2': '0,10', 'k3': '257488264,50'},
            {'k1': 'Serbie', 'k2': '0,10', 'k3': '255552706,00'},
            {'k1': 'Liban', 'k2': '0,10', 'k3': '241964559,00'},
            {'k1': 'Kirghizistan', 'k2': '0,10', 'k3': '228370645,00'},
            {'k1': 'Panama', 'k2': '0,15', 'k3': '220168846,80'},
            {'k1': 'République centrafricaine', 'k2': '0,10', 'k3': '209697427,50'},
            {'k1': 'Lebanon', 'k2': '0,09', 'k3': '206088779,08'},
            {'k1': 'Slovaquie', 'k2': '0,10', 'k3': '198940366,50'},
            {'k1': 'Bosnia and Herzegovina', 'k2': '0,14', 'k3': '183016074,96'},
            {'k1': 'Somaliland', 'k2': '0,10', 'k3': '181741457,00'},
            {'k1': 'Benin', 'k2': '0,04', 'k3': '180431917,30'},
            {'k1': 'Pount', 'k2': '0,10', 'k3': '179041479,00'},
            {'k1': 'Sweden', 'k2': '0,05', 'k3': '178637021,04'},
            {'k1': 'Guyana', 'k2': '0,59', 'k3': '177335343,44'},
            {'k1': 'Liberia', 'k2': '0,08', 'k3': '162821401,68'},
            {'k1': 'Mozambique', 'k2': '0,02', 'k3': '162237795,15'},
            {'k1': 'Qatar', 'k2': '0,16', 'k3': '160245628,80'},
            {'k1': 'Togo', 'k2': '0,06', 'k3': '152974608,71'},
            {'k1': 'Madagascar', 'k2': '0,02', 'k3': '149779940,00'},
            {'k1': 'Oman', 'k2': '0,08', 'k3': '143158499,82'},
            {'k1': 'Lithuania', 'k2': '0,13', 'k3': '134695573,32'},
            {'k1': 'Congo', 'k2': '0,07', 'k3': '132964635,65'},
            {'k1': 'Guinea', 'k2': '0,03', 'k3': '130124500,20'},
            {'k1': 'Moldavie', 'k2': '0,10', 'k3': '129485173,50'},
            {'k1': 'Namibia', 'k2': '0,14', 'k3': '123652235,52'},
            {'k1': 'Mongolie', 'k2': '0,10', 'k3': '117881787,00'},
            {'k1': 'Palestine', 'k2': '0,06', 'k3': '117086377,91'},
            {'k1': 'Sierra Leone', 'k2': '0,04', 'k3': '116651785,91'},
            {'k1': 'Cyprus', 'k2': '0,25', 'k3': '110348496,52'},
            {'k1': 'Slovenia', 'k2': '0,15', 'k3': '109557396,25'},
            {'k1': 'Arménie', 'k2': '0,10', 'k3': '108402883,00'},
            {'k1': 'Mauritius', 'k2': '0,23', 'k3': '106250226,15'},
            {'k1': 'Equatorial Guinea', 'k2': '0,14', 'k3': '105925955,04'},
            {'k1': 'Bhoutan', 'k2': '0,10', 'k3': '101783863,50'},
            {'k1': 'Denmark', 'k2': '0,05', 'k3': '99326712,34'},
            {'k1': 'Georgia', 'k2': '0,07', 'k3': '92569441,42'},
            {'k1': 'Macao', 'k2': '0,37', 'k3': '89110440,08'},
            {'k1': 'Latvia', 'k2': '0,12', 'k3': '87549993,54'},
            {'k1': 'Eritrea', 'k2': '0,05', 'k3': '85212045,90'},
            {'k1': 'Botswana', 'k2': '0,10', 'k3': '84865493,00'},
            {'k1': 'Estonia', 'k2': '0,18', 'k3': '84741103,92'},
            {'k1': 'Lesotho', 'k2': '0,10', 'k3': '79704575,50'},
            {'k1': 'Canaries', 'k2': '0,10', 'k3': '76946416,50'},
            {'k1': 'Bahrain', 'k2': '0,13', 'k3': '76706751,66'},
            {'k1': 'Macédoine du Nord', 'k2': '0,10', 'k3': '75778708,50'},
            {'k1': 'Albania', 'k2': '0,07', 'k3': '72289109,94'},
            {'k1': 'Kosovo', 'k2': '0,10', 'k3': '65645469,00'},
            {'k1': 'Mauritanie', 'k2': '0,05', 'k3': '65439006,75'},
            {'k1': 'Maldives', 'k2': '0,32', 'k3': '62754085,73'},
            {'k1': 'Comoros', 'k2': '0,20', 'k3': '62028420,11'},
            {'k1': 'Fiji', 'k2': '0,19', 'k3': '61410171,06'},
            {'k1': 'Barbados', 'k2': '0,57', 'k3': '59375181,45'},
            {'k1': 'Bahamas', 'k2': '0,39', 'k3': '56857579,35'},
            {'k1': 'Timor oriental', 'k2': '0,10', 'k3': '46041355,50'},
            {'k1': 'Reunion', 'k2': '0,14', 'k3': '45543555,36'},
            {'k1': 'Eswatini (Swaziland)', 'k2': '0,10', 'k3': '42312625,00'},
            {'k1': 'Djibouti', 'k2': '0,10', 'k3': '39437117,41'},
            {'k1': 'Gabon', 'k2': '0,05', 'k3': '39334438,89'},
            {'k1': 'Gambia', 'k2': '0,05', 'k3': '38680936,32'},
            {'k1': 'Iceland', 'k2': '0,28', 'k3': '35738774,25'},
            {'k1': 'Suriname', 'k2': '0,16', 'k3': '35589314,05'},
            {'k1': 'Malta', 'k2': '0,21', 'k3': '34880411,05'},
            {'k1': 'Saint Lucia', 'k2': '0,52', 'k3': '34046948,88'},
            {'k1': 'Jamaica', 'k2': '0,03', 'k3': '33865202,24'},
            {'k1': 'Martinique', 'k2': '0,25', 'k3': '33513280,92'},
            {'k1': 'Montenegro', 'k2': '0,14', 'k3': '32711189,04'},
            {'k1': 'Guinea-Bissau', 'k2': '0,05', 'k3': '31236230,61'},
            {'k1': 'Vanuatu', 'k2': '0,30', 'k3': '30726030,33'},
            {'k1': 'New Caledonia', 'k2': '0,25', 'k3': '25939555,74'},
            {'k1': 'French Polynesia', 'k2': '0,25', 'k3': '25378937,64'},
            {'k1': 'Solomon Islands', 'k2': '0,10', 'k3': '25077519,18'},
            {'k1': 'Antigua and Barbuda', 'k2': '0,66', 'k3': '25073835,60'},
            {'k1': 'Belize', 'k2': '0,17', 'k3': '24989579,00'},
            {'k1': 'Sahara occidental', 'k2': '0,10', 'k3': '23872898,00'},
            {'k1': 'Luxembourg', 'k2': '0,10', 'k3': '22407131,00'},
            {'k1': 'Netherlands Antilles', 'k2': '0,25', 'k3': '21183361,92'},
            {'k1': 'Guadeloupe', 'k2': '0,14', 'k3': '20114922,24'},
            {'k1': 'Transnistrie', 'k2': '0,10', 'k3': '18382860,00'},
            {'k1': 'Guam', 'k2': '0,25', 'k3': '16520159,88'},
            {'k1': 'French Guiana', 'k2': '0,14', 'k3': '15595130,16'},
            {'k1': 'Channel Islands', 'k2': '0,25', 'k3': '15412444,74'},
            {'k1': 'Curacao', 'k2': '0,25', 'k3': '14717903,76'},
            {'k1': 'Grenada', 'k2': '0,33', 'k3': '13697035,63'},
            {'k1': 'Saint Kitts and Nevis', 'k2': '0,65', 'k3': '13450114,95'},
            {'k1': 'Cape Verde', 'k2': '0,07', 'k3': '12908321,73'},
            {'k1': 'Seychelles', 'k2': '0,36', 'k3': '12677995,41'},
            {'k1': 'Aruba', 'k2': '0,25', 'k3': '10271682,54'},
            {'k1': 'Mayotte', 'k2': '0,10', 'k3': '9868578,00'},
            {'k1': 'Madère', 'k2': '0,10', 'k3': '9284432,00'},
            {'k1': 'Abkhazie', 'k2': '0,10', 'k3': '8990424,50'},
            {'k1': 'Açores', 'k2': '0,10', 'k3': '8900963,00'},
            {'k1': 'Saint Vincent and the Grenadines', 'k2': '0,22', 'k3': '8877102,59'},
            {'k1': 'Tonga', 'k2': '0,22', 'k3': '8030349,31'},
            {'k1': 'Sao Tome and Principe', 'k2': '0,10', 'k3': '7585543,15'},
            {'k1': 'Samoa', 'k2': '0,10', 'k3': '7490540,59'},
            {'k1': 'Cayman Islands', 'k2': '0,25', 'k3': '5925351,60'},
            {'k1': 'Guernsey', 'k2': '0,25', 'k3': '5797131,48'},
            {'k1': 'Bermuda', 'k2': '0,25', 'k3': '5665232,16'},
            {'k1': 'Artsakh (Haut-Karabakh)', 'k2': '0,10', 'k3': '5398569,00'},
            {'k1': 'Greenland', 'k2': '0,25', 'k3': '5153179,50'},
            {'k1': 'Northern Mariana Islands', 'k2': '0,25', 'k3': '4765207,86'},
            {'k1': 'Faeroe Islands', 'k2': '0,25', 'k3': '4719677,76'},
            {'k1': 'Kiribati', 'k2': '0,10', 'k3': '4312071,31'},
            {'k1': 'Brunei', 'k2': '0,03', 'k3': '4036884,67'},
            {'k1': 'Turks and Caicos Islands', 'k2': '0,25', 'k3': '3956335,74'},
            {'k1': 'Îles Vierges des États-Unis', 'k2': '0,10', 'k3': '3952877,00'},
            {'k1': 'Sint Maarten (Dutch part)', 'k2': '0,25', 'k3': '3943918,44'},
            {'k1': 'Dominican Republic', 'k2': '0,14', 'k3': '3925128,24'},
            {'k1': 'Marshall Islands', 'k2': '0,19', 'k3': '3900863,04'},
            {'k1': 'Micronesia (country)', 'k2': '0,10', 'k3': '3879653,62'},
            {'k1': 'Monaco', 'k2': '0,25', 'k3': '3522834,00'},
            {'k1': 'Gibraltar', 'k2': '0,25', 'k3': '3400868,52'},
            {'k1': 'British Virgin Islands', 'k2': '0,25', 'k3': '3030189,12'},
            {'k1': 'Man', 'k2': '0,10', 'k3': '3015593,50'},
            {'k1': 'Andorre', 'k2': '0,10', 'k3': '2793053,00'},
            {'k1': 'Ossétie du Sud-Alanie', 'k2': '0,10', 'k3': '2104298,00'},
            {'k1': 'Samoa américaines', 'k2': '0,10', 'k3': '1963335,00'},
            {'k1': 'Anguilla', 'k2': '0,25', 'k3': '1395704,52'},
            {'k1': 'Liechtenstein', 'k2': '0,10', 'k3': '1391161,00'},
            {'k1': 'Saint-Martin (France)', 'k2': '0,10', 'k3': '1304729,00'},
            {'k1': 'Saint-Marin', 'k2': '0,10', 'k3': '1219793,50'},
            {'k1': 'Palau', 'k2': '0,14', 'k3': '936619,20'},
            {'k1': 'Cook Islands', 'k2': '0,14', 'k3': '910759,68'},
            {'k1': 'Pays-Bas caribéens', 'k2': '0,10', 'k3': '896002,00'},
            {'k1': 'Nauru', 'k2': '0,14', 'k3': '667301,76'},
            {'k1': 'Saint Pierre and Miquelon', 'k2': '0,25', 'k3': '552615,84'},
            {'k1': 'Tuvalu', 'k2': '0,14', 'k3': '504838,80'},
            {'k1': 'Wallis-et-Futuna', 'k2': '0,10', 'k3': '422013,00'},
            {'k1': 'Saint-Barthélemy', 'k2': '0,10', 'k3': '357444,50'},
            {'k1': 'Falkland Islands', 'k2': '0,25', 'k3': '312548,04'},
            {'k1': 'Saint Helena', 'k2': '0,14', 'k3': '299854,80'},
            {'k1': 'Montserrat', 'k2': '0,14', 'k3': '280828,08'},
            {'k1': 'Niue', 'k2': '0,25', 'k3': '234089,10'},
            {'k1': 'Chagos', 'k2': '0,10', 'k3': '154723,50'},
            {'k1': 'Malouines', 'k2': '0,10', 'k3': '132020,50'},
            {'k1': 'Christmas Island', 'k2': '0,25', 'k3': '128955,96'},
            {'k1': 'Norfolk Island', 'k2': '0,10', 'k3': '66843,91'},
            {'k1': 'Tokelau', 'k2': '0,10', 'k3': '58497,82'},
            {'k1': 'Cocos Islands', 'k2': '0,25', 'k3': '54820,08'},
            {'k1': 'Antarctique', 'k2': '0,10', 'k3': '54750,00'},
            {'k1': 'Vatican', 'k2': '0,10', 'k3': '29346,00'},
            {'k1': 'Terres australes et antarctiques françaises (TAAF)', 'k2': '0,10', 'k3': '7154,00'},
            {'k1': 'Pitcairn', 'k2': '0,10', 'k3': '1825,00'},
            {'k1': 'Géorgie du Sud-et-les Îles Sandwich du Sud', 'k2': '0,10', 'k3': '1277,50'},
            {'k1': 'Total', 'k2': '0,17', 'k3': '320909931067,18'}
        ]
    }
    return render(request, "contents/international_plastic_waste.html", context)


def forecast_of_worldwide_coal_reserves(request):
    context = {
        'data': [
            {'k1': '2019', 'k2': '1069,6'},
            {'k1': '2020', 'k2': '1061,04'},
            {'k1': '2021', 'k2': '1052,55'},
            {'k1': '2022', 'k2': '1044,13'},
            {'k1': '2023', 'k2': '1035,78'},
            {'k1': '2024', 'k2': '1027,5'},
            {'k1': '2025', 'k2': '1019,28'},
            {'k1': '2026', 'k2': '1011,12'},
            {'k1': '2027', 'k2': '1003,03'},
            {'k1': '2028', 'k2': '995,01'},
            {'k1': '2029', 'k2': '987,05'},
            {'k1': '2030', 'k2': '979,15'},
            {'k1': '2031', 'k2': '971,32'},
            {'k1': '2032', 'k2': '963,55'},
            {'k1': '2033', 'k2': '955,84'},
            {'k1': '2034', 'k2': '948,19'},
            {'k1': '2035', 'k2': '940,61'},
            {'k1': '2036', 'k2': '933,08'},
            {'k1': '2037', 'k2': '925,62'},
            {'k1': '2038', 'k2': '918,21'},
            {'k1': '2039', 'k2': '910,87'},
            {'k1': '2040', 'k2': '903,58'},
            {'k1': '2041', 'k2': '896,35'},
            {'k1': '2042', 'k2': '889,18'},
            {'k1': '2043', 'k2': '882,07'},
            {'k1': '2044', 'k2': '875,01'},
            {'k1': '2045', 'k2': '868,01'},
            {'k1': '2046', 'k2': '861,07'},
            {'k1': '2047', 'k2': '854,18'},
            {'k1': '2048', 'k2': '847,34'},
            {'k1': '2049', 'k2': '840,57'},
            {'k1': '2050', 'k2': '833,84'},
            {'k1': '2051', 'k2': '827,17'},
            {'k1': '2052', 'k2': '820,55'},
            {'k1': '2053', 'k2': '813,99'},
            {'k1': '2054', 'k2': '807,48'},
            {'k1': '2055', 'k2': '801,02'},
            {'k1': '2056', 'k2': '794,61'},
            {'k1': '2057', 'k2': '788,25'},
            {'k1': '2058', 'k2': '781,95'},
            {'k1': '2059', 'k2': '775,69'},
            {'k1': '2060', 'k2': '769,48'},
            {'k1': '2061', 'k2': '763,33'},
            {'k1': '2062', 'k2': '757,22'},
            {'k1': '2063', 'k2': '751,16'},
            {'k1': '2064', 'k2': '745,16'},
            {'k1': '2065', 'k2': '739,19'},
            {'k1': '2066', 'k2': '733,28'},
            {'k1': '2067', 'k2': '727,41'},
            {'k1': '2068', 'k2': '721,59'},
            {'k1': '2069', 'k2': '715,82'},
            {'k1': '2070', 'k2': '710,1'},
            {'k1': '2071', 'k2': '704,41'},
            {'k1': '2072', 'k2': '698,78'},
            {'k1': '2073', 'k2': '693,19'},
            {'k1': '2074', 'k2': '687,64'},
            {'k1': '2075', 'k2': '682,14'},
            {'k1': '2076', 'k2': '676,69'},
            {'k1': '2077', 'k2': '671,27'},
            {'k1': '2078', 'k2': '665,9'},
            {'k1': '2079', 'k2': '660,57'},
            {'k1': '2080', 'k2': '655,29'},
            {'k1': '2081', 'k2': '650,05'},
            {'k1': '2082', 'k2': '644,85'},
            {'k1': '2083', 'k2': '639,69'},
            {'k1': '2084', 'k2': '634,57'},
            {'k1': '2085', 'k2': '629,49'},
            {'k1': '2086', 'k2': '624,46'},
            {'k1': '2087', 'k2': '619,46'},
            {'k1': '2088', 'k2': '614,51'},
            {'k1': '2089', 'k2': '609,59'},
            {'k1': '2090', 'k2': '604,71'},
            {'k1': '2091', 'k2': '599,88'},
            {'k1': '2092', 'k2': '595,08'},
            {'k1': '2093', 'k2': '590,32'},
            {'k1': '2094', 'k2': '585,59'},
            {'k1': '2095', 'k2': '580,91'},
            {'k1': '2096', 'k2': '576,26'},
            {'k1': '2097', 'k2': '571,65'},
            {'k1': '2098', 'k2': '567,08'},
            {'k1': '2099', 'k2': '562,54'},
            {'k1': '2100', 'k2': '558,04'}
        ]
    }
    return render(request, "contents/forecast_of_worldwide_coal_reserves.html", context)


def forcecast_of_worldwide_crude_oil_reserves(request):
    context = {
        'data': [
            {'k1': '2014', 'k2': '186610000000'},
            {'k1': '2015', 'k2': '177279500000'},
            {'k1': '2016', 'k2': '168415525000'},
            {'k1': '2017', 'k2': '159994748750'},
            {'k1': '2018', 'k2': '151995011313'},
            {'k1': '2019', 'k2': '144395260747'},
            {'k1': '2020', 'k2': '137175497710'},
            {'k1': '2021', 'k2': '130316722824'},
            {'k1': '2022', 'k2': '123800886683'},
            {'k1': '2023', 'k2': '117610842349'},
            {'k1': '2024', 'k2': '111730300231'},
            {'k1': '2025', 'k2': '106143785220'},
            {'k1': '2026', 'k2': '100836595959'},
            {'k1': '2027', 'k2': '95794766161'},
            {'k1': '2028', 'k2': '91005027853'},
            {'k1': '2029', 'k2': '86454776460'},
            {'k1': '2030', 'k2': '82132037637'},
            {'k1': '2031', 'k2': '78025435755'},
            {'k1': '2032', 'k2': '74124163967'},
            {'k1': '2033', 'k2': '70417955769'},
            {'k1': '2034', 'k2': '66897057981'},
            {'k1': '2035', 'k2': '63552205082'},
            {'k1': '2036', 'k2': '60374594828'},
            {'k1': '2037', 'k2': '57355865086'},
            {'k1': '2038', 'k2': '54488071832'},
            {'k1': '2039', 'k2': '51763668240'},
            {'k1': '2040', 'k2': '49175484828'},
            {'k1': '2041', 'k2': '46716710587'},
            {'k1': '2042', 'k2': '44380875057'},
            {'k1': '2043', 'k2': '42161831305'},
            {'k1': '2044', 'k2': '40053739739'},
            {'k1': '2045', 'k2': '38051052752'},
            {'k1': '2046', 'k2': '36148500115'},
            {'k1': '2047', 'k2': '34341075109'},
            {'k1': '2048', 'k2': '32624021354'},
            {'k1': '2049', 'k2': '30992820286'},
            {'k1': '2050', 'k2': '29443179272'},
            {'k1': '2051', 'k2': '27971020308'},
            {'k1': '2052', 'k2': '26572469293'},
            {'k1': '2053', 'k2': '25243845828'},
            {'k1': '2054', 'k2': '23981653537'},
            {'k1': '2055', 'k2': '22782570860'},
            {'k1': '2056', 'k2': '21643442317'},
            {'k1': '2057', 'k2': '20561270201'},
            {'k1': '2058', 'k2': '19533206691'},
            {'k1': '2059', 'k2': '18556546356'},
            {'k1': '2060', 'k2': '17628719039'},
            {'k1': '2061', 'k2': '16747283087'},
            {'k1': '2062', 'k2': '15909918932'},
            {'k1': '2063', 'k2': '15114422986'},
            {'k1': '2064', 'k2': '14358701836'},
            {'k1': '2065', 'k2': '13640766745'},
            {'k1': '2066', 'k2': '12958728407'},
            {'k1': '2067', 'k2': '12310791987'},
            {'k1': '2068', 'k2': '11695252388'},
            {'k1': '2069', 'k2': '11110489768'},
            {'k1': '2070', 'k2': '10554965280'},
            {'k1': '2071', 'k2': '10027217016'},
            {'k1': '2072', 'k2': '9525856165'},
            {'k1': '2073', 'k2': '9049563357'},
            {'k1': '2074', 'k2': '8597085189'},
            {'k1': '2075', 'k2': '8167230930'},
            {'k1': '2076', 'k2': '7758869383'},
            {'k1': '2077', 'k2': '7370925914'},
            {'k1': '2078', 'k2': '7002379618'},
            {'k1': '2079', 'k2': '6652260637'},
            {'k1': '2080', 'k2': '6319647605'},
            {'k1': '2081', 'k2': '6003665225'},
            {'k1': '2082', 'k2': '5703481964'},
            {'k1': '2083', 'k2': '5418307866'},
            {'k1': '2084', 'k2': '5147392472'},
            {'k1': '2085', 'k2': '4890022849'},
            {'k1': '2086', 'k2': '4645521706'},
            {'k1': '2087', 'k2': '4413245621'},
            {'k1': '2088', 'k2': '4192583340'},
            {'k1': '2089', 'k2': '3982954173'},
            {'k1': '2090', 'k2': '3783806464'},
            {'k1': '2091', 'k2': '3594616141'},
            {'k1': '2092', 'k2': '3414885334'},
            {'k1': '2093', 'k2': '3244141067'},
            {'k1': '2094', 'k2': '3081934014'},
            {'k1': '2095', 'k2': '2927837313'},
            {'k1': '2096', 'k2': '2781445448'},
            {'k1': '2097', 'k2': '2642373175'},
            {'k1': '2098', 'k2': '2510254516'},
            {'k1': '2099', 'k2': '2384741791'},
            {'k1': '2100', 'k2': '2265504701'}
        ]
    }
    return render(request, "contents/forcecast_of_worldwide_crude_oil_reserves.html", context)


def forecast_of_worldwide_uranium_reserves(request):
    context = {
        'data': [
            {'k1': '2009', 'k2': '7813591'},
            {'k1': '2010', 'k2': '7758896'},
            {'k1': '2011', 'k2': '7704584'},
            {'k1': '2012', 'k2': '7650652'},
            {'k1': '2013', 'k2': '7597097'},
            {'k1': '2014', 'k2': '7543917'},
            {'k1': '2015', 'k2': '7491110'},
            {'k1': '2016', 'k2': '7438672'},
            {'k1': '2017', 'k2': '7386601'},
            {'k1': '2018', 'k2': '7334895'},
            {'k1': '2019', 'k2': '7283551'},
            {'k1': '2020', 'k2': '7232566'},
            {'k1': '2021', 'k2': '7181938'},
            {'k1': '2022', 'k2': '7131665'},
            {'k1': '2023', 'k2': '7081743'},
            {'k1': '2024', 'k2': '7032171'},
            {'k1': '2025', 'k2': '6982945'},
            {'k1': '2026', 'k2': '6934065'},
            {'k1': '2027', 'k2': '6885526'},
            {'k1': '2028', 'k2': '6837328'},
            {'k1': '2029', 'k2': '6789466'},
            {'k1': '2030', 'k2': '6741940'},
            {'k1': '2031', 'k2': '6694747'},
            {'k1': '2032', 'k2': '6647883'},
            {'k1': '2033', 'k2': '6601348'},
            {'k1': '2034', 'k2': '6555139'},
            {'k1': '2035', 'k2': '6509253'},
            {'k1': '2036', 'k2': '6463688'},
            {'k1': '2037', 'k2': '6418442'},
            {'k1': '2038', 'k2': '6373513'},
            {'k1': '2039', 'k2': '6328898'},
            {'k1': '2040', 'k2': '6284596'},
            {'k1': '2041', 'k2': '6240604'},
            {'k1': '2042', 'k2': '6196920'},
            {'k1': '2043', 'k2': '6153541'},
            {'k1': '2044', 'k2': '6110467'},
            {'k1': '2045', 'k2': '6067693'},
            {'k1': '2046', 'k2': '6025219'},
            {'k1': '2047', 'k2': '5983043'},
            {'k1': '2048', 'k2': '5941162'},
            {'k1': '2049', 'k2': '5899573'},
            {'k1': '2050', 'k2': '5858276'},
            {'k1': '2051', 'k2': '5817269'},
            {'k1': '2052', 'k2': '5776548'},
            {'k1': '2053', 'k2': '5736112'},
            {'k1': '2054', 'k2': '5695959'},
            {'k1': '2055', 'k2': '5656087'},
            {'k1': '2056', 'k2': '5616495'},
            {'k1': '2057', 'k2': '5577179'},
            {'k1': '2058', 'k2': '5538139'},
            {'k1': '2059', 'k2': '5499372'},
            {'k1': '2060', 'k2': '5460876'},
            {'k1': '2061', 'k2': '5422650'},
            {'k1': '2062', 'k2': '5384692'},
            {'k1': '2063', 'k2': '5346999'},
            {'k1': '2064', 'k2': '5309570'},
            {'k1': '2065', 'k2': '5272403'},
            {'k1': '2066', 'k2': '5235496'},
            {'k1': '2067', 'k2': '5198848'},
            {'k1': '2068', 'k2': '5162456'},
            {'k1': '2069', 'k2': '5126318'},
            {'k1': '2070', 'k2': '5090434'},
            {'k1': '2071', 'k2': '5054801'},
            {'k1': '2072', 'k2': '5019418'},
            {'k1': '2073', 'k2': '4984282'},
            {'k1': '2074', 'k2': '4949392'},
            {'k1': '2075', 'k2': '4914746'},
            {'k1': '2076', 'k2': '4880343'},
            {'k1': '2077', 'k2': '4846180'},
            {'k1': '2078', 'k2': '4812257'},
            {'k1': '2079', 'k2': '4778571'},
            {'k1': '2080', 'k2': '4745121'},
            {'k1': '2081', 'k2': '4711905'},
            {'k1': '2082', 'k2': '4678922'},
            {'k1': '2083', 'k2': '4646170'},
            {'k1': '2084', 'k2': '4613646'},
            {'k1': '2085', 'k2': '4581351'},
            {'k1': '2086', 'k2': '4549281'},
            {'k1': '2087', 'k2': '4517437'},
            {'k1': '2088', 'k2': '4485814'},
            {'k1': '2089', 'k2': '4454414'},
            {'k1': '2090', 'k2': '4423233'},
            {'k1': '2091', 'k2': '4392270'},
            {'k1': '2092', 'k2': '4361524'},
            {'k1': '2093', 'k2': '4330994'},
            {'k1': '2094', 'k2': '4300677'},
            {'k1': '2095', 'k2': '4270572'},
            {'k1': '2096', 'k2': '4240678'},
            {'k1': '2097', 'k2': '4210993'},
            {'k1': '2098', 'k2': '4181516'},
            {'k1': '2099', 'k2': '4152246'},
            {'k1': '2100', 'k2': '4123180'}
        ]
    }
    return render(request, "contents/forecast_of_worldwide_uranium_reserves.html", context)


def worldwide_mercury_producers(request):
    context = {
        'data': [
            {'k1': 'Finland', 'k2': 'Yes', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Russia', 'k2': 'Yes', 'k3': 'No', 'k4': 'Yes'},
            {'k1': 'Canada', 'k2': 'Yes', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Chile', 'k2': 'Yes', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Argentina', 'k2': 'Yes', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'China', 'k2': 'Yes', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Mexico', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Spain', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Algeria', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'USA', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Tchecoslovakia', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Turkey', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Yougoslavia', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Germany', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Australia', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Colombia', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Irland', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Italy', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Japan', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Peru', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'The Philippines', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Tunisia', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Thailand', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Ukrain', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Tadjikistan', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Kirghizistan', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Morocco', 'k2': 'No', 'k3': 'No', 'k4': 'No'},
            {'k1': 'Iran', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'},
            {'k1': 'Norway', 'k2': 'No', 'k3': 'Yes', 'k4': 'No'}
        ]
    }
    return render(request, "contents/worldwide_mercury_producers.html", context)


def countries_ratified_minamata_convention(request):
    context = {
        'data': [
            {'k1': 'Angola'},
            {'k1': 'Argentina'},
            {'k1': 'Armenia'},
            {'k1': 'Australia'},
            {'k1': 'Austria'},
            {'k1': 'Bangladesh'},
            {'k1': 'Belgium'},
            {'k1': 'Benin'},
            {'k1': 'Bolivia'},
            {'k1': 'Brazil'},
            {'k1': 'Bulgaria'},
            {'k1': 'Burkina Faso'},
            {'k1': 'Cambodia'},
            {'k1': 'Canada'},
            {'k1': 'Central African Republic'},
            {'k1': 'Chile'},
            {'k1': 'China'},
            {'k1': 'Colombia'},
            {'k1': 'Comoros'},
            {'k1': 'Costa Rica'},
            {'k1': 'Ivory Coast'},
            {'k1': 'Czech Republic'},
            {'k1': 'Denmark'},
            {'k1': 'Djibouti'},
            {'k1': 'Dominican Republic'},
            {'k1': 'Ecuador'},
            {'k1': 'Ethiopia'},
            {'k1': 'European Union'},
            {'k1': 'Finland'},
            {'k1': 'France'},
            {'k1': 'Gambia'},
            {'k1': 'Georgia'},
            {'k1': 'Germany'},
            {'k1': 'Greece'},
            {'k1': 'Guatemala'},
            {'k1': 'Guyana'},
            {'k1': 'Hungary'},
            {'k1': 'Indonesia'},
            {'k1': 'Iran'},
            {'k1': 'Iraq'},
            {'k1': 'Ireland'},
            {'k1': 'Israel'},
            {'k1': 'Italy'},
            {'k1': 'Jamaica'},
            {'k1': 'Japan'},
            {'k1': 'Jordan'},
            {'k1': 'Kenya'},
            {'k1': 'Kuwait'},
            {'k1': 'Libya'},
            {'k1': 'Lithuania'},
            {'k1': 'Luxembourg'},
            {'k1': 'Madagascar'},
            {'k1': 'Malawi'},
            {'k1': 'Mali'},
            {'k1': 'Mauritania'},
            {'k1': 'Mauritius'},
            {'k1': 'Mexico'},
            {'k1': 'Moldova'},
            {'k1': 'Mongolia'},
            {'k1': 'Mozambique'},
            {'k1': 'Nepal'},
            {'k1': 'Netherlands'},
            {'k1': 'New Zealand'},
            {'k1': 'Nicaragua'},
            {'k1': 'Niger'},
            {'k1': 'Nigeria'},
            {'k1': 'Norway'},
            {'k1': 'Pakistan'},
            {'k1': 'Panama'},
            {'k1': 'Peru'},
            {'k1': 'Philippines'},
            {'k1': 'Romania'},
            {'k1': 'Samoa'},
            {'k1': 'Senegal'},
            {'k1': 'Singapore'},
            {'k1': 'Slovakia'},
            {'k1': 'Slovenia'},
            {'k1': 'South Africa'},
            {'k1': 'Spain'},
            {'k1': 'Sweden'},
            {'k1': 'Switzerland'},
            {'k1': 'Tanzania'},
            {'k1': 'Togo'},
            {'k1': 'Tunisia'},
            {'k1': 'Uganda'},
            {'k1': 'United Arab Emirates'},
            {'k1': 'United Kingdom'},
            {'k1': 'Uruguay'},
            {'k1': 'Venezuela'},
            {'k1': 'Vietnam'},
            {'k1': 'Zambia'},
            {'k1': 'Zimbabwe'}
        ]
    }
    return render(request, "contents/countries_ratified_minamata_convention.html", context)


def communes_desservies_en_gaz_json(request):
    with open('static/contents/static/open_data_grdf/communes-desservies-en-gaz.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def les_sites_dinjection_de_biomethane_en_france_json(request):
    with open('static/contents/static/open_data_grdf/les-sites-dinjection-de-biomethane-en-france.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77304_parcelles_json(request):
    with open('static/contents/static/77304/cadastre-77304-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77304_batiments_json(request):
    with open('static/contents/static/77304/cadastre-77304-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77015_parcelles_json(request):
    with open('static/contents/static/77015/cadastre-77015-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77015_batiments_json(request):
    with open('static/contents/static/77015/cadastre-77015-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77356_parcelles_json(request):
    with open('static/contents/static/77356/cadastre-77356-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77356_batiments_json(request):
    with open('static/contents/static/77356/cadastre-77356-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77452_parcelles_json(request):
    with open('static/contents/static/77452/cadastre-77452-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77452_batiments_json(request):
    with open('static/contents/static/77452/cadastre-77452-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77532_parcelles_json(request):
    with open('static/contents/static/77532/cadastre-77532-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77532_batiments_json(request):
    with open('static/contents/static/77532/cadastre-77532-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78264_parcelles_json(request):
    with open('static/contents/static/78264/cadastre-78264-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78264_batiments_json(request):
    with open('static/contents/static/78264/cadastre-78264-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78606_parcelles_json(request):
    with open('static/contents/static/78606/cadastre-78606-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78606_batiments_json(request):
    with open('static/contents/static/78606/cadastre-78606-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91075_parcelles_json(request):
    with open('static/contents/static/91075/cadastre-91075-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91075_batiments_json(request):
    with open('static/contents/static/91075/cadastre-91075-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91145_parcelles_json(request):
    with open('static/contents/static/91145/cadastre-91145-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91145_batiments_json(request):
    with open('static/contents/static/91145/cadastre-91145-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95141_parcelles_json(request):
    with open('static/contents/static/95141/cadastre-95141-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95141_batiments_json(request):
    with open('static/contents/static/95141/cadastre-95141-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95144_parcelles_json(request):
    with open('static/contents/static/95144/cadastre-95144-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95144_batiments_json(request):
    with open('static/contents/static/95144/cadastre-95144-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95214_parcelles_json(request):
    with open('static/contents/static/95214/cadastre-95214-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95214_batiments_json(request):
    with open('static/contents/static/95214/cadastre-95214-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95387_parcelles_json(request):
    with open('static/contents/static/95387/cadastre-95387-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95387_batiments_json(request):
    with open('static/contents/static/95387/cadastre-95387-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95492_parcelles_json(request):
    with open('static/contents/static/95492/cadastre-95492-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95492_batiments_json(request):
    with open('static/contents/static/95492/cadastre-95492-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95611_parcelles_json(request):
    with open('static/contents/static/95611/cadastre-95611-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95611_batiments_json(request):
    with open('static/contents/static/95611/cadastre-95611-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95633_parcelles_json(request):
    with open('static/contents/static/95633/cadastre-95633-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95633_batiments_json(request):
    with open('static/contents/static/95633/cadastre-95633-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77010_parcelles_json(request):
    with open('static/contents/static/77010/cadastre-77010-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77010_batiments_json(request):
    with open('static/contents/static/77010/cadastre-77010-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77044_parcelles_json(request):
    with open('static/contents/static/77044/cadastre-77044-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77044_batiments_json(request):
    with open('static/contents/static/77044/cadastre-77044-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77071_parcelles_json(request):
    with open('static/contents/static/77071/cadastre-77071-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77071_batiments_json(request):
    with open('static/contents/static/77071/cadastre-77071-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77077_parcelles_json(request):
    with open('static/contents/static/77077/cadastre-77077-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77077_batiments_json(request):
    with open('static/contents/static/77077/cadastre-77077-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77089_parcelles_json(request):
    with open('static/contents/static/77089/cadastre-77089-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77089_batiments_json(request):
    with open('static/contents/static/77089/cadastre-77089-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77162_parcelles_json(request):
    with open('static/contents/static/77162/cadastre-77162-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77162_batiments_json(request):
    with open('static/contents/static/77162/cadastre-77162-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77172_parcelles_json(request):
    with open('static/contents/static/77172/cadastre-77172-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77172_batiments_json(request):
    with open('static/contents/static/77172/cadastre-77172-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77188_parcelles_json(request):
    with open('static/contents/static/77188/cadastre-77188-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77188_batiments_json(request):
    with open('static/contents/static/77188/cadastre-77188-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77196_parcelles_json(request):
    with open('static/contents/static/77196/cadastre-77196-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77196_batiments_json(request):
    with open('static/contents/static/77196/cadastre-77196-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77232_parcelles_json(request):
    with open('static/contents/static/77232/cadastre-77232-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77232_batiments_json(request):
    with open('static/contents/static/77232/cadastre-77232-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77283_parcelles_json(request):
    with open('static/contents/static/77283/cadastre-77283-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77283_batiments_json(request):
    with open('static/contents/static/77283/cadastre-77283-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77291_parcelles_json(request):
    with open('static/contents/static/77291/cadastre-77291-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77291_batiments_json(request):
    with open('static/contents/static/77291/cadastre-77291-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77293_parcelles_json(request):
    with open('static/contents/static/77293/cadastre-77293-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77293_batiments_json(request):
    with open('static/contents/static/77293/cadastre-77293-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77354_parcelles_json(request):
    with open('static/contents/static/77354/cadastre-77354-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77354_batiments_json(request):
    with open('static/contents/static/77354/cadastre-77354-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77406_parcelles_json(request):
    with open('static/contents/static/77406/cadastre-77406-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77406_batiments_json(request):
    with open('static/contents/static/77406/cadastre-77406-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77432_parcelles_json(request):
    with open('static/contents/static/77432/cadastre-77432-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77432_batiments_json(request):
    with open('static/contents/static/77432/cadastre-77432-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77480_parcelles_json(request):
    with open('static/contents/static/77480/cadastre-77480-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77480_batiments_json(request):
    with open('static/contents/static/77480/cadastre-77480-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77534_parcelles_json(request):
    with open('static/contents/static/77534/cadastre-77534-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_77534_batiments_json(request):
    with open('static/contents/static/77534/cadastre-77534-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78020_parcelles_json(request):
    with open('static/contents/static/78020/cadastre-78020-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78020_batiments_json(request):
    with open('static/contents/static/78020/cadastre-78020-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78034_parcelles_json(request):
    with open('static/contents/static/78034/cadastre-78034-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78034_batiments_json(request):
    with open('static/contents/static/78034/cadastre-78034-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78246_parcelles_json(request):
    with open('static/contents/static/78246/cadastre-78246-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78246_batiments_json(request):
    with open('static/contents/static/78246/cadastre-78246-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78289_parcelles_json(request):
    with open('static/contents/static/78289/cadastre-78289-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78289_batiments_json(request):
    with open('static/contents/static/78289/cadastre-78289-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78307_parcelles_json(request):
    with open('static/contents/static/78307/cadastre-78307-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78307_batiments_json(request):
    with open('static/contents/static/78307/cadastre-78307-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78381_parcelles_json(request):
    with open('static/contents/static/78381/cadastre-78381-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78381_batiments_json(request):
    with open('static/contents/static/78381/cadastre-78381-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78410_parcelles_json(request):
    with open('static/contents/static/78410/cadastre-78410-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78410_batiments_json(request):
    with open('static/contents/static/78410/cadastre-78410-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78443_parcelles_json(request):
    with open('static/contents/static/78443/cadastre-78443-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78443_batiments_json(request):
    with open('static/contents/static/78443/cadastre-78443-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78464_parcelles_json(request):
    with open('static/contents/static/78464/cadastre-78464-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78464_batiments_json(request):
    with open('static/contents/static/78464/cadastre-78464-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78497_parcelles_json(request):
    with open('static/contents/static/78497/cadastre-78497-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78497_batiments_json(request):
    with open('static/contents/static/78497/cadastre-78497-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78516_parcelles_json(request):
    with open('static/contents/static/78516/cadastre-78516-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78516_batiments_json(request):
    with open('static/contents/static/78516/cadastre-78516-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78557_parcelles_json(request):
    with open('static/contents/static/78557/cadastre-78557-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78557_batiments_json(request):
    with open('static/contents/static/78557/cadastre-78557-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78569_parcelles_json(request):
    with open('static/contents/static/78569/cadastre-78569-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78569_batiments_json(request):
    with open('static/contents/static/78569/cadastre-78569-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78588_parcelles_json(request):
    with open('static/contents/static/78588/cadastre-78588-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78588_batiments_json(request):
    with open('static/contents/static/78588/cadastre-78588-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78623_parcelles_json(request):
    with open('static/contents/static/78623/cadastre-78623-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_78623_batiments_json(request):
    with open('static/contents/static/78623/cadastre-78623-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91041_parcelles_json(request):
    with open('static/contents/static/91041/cadastre-91041-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91041_batiments_json(request):
    with open('static/contents/static/91041/cadastre-91041-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91293_parcelles_json(request):
    with open('static/contents/static/91293/cadastre-91293-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91293_batiments_json(request):
    with open('static/contents/static/91293/cadastre-91293-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91469_parcelles_json(request):
    with open('static/contents/static/91469/cadastre-91469-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91469_batiments_json(request):
    with open('static/contents/static/91469/cadastre-91469-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91546_parcelles_json(request):
    with open('static/contents/static/91546/cadastre-91546-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91546_batiments_json(request):
    with open('static/contents/static/91546/cadastre-91546-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91639_parcelles_json(request):
    with open('static/contents/static/91639/cadastre-91639-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_91639_batiments_json(request):
    with open('static/contents/static/91639/cadastre-91639-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95008_parcelles_json(request):
    with open('static/contents/static/95008/cadastre-95008-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95008_batiments_json(request):
    with open('static/contents/static/95008/cadastre-95008-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95101_parcelles_json(request):
    with open('static/contents/static/95101/cadastre-95101-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95101_batiments_json(request):
    with open('static/contents/static/95101/cadastre-95101-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95395_parcelles_json(request):
    with open('static/contents/static/95395/cadastre-95395-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95395_batiments_json(request):
    with open('static/contents/static/95395/cadastre-95395-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95541_parcelles_json(request):
    with open('static/contents/static/95541/cadastre-95541-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95541_batiments_json(request):
    with open('static/contents/static/95541/cadastre-95541-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95554_parcelles_json(request):
    with open('static/contents/static/95554/cadastre-95554-parcelles.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def cadastre_95554_batiments_json(request):
    with open('static/contents/static/95554/cadastre-95554-batiments.json') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)


def resume_of_mr_jason_aloyau(request):
    return render(request, "contents/resume_of_mr_jason_aloyau.html")


def sale_of_databases_of_mathematics(request):
    return render(request, "contents/sale_of_databases_of_mathematics.html")


def sale_of_database_of_mathematics_about_complex_variables(request):
    return render(request, "contents/sale_of_database_of_mathematics_about_complex_variables.html")


def sale_of_database_of_mathematics_about_quantum_groups(request):
    return render(request, 'contents/sale_of_database_of_mathematics_about_quantum_groups.html')


def sale_of_database_of_mathematics_about_non_commutative_algebra(request):
    return render(request, 'contents/sale_of_database_of_mathematics_about_non_commutative_algebra.html')


def sale_of_database_of_mathematics_about_factorization_divisibility(request):
    return render(request, 'contents/sale_of_database_of_mathematics_about_factorization_divisibility.html')


def sale_of_database_of_mathematics_about_matrix(request):
    return render(request, 'contents/sale_of_database_of_mathematics_about_matrix.html')


# http://www.leonland.de/elements_by_price/en/list
def mendeleev_table(request):
    context = {
        'data': [
            {
                'k1': 'Hydrogen',
                'k2': '1',
                'k3': 'H',
                'k4': '1.008',
                'k5': '3.70',
                'k6': 'No natural resources / Artificial production by methane vapor forming or '
                      'partial oxidation of oil or coal gasification or electrolysis of water or '
                      'electronic polarization of water molecule with Stanley Meyer water electrolyser / '
                      'United States / China / United Kingdom / European union / Canada / Russia / Norway'
            },
            {
                'k1': 'Helium',
                'k2': '2',
                'k3': 'He',
                'k4': '4.00260',
                'k5': '4.99',
                'k6': 'No natural resources / Artificial production by fractional distillation of natural gas, or '
                      'diffusion of raw natural gas through semi-permeable membranes or other barriers,'
                      ' or by bombarding lithium or boron with high-energy protons / United States'
            },
            {
                'k1': 'Lithium',
                'k2': '3',
                'k3': 'Li',
                'k4': '6.940',
                'k5': '9.39',
                'k6': 'Argentina / Australia / Bolivia / Brazil / Canada / Chile / China / '
                      'Democratic Republic of the Congo / United States / Germany / Mexico / Czech Republic / '
                      'Spain / Portugal / Mali / Russia / Serbia / Zimbabwe'
            },
            {
                'k1': 'Beryllium',
                'k2': '4',
                'k3': 'Be',
                'k4': '9.01218',
                'k5': '831.60',
                'k6': 'United States / China / Kazakhstan'
            },
        ]
    }
    return render(request, "contents/mendeleev_table.html", context)


def general_conditions_of_sales(request):
    return render(request, 'contents/general_conditions_of_sales.html')


def fundamental_research_of_inventions(request):
    return render(request, 'contents/fundamental_research_of_inventions/fundamental_research_of_inventions.html')


def fundamental_research_of_patent_us_4661747(request):
    return render(request, 'contents/fundamental_research_of_inventions/fundamental_research_of_patent_us_4661747A.html')
