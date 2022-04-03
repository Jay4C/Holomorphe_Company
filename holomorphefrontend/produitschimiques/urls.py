from django.urls import path

from . import views

urlpatterns = [
    path('distribution_channels',
         views.distribution_channels,
         name='distribution_channels'),
    path('gas-mixture-of-pure-dihydrogen',
         views.vente_hydrogene,
         name='vente_hydrogene'),
    path(
        'fundamental-research-of-the-us-patent-us4936961a',
        views.fundamental_research_of_the_us_patent_us4936961a,
        name='fundamental_research_of_the_us_patent_us4936961a'),
    path(
        'fundamental-research-of-the-us-patent-us4936961a-part-2',
        views.fundamental_research_of_the_us_patent_us4936961a_part_2,
        name='fundamental_research_of_the_us_patent_us4936961a_part_2'),
    path(
        'cad-stanley-meyer-water-electrolyser',
        views.cad_stanley_meyer_water_electrolyser,
        name='cad_stanley_meyer_water_electrolyser'),
    path(
        'comparison_of_electrolysers',
        views.comparison_of_electrolysers,
        name='comparison_of_electrolysers'),
    path(
        'investment',
        views.investment,
        name='investment'),
    path(
        'electronic_circuit_diagram_of_stanley_meyer_water_electrolyser',
        views.electronic_circuit_diagram_of_stanley_meyer_water_electrolyser,
        name='electronic_circuit_diagram_of_stanley_meyer_water_electrolyser'),
    path(
        'laws',
        views.laws,
        name='laws'),
    path(
        'business_model_canvas',
        views.business_model_canvas,
        name='business_model_canvas'),
    path(
        'about_electronics',
        views.about_electronics,
        name='about_electronics'),
    path(
        'about_electrolysis',
        views.about_electrolysis,
        name='about_electrolysis'),
    path(
        'about_electromagnetism',
        views.about_electromagnetism,
        name='about_electromagnetism'),
    path(
        'about_electrochemistry',
        views.about_electrochemistry,
        name='about_electrochemistry'),
    path(
        'about_stanley_meyer',
        views.about_stanley_meyer,
        name='about_stanley_meyer'),
    path(
        'electronic_design_automation_of_stanley_meyer_water_electrolyser',
        views.electronic_design_automation_of_stanley_meyer_water_electrolyser,
        name='electronic_design_automation_of_stanley_meyer_water_electrolyser'),
    path(
        'hydrogen_generator',
        views.hydrogen_generator,
        name='hydrogen_generator'),
    path(
        'hydrogen_rack',
        views.hydrogen_rack,
        name='hydrogen_rack'),
    path(
        'voltage_intensifier_circuit',
        views.voltage_intensifier_circuit,
        name='voltage_intensifier_circuit'),
    path(
        'smart_grid',
        views.smart_grid,
        name='smart_grid'),
    path(
        'business_execution',
        views.business_execution,
        name='business_execution'),
    path(
        'hydrogen_economy',
        views.hydrogen_economy,
        name='hydrogen_economy'),
    path(
        'use_cases_with_stanley_meyer_water_electrolyser',
        views.use_cases_with_stanley_meyer_water_electrolyser,
        name='use_cases_with_stanley_meyer_water_electrolyser'),
    path(
        'theories_to_know_about_stanley_meyer_water_electrolyser',
        views.theories_to_know_about_stanley_meyer_water_electrolyser,
        name='theories_to_know_about_stanley_meyer_water_electrolyser'),
    path(
        'sale_of_open_source_software',
        views.sale_of_open_source_software,
        name='sale_of_open_source_software'),
    path(
        'types_of_funding',
        views.types_of_funding,
        name='types_of_funding'),
    path(
        'cleantech_company',
        views.cleantech_company,
        name='cleantech_company'),
    path(
        'videos_about_stanley_meyer_water_electrolyser',
        views.videos_about_stanley_meyer_water_electrolyser,
        name='videos_about_stanley_meyer_water_electrolyser'),
    path(
        'stanley_meyer_patents',
        views.stanley_meyer_patents,
        name='stanley_meyer_patents'),
    path(
        'quality_management',
        views.quality_management,
        name='quality_management'),
]
