from django.shortcuts import render


def vente_hydrogene(request):
    return render(request, "produitschimiques/index.html")


def fundamental_research_of_the_us_patent_us4936961a(request):
    return render(request, "produitschimiques/fundamental_research_of_the_us_patent_us4936961a.html")


def fundamental_research_of_the_us_patent_us4936961a_part_2(request):
    return render(request, "produitschimiques/fundamental_research_of_the_us_patent_us4936961a_part_2.html")


def cad_stanley_meyer_water_electrolyser(request):
    return render(request, "produitschimiques/cad_stanley_meyer_water_electrolyser.html")


def comparison_of_electrolysers(request):
    return render(request, "produitschimiques/comparison_of_electrolysers.html")


def investment(request):
    context = {
        "data_electrolyser": [
            {'k1': 'Bottom support', 'k2': '1', 'k3': '65,52 €', 'k4': '20', 'k5': '78,62 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '65,52 €', 'k10': '78,62 €', 'k11': '10080'},
            {'k1': 'Top support', 'k2': '1', 'k3': '64,98 €', 'k4': '20', 'k5': '77,98 €', 'k6': '0,00 €', 'k7': '20',
             'k8': '0,00 €', 'k9': '64,98 €', 'k10': '77,98 €', 'k11': '10080'},
            {'k1': 'Tank', 'k2': '1', 'k3': '639,20 €', 'k4': '20', 'k5': '767,04 €', 'k6': '0,00 €', 'k7': '20',
             'k8': '0,00 €', 'k9': '639,20 €', 'k10': '767,04 €', 'k11': '10080'},
            {'k1': 'Disk for the anodes', 'k2': '1', 'k3': '210,12 €', 'k4': '20', 'k5': '252,14 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '210,12 €', 'k10': '252,14 €', 'k11': '10080'},
            {'k1': 'Disk for the cathodes', 'k2': '1', 'k3': '180,09 €', 'k4': '20', 'k5': '216,11 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '180,09 €', 'k10': '216,11 €', 'k11': '10080'},
            {'k1': 'Anode', 'k2': '132', 'k3': '2,20 €', 'k4': '20', 'k5': '348,48 €', 'k6': '14,82 €', 'k7': '20',
             'k8': '17,78 €', 'k9': '17,02 €', 'k10': '366,26 €', 'k11': '10080'},
            {'k1': 'Cathode', 'k2': '132', 'k3': '5,03 €', 'k4': '20', 'k5': '797,28 €', 'k6': '14,82 €', 'k7': '20',
             'k8': '17,78 €', 'k9': '19,85 €', 'k10': '815,06 €', 'k11': '10080'},
            {'k1': 'Spacer between anode and cathode', 'k2': '264', 'k3': '5,50 €', 'k4': '20', 'k5': '1 742,40 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '5,50 €', 'k10': '1 742,40 €', 'k11': '10080'},
            {'k1': 'Ferrite core for the transformer', 'k2': '2', 'k3': '24,80 €', 'k4': '23', 'k5': '61,01 €',
             'k6': '7,90 €', 'k7': '23', 'k8': '9,72 €', 'k9': '57,50 €', 'k10': '70,73 €', 'k11': '2880'},
            {'k1': '24 AWG copper wire for the transformer', 'k2': '1', 'k3': '12,38 €', 'k4': '20', 'k5': '14,86 €',
             'k6': '7,90 €', 'k7': '23', 'k8': '9,72 €', 'k9': '20,28 €', 'k10': '24,57 €', 'k11': '2880'},
            {'k1': 'Transformer', 'k2': '1', 'k3': '47,16 €', 'k4': '20', 'k5': '56,59 €', 'k6': '0,00 €', 'k7': '20',
             'k8': '0,00 €', 'k9': '47,16 €', 'k10': '56,59 €', 'k11': '10080'},
            {'k1': 'Screw 5mm in diameter and 30 mm long', 'k2': '80', 'k3': '0,01 €', 'k4': '20', 'k5': '0,96 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '0,01 €', 'k10': '0,96 €', 'k11': '1440'},
            {'k1': 'Ring 5mm in diameter', 'k2': '320', 'k3': '0,01 €', 'k4': '20', 'k5': '3,84 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '0,01 €', 'k10': '3,84 €', 'k11': '1440'},
            {'k1': 'Nut in 5mm diameter', 'k2': '80', 'k3': '0,01 €', 'k4': '20', 'k5': '0,96 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '0,01 €', 'k10': '0,96 €', 'k11': '1440'},
            {'k1': 'Total', 'k2': '1017', 'k3': '1 257,01 €', 'k4': '-', 'k5': '4 418,27 €', 'k6': '45,43 €', 'k7': '-',
             'k8': '54,99 €', 'k9': '1 327,25 €', 'k10': '4 473,26 €', 'k11': '100800'},
        ],
        "data_hydrogen_container": [
            {'k1': 'Container', 'k2': '1', 'k3': '1 000,00 €', 'k4': '20', 'k5': '1 200,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '1 000,00 €', 'k10': '1 200,00 €', 'k11': '4320'},
            {'k1': 'Electrolyser', 'k2': '720', 'k3': '1 327,25 €', 'k4': '20', 'k5': '1 146 741,12 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '1 327,25 €', 'k10': '1 146 741,12 €', 'k11': '5184000'},
            {'k1': 'Raspberry Pi card', 'k2': '1', 'k3': '50,00 €', 'k4': '20', 'k5': '60,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '50,00 €', 'k10': '60,00 €', 'k11': '1440'},
            {'k1': 'Router 4G', 'k2': '1', 'k3': '50,00 €', 'k4': '20', 'k5': '60,00 €', 'k6': '0,00 €', 'k7': '20',
             'k8': '0,00 €', 'k9': '50,00 €', 'k10': '60,00 €', 'k11': '1440'},
            {'k1': 'Camera with IP Ethernet', 'k2': '1', 'k3': '50,00 €', 'k4': '20', 'k5': '60,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '50,00 €', 'k10': '60,00 €', 'k11': '1440'},
            {'k1': 'SIM card', 'k2': '1', 'k3': '20,00 €', 'k4': '20', 'k5': '24,00 €', 'k6': '0,00 €', 'k7': '20',
             'k8': '0,00 €', 'k9': '20,00 €', 'k10': '24,00 €', 'k11': '1440'},
            {'k1': 'Female nipple 12/17', 'k2': '2880', 'k3': '3,00 €', 'k4': '20', 'k5': '10 368,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '3,00 €', 'k10': '10 368,00 €', 'k11': '4147200'},
            {'k1': 'Male nipple 12/17', 'k2': '1440', 'k3': '3,00 €', 'k4': '20', 'k5': '5 184,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '3,00 €', 'k10': '5 184,00 €', 'k11': '2073600'},
            {'k1': '12/17 male faucet for gas', 'k2': '720', 'k3': '20,00 €', 'k4': '20', 'k5': '17 280,00 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '20,00 €', 'k10': '17 280,00 €', 'k11': '1036800'},
            {'k1': '12/17 male faucet for water', 'k2': '720', 'k3': '5,00 €', 'k4': '20', 'k5': '4 320,00 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '5,00 €', 'k10': '4 320,00 €', 'k11': '1036800'},
            {'k1': 'Flexible supply for water', 'k2': '720', 'k3': '10,00 €', 'k4': '20', 'k5': '8 640,00 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '10,00 €', 'k10': '8 640,00 €', 'k11': '1036800'},
            {'k1': 'Flexible supply for gas', 'k2': '720', 'k3': '50,00 €', 'k4': '20', 'k5': '43 200,00 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '50,00 €', 'k10': '43 200,00 €', 'k11': '1036800'},
            {'k1': 'Plumbing T', 'k2': '1440', 'k3': '4,00 €', 'k4': '20', 'k5': '6 912,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '4,00 €', 'k10': '6 912,00 €', 'k11': '2073600'},
            {'k1': 'Shelf 100 cm length / 50 cm width / 200 cm height', 'k2': '18', 'k3': '120,00 €', 'k4': '20',
             'k5': '2 592,00 €', 'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '120,00 €', 'k10': '2 592,00 €',
             'k11': '25920'},
            {'k1': 'Hydrogen gas pressure sensor', 'k2': '720', 'k3': '30,00 €', 'k4': '20', 'k5': '25 920,00 €',
             'k6': '0,00 €', 'k7': '20', 'k8': '0,00 €', 'k9': '30,00 €', 'k10': '25 920,00 €', 'k11': '1036800'},
            {'k1': 'Digital manometer', 'k2': '720', 'k3': '30,00 €', 'k4': '20', 'k5': '25 920,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '30,00 €', 'k10': '25 920,00 €', 'k11': '1036800'},
            {'k1': 'Hydrogen gas detector', 'k2': '4', 'k3': '30,00 €', 'k4': '20', 'k5': '144,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '30,00 €', 'k10': '144,00 €', 'k11': '5760'},
            {'k1': 'Hydrogen gas compressor', 'k2': '1', 'k3': '300,00 €', 'k4': '20', 'k5': '360,00 €', 'k6': '0,00 €',
             'k7': '20', 'k8': '0,00 €', 'k9': '300,00 €', 'k10': '360,00 €', 'k11': '1440'},
            {'k1': 'Oxygen filter', 'k2': '1', 'k3': '20,00 €', 'k4': '20', 'k5': '24,00 €', 'k6': '0,00 €', 'k7': '20',
             'k8': '0,00 €', 'k9': '20,00 €', 'k10': '24,00 €', 'k11': '1440'},
            {'k1': 'Total', 'k2': '10827', 'k3': '2 802,25 €', 'k4': '-', 'k5': '1 298 625,12 €', 'k6': '0,00 €',
             'k7': '-', 'k8': '0,00 €', 'k9': '2 802,25 €', 'k10': '1 298 625,12 €', 'k11': '19740960'},
        ]
    }
    return render(request, "produitschimiques/investment.html", context)


def electronic_circuit_diagram_of_stanley_meyer_water_electrolyser(request):
    return render(request, "produitschimiques/electronic_circuit_diagram_of_stanley_meyer_water_electrolyser.html")


def laws(request):
    return render(request, "produitschimiques/laws.html")


def business_model_canvas(request):
    return render(request, "produitschimiques/business_model_canvas.html")


def about_electrochemistry(request):
    return render(request, "produitschimiques/about_electrochemistry.html")


def about_electrolysis(request):
    return render(request, "produitschimiques/about_electrolysis.html")


def about_electromagnetism(request):
    return render(request, "produitschimiques/about_electromagnetism.html")


def about_electronics(request):
    return render(request, "produitschimiques/about_electronics.html")


def about_stanley_meyer(request):
    return render(request, "produitschimiques/about_stanley_meyer.html")


def electronic_design_automation_of_stanley_meyer_water_electrolyser(request):
    return render(request, "produitschimiques/electronic_design_automation_of_stanley_meyer_water_electrolyser.html")


def hydrogen_generator(request):
    return render(request, "produitschimiques/hydrogen_generator.html")


def hydrogen_rack(request):
    return render(request, "produitschimiques/hydrogen_rack.html")


def voltage_intensifier_circuit(request):
    return render(request, "produitschimiques/voltage_intensifier_circuit.html")


def smart_grid(request):
    return render(request, "produitschimiques/smart_grid.html")


def business_execution(request):
    return render(request, "produitschimiques/business_execution.html")


def hydrogen_economy(request):
    return render(request, "produitschimiques/hydrogen_economy.html")


def use_cases_with_stanley_meyer_water_electrolyser(request):
    return render(request, "produitschimiques/use_cases_with_stanley_meyer_water_electrolyser.html")


def theories_to_know_about_stanley_meyer_water_electrolyser(request):
    return render(request, "produitschimiques/theories_to_know_about_stanley_meyer_water_electrolyser.html")


def sale_of_open_source_software(request):
    return render(request, "produitschimiques/sale_of_open_source_software.html")


def types_of_funding(request):
    return render(request, "produitschimiques/types_of_funding.html")


def cleantech_company(request):
    return render(request, "produitschimiques/cleantech_company.html")


def videos_about_stanley_meyer_water_electrolyser(request):
    return render(request, "produitschimiques/videos_about_stanley_meyer_water_electrolyser.html")


def stanley_meyer_patents(request):
    return render(request, "produitschimiques/stanley_meyer_patents.html")


def distribution_channels(request):
    return render(request, "produitschimiques/distribution_channels.html")


def quality_management(request):
    return render(request, "produitschimiques/quality_management.html")
