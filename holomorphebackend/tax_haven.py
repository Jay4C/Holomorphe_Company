from flask import Flask, jsonify

app = Flask(__name__)

# This API concerns tax haven.

# others
table_active = "table-active"
trust = "Trust"
company = "Company"
country = "Country"
topic = "topic"
table_success = "table-success"
table_danger = "table-danger"
color = "color"
value = "value"
comparison = "comparison"
yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands = "Yes, GBP £17 per GBP £1,000 of capital above GBP £2,000 with a maximum duty of GBP £5,000"
gbp_one = "GBP £1"
chf_100000 = "CHF 100,000"
calendar_year_one_one_thirty_one_twelve = "Calendar year (01/01 - 31/12)"
yes_one_year = "Yes, 1 year"
n_a_the_cayman_islands_do_not_levy_corporation_tax = "N/A - The Cayman Islands do not levy corporation tax"
calendar_or_accounting_year = "Calendar or accounting year"
yes_five_years = "Yes, 5 years"
euro = "Euro (EUR)"
yes_if_incurred_for_the_production_of_taxable_income = "Yes if incurred for the production of taxable income"
treated_as_a_company_i_e_zero_percent_tax = "Treated as a company i.e. 0% tax"
yes_where_applicable = "Yes where applicable"
n_a_ras_al_khaimah_does_not_levy_vat = "N/A - Ras Al Khaimah does not levy VAT"
n_a_the_bvi_does_not_levy_corporation_tax = "N/A - The BVI does not levy corporation tax"
n_a_no_requirement_for_tax_return = "N/A - No requirement for tax return"
accounting_year = "Accounting year"
n_a_no_vat_in_dubai = "N/A - No VAT in Dubai"
n_a_our_analysis_covers_only_belize_ibcs = "N/A - Our analysis covers only Belize IBCs"
taxed_in_the_hands_of_each_partner = "Taxed in the hands of each partner"
pound_sterling_gpb = "Pound Sterling (GPB)"
n_a_no_vat_in_hong_kong = "N/A - No VAT in Hong Kong"
n_a_ras_al_khaimah_does_not_levy_corporation_tax = "N/A - Ras Al Khaimah does not levy corporation tax"
n_a_no_tax_for_dubai_difc_companies = "N/A - No tax for Dubai DIFC companies"
n_a_the_bahamas_does_not_levy_corporation_tax = "N/A - The Bahamas does not levy corporation tax"
n_a_bermuda_does_not_levy_corporation_tax = "N/A - Bermuda does not levy corporation tax"
at_least_one_director_should_be_an_individual_resident_in_singapore = "At least 1 director should be an individual resident in Singapore"
not_tax_deductible_since_capital_gains_are_not_taxable = "Not tax-deductible since capital gains are not taxable"
no_information_is_declosed_to_any_person = "No information is disclosed to any person"
n_a_no_vat_in_bermuda = "N/A - No VAT in Bermuda"
n_a_no_vat_in_the_bvi = "N/A - No VAT in the BVI"
n_a_no_vat_in_the_cayman_islands = "N/A - No VAT in the Cayman Islands"
n_a_no_vat_in_gibraltar = "N/A - No VAT in Gibraltar"
n_a_no_vat_in_guernsey = "N/A - No VAT in Guernsey"
no_maximum_duration = "No maximum duration"
hundred_fifty_years = "150 years"
hundred_years = "100 years"
yes_at_least_one = "Yes, at least 1"
n_a_no_specific_legislation_for_asset_protection = "N/A - no specific legislation for asset protection"
five_ten_days = "5 - 10 days"
two_five_days = "2 - 5 days"
one_five_days = "1 - 5 days"
yes_to_service_provider_and_authorities = "Yes, to service provider and Authorities"
three_four_days = "3 - 4 days"
yes_ci_dollar_fifty = "Yes, CI$50"
one_two_days = "1 - 2 days"
uk_gaap_ias_ifrs = "UK GAAP, IAS or IFRS"
n_a_no_requirement_for_financial_statements = "N/A - no requirement for financial statements"
no_but_filed_with_the_authorities = "No (but filed with the Authorities)"
yes_to_service_provider ="Yes, to service provider"
n_a_no_audit_requirement = "N/A - no audit requirement"
treated_as_a_company = "Treated as a company"
n_a_the_belize_ibc_is_not_subject_to_corporation_tax = "N/A - The Belize IBC is not subject to corporation tax"
yes_indefinitely = "Yes, indefinitely"

# Trusts
bahamas_non_resident_trust = "Bahamas Non-Resident Trust"
barbados_international_trust = "Barbados International Trust"
belize_international_trust = "Belize International Trust"
bermuda_trust = "Bermuda Trust"
bvi_trust = "BVI Trust"
cayman_ordinary_trust = "Cayman Ordinary Trust"
cyprus_international_trust = "Cyprus International Trust"
gibraltar_trust = "Gibraltar Trust"
guernsey_trust = "Guernsey Trust"
hong_kong_foreign_trust = "Hong Kong Foreign Trust"
isle_of_man_trust = "Isle of Man Trust"
jersey_international_trust = "Jersey International Trust"
liechtenstein_trust = "Liechtenstein Trust"
malta_trust = "Malta Trust"
mauritius_non_resident_trust = "Mauritius Non-Resident Trust"
panama_trust = "Panama Trust"
seychelles_international_trust = "Seychelles International Trust"
singapore_foreign_trust = "Singapore Foreign Trust"

# Companies
andorra_private_limited_company = "Andorra Private Limited Company"
bahamas_ibc = "Bahamas IBC"
andorra_private_anonymous_company = "Andorra Private Anonymous Company"
barbados_ibc = "Barbados IBC"
barbados_isrl = "Barbados ISRL"
belize_ibc = "Belize IBC"
bermuda_exempt_company = "Bermuda Exempt Company"
bvi_ibc = "BVI IBC"
cayman_exempted_company = "Cayman Exempted Company"
cayman_exempted_limited_duration_company = "Cayman Exempted Limited Duration Company"
cayman_ordinary_non_resident_company = "Cayman Ordinary Non-Resident Company"
cyprus_private_company = "Cyprus Private Company"
cyprus_public_company = "Cyprus Public Company"
gibraltar_non_resident_company = "Gibraltar Non-Resident Company"
egypt_limited_liability_company_llc = "Egypt Limited Liability Company (LLC)"
guernsey_limited_company = "Guernsey Limited Company"
hong_kong_private_company = "Hong Kong Private Company"
hong_kong_public_company = "Hong Kong Public Company"
ireland_private_company = "Ireland Private Company"
ireland_public_company = "Ireland Public Company"
isle_of_man_private_company_act_1931 = "Isle of Man Private Company (Act 1931)"
isle_of_man_limited_company_act_2006 = "Isle of Man Limited Company (Act 2006)"
isle_of_man_public_company_act_1931 = "Isle of Man Public Company (Act 1931)"
jersey_private_company = "Jersey Private Company"
jersey_public_company = "Jersey Public Company"
liechtenstein_stock_company_ag = "Liechtenstein Stock Company (AG)"
lithuania_private_limited_company = "Lithuania Private Limited Company"
luxembourg_private_company = "Luxembourg Private Company"
luxembourg_public_company_sa = "Luxembourg Public Company (SA)"
malta_private_company = "Malta Private Company"
malta_public_company = "Malta Public Company"
mauritius_gbc1_company = "Mauritius GBC1 Company"
mauritius_gbc2_company = "Mauritius GBC2 Company"
netherlands_bv_company_dutch_bv = "Netherlands BV Company (Dutch BV)"
panama_corporation = "Panama Corporation"
seychelles_ibc = "Seychelles IBC"
seychelles_csl = "Seychelles CSL"
singapore_private_exempt_company = "Singapore Private Exempt Company"
singapore_private_company = "Singapore Private Company"
singapore_public_company = "Singapore Public Company"
swiss_limited_company_sarl_gmbh = "Swiss Limited Company (Sarl / GmbH)"
swiss_stock_corporation_ag_sa = "Swiss Stock Corporation (AG / SA)"
dubai_difc_ltd_company = "Dubai (DIFC) LTD Company"
dubai_difc_llc_company = "Dubai (DIFC) LLC Company"
rak_offshore_ibc = "RAK Offshore IBC"

# Countries
british_virgin_islands = "British Virgin Islands"
cayman_islands = "Cayman Islands"
cyprus = "Cyprus"
egypt = "Egypt"
bermuda = "Bermuda"
bahamas = "Bahamas"
barbados = "Barbados"
andorra = "Andorra"
belize = "Belize"
gibraltar = "Gibraltar"
guernsey = "Guernsey"
hong_kong = "Hong Kong"
ireland = "Ireland"
isle_of_man = "Isle of Man"
jersey = "Jersey"
liechtenstein = "Liechtenstein"
luxembourg = "Luxembourg"
lithuania = "Lithuania"
malta = "Malta"
mauritius = "Mauritius"
netherlands = "Netherlands"
panama = "Panama"
seychelles = "Seychelles"
singapore = "Singapore"
dubai = "Dubai"
ras_al_khaimah = "Ras Al Khaimah"
switzerland = "Switzerland"


# Get information about corporation tax
@app.route("/corporation_tax")
def corporation_tax():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "IBCs and ISRLs at 0.25% - 2.5% ; Small Companies at 15% ; Regular Companies at 25%", color: table_danger},
            {comparison: andorra, value: "10%", color: table_danger},
            {comparison: belize, value: "0% (for IBCs)", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "12.5%", color: table_danger},
            {comparison: egypt, value: "Normal 22.5/27.5% ; - Oil prospecting and productions companies 40.55/45.55% ; - Special economic zones 10%", color: table_danger},
            {comparison: gibraltar, value: "10%", color: table_success},
            {comparison: guernsey, value: "0% except for banking business (10%) and income from immovable property situated in Guernsey (20%)", color: table_success},
            {comparison: hong_kong, value: "16.5%", color: table_danger},
            {comparison: ireland, value: "12.5% for trading and 25% for non-trading profits", color: table_danger},
            {comparison: isle_of_man, value: "0% except from licensed banks deposit-taking activities and income from immovable property (10%)", color: table_danger},
            {comparison: jersey, value: "0% except for financial services companies (10%), utility companies (20%) and income from immovable property (20%)", color: table_success},
            {comparison: liechtenstein, value: "12.5%", color: table_danger},
            {comparison: luxembourg, value: "Effective 28.15% or 29.22% (i.e. including Surcharge and Municipal Business Tax)", color: table_danger},
            {comparison: lithuania, value: "15% / 5%", color: table_danger},
            {comparison: malta, value: "35% but due to imputation system the effective tax is 0% - 10%", color: table_danger},
            {comparison: mauritius, value: "GBC1 companies at 15% ; - GBC2 companies at 0% ; - Other companies at 15% (Alternative Minimum Tax may apply)", color: table_danger},
            {comparison: netherlands, value: "Taxable profits up to €200,000 at 20% ; - Taxable profits over €200,000 at 25%", color: table_danger},
            {comparison: panama, value: "25% but for companies over taxable revenues of US$1.5m an alternative tax may apply", color: table_danger},
            {comparison: seychelles, value: "IBCs at 0% ; - CSLs at 1.5% ; - Other companies (business tax) at 25% on first SCR 1,000,000 and 30% on remainder except for some financial institutions, telecom companies, alcohol producers, etc at 33%", color: table_danger},
            {comparison: singapore, value: "17% but 75% of the first SGD 10,000 and 75% of the next SGD 290,000 are exempt", color: table_danger},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "Companies under Holding Companies regime at effective 7.83% ; - Other companies at 11.5% - 24.2% (combined Federal, Cantonal and Municipal taxes)", color: table_danger}
        ],
        topic: "Corporation tax",
        comparison: country
    }
    return jsonify(context)


# Get information about vat tax
@app.route("/vat_tax")
def vat_tax():
    context = {
        "data": [
            {comparison: bahamas, value: "N/A - No VAT in The Bahamas. Proposed VAT system may apply from 1 July 2014 (standard rate of 15%", color: table_success},
            {comparison: barbados, value: "17.5%", color: table_danger},
            {comparison: andorra, value: "4.5%", color: table_danger},
            {comparison: belize, value: "12.5%", color: table_danger},
            {comparison: bermuda, value: n_a_no_vat_in_bermuda, color: table_success},
            {comparison: british_virgin_islands, value: n_a_no_vat_in_the_bvi, color: table_success},
            {comparison: cayman_islands, value: n_a_no_vat_in_the_cayman_islands, color: table_success},
            {comparison: cyprus, value: "19%", color: table_danger},
            {comparison: egypt, value: "10% (25%-30%-45% for specific goods)", color: table_danger},
            {comparison: gibraltar, value: n_a_no_vat_in_gibraltar, color: table_success},
            {comparison: guernsey, value: n_a_no_vat_in_guernsey, color: table_success},
            {comparison: hong_kong, value: n_a_no_vat_in_hong_kong, color: table_danger},
            {comparison: ireland, value: "23%", color: table_danger},
            {comparison: isle_of_man, value: "20%", color: table_danger},
            {comparison: jersey, value: "5%", color: table_danger},
            {comparison: liechtenstein, value: "8%", color: table_danger},
            {comparison: luxembourg, value: "15%", color: table_danger},
            {comparison: lithuania, value: "21%", color: table_danger},
            {comparison: malta, value: "18%", color: table_danger},
            {comparison: mauritius, value: "15%", color: table_danger},
            {comparison: netherlands, value: "21%", color: table_danger},
            {comparison: panama, value: "7%", color: table_danger},
            {comparison: seychelles, value: "15%", color: table_danger},
            {comparison: singapore, value: "7%", color: table_danger},
            {comparison: dubai, value: n_a_no_vat_in_dubai, color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_vat, color: table_success},
            {comparison: switzerland, value: "8%", color: table_danger}
        ],
        topic: "VAT tax",
        comparison: country
    }
    return jsonify(context)


# Get information about eu_members
@app.route("/eu_members")
def eu_members():
    context = {
        "data": [
            {comparison: bahamas, value: "No", color: table_success},
            {comparison: barbados, value: "No", color: table_success},
            {comparison: andorra, value: "No", color: table_success},
            {comparison: belize, value: "No", color: table_success},
            {comparison: bermuda, value: "No", color: table_success},
            {comparison: british_virgin_islands, value: "No", color: table_success},
            {comparison: cayman_islands, value: "No", color: table_success},
            {comparison: cyprus, value: "Yes", color: table_danger},
            {comparison: egypt, value: "No", color: table_success},
            {comparison: gibraltar, value: "Yes - as a dependent territory of the United Kingdom", color: table_danger},
            {comparison: guernsey, value: "No", color: table_success},
            {comparison: hong_kong, value: "No", color: table_success},
            {comparison: ireland, value: "Yes", color: table_danger},
            {comparison: isle_of_man, value: "No", color: table_success},
            {comparison: jersey, value: "No", color: table_success},
            {comparison: liechtenstein, value: "No", color: table_success},
            {comparison: luxembourg, value: "Yes", color: table_danger},
            {comparison: lithuania, value: "Yes", color: table_danger},
            {comparison: malta, value: "Yes", color: table_danger},
            {comparison: mauritius, value: "No", color: table_success},
            {comparison: netherlands, value: "Yes", color: table_danger},
            {comparison: panama, value: "No", color: table_success},
            {comparison: seychelles, value: "No", color: table_success},
            {comparison: singapore, value: "No", color: table_success},
            {comparison: dubai, value: "No", color: table_success},
            {comparison: ras_al_khaimah, value: "No", color: table_success},
            {comparison: switzerland, value: "No", color: table_success}
        ],
        topic: "EU members",
        comparison: country
    }
    return jsonify(context)


# Get information about currency
@app.route("/currency")
def currency():
    context = {
        "data": [
            {comparison: bahamas, value: "Bahamian Dollar (BSD)", color: table_success},
            {comparison: barbados, value: "Barbados Dollar (BD)", color: table_success},
            {comparison: andorra, value: euro, color: table_success},
            {comparison: belize, value: "Belize Dollar (BZD)", color: table_success},
            {comparison: bermuda, value: "Bermudian Dollar (BMD)", color: table_success},
            {comparison: british_virgin_islands, value: "US Dollar (USD)", color: table_success},
            {comparison: cayman_islands, value: "Cayman Islands Dollar (CID)", color: table_success},
            {comparison: cyprus, value: euro, color: table_success},
            {comparison: egypt, value: "Egyptian Pound (EGP)", color: table_success},
            {comparison: gibraltar, value: pound_sterling_gpb, color: table_success},
            {comparison: guernsey, value: pound_sterling_gpb, color: table_success},
            {comparison: hong_kong, value: "Hong Kong Dollar (HKD)", color: table_success},
            {comparison: ireland, value: euro, color: table_success},
            {comparison: isle_of_man, value: pound_sterling_gpb, color: table_success},
            {comparison: jersey, value: pound_sterling_gpb, color: table_success},
            {comparison: liechtenstein, value: "Swiss Franc (CHF)", color: table_success},
            {comparison: luxembourg, value: euro, color: table_success},
            {comparison: lithuania, value: euro, color: table_success},
            {comparison: malta, value: euro, color: table_success},
            {comparison: mauritius, value: "Mauritian Rupee (MUR)", color: table_success},
            {comparison: netherlands, value: euro, color: table_success},
            {comparison: panama, value: "Balboa (PAB), US Dollar (USD)", color: table_success},
            {comparison: seychelles, value: "Seychelles Rupee (SCR)", color: table_success},
            {comparison: singapore, value: "Singapore Dollar (SGD)", color: table_success},
            {comparison: dubai, value: "UAE Dirham (AED)", color: table_success},
            {comparison: ras_al_khaimah, value: "UAE Dirham (AED)", color: table_success},
            {comparison: switzerland, value: "Swiss Franc (CHF)", color: table_success}
        ],
        topic: "Currency",
        comparison: country
    }
    return jsonify(context)


# Get information about carry_forward_of_ordinary_tax_losses
@app.route("/carry_forward_of_ordinary_tax_losses")
def carry_forward_of_ordinary_tax_losses():
    context = {
        "data": [
            {comparison: bahamas, value: n_a_the_bahamas_does_not_levy_corporation_tax, color: table_danger},
            {comparison: barbados, value: "Yes, 9 years", color: table_success},
            {comparison: andorra, value: "Yes, 10 years", color: table_success},
            {comparison: belize, value: n_a_the_belize_ibc_is_not_subject_to_corporation_tax, color: table_danger},
            {comparison: bermuda, value: n_a_bermuda_does_not_levy_corporation_tax, color: table_danger},
            {comparison: british_virgin_islands, value: n_a_the_bvi_does_not_levy_corporation_tax, color: table_danger},
            {comparison: cayman_islands, value: n_a_the_cayman_islands_do_not_levy_corporation_tax, color: table_danger},
            {comparison: cyprus, value: "Yes, for 5 years", color: table_success},
            {comparison: egypt, value: yes_five_years, color: table_success},
            {comparison: gibraltar, value: yes_indefinitely, color: table_success},
            {comparison: guernsey, value: yes_indefinitely, color: table_success},
            {comparison: hong_kong, value: yes_indefinitely, color: table_success},
            {comparison: ireland, value: yes_indefinitely, color: table_success},
            {comparison: isle_of_man, value: yes_indefinitely, color: table_success},
            {comparison: jersey, value: yes_indefinitely, color: table_success},
            {comparison: liechtenstein, value: "Yes, indefinitely but only 70% can be utilized each year", color: table_success},
            {comparison: luxembourg, value: yes_indefinitely, color: table_success},
            {comparison: lithuania, value: yes_indefinitely, color: table_success},
            {comparison: malta, value: yes_indefinitely, color: table_success},
            {comparison: mauritius, value: yes_five_years, color: table_success},
            {comparison: netherlands, value: "Yes, 9 years", color: table_success},
            {comparison: panama, value: "Yes, 5 years (subject to restrictions)", color: table_success},
            {comparison: seychelles, value: yes_five_years, color: table_success},
            {comparison: singapore, value: yes_indefinitely, color: table_success},
            {comparison: dubai, value: n_a_no_tax_for_dubai_difc_companies, color: table_danger},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_danger},
            {comparison: switzerland, value: "Yes, 7 years", color: table_success}
        ],
        topic: "Carry forward of ordinary tax losses",
        comparison: country
    }
    return jsonify(context)


# Get information about carry_back_of_ordinary_tax_losses
@app.route("/carry_back_of_ordinary_tax_losses")
def carry_back_of_ordinary_tax_losses():
    context = {
        "data": [
            {comparison: bahamas, value: n_a_the_bahamas_does_not_levy_corporation_tax, color: table_danger},
            {comparison: barbados, value: "No", color: table_danger},
            {comparison: andorra, value: "No", color: table_danger},
            {comparison: belize, value: n_a_the_belize_ibc_is_not_subject_to_corporation_tax, color: table_danger},
            {comparison: bermuda, value: n_a_bermuda_does_not_levy_corporation_tax, color: table_danger},
            {comparison: british_virgin_islands, value: n_a_the_bvi_does_not_levy_corporation_tax, color: table_danger},
            {comparison: cayman_islands, value: n_a_the_cayman_islands_do_not_levy_corporation_tax, color: table_danger},
            {comparison: cyprus, value: "No", color: table_danger},
            {comparison: egypt, value: "Only for losses incurred in long-term projects may be carried back to offset profits from the same project for an unlimited number of years.", color: table_danger},
            {comparison: gibraltar, value: "No", color: table_danger},
            {comparison: guernsey, value: "No", color: table_danger},
            {comparison: hong_kong, value: "No", color: table_danger},
            {comparison: ireland, value: yes_one_year, color: table_success},
            {comparison: isle_of_man, value: yes_one_year, color: table_success},
            {comparison: jersey, value: "No", color: table_danger},
            {comparison: liechtenstein, value: "No", color: table_danger},
            {comparison: luxembourg, value: "No", color: table_danger},
            {comparison: lithuania, value: "No", color: table_danger},
            {comparison: malta, value: "No", color: table_danger},
            {comparison: mauritius, value: "No", color: table_danger},
            {comparison: netherlands, value: yes_one_year, color: table_success},
            {comparison: panama, value: "No", color: table_danger},
            {comparison: seychelles, value: "No", color: table_danger},
            {comparison: singapore, value: "Yes, 1 year (subject to a cap of SGD 100,000)", color: table_danger},
            {comparison: dubai, value: n_a_no_tax_for_dubai_difc_companies, color: table_danger},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_danger},
            {comparison: switzerland, value: "No", color: table_danger}
        ],
        topic: "Carry back of ordinary tax losses",
        comparison: country
    }
    return jsonify(context)


# Get information about capital_gains_tax_rate
@app.route("/capital_gains_tax_rate")
def capital_gains_tax_rate():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "0%", color: table_success},
            {comparison: andorra, value: "10%", color: table_danger},
            {comparison: belize, value: "N/A - The Belize IBC is not subject to capital gains tax", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "20% (only on immovable property situated in Cyprus)", color: table_danger},
            {comparison: egypt, value: "Sale of securities 10/25/30% ; - Sale of other assets 25/30%", color: table_danger},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "0%", color: table_success},
            {comparison: ireland, value: "30% or 0% if participation exemption applies", color: table_danger},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "12.5% except for domestic real estate (2% - 14% depending on the amount of the gain)", color: table_danger},
            {comparison: luxembourg, value: "0% on disposal of shares in qualifying participations, otherwise effective 27.75% or 28.80% (to be increased to 28.15% and 29.22% from 1 January 2013)", color: table_danger},
            {comparison: lithuania, value: "15%", color: table_danger},
            {comparison: malta, value: "0% for participation holdings or effectively 0% - 5%", color: table_success},
            {comparison: mauritius, value: "0%", color: table_success},
            {comparison: netherlands, value: "Gains on disposal of qualifying participations are  exempt ; - Other gains at 20% or 25%", color: table_danger},
            {comparison: panama, value: "10% plus 3% withholding tax (5% withholding tax for securities)", color: table_danger},
            {comparison: seychelles, value: "0%", color: table_success},
            {comparison: singapore, value: "0%", color: table_success},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "N/A - Ras Al Khaimah does not levy capital gains tax", color: table_success},
            {comparison: switzerland, value: "Corporation tax rates apply except for qualifying participations which are exempt", color: table_success}
        ],
        topic: "Capital gains tax rate",
        comparison: country
    }
    return jsonify(context)


# Get information about capital_losses
@app.route("/capital_losses")
def capital_losses():
    context = {
        "data": [
            {comparison: bahamas, value: "Not tax-deductible since capital gains are not taxable.", color: table_danger},
            {comparison: barbados, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: andorra, value: "No", color: table_danger},
            {comparison: belize, value: "N/A - The Belize IBC is not subject to capital gains tax", color: table_danger},
            {comparison: bermuda, value: "Not tax-deductible since capital losses are not taxable", color: table_danger},
            {comparison: british_virgin_islands, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: cayman_islands, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: cyprus, value: "Can be carried forward indefinitely", color: table_success},
            {comparison: egypt, value: "From sale of securities: Yes, restricted to 3 years ; - From sale of other assets: Yes, restricted to 5 years", color: table_success},
            {comparison: gibraltar, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: guernsey, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: hong_kong, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: ireland, value: "Can be set-off against taxable capital gains of same year or carried forward", color: table_danger},
            {comparison: isle_of_man, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: jersey, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: liechtenstein, value: "No specific rule in the legislation", color: table_success},
            {comparison: luxembourg, value: "Treated as ordinary losses", color: table_success},
            {comparison: lithuania, value: "Yes", color: table_success},
            {comparison: malta, value: "Can be carried forward indefinitely", color: table_success},
            {comparison: mauritius, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: netherlands, value: "Can be set-off against other taxable income except from capital losses on qualifying participations", color: table_danger},
            {comparison: panama, value: "Not deductible from capital gains", color: table_danger},
            {comparison: seychelles, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: singapore, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: dubai, value: not_tax_deductible_since_capital_gains_are_not_taxable, color: table_danger},
            {comparison: ras_al_khaimah, value: "N/A - Ras Al Khaimah does not levy capital gains tax", color: table_danger},
            {comparison: switzerland, value: "Can be set-off against taxable profits", color: table_success}
        ],
        topic: "Capital losses",
        comparison: country
    }
    return jsonify(context)


# Get information about vat_reduced_rate
@app.route("/vat_reduced_rate")
def vat_reduced_rate():
    context = {
        "data": [
            {comparison: bahamas, value: "N/A - No VAT in The Bahamas. Proposed VAT system may apply from 1 July 2014 (reduced rate of 0%)", color: table_success},
            {comparison: barbados, value: "8.75% and 0%", color: table_danger},
            {comparison: andorra, value: "9.5%, 1% and 0%", color: table_danger},
            {comparison: belize, value: "0%", color: table_success},
            {comparison: bermuda, value: n_a_no_vat_in_bermuda, color: table_success},
            {comparison: british_virgin_islands, value: n_a_no_vat_in_the_bvi, color: table_success},
            {comparison: cayman_islands, value: n_a_no_vat_in_the_cayman_islands, color: table_success},
            {comparison: cyprus, value: "9%, 5% and 0%", color: table_danger},
            {comparison: egypt, value: "0/5%", color: table_danger},
            {comparison: gibraltar, value: n_a_no_vat_in_gibraltar, color: table_success},
            {comparison: guernsey, value: n_a_no_vat_in_guernsey, color: table_success},
            {comparison: hong_kong, value: n_a_no_vat_in_hong_kong, color: table_success},
            {comparison: ireland, value: "13.5%, 9%, 4.8% and 0%", color: table_danger},
            {comparison: isle_of_man, value: "5% and 0%", color: table_danger},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "3.8% and 2.5%", color: table_danger},
            {comparison: luxembourg, value: "12%, 6% and 3%", color: table_danger},
            {comparison: lithuania, value: "9% / 5% / 0%", color: table_danger},
            {comparison: malta, value: "7% and 5%", color: table_danger},
            {comparison: mauritius, value: "N/A", color: table_danger},
            {comparison: netherlands, value: "6% and 0%", color: table_danger},
            {comparison: panama, value: "N/A", color: table_danger},
            {comparison: seychelles, value: "0%", color: table_danger},
            {comparison: singapore, value: "0%", color: table_danger},
            {comparison: dubai, value: n_a_no_vat_in_dubai, color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_vat, color: table_success},
            {comparison: switzerland, value: "3.8%, 2.5% and 0%", color: table_danger}
        ],
        topic: "VAT reduced rate",
        comparison: country
    }
    return jsonify(context)


# Get information about vat_registration_threshhold
@app.route("/vat_registration_threshhold")
def vat_registration_threshhold():
    context = {
        "data": [
            {comparison: bahamas, value: "N/A - No VAT in The Bahamas. Proposed VAT system may apply from 1 July 2014 (registration threshold of B$50,000)", color: table_success},
            {comparison: barbados, value: "B$80,000", color: table_danger},
            {comparison: andorra, value: "€ 40,00", color: table_danger},
            {comparison: belize, value: "BZD 75,000", color: table_danger},
            {comparison: bermuda, value: n_a_no_vat_in_bermuda, color: table_success},
            {comparison: british_virgin_islands, value: n_a_no_vat_in_the_bvi, color: table_success},
            {comparison: cayman_islands, value: n_a_no_vat_in_the_cayman_islands, color: table_success},
            {comparison: cyprus, value: "€ 15,60", color: table_danger},
            {comparison: egypt, value: "1EGP for import and export ; - 54,000 EGP for services and manufacturing ; - 150,000 EGP for trading.", color: table_danger},
            {comparison: gibraltar, value: n_a_no_vat_in_gibraltar, color: table_success},
            {comparison: guernsey, value: n_a_no_vat_in_guernsey, color: table_success},
            {comparison: hong_kong, value: n_a_no_vat_in_hong_kong, color: table_success},
            {comparison: ireland, value: "€37,500 or €75,000", color: table_danger},
            {comparison: isle_of_man, value: "£73,000", color: table_danger},
            {comparison: jersey, value: "£300,000", color: table_danger},
            {comparison: liechtenstein, value: chf_100000, color: table_danger},
            {comparison: luxembourg, value: "€10,000 (to be increased to €25,000 from 1 January 2013)", color: table_danger},
            {comparison: lithuania, value: "€ 45,00", color: table_danger},
            {comparison: malta, value: "€ 7,00", color: table_danger},
            {comparison: mauritius, value: "MUR 2,000,000", color: table_danger},
            {comparison: netherlands, value: "No threshold", color: table_success},
            {comparison: panama, value: "US$36,000", color: table_danger},
            {comparison: seychelles, value: "SCR 2,000,000", color: table_danger},
            {comparison: singapore, value: "SGD 1,000,000", color: table_danger},
            {comparison: dubai, value: n_a_no_vat_in_dubai, color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_vat, color: table_success},
            {comparison: switzerland, value: chf_100000, color: table_danger}
        ],
        topic: "VAT registration threshold",
        comparison: country
    }
    return jsonify(context)


# Get information about vat_filing_and_payment
@app.route("/vat_filing_and_payment")
def vat_filing_and_payment():
    context = {
        "data": [
            {comparison: bahamas, value: "N/A - No VAT in The Bahamas. Proposed VAT system may apply from 1 July 2014 (monthly VAT filing and payment)", color: table_success},
            {comparison: barbados, value: "Every 2 months", color: table_success},
            {comparison: andorra, value: "Depends on turnover: - Up to €250,000 - Semi-annually ; - €250,000 - €3,600,000 - Quarterly ; - Over €3,600,000 - Monthly", color: table_danger},
            {comparison: belize, value: "Monthly", color: table_danger},
            {comparison: bermuda, value: n_a_no_vat_in_bermuda, color: table_success},
            {comparison: british_virgin_islands, value: n_a_no_vat_in_the_bvi, color: table_success},
            {comparison: cayman_islands, value: n_a_no_vat_in_the_cayman_islands, color: table_success},
            {comparison: cyprus, value: "Quarterly", color: table_danger},
            {comparison: egypt, value: "Monthly", color: table_danger},
            {comparison: gibraltar, value: n_a_no_vat_in_gibraltar, color: table_success},
            {comparison: guernsey, value: n_a_no_vat_in_guernsey, color: table_success},
            {comparison: hong_kong, value: n_a_no_vat_in_hong_kong, color: table_success},
            {comparison: ireland, value: "Every 2 months", color: table_danger},
            {comparison: isle_of_man, value: "Quarterly", color: table_danger},
            {comparison: jersey, value: "Quarterly", color: table_danger},
            {comparison: liechtenstein, value: "Quarterly", color: table_danger},
            {comparison: luxembourg, value: "Monthly or quarterly", color: table_danger},
            {comparison: lithuania, value: "Monthly", color: table_danger},
            {comparison: malta, value: "Quarterly", color: table_danger},
            {comparison: mauritius, value: "Every 1 or 4 months", color: table_danger},
            {comparison: netherlands, value: "Monthly, quarterly or annually", color: table_danger},
            {comparison: panama, value: "Monthly", color: table_danger},
            {comparison: seychelles, value: "Monthly", color: table_danger},
            {comparison: singapore, value: "Quarterly", color: table_danger},
            {comparison: dubai, value: n_a_no_vat_in_dubai, color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_vat, color: table_success},
            {comparison: switzerland, value: "Quarterly", color: table_danger}
        ],
        topic: "VAT filing and payment",
        comparison: country
    }
    return jsonify(context)


# Get information about other_taxes
@app.route("/other_taxes")
def other_taxes():
    context = {
        "data": [
            {comparison: bahamas, value: "Real Property Tax on land and buildings at 0.5% - 1.5% depending on the asset value", color: table_success},
            {comparison: barbados, value: "N/A", color: table_success},
            {comparison: andorra, value: "N/A", color: table_success},
            {comparison: belize, value: "N/A", color: table_success},
            {comparison: bermuda, value: "N/A", color: table_success},
            {comparison: british_virgin_islands, value: "N/A", color: table_success},
            {comparison: cayman_islands, value: "N/A", color: table_success},
            {comparison: cyprus, value: "N/A", color: table_success},
            {comparison: egypt, value: "Real estate tax , Social Insurance , Contracting Social Insurance", color: table_danger},
            {comparison: gibraltar, value: "N/A", color: table_success},
            {comparison: guernsey, value: "N/A", color: table_success},
            {comparison: hong_kong, value: "N/A", color: table_success},
            {comparison: ireland, value: "N/A", color: table_success},
            {comparison: isle_of_man, value: "N/A", color: table_success},
            {comparison: jersey, value: "N/A", color: table_success},
            {comparison: liechtenstein, value: "N/A", color: table_success},
            {comparison: luxembourg, value: "Municipal tax at 6% - 12% ; - Employment Fund Surcharge at 5% on tax liability (to increase to 7% from 01/01/2013) ; - Net Wealth Tax at 0.5% (qualifying participation are exempt)", color: table_danger},
            {comparison: lithuania, value: "Immovable property tax ;  Land tax ; Environmental pollution tax", color: table_danger},
            {comparison: malta, value: "N/A", color: table_success},
            {comparison: mauritius, value: "N/A", color: table_success},
            {comparison: netherlands, value: "N/A", color: table_success},
            {comparison: panama, value: "Notice of Operations Tax at 2% (1% for companies in free zones or special trade zones) on equity with a minimum liability of US$100 and maximum US$60,000 (US$50,000 for companies in free zones and special trade zones) ; - Transfer tax on Panama real estate at 2% ; - Real Property Tax on Panama real estate at 1.75% - 2.1%", color: table_danger},
            {comparison: seychelles, value: "N/A", color: table_success},
            {comparison: singapore, value: "N/A", color: table_success},
            {comparison: dubai, value: "N/A", color: table_success},
            {comparison: ras_al_khaimah, value: "N/A", color: table_success},
            {comparison: switzerland, value: "Corporate net wealth tax at 0.001% - 0.5288%", color: table_danger}
        ],
        topic: "Other taxes",
        comparison: country
    }
    return jsonify(context)


# Get information about taxable_period
@app.route("/taxable_period")
def taxable_period():
    context = {
        "data": [
            {comparison: bahamas, value: n_a_the_bahamas_does_not_levy_corporation_tax, color: table_success},
            {comparison: barbados, value: accounting_year, color: table_success},
            {comparison: andorra, value: "Accounting period", color: table_success},
            {comparison: belize, value: "N/A - The Belize IBC is exempt from corporation tax", color: table_success},
            {comparison: bermuda, value: n_a_bermuda_does_not_levy_corporation_tax, color: table_success},
            {comparison: british_virgin_islands, value: n_a_the_bvi_does_not_levy_corporation_tax, color: table_success},
            {comparison: cayman_islands, value: n_a_the_cayman_islands_do_not_levy_corporation_tax, color: table_success},
            {comparison: cyprus, value: calendar_year_one_one_thirty_one_twelve, color: table_success},
            {comparison: egypt, value: "Financial year", color: table_success},
            {comparison: gibraltar, value: accounting_year, color: table_success},
            {comparison: guernsey, value: "Calendar year or any other 12-month period", color: table_success},
            {comparison: hong_kong, value: "01/04 - 31/03 of the following year", color: table_success},
            {comparison: ireland, value: accounting_year, color: table_success},
            {comparison: isle_of_man, value: accounting_year, color: table_success},
            {comparison: jersey, value: calendar_year_one_one_thirty_one_twelve, color: table_success},
            {comparison: liechtenstein, value: calendar_year_one_one_thirty_one_twelve, color: table_success},
            {comparison: luxembourg, value: calendar_or_accounting_year, color: table_success},
            {comparison: lithuania, value: "12 month period", color: table_success},
            {comparison: malta, value: calendar_year_one_one_thirty_one_twelve, color: table_success},
            {comparison: mauritius, value: calendar_or_accounting_year, color: table_success},
            {comparison: netherlands, value: "Calendar year or any other 12-month period", color: table_success},
            {comparison: panama, value: calendar_or_accounting_year, color: table_success},
            {comparison: seychelles, value: calendar_year_one_one_thirty_one_twelve, color: table_success},
            {comparison: singapore, value: calendar_or_accounting_year, color: table_success},
            {comparison: dubai, value: "N/A - no tax for Dubai DIFC companies", color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_success},
            {comparison: switzerland, value: accounting_year, color: table_success}
        ],
        topic: "Taxable period",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_return_requirement
@app.route("/tax_return_requirement")
def tax_return_requirement():
    context = {
        "data": [
            {comparison: bahamas, value: "No", color: table_success},
            {comparison: barbados, value: "Yes", color: table_danger},
            {comparison: andorra, value: "Yes", color: table_danger},
            {comparison: belize, value: "No", color: table_success},
            {comparison: bermuda, value: "No", color: table_success},
            {comparison: british_virgin_islands, value: "No - The BVI does not levy corporation tax", color: table_success},
            {comparison: cayman_islands, value: "No", color: table_success},
            {comparison: cyprus, value: "Yes", color: table_danger},
            {comparison: egypt, value: "Yes", color: table_danger},
            {comparison: gibraltar, value: "Yes", color: table_danger},
            {comparison: guernsey, value: "Yes", color: table_danger},
            {comparison: hong_kong, value: "Yes", color: table_danger},
            {comparison: ireland, value: "Yes", color: table_danger},
            {comparison: isle_of_man, value: "Yes", color: table_danger},
            {comparison: jersey, value: "Yes", color: table_danger},
            {comparison: liechtenstein, value: "Yes", color: table_danger},
            {comparison: luxembourg, value: "Yes", color: table_danger},
            {comparison: lithuania, value: "Yes", color: table_danger},
            {comparison: malta, value: "Yes", color: table_danger},
            {comparison: mauritius, value: "Yes", color: table_danger},
            {comparison: netherlands, value: "Yes", color: table_danger},
            {comparison: panama, value: "Yes", color: table_danger},
            {comparison: seychelles, value: "Yes", color: table_danger},
            {comparison: singapore, value: "Yes", color: table_danger},
            {comparison: dubai, value: "No", color: table_success},
            {comparison: ras_al_khaimah, value: "No", color: table_success},
            {comparison: switzerland, value: "Yes", color: table_danger}
        ],
        topic: "Tax return requirement",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_return_due_date
@app.route("/tax_return_due_date")
def tax_return_due_date():
    context = {
        "data": [
            {comparison: bahamas, value: "N/A - No requirement to file tax return", color: table_success},
            {comparison: barbados, value: "15/03 or 15/06 depending on year-end", color: table_success},
            {comparison: andorra, value: "7 months after the tax year end", color: table_success},
            {comparison: belize, value: "N/A - The Belize IBC is not required to file a tax return", color: table_success},
            {comparison: bermuda, value: n_a_no_requirement_for_tax_return, color: table_success},
            {comparison: british_virgin_islands, value: n_a_the_bvi_does_not_levy_corporation_tax, color: table_success},
            {comparison: cayman_islands, value: n_a_no_requirement_for_tax_return, color: table_success},
            {comparison: cyprus, value: "15 months after the end of tax year", color: table_success},
            {comparison: egypt, value: "1 May of each year or 4 months after the end of the financial year", color: table_success},
            {comparison: gibraltar, value: "6 months after the tax year-end or 9 months if audited financial statements are needed", color: table_success},
            {comparison: guernsey, value: "30/11 of the following year", color: table_success},
            {comparison: hong_kong, value: "End of April of following year", color: table_success},
            {comparison: ireland, value: "9 months after the tax year-end", color: table_success},
            {comparison: isle_of_man, value: "12 months after the tax year-end", color: table_success},
            {comparison: jersey, value: "7 months after the tax year-end i.e. 31/07", color: table_success},
            {comparison: liechtenstein, value: "01/07 of the following year", color: table_success},
            {comparison: luxembourg, value: "31/05 of the following tax year", color: table_success},
            {comparison: lithuania, value: "15th day of sixth month of the following tax year", color: table_success},
            {comparison: malta, value: "31/09 of the following year", color: table_success},
            {comparison: mauritius, value: "6 months after the tax year-end", color: table_success},
            {comparison: netherlands, value: "5 months after the tax year-end", color: table_success},
            {comparison: panama, value: "3 months from tax year-end", color: table_success},
            {comparison: seychelles, value: "31/03 of the following year", color: table_success},
            {comparison: singapore, value: "30/11 of the following year", color: table_success},
            {comparison: dubai, value: n_a_no_requirement_for_tax_return, color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_success},
            {comparison: switzerland, value: "Usually 30/09 but depends on the Canton", color: table_success}
        ],
        topic: "Tax return requirement",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_residency_requirements
@app.route("/tax_residency_requirements")
def tax_residency_requirements():
    context = {
        "data": [
            {comparison: bahamas, value: n_a_the_bahamas_does_not_levy_corporation_tax, color: table_success},
            {comparison: barbados, value: "Management and control to be exercised in Barbados", color: table_success},
            {comparison: andorra, value: "Incorporation in Andorra or central management and control to be exercised in Andorra", color: table_success},
            {comparison: belize, value: "N/A - The Belize IBC is exempt from corporation tax", color: table_success},
            {comparison: bermuda, value: "Incorporation in Bermuda", color: table_success},
            {comparison: british_virgin_islands, value: "Management and control to be exercised in the BVI", color: table_success},
            {comparison: cayman_islands, value: n_a_the_cayman_islands_do_not_levy_corporation_tax, color: table_success},
            {comparison: cyprus, value: "Management and control to be exercised in Cyprus", color: table_success},
            {comparison: egypt, value: "Effective management in Egypt", color: table_success},
            {comparison: gibraltar, value: "Management and control to be exercised in Gibraltar", color: table_success},
            {comparison: guernsey, value: "Management and control to be exercised in Guernsey", color: table_success},
            {comparison: hong_kong, value: "Management and control to be exercised in Hong Kong", color: table_success},
            {comparison: ireland, value: "Central management and control to be exercised in Ireland", color: table_success},
            {comparison: isle_of_man, value: "Management and control to be exercised in Isle of Man", color: table_success},
            {comparison: jersey, value: "Management and control to be exercised in Jersey", color: table_success},
            {comparison: liechtenstein, value: "Legal seat or effective place of business in Liechtenstein", color: table_success},
            {comparison: luxembourg, value: "Legal seat or place of central management in Luxembourg", color: table_success},
            {comparison: lithuania, value: "Incorporated in Lithuania or if the activities create a PE in Lithuania", color: table_success},
            {comparison: malta, value: "Management and control to be exercised in Malta", color: table_success},
            {comparison: mauritius, value: "Management and control to be exercised in the Mauritius", color: table_success},
            {comparison: netherlands, value: "Management and control to be exercised in Netherlands", color: table_success},
            {comparison: panama, value: "Principal business to be carried in Panama", color: table_success},
            {comparison: seychelles, value: "Management and control to be exercised in Seychelles or voting power to be exercised by shareholders resident in Seychelles", color: table_success},
            {comparison: singapore, value: "Management and control to be exercised in Singapore", color: table_success},
            {comparison: dubai, value: "Registered in Dubai DIFC and management and control exercised in Dubai", color: table_success},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_success},
            {comparison: switzerland, value: "Effective place of business to be in Switzerland", color: table_success}
        ],
        topic: "Tax residency requirements",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_rate_on_dividends_from_local_investments
@app.route("/tax_rate_on_dividends_from_local_investments")
def tax_rate_on_dividends_from_local_investments():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "0%", color: table_success},
            {comparison: andorra, value: "Exempt if the company owns at least 5% for a period of at least 1 year", color: table_success},
            {comparison: belize, value: "0%", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "0%", color: table_success},
            {comparison: egypt, value: "5/10%", color: table_danger},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "0%", color: table_success},
            {comparison: ireland, value: "0% or surcharge of 20% for close companies if dividend income is not redistributed within 18 months", color: table_success},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "0%", color: table_success},
            {comparison: luxembourg, value: "0% if from qualifying participation, otherwise effective 28.15% or 29.22%", color: table_danger},
            {comparison: lithuania, value: "15%/0%", color: table_danger},
            {comparison: malta, value: "0% if under participation exemption or 35% (effectively 0% - 10%)", color: table_success},
            {comparison: mauritius, value: "0%", color: table_success},
            {comparison: netherlands, value: "0% if from qualifying participation or 20%/25%", color: table_success},
            {comparison: panama, value: "0% if dividends are declared ; - 4% if no dividends are declared", color: table_success},
            {comparison: seychelles, value: "15%", color: table_danger},
            {comparison: singapore, value: "0%", color: table_success},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "Exempt if received from qualifying participation, otherwise corporation tax rates apply", color: table_success}
        ],
        topic: "Tax rate on dividends from local investments",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_rate_on_dividends_from_foreign_investments
@app.route("/tax_rate_on_dividends_from_foreign_investments")
def tax_rate_on_dividends_from_foreign_investments():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "0% if Barbados company holds more than 10% and shares not held as portfolio investment", color: table_danger},
            {comparison: andorra, value: "Exempt if the company owns at least 5% for a period of at least 1 year", color: table_danger},
            {comparison: belize, value: "0%", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "0% (subject to easily met criteria)", color: table_success},
            {comparison: egypt, value: "5 / 10%", color: table_danger},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "0%", color: table_success},
            {comparison: ireland, value: "12.5% or 25%", color: table_success},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "0%", color: table_success},
            {comparison: luxembourg, value: "0% if from qualifying participation, otherwise effective 28.15% or 29.22%", color: table_danger},
            {comparison: lithuania, value: "15% / 0%", color: table_danger},
            {comparison: malta, value: "0% if under participation exemption or 35% (effectively 5% - 10%)", color: table_danger},
            {comparison: mauritius, value: "GBC1 companies - 3% ; - Other companies - 15% (or Alternative Minimum Tax)", color: table_danger},
            {comparison: netherlands, value: "0% if from qualifying participation or 20%/25%", color: table_danger},
            {comparison: panama, value: "0%", color: table_success},
            {comparison: seychelles, value: "IBCs at 0% ; - CSLs at 1.5% ; - Other companies (business tax) at 25% on first SCR 1,000,000 and 30% on remainder except for some financial institutions, telecom companies, alcohol producers, etc at 33%", color: table_danger},
            {comparison: singapore, value: "0% if the foreign tax burden is at least 15% and the tax has been paid. Otherwise corporation tax rates apply", color: table_danger},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "Exempt if received from qualifying participation, otherwise corporation tax rates apply", color: table_danger}
        ],
        topic: "Tax rate on dividends from foreign investments",
        comparison: country
    }
    return jsonify(context)


# Get information about withholding_tax_on_dividend_payments_to_foreign_shareholders
@app.route("/withholding_tax_on_dividend_payments_to_foreign_shareholders")
def withholding_tax_on_dividend_payments_to_foreign_shareholders():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "0% for IBCs, ISRLs. ; - 0% for other companies if paid from foreign-source income. ; - 15% in all other cases.", color: table_danger},
            {comparison: andorra, value: "0%", color: table_success},
            {comparison: belize, value: "0%", color: table_danger},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "0%", color: table_success},
            {comparison: egypt, value: "5/10%", color: table_danger},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "0%", color: table_success},
            {comparison: ireland, value: "20%", color: table_danger},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "0%", color: table_success},
            {comparison: luxembourg, value: "0% or 15%", color: table_danger},
            {comparison: lithuania, value: "15%/0%", color: table_danger},
            {comparison: malta, value: "0%", color: table_success},
            {comparison: mauritius, value: "0%", color: table_success},
            {comparison: netherlands, value: "15%", color: table_danger},
            {comparison: panama, value: "10% if paid from Panama-source income ; - 5% if paid from non Panama-source income or income from exports ; - 20% in case of bearer shares", color: table_danger},
            {comparison: seychelles, value: "15% (0% for IBCs and CSLs)", color: table_danger},
            {comparison: singapore, value: "0%", color: table_success},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "35%", color: table_danger}
        ],
        topic: "Withholding tax on dividend payments to foreign shareholders",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_rate_on_interest_income
@app.route("/tax_rate_on_interest_income")
def tax_rate_on_interest_income():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "Normal corporation tax rates apply", color: table_success},
            {comparison: andorra, value: "10%", color: table_danger},
            {comparison: belize, value: "0%", color: table_danger},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "12.5% for active and 30% for passive interest income", color: table_danger},
            {comparison: egypt, value: "25 / 30%", color: table_danger},
            {comparison: gibraltar, value: "0% (except for banks)", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "16.5% except from deposits in financial institutions in Hong Kong (0%)", color: table_danger},
            {comparison: ireland, value: "25%", color: table_danger},
            {comparison: isle_of_man, value: "0% except for licensed banks (10%)", color: table_danger},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "12.5%", color: table_danger},
            {comparison: luxembourg, value: "Effective 28.15% or 29.22%", color: table_danger},
            {comparison: lithuania, value: "15%", color: table_danger},
            {comparison: malta, value: "0% for passive and 35% (effectively 0% - 10%) for active interest income", color: table_danger},
            {comparison: mauritius, value: "GBC1 companies - 3% ; - Other company types - 15% (or Alternative Minimum Tax)", color: table_danger},
            {comparison: netherlands, value: "20% or 25%", color: table_danger},
            {comparison: panama, value: "25% (only on Panama-source interest)", color: table_danger},
            {comparison: seychelles, value: "10% (business tax)", color: table_danger},
            {comparison: singapore, value: "17%", color: table_danger},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "Corporation tax rates apply", color: table_danger}
        ],
        topic: "Tax rate on interest income",
        comparison: country
    }
    return jsonify(context)


# Get information about withholding_tax_on_interest_payments_to_foreign_recipients
@app.route("/withholding_tax_on_interest_payments_to_foreign_recipients")
def withholding_tax_on_interest_payments_to_foreign_recipients():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "0% for IBCs and ISRLs.  ; - 15% in all other cases.", color: table_danger},
            {comparison: andorra, value: "0%", color: table_success},
            {comparison: belize, value: "0%", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "0%", color: table_success},
            {comparison: egypt, value: "20%", color: table_danger},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "0%", color: table_success},
            {comparison: ireland, value: "20%", color: table_danger},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "0%", color: table_success},
            {comparison: luxembourg, value: "0%", color: table_success},
            {comparison: lithuania, value: "10% / 15%", color: table_danger},
            {comparison: malta, value: "0%", color: table_success},
            {comparison: mauritius, value: "GBC1 companies - 0% ; - Other companies - 15%", color: table_danger},
            {comparison: netherlands, value: "0%", color: table_success},
            {comparison: panama, value: "12.5%", color: table_danger},
            {comparison: seychelles, value: "10% (0% for IBCs and CSLs)", color: table_danger},
            {comparison: singapore, value: "15%", color: table_danger},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "35% if derived from deposits with Swiss banks, bonds or bond-like loans, otherwise 0%", color: table_danger}
        ],
        topic: "Withholding tax on interest payments to foreign recipients",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_deductibility_of_interest_expense
@app.route("/tax_deductibility_of_interest_expense")
def tax_deductibility_of_interest_expense():
    context = {
        "data": [
            {comparison: bahamas, value: n_a_the_bahamas_does_not_levy_corporation_tax, color: table_danger},
            {comparison: barbados, value: "Yes", color: table_success},
            {comparison: andorra, value: "Yes", color: table_success},
            {comparison: belize, value: n_a_the_belize_ibc_is_not_subject_to_corporation_tax, color: table_danger},
            {comparison: bermuda, value: n_a_bermuda_does_not_levy_corporation_tax, color: table_danger},
            {comparison: british_virgin_islands, value: n_a_the_bvi_does_not_levy_corporation_tax, color: table_danger},
            {comparison: cayman_islands, value: n_a_the_cayman_islands_do_not_levy_corporation_tax, color: table_danger},
            {comparison: cyprus, value: "Yes", color: table_success},
            {comparison: egypt, value: "Yes - Maximum debt-to-equity ratio is 4:1 only related interest considered deductible expense", color: table_success},
            {comparison: gibraltar, value: "Yes", color: table_success},
            {comparison: guernsey, value: "Yes", color: table_success},
            {comparison: hong_kong, value: "Yes", color: table_success},
            {comparison: ireland, value: "Yes", color: table_success},
            {comparison: isle_of_man, value: yes_where_applicable, color: table_success},
            {comparison: jersey, value: yes_where_applicable, color: table_success},
            {comparison: liechtenstein, value: "Yes", color: table_success},
            {comparison: luxembourg, value: yes_if_incurred_for_the_production_of_taxable_income, color: table_success},
            {comparison: lithuania, value: "Yes", color: table_success},
            {comparison: malta, value: yes_if_incurred_for_the_production_of_taxable_income, color: table_success},
            {comparison: mauritius, value: "Yes", color: table_success},
            {comparison: netherlands, value: "Yes", color: table_success},
            {comparison: panama, value: "Yes if incurred for the production of Panama-source income", color: table_success},
            {comparison: seychelles, value: "Yes", color: table_success},
            {comparison: singapore, value: "Yes", color: table_success},
            {comparison: dubai, value: n_a_no_tax_for_dubai_difc_companies, color: table_danger},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_danger},
            {comparison: switzerland, value: "Yes", color: table_success}
        ],
        topic: "Tax deductibility of interest expense",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_rate_on_royalty_income
@app.route("/tax_rate_on_royalty_income")
def tax_rate_on_royalty_income():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "Normal corporation tax rates apply", color: table_success},
            {comparison: andorra, value: "10%", color: table_danger},
            {comparison: belize, value: "0%", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "12.5% (on 20% of royalty income)", color: table_danger},
            {comparison: egypt, value: "25/30%", color: table_danger},
            {comparison: gibraltar, value: "10%", color: table_danger},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "16.5% but reduced rates may apply for certain types", color: table_danger},
            {comparison: ireland, value: "25%", color: table_danger},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "12.5% (on 20% of royalty income)", color: table_danger},
            {comparison: luxembourg, value: "Effective 28.15% or 29.22%", color: table_danger},
            {comparison: lithuania, value: "15%", color: table_danger},
            {comparison: malta, value: "0% for passive and 35% (effectively 0% - 10%) for active royalty income", color: table_success},
            {comparison: mauritius, value: "GBC1 companies - 3% ;  - Other company types - 15% (or Alternative Minimum Tax)", color: table_danger},
            {comparison: netherlands, value: "20% or 25%", color: table_danger},
            {comparison: panama, value: "25% (only on Panama-source royalties)", color: table_danger},
            {comparison: seychelles, value: "Taxed under corporation tax", color: table_success},
            {comparison: singapore, value: "17%", color: table_danger},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "Corporation tax rates apply", color: table_success}
        ],
        topic: "Tax rate on royalty income",
        comparison: country
    }
    return jsonify(context)


# Get information about withholding_tax_on_royalty_payments_to_foreign_recipients
@app.route("/withholding_tax_on_royalty_payments_to_foreign_recipients")
def withholding_tax_on_royalty_payments_to_foreign_recipients():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "0% for IBCs and ISRLs.  ; - 15% in all other cases.", color: table_danger},
            {comparison: andorra, value: "5%", color: table_danger},
            {comparison: belize, value: "0%", color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "10% if the right/asset is used in Cyprus. ; - 0% in all other cases.", color: table_danger},
            {comparison: egypt, value: "20%", color: table_danger},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "16.5% on royalties to affiliated companies ; - 4.95% in all other cases", color: table_danger},
            {comparison: ireland, value: "20% for patent royalties ; - 0% in all other cases", color: table_danger},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "0%", color: table_success},
            {comparison: luxembourg, value: "0%", color: table_success},
            {comparison: lithuania, value: "10%/15%", color: table_danger},
            {comparison: malta, value: "0%", color: table_success},
            {comparison: mauritius, value: "GBC1 companies - 0% ; - Other companies - 15%", color: table_danger},
            {comparison: netherlands, value: "0%", color: table_success},
            {comparison: panama, value: "12.5% (if the royalty expense is claimed as tax-deductible)", color: table_danger},
            {comparison: seychelles, value: "15% (0% for IBCs and CSLs)", color: table_danger},
            {comparison: singapore, value: "10%", color: table_danger},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "0%", color: table_success},
            {comparison: switzerland, value: "0%", color: table_success}
        ],
        topic: "Withholding tax on royalty payments to foreign recipients",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_deductibility_of_royalty_expense
@app.route("/tax_deductibility_of_royalty_expense")
def tax_deductibility_of_royalty_expense():
    context = {
        "data": [
            {comparison: bahamas, value: n_a_the_bahamas_does_not_levy_corporation_tax, color: table_danger},
            {comparison: barbados, value: "Yes", color: table_success},
            {comparison: andorra, value: "Yes", color: table_success},
            {comparison: belize, value: n_a_the_belize_ibc_is_not_subject_to_corporation_tax, color: table_danger},
            {comparison: bermuda, value: n_a_bermuda_does_not_levy_corporation_tax, color: table_danger},
            {comparison: british_virgin_islands, value: n_a_the_bvi_does_not_levy_corporation_tax, color: table_danger},
            {comparison: cayman_islands, value: n_a_the_cayman_islands_do_not_levy_corporation_tax, color: table_danger},
            {comparison: cyprus, value: "Yes", color: table_success},
            {comparison: egypt, value: "Yes", color: table_success},
            {comparison: gibraltar, value: "Yes", color: table_success},
            {comparison: guernsey, value: "Yes", color: table_success},
            {comparison: hong_kong, value: "Yes", color: table_success},
            {comparison: ireland, value: "Yes", color: table_success},
            {comparison: isle_of_man, value: yes_where_applicable, color: table_success},
            {comparison: jersey, value: yes_where_applicable, color: table_success},
            {comparison: liechtenstein, value: "Yes", color: table_success},
            {comparison: luxembourg, value: yes_if_incurred_for_the_production_of_taxable_income, color: table_success},
            {comparison: lithuania, value: "Yes", color: table_success},
            {comparison: malta, value: yes_if_incurred_for_the_production_of_taxable_income, color: table_success},
            {comparison: mauritius, value: "Yes", color: table_success},
            {comparison: netherlands, value: "Yes", color: table_success},
            {comparison: panama, value: "Yes if incurred for the production of Panama-source income", color: table_success},
            {comparison: seychelles, value: "Yes", color: table_success},
            {comparison: singapore, value: "Yes", color: table_success},
            {comparison: dubai, value: n_a_no_tax_for_dubai_difc_companies, color: table_danger},
            {comparison: ras_al_khaimah, value: n_a_ras_al_khaimah_does_not_levy_corporation_tax, color: table_danger},
            {comparison: switzerland, value: "Yes", color: table_success}
        ],
        topic: "Tax deductibility of royalty expense",
        comparison: country
    }
    return jsonify(context)


# Get information about taxability_of_disposal_of_shares_by_foreign_shareholder
@app.route("/taxability_of_disposal_of_shares_by_foreign_shareholder")
def taxability_of_disposal_of_shares_by_foreign_shareholder():
    context = {
        "data": [
            {comparison: bahamas, value: "No", color: table_success},
            {comparison: barbados, value: "No, unless it holds Bahamian real estate", color: table_success},
            {comparison: andorra, value: "Exempt for individual shareholders. Also exempt for corporate shareholders if participation exemption criteria are met", color: table_success},
            {comparison: belize, value: "No", color: table_success},
            {comparison: bermuda, value: "No if the company does not own real estate in Bermuda", color: table_success},
            {comparison: british_virgin_islands, value: "No", color: table_success},
            {comparison: cayman_islands, value: "No", color: table_success},
            {comparison: cyprus, value: "No, as long as the company does not own Cyprus real estate", color: table_success},
            {comparison: egypt, value: "No", color: table_success},
            {comparison: gibraltar, value: "No as long as the company does not own Gibraltar real estate", color: table_success},
            {comparison: guernsey, value: "No", color: table_success},
            {comparison: hong_kong, value: "Yes, only stamp duty up to 4.25%", color: table_danger},
            {comparison: ireland, value: "If the company does not own Irish land, buildings, mineral rights and exploration rights in the Irish continental shelf then only stamp duty of 1%", color: table_danger},
            {comparison: isle_of_man, value: "No", color: table_success},
            {comparison: jersey, value: "No", color: table_success},
            {comparison: liechtenstein, value: "No", color: table_success},
            {comparison: luxembourg, value: "No", color: table_success},
            {comparison: lithuania, value: "No", color: table_success},
            {comparison: malta, value: "No if the company does not hold Maltese real estate or if its foreign shareholder company is not controlled by Maltese residents", color: table_success},
            {comparison: mauritius, value: "No", color: table_success},
            {comparison: netherlands, value: "No if it satisfies the participation exemption criteria", color: table_success},
            {comparison: panama, value: "Yes, 10% on capital gains and 5% withholding tax", color: table_danger},
            {comparison: seychelles, value: "No", color: table_success},
            {comparison: singapore, value: "No", color: table_success},
            {comparison: dubai, value: "No", color: table_success},
            {comparison: ras_al_khaimah, value: "No", color: table_success},
            {comparison: switzerland, value: "No for individuals and companies that satisfy the participation exemption criteria", color: table_success}
        ],
        topic: "Taxability of disposal of shares by foreign shareholder",
        comparison: country
    }
    return jsonify(context)


# Get information about taxation_of_partnership_profits
@app.route("/taxation_of_partnership_profits")
def taxation_of_partnership_profits():
    context = {
        "data": [
            {comparison: bahamas, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: barbados, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: andorra, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: belize, value: n_a_our_analysis_covers_only_belize_ibcs, color: table_success},
            {comparison: bermuda, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: british_virgin_islands, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: cayman_islands, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: cyprus, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: egypt, value: "No", color: table_success},
            {comparison: gibraltar, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: guernsey, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: hong_kong, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: ireland, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: isle_of_man, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: jersey, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: liechtenstein, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: luxembourg, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: lithuania, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: malta, value: "Taxed in the hands of each partner except Limited Partnerships which are treated as companies", color: table_danger},
            {comparison: mauritius, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: netherlands, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: panama, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: seychelles, value: "Partnership taxed as individual", color: table_danger},
            {comparison: singapore, value: taxed_in_the_hands_of_each_partner, color: table_danger},
            {comparison: dubai, value: n_a_no_tax_for_dubai_difc_companies, color: table_success},
            {comparison: ras_al_khaimah, value: "N/A", color: table_success},
            {comparison: switzerland, value: taxed_in_the_hands_of_each_partner, color: table_danger}
        ],
        topic: "Taxation of partnership profits",
        comparison: country
    }
    return jsonify(context)


# Get information about taxation_of_branch_profits
@app.route("/taxation_of_branch_profits")
def taxation_of_branch_profits():
    context = {
        "data": [
            {comparison: bahamas, value: "Taxed as a company i.e. 0%", color: table_success},
            {comparison: barbados, value: "Taxed as a company", color: table_success},
            {comparison: andorra, value: treated_as_a_company, color: table_success},
            {comparison: belize, value: n_a_our_analysis_covers_only_belize_ibcs, color: table_success},
            {comparison: bermuda, value: "Taxed as a company", color: table_success},
            {comparison: british_virgin_islands, value: treated_as_a_company_i_e_zero_percent_tax, color: table_success},
            {comparison: cayman_islands, value: treated_as_a_company_i_e_zero_percent_tax, color: table_success},
            {comparison: cyprus, value: "Treated as a company i.e. taxed at 12.5%", color: table_danger},
            {comparison: egypt, value: "25 / 30%", color: table_danger},
            {comparison: gibraltar, value: "Treated as a company i.e. 10% tax", color: table_danger},
            {comparison: guernsey, value: "Treated as a company (0%, 10% or 20%)", color: table_danger},
            {comparison: hong_kong, value: treated_as_a_company, color: table_success},
            {comparison: ireland, value: treated_as_a_company, color: table_success},
            {comparison: isle_of_man, value: treated_as_a_company, color: table_success},
            {comparison: jersey, value: treated_as_a_company, color: table_success},
            {comparison: liechtenstein, value: treated_as_a_company, color: table_success},
            {comparison: luxembourg, value: treated_as_a_company, color: table_success},
            {comparison: lithuania, value: "Yes", color: table_success},
            {comparison: malta, value: treated_as_a_company, color: table_success},
            {comparison: mauritius, value: treated_as_a_company, color: table_success},
            {comparison: netherlands, value: treated_as_a_company, color: table_success},
            {comparison: panama, value: treated_as_a_company, color: table_success},
            {comparison: seychelles, value: treated_as_a_company, color: table_success},
            {comparison: singapore, value: treated_as_a_company, color: table_success},
            {comparison: dubai, value: treated_as_a_company_i_e_zero_percent_tax, color: table_success},
            {comparison: ras_al_khaimah, value: "N/A", color: table_success},
            {comparison: switzerland, value: treated_as_a_company, color: table_success}
        ],
        topic: "Taxation of branch profits",
        comparison: country
    }
    return jsonify(context)


# Get information about branch_remittance_tax
@app.route("/branch_remittance_tax")
def branch_remittance_tax():
    context = {
        "data": [
            {comparison: bahamas, value: "0%", color: table_success},
            {comparison: barbados, value: "10%", color: table_danger},
            {comparison: andorra, value: "No", color: table_success},
            {comparison: belize, value: n_a_our_analysis_covers_only_belize_ibcs, color: table_success},
            {comparison: bermuda, value: "0%", color: table_success},
            {comparison: british_virgin_islands, value: "0%", color: table_success},
            {comparison: cayman_islands, value: "0%", color: table_success},
            {comparison: cyprus, value: "0%", color: table_success},
            {comparison: egypt, value: "No", color: table_success},
            {comparison: gibraltar, value: "0%", color: table_success},
            {comparison: guernsey, value: "0%", color: table_success},
            {comparison: hong_kong, value: "0%", color: table_success},
            {comparison: ireland, value: "0%", color: table_success},
            {comparison: isle_of_man, value: "0%", color: table_success},
            {comparison: jersey, value: "0%", color: table_success},
            {comparison: liechtenstein, value: "0%", color: table_success},
            {comparison: luxembourg, value: "0%", color: table_success},
            {comparison: lithuania, value: "No", color: table_success},
            {comparison: malta, value: "0%", color: table_success},
            {comparison: mauritius, value: "0%", color: table_success},
            {comparison: netherlands, value: "0%", color: table_success},
            {comparison: panama, value: "10%", color: table_danger},
            {comparison: seychelles, value: "0%", color: table_success},
            {comparison: singapore, value: "0%", color: table_success},
            {comparison: dubai, value: "0%", color: table_success},
            {comparison: ras_al_khaimah, value: "N/A", color: table_success},
            {comparison: switzerland, value: "0%", color: table_success}
        ],
        topic: "Branch remittance tax",
        comparison: country
    }
    return jsonify(context)


# Get information about stamp_duty
@app.route("/stamp_duty")
def stamp_duty():
    context = {
        "data": [
            {comparison: bahamas, value: "Yes", color: table_danger},
            {comparison: barbados, value: "Yes", color: table_danger},
            {comparison: andorra, value: "No", color: table_success},
            {comparison: belize, value: "N/A - The Belize IBC is not subject to stamp duty", color: table_success},
            {comparison: bermuda, value: "Yes", color: table_danger},
            {comparison: british_virgin_islands, value: "Yes", color: table_danger},
            {comparison: cayman_islands, value: "Yes", color: table_danger},
            {comparison: cyprus, value: "Yes", color: table_danger},
            {comparison: egypt, value: "Yes", color: table_danger},
            {comparison: gibraltar, value: "Yes", color: table_danger},
            {comparison: guernsey, value: "No", color: table_success},
            {comparison: hong_kong, value: "Yes", color: table_danger},
            {comparison: ireland, value: "Yes", color: table_danger},
            {comparison: isle_of_man, value: "No", color: table_success},
            {comparison: jersey, value: "Yes", color: table_danger},
            {comparison: liechtenstein, value: "Yes", color: table_danger},
            {comparison: luxembourg, value: "No", color: table_success},
            {comparison: lithuania, value: "No", color: table_success},
            {comparison: malta, value: "Yes", color: table_danger},
            {comparison: mauritius, value: "No", color: table_success},
            {comparison: netherlands, value: "No", color: table_success},
            {comparison: panama, value: "Yes", color: table_danger},
            {comparison: seychelles, value: "No", color: table_success},
            {comparison: singapore, value: "Yes", color: table_danger},
            {comparison: dubai, value: "No", color: table_success},
            {comparison: ras_al_khaimah, value: "No", color: table_success},
            {comparison: switzerland, value: "Yes", color: table_danger}
        ],
        topic: "Stamp duty",
        comparison: country
    }
    return jsonify(context)


# Get information about spoken_languages
@app.route("/spoken_languages")
def spoken_languages():
    context = {
        "data": [
            {comparison: bahamas, value: "English", color: table_success},
            {comparison: barbados, value: "English, Bajan Creole", color: table_success},
            {comparison: andorra, value: "Catalan", color: table_success},
            {comparison: belize, value: "English", color: table_success},
            {comparison: bermuda, value: "English (official) and Portuguese (non-official)", color: table_success},
            {comparison: british_virgin_islands, value: "English", color: table_success},
            {comparison: cayman_islands, value: "English, Cayman Islands English", color: table_success},
            {comparison: cyprus, value: "Greek, Turkish", color: table_success},
            {comparison: egypt, value: "Arabic", color: table_success},
            {comparison: gibraltar, value: "English (official), Spanish, Llanito", color: table_success},
            {comparison: guernsey, value: "English, Guernsey dialect, Sercquiais, Auregnais dialect", color: table_success},
            {comparison: hong_kong, value: "English, Chinese (only Cantonese)", color: table_success},
            {comparison: ireland, value: "English, Irish, Ulster Scots", color: table_success},
            {comparison: isle_of_man, value: "English, Manx", color: table_success},
            {comparison: jersey, value: "English, French and Jersey dialect", color: table_success},
            {comparison: liechtenstein, value: "German", color: table_success},
            {comparison: luxembourg, value: " Luxembourgish, French, German", color: table_success},
            {comparison: lithuania, value: "Lithuanian", color: table_success},
            {comparison: malta, value: "Maltese, Maltese Sign Language, English, Italian", color: table_success},
            {comparison: mauritius, value: "English, French, Malay, Chinese, Tamil, 84% Creole (de facto), 5.3% Bhojpuri-Hindustani, 3.6% French, 7.1% Others (including English and Chinese)", color: table_success},
            {comparison: netherlands, value: "West Frisian, Papiamento, English, Limburgish, Dutch Low Saxon", color: table_success},
            {comparison: panama, value: "Spanish", color: table_success},
            {comparison: seychelles, value: "Seychellois Creole, English and French", color: table_success},
            {comparison: singapore, value: "English, Malay, Mandarin, Tamil, Roman (Latin), Simplified Chinese, Tamil", color: table_success},
            {comparison: dubai, value: "Arabic", color: table_success},
            {comparison: ras_al_khaimah, value: "Arabic", color: table_success},
            {comparison: switzerland, value: "German, French, Italian, Romansh", color: table_success}
        ],
        topic: "Spoken languages",
        comparison: country
    }
    return jsonify(context)


# Get information about oecd_members
@app.route("/oecd_members")
def oecd_members():
    context = {
        "data": [
            {comparison: bahamas, value: "No", color: table_success},
            {comparison: barbados, value: "No", color: table_success},
            {comparison: andorra, value: "No", color: table_success},
            {comparison: belize, value: "No", color: table_success},
            {comparison: bermuda, value: "No", color: table_success},
            {comparison: british_virgin_islands, value: "No", color: table_success},
            {comparison: cayman_islands, value: "No", color: table_success},
            {comparison: cyprus, value: "No", color: table_success},
            {comparison: egypt, value: "No", color: table_success},
            {comparison: gibraltar, value: "No", color: table_success},
            {comparison: guernsey, value: "No", color: table_success},
            {comparison: hong_kong, value: "No", color: table_success},
            {comparison: ireland, value: "Yes", color: table_danger},
            {comparison: isle_of_man, value: "No", color: table_success},
            {comparison: jersey, value: "No", color: table_success},
            {comparison: liechtenstein, value: "No", color: table_success},
            {comparison: luxembourg, value: "Yes", color: table_danger},
            {comparison: lithuania, value: "Yes", color: table_danger},
            {comparison: malta, value: "No", color: table_success},
            {comparison: mauritius, value: "No", color: table_success},
            {comparison: netherlands, value: "Yes", color: table_danger},
            {comparison: panama, value: "No", color: table_success},
            {comparison: seychelles, value: "No", color: table_success},
            {comparison: singapore, value: "No", color: table_success},
            {comparison: dubai, value: "No", color: table_success},
            {comparison: ras_al_khaimah, value: "No", color: table_success},
            {comparison: switzerland, value: "Yes", color: table_danger}
        ],
        topic: "OECD members",
        comparison: country
    }
    return jsonify(context)


# Get information about death_penalty
@app.route("/death_penalty")
def death_penalty():
    context = {
        "data": [
            {comparison: bahamas, value: "No", color: table_success},
            {comparison: barbados, value: "No", color: table_success},
            {comparison: andorra, value: "No", color: table_success},
            {comparison: belize, value: "No", color: table_success},
            {comparison: bermuda, value: "No", color: table_success},
            {comparison: british_virgin_islands, value: "No", color: table_success},
            {comparison: cayman_islands, value: "No", color: table_success},
            {comparison: cyprus, value: "No", color: table_success},
            {comparison: egypt, value: "Yes", color: table_danger},
            {comparison: gibraltar, value: "No", color: table_success},
            {comparison: guernsey, value: "No", color: table_success},
            {comparison: hong_kong, value: "No", color: table_success},
            {comparison: ireland, value: "No", color: table_success},
            {comparison: isle_of_man, value: "No", color: table_success},
            {comparison: jersey, value: "No", color: table_success},
            {comparison: liechtenstein, value: "No", color: table_success},
            {comparison: luxembourg, value: "No", color: table_success},
            {comparison: lithuania, value: "No", color: table_success},
            {comparison: malta, value: "No", color: table_success},
            {comparison: mauritius, value: "No", color: table_success},
            {comparison: netherlands, value: "No", color: table_success},
            {comparison: panama, value: "No", color: table_success},
            {comparison: seychelles, value: "No", color: table_success},
            {comparison: singapore, value: "Yes", color: table_danger},
            {comparison: dubai, value: "Yes", color: table_danger},
            {comparison: ras_al_khaimah, value: "Yes", color: table_danger},
            {comparison: switzerland, value: "No", color: table_success}
        ],
        topic: "Death penalty",
        comparison: country
    }
    return jsonify(context)


# Get information about airport
@app.route("/airport")
def airport():
    context = {
        "data": [
            {comparison: bahamas, value: "Lynden Pindling International Airport / Nassau", color: table_success},
            {comparison: barbados, value: "Grantley Adams International Airport / Seawell, Christ Church", color: table_success},
            {comparison: andorra, value: "Aéroport Andorre–La Seu d'Urgell / Aeroport Andorra - La Seu, s/n, 25711 Montferrer, Lérida, Espagne", color: table_success},
            {comparison: belize, value: "Philip S. W. Goldson International Airport / Ladyville", color: table_success},
            {comparison: bermuda, value: "L.F. Wade International Airport / St. David's Island", color: table_success},
            {comparison: british_virgin_islands, value: " Terrance B. Lettsome International Airport / Beef Island / Tortola", color: table_success},
            {comparison: cayman_islands, value: "Owen Roberts International Airport /  George Town, Grand Cayman", color: table_success},
            {comparison: cyprus, value: "Nicosia International Airport / Nicosia", color: table_success},
            {comparison: egypt, value: "Cairo International Airport / Le Caire", color: table_success},
            {comparison: gibraltar, value: "Aéroport international de Gibraltar / British Lines Road, GX11 1AA, Gibraltar", color: table_success},
            {comparison: guernsey, value: "Guernsey Airport / Forest, Guernsey", color: table_success},
            {comparison: hong_kong, value: "Aéroport international de Hong Kong / 1 Sky Plaza Rd, Chek Lap Kok, Hong Kong", color: table_success},
            {comparison: ireland, value: "Dublin Airport / Dublin", color: table_success},
            {comparison: isle_of_man, value: "Isle of Man Airport; Ronaldsway Airport / Ronaldsway, Malew, Isle of Man", color: table_success},
            {comparison: jersey, value: "Aéroport de Jersey / St Peter JE1 1BY, Jersey", color: table_success},
            {comparison: liechtenstein, value: "No airport", color: table_success},
            {comparison: lithuania, value: "Vilnius International Airport / Vilnius", color: table_success},
            {comparison: luxembourg, value: "Aéroport de Luxembourg-Findel / Luxembourg City", color: table_success},
            {comparison: malta, value: "Aéroport international de Malte / Luqa LQA 4000, Malte", color: table_success},
            {comparison: mauritius, value: "Mauritius_Airport / A10 Royal Road, Plaine Magnien, Maurice", color: table_success},
            {comparison: netherlands, value: "Amsterdam Airport Schiphol / Amsterdam / Haarlemmermeer", color: table_success},
            {comparison: panama, value: "Tocumen International Airport / Panama City", color: table_success},
            {comparison: seychelles, value: "Seychelles_Airport / 5th June Ave, Mahé, Anse des Genets, Seychelles", color: table_success},
            {comparison: singapore, value: "Singapore Changi Airport / Changi Air Base /  Changi, Singapore", color: table_success},
            {comparison: dubai, value: "Aéroport international de Dubaï / Dubaï - Émirats arabes unis", color: table_success},
            {comparison: ras_al_khaimah, value: "Aéroport international de Ras el Khaïmah / North Ras Al Khaimah - Émirats arabes unis", color: table_success},
            {comparison: switzerland, value: "Bern Airport / Berne", color: table_success}
        ],
        topic: "Airport",
        comparison: country
    }
    return jsonify(context)


# Get information about average_lowest_temperature
@app.route("/average_lowest_temperature")
def average_lowest_temperature():
    context = {
        "data": [
            {comparison: bahamas, value: "18,17", color: table_success},
            {comparison: barbados, value: "23,71", color: table_success},
            {comparison: andorra, value: "-0,92", color: table_success},
            {comparison: belize, value: "19,72", color: table_success},
            {comparison: bermuda, value: "9", color: table_success},
            {comparison: british_virgin_islands, value: "21", color: table_success},
            {comparison: cayman_islands, value: "21,17", color: table_success},
            {comparison: cyprus, value: "7,03", color: table_success},
            {comparison: egypt, value: "10,95", color: table_success},
            {comparison: gibraltar, value: "11", color: table_success},
            {comparison: guernsey, value: "6", color: table_success},
            {comparison: hong_kong, value: "11,62", color: table_success},
            {comparison: ireland, value: "0,27", color: table_success},
            {comparison: isle_of_man, value: "-0,14", color: table_success},
            {comparison: jersey, value: "6", color: table_success},
            {comparison: liechtenstein, value: "-12,01", color: table_success},
            {comparison: luxembourg, value: "-7,17", color: table_success},
            {comparison: lithuania, value: "-15,18", color: table_success},
            {comparison: malta, value: "8,4", color: table_success},
            {comparison: mauritius, value: "19,24", color: table_success},
            {comparison: netherlands, value: "-5,42", color: table_success},
            {comparison: panama, value: "24,08", color: table_success},
            {comparison: seychelles, value: "22,61", color: table_success},
            {comparison: singapore, value: "24,03", color: table_success},
            {comparison: dubai, value: "15,74", color: table_success},
            {comparison: ras_al_khaimah, value: "15,74", color: table_success},
            {comparison: switzerland, value: "-8,81", color: table_success}
        ],
        topic: "Average lowest temperature",
        comparison: country
    }
    return jsonify(context)


# Get information about average_annual_precipitation
@app.route("/average_annual_precipitation")
def average_annual_precipitation():
    context = {
        "data": [
            {comparison: bahamas, value: "165,00", color: table_success},
            {comparison: barbados, value: "620,00", color: table_success},
            {comparison: andorra, value: "214,00", color: table_success},
            {comparison: belize, value: "589,00", color: table_success},
            {comparison: bermuda, value: "160,00", color: table_success},
            {comparison: british_virgin_islands, value: "145,00", color: table_success},
            {comparison: cayman_islands, value: "414,00", color: table_success},
            {comparison: cyprus, value: "95,00", color: table_success},
            {comparison: egypt, value: "22,63", color: table_success},
            {comparison: gibraltar, value: "140,00", color: table_success},
            {comparison: guernsey, value: "61,00", color: table_success},
            {comparison: hong_kong, value: "455,00", color: table_success},
            {comparison: ireland, value: "273,00", color: table_success},
            {comparison: isle_of_man, value: "125,00", color: table_success},
            {comparison: jersey, value: "61,00", color: table_success},
            {comparison: liechtenstein, value: "1 000,00", color: table_success},
            {comparison: luxembourg, value: "100,00", color: table_success},
            {comparison: lithuania, value: "80,00", color: table_success},
            {comparison: malta, value: "108,60", color: table_success},
            {comparison: mauritius, value: "1 409,00", color: table_success},
            {comparison: netherlands, value: "900,00", color: table_success},
            {comparison: panama, value: "4 296,41", color: table_success},
            {comparison: seychelles, value: "3 500,00", color: table_success},
            {comparison: singapore, value: "2 340,00", color: table_success},
            {comparison: dubai, value: "10,00", color: table_success},
            {comparison: ras_al_khaimah, value: "10,00", color: table_success},
            {comparison: switzerland, value: "2 368,00", color: table_success}
        ],
        topic: "Average annual precipitation",
        comparison: country
    }
    return jsonify(context)


# Get information about registry_of_commerce
@app.route("/registry_of_commerce")
def registry_of_commerce():
    context = {
        "data": [
            {comparison: bahamas, value: "Bahamas Chamber of Industry and Commerce /  Shirley Street & Collins Avenue P.O. Box N-665 Nassau Bahamas", color: table_success},
            {comparison: barbados, value: "Barbados Chamber of Commerce & Industry / Braemar Court, Deighton Road, St. Michael Barbados", color: table_success},
            {comparison: andorra, value: "Cambra de Comerç, Indústria i Serveis d'Andorra / Carrer Prat de la Creu, 8, AD500 Andorra la Vella, Andorre", color: table_success},
            {comparison: belize, value: "BELIZE CHAMBER OF COMMERCE AND INDUSTRY / P.O. Box 291 4792 Coney Drive First Floor, Withfield Tower Belize City, Belize Central America", color: table_success},
            {comparison: bermuda, value: "Registrar of Companies of Bermuda / 30 Parliament Street Hamilton HM 12 Bermuda", color: table_success},
            {comparison: british_virgin_islands, value: "British Virgin Islands Financial Services Commission / Pasea Estate P.O. Box 418 Road Town, Tortola, VG 1110 British Virgin Islands", color: table_success},
            {comparison: cayman_islands, value: "Cayman Islands Chamber of Commerce / 23 Lime Tree Bay Avenue, West Bay Road Governors Square, KY1-1102, Îles Caïmans", color: table_success},
            {comparison: cyprus, value: "Ministère de l'énergie, du commerce, de l'industrie et du tourisme, Andreas Araouzou 6, Nicosie, Chypre / Département deEnergie,Commerce,Industrie etTourisme, CY-1421, Nicosie, Chypre", color: table_success},
            {comparison: egypt, value: "Cairo Chamber of Commerce / 92 El Tahrir, Ad Dawawin, Abdeen, Cairo Governorate, Égypte", color: table_success},
            {comparison: gibraltar, value: "Gibraltar Chamber Of Commerce / Watergate House 2/6 Casemates Gibraltar", color: table_success},
            {comparison: guernsey, value: "Guernsey Registry / Market Building PO Box 451 Fountain Street St Peter Port Guernsey GY1 3GX Channel Islands", color: table_success},
            {comparison: hong_kong, value: "Hong Kong Companies Registry / 14th floor, High Block, Queensway Government Offices, 66 Queensway, Hong Kong", color: table_success},
            {comparison: ireland, value: "Companies Registration Office Ireland / Bloom House, Gloucester Place Lower, Dublin 1, D01 C8P4", color: table_success},
            {comparison: isle_of_man, value: "I O M Chamber of Commerce / 21 Athol St, Douglas IM1 1LB", color: table_success},
            {comparison: jersey, value: "Jersey Chamber of Commerce / 25 Pier Rd, St Helier JE1 4HF, Jersey", color: table_success},
            {comparison: liechtenstein, value: "Liechensteinische Industrie- und Handelskammer (LIHK) / Altenbach 8, 9490 Vaduz, Liechtenstein", color: table_success},
            {comparison: luxembourg, value: "Registre de commerce et des societes / 14, rue Erasme L-1468 Luxembourg", color: table_success},
            {comparison: lithuania, value: "State Enterprise Centre of Registers  / Vinco Kudirkos g. 18-3, LT-03105 Vilnius, LITHUANIA", color: table_success},
            {comparison: malta, value: "Malta Chamber of Commerce / 64 Republic St, Valletta, Malte", color: table_success},
            {comparison: mauritius, value: "The Mauritius Chamber of Commerce and Industry / 2nd Floor, Anglo-Mauritius House, 6, Adolphe de Plevitz Street, Port Louis, Mauritius", color: table_success},
            {comparison: netherlands, value: "Chambre de commerce d'Amsterdam / De Ruijterkade 5  ,1013 AA  Amsterdam", color: table_success},
            {comparison: panama, value: "Registro publico de panama / Vía España, Panamá, Panama", color: table_success},
            {comparison: seychelles, value: "Seychelles Chamber Of Commerce & Industry / H.I.S House, Providence Industrial Estate, Victoria, Mahe, Seychelles", color: table_success},
            {comparison: singapore, value: "Singapore International Chamber of Commerce / 6 Raffles Quay #10-01 Singapore 048580", color: table_success},
            {comparison: dubai, value: "Dubai Chamber of Commerce & Industry / Baniyas Road, Deira P.O. Box 1457 – Dubai, U.A.E", color: table_success},
            {comparison: ras_al_khaimah, value: "RAK International Corporate Centre / Floor 8, Post Box #30099, RAKBANK Headquarters, Government of Ras Al Khaimah, Ras Al Khaimah, United Arab Emirates", color: table_success},
            {comparison: switzerland, value: "Handelsregisteramt des Kantons Bern / Gerechtigkeitsgasse 36 Postfach 627 3000 Bern 8", color: table_success}
        ],
        topic: "Registry of commerce",
        comparison: country
    }
    return jsonify(context)


# Get information about highest_personal_income_tax
@app.route("/highest_personal_income_tax")
def highest_personal_income_tax():
    context = {
        "data": [
            {comparison: bahamas, value: "0", color: table_success},
            {comparison: barbados, value: "33,5", color: table_danger},
            {comparison: andorra, value: "10", color: table_danger},
            {comparison: belize, value: "More than $26 000, it's 25% and less than $26 000, it's 0%", color: table_danger},
            {comparison: bermuda, value: "0", color: table_success},
            {comparison: british_virgin_islands, value: "0", color: table_success},
            {comparison: cayman_islands, value: "0", color: table_success},
            {comparison: cyprus, value: "35", color: table_danger},
            {comparison: egypt, value: "22,5", color: table_danger},
            {comparison: gibraltar, value: "First £25,001: 20% / £25,001 - £353,000: 29% / £353,001 - £704,800: 20% / £704,801 - £1,000,000: 10%", color: table_danger},
            {comparison: guernsey, value: "20", color: table_danger},
            {comparison: hong_kong, value: "17", color: table_danger},
            {comparison: ireland, value: "48", color: table_danger},
            {comparison: isle_of_man, value: "20", color: table_danger},
            {comparison: jersey, value: "20", color: table_danger},
            {comparison: liechtenstein, value: "24", color: table_danger},
            {comparison: luxembourg, value: "48,78", color: table_danger},
            {comparison: lithuania, value: "15", color: table_danger},
            {comparison: malta, value: "35", color: table_danger},
            {comparison: mauritius, value: "15", color: table_danger},
            {comparison: netherlands, value: "52", color: table_danger},
            {comparison: panama, value: "25", color: table_danger},
            {comparison: seychelles, value: "15", color: table_danger},
            {comparison: singapore, value: "22", color: table_danger},
            {comparison: dubai, value: "0", color: table_success},
            {comparison: ras_al_khaimah, value: "0", color: table_success},
            {comparison: switzerland, value: "40", color: table_danger}
        ],
        topic: "Highest personal income tax",
        comparison: country
    }
    return jsonify(context)


# Get information about land_area
@app.route("/land_area")
def land_area():
    context = {
        "data": [
            {comparison: bahamas, value: "13 878,00", color: table_success},
            {comparison: barbados, value: "431,00", color: table_success},
            {comparison: andorra, value: "467,60", color: table_success},
            {comparison: belize, value: "22 966,00", color: table_success},
            {comparison: bermuda, value: "53,20", color: table_success},
            {comparison: british_virgin_islands, value: "153,00", color: table_success},
            {comparison: cayman_islands, value: "264,00", color: table_success},
            {comparison: cyprus, value: "9 251,00", color: table_success},
            {comparison: egypt, value: "1 010 000,00", color: table_success},
            {comparison: gibraltar, value: "6,80", color: table_success},
            {comparison: guernsey, value: "65,00", color: table_success},
            {comparison: hong_kong, value: "2 754,00", color: table_success},
            {comparison: ireland, value: "84 421,00", color: table_success},
            {comparison: isle_of_man, value: "572,00", color: table_success},
            {comparison: jersey, value: "119,50", color: table_success},
            {comparison: liechtenstein, value: "160,00", color: table_success},
            {comparison: luxembourg, value: "2 586,00", color: table_success},
            {comparison: lithuania, value: "65 300,00", color: table_success},
            {comparison: malta, value: "316,00", color: table_success},
            {comparison: mauritius, value: "2 040,00", color: table_success},
            {comparison: netherlands, value: "41 543,00", color: table_success},
            {comparison: panama, value: "74 177,00", color: table_success},
            {comparison: seychelles, value: "459,00", color: table_success},
            {comparison: singapore, value: "719,90", color: table_success},
            {comparison: dubai, value: "4 114,00", color: table_success},
            {comparison: ras_al_khaimah, value: "2 486,00", color: table_success},
            {comparison: switzerland, value: "41 285,00", color: table_success}
        ],
        topic: "Land area",
        comparison: country
    }
    return jsonify(context)


# Get information about population
@app.route("/population")
def population():
    context = {
        "data": [
            {comparison: bahamas, value: "0,38", color: table_success},
            {comparison: barbados, value: "0,286388", color: table_success},
            {comparison: andorra, value: "0,077281", color: table_success},
            {comparison: belize, value: "0,39", color: table_success},
            {comparison: bermuda, value: "0,07", color: table_success},
            {comparison: british_virgin_islands, value: "0,031196", color: table_success},
            {comparison: cayman_islands, value: "0,06", color: table_success},
            {comparison: cyprus, value: "0,86", color: table_success},
            {comparison: egypt, value: "96,2", color: table_success},
            {comparison: gibraltar, value: "0,034571", color: table_success},
            {comparison: guernsey, value: "0,066502", color: table_success},
            {comparison: hong_kong, value: "7,41", color: table_success},
            {comparison: ireland, value: "4,84", color: table_success},
            {comparison: isle_of_man, value: "0,084831", color: table_success},
            {comparison: jersey, value: "0,1055", color: table_success},
            {comparison: liechtenstein, value: "0,04", color: table_success},
            {comparison: luxembourg, value: "0,6", color: table_success},
            {comparison: lithuania, value: "2,81", color: table_success},
            {comparison: malta, value: "0,48", color: table_success},
            {comparison: mauritius, value: "1,26", color: table_success},
            {comparison: netherlands, value: "17,12", color: table_success},
            {comparison: panama, value: "4,1", color: table_success},
            {comparison: seychelles, value: "0,1", color: table_success},
            {comparison: singapore, value: "5,61", color: table_success},
            {comparison: dubai, value: "3,331", color: table_success},
            {comparison: ras_al_khaimah, value: "0,115949", color: table_success},
            {comparison: switzerland, value: "8,48", color: table_success}
        ],
        topic: "Population",
        comparison: country
    }
    return jsonify(context)


# Get information about taxation_on_foreign_income
@app.route("/taxation_on_foreign_income")
def taxation_on_foreign_income():
    context = {
        "data": [
            {comparison: bahamas, value: "0", color: table_success},
            {comparison: barbados, value: "2,5", color: table_danger},
            {comparison: andorra, value: "10", color: table_danger},
            {comparison: belize, value: "0", color: table_success},
            {comparison: bermuda, value: "0", color: table_success},
            {comparison: british_virgin_islands, value: "0", color: table_success},
            {comparison: cayman_islands, value: "0", color: table_success},
            {comparison: cyprus, value: "12,5", color: table_danger},
            {comparison: egypt, value: "22,5", color: table_danger},
            {comparison: gibraltar, value: "0", color: table_success},
            {comparison: guernsey, value: "0", color: table_success},
            {comparison: hong_kong, value: "0", color: table_success},
            {comparison: ireland, value: "12,5", color: table_danger},
            {comparison: isle_of_man, value: "0", color: table_success},
            {comparison: jersey, value: "0", color: table_success},
            {comparison: liechtenstein, value: "12,5", color: table_danger},
            {comparison: luxembourg, value: "18", color: table_danger},
            {comparison: lithuania, value: "21", color: table_danger},
            {comparison: malta, value: "35", color: table_danger},
            {comparison: mauritius, value: "15", color: table_danger},
            {comparison: netherlands, value: "25", color: table_danger},
            {comparison: panama, value: "0", color: table_success},
            {comparison: seychelles, value: "0", color: table_success},
            {comparison: singapore, value: "0", color: table_success},
            {comparison: dubai, value: "0", color: table_success},
            {comparison: ras_al_khaimah, value: "0", color: table_success},
            {comparison: switzerland, value: "7,83", color: table_danger}
        ],
        topic: "Taxation on foreign income",
        comparison: country
    }
    return jsonify(context)


# Get information about net_worth_tax
@app.route("/net_worth_tax")
def net_worth_tax():
    context = {
        "data": [
            {comparison: bahamas, value: "No", color: table_success},
            {comparison: barbados, value: "No", color: table_success},
            {comparison: andorra, value: "No", color: table_success},
            {comparison: belize, value: "-", color: table_danger},
            {comparison: bermuda, value: "No", color: table_success},
            {comparison: british_virgin_islands, value: "No", color: table_success},
            {comparison: cayman_islands, value: "No", color: table_success},
            {comparison: cyprus, value: "-", color: table_danger},
            {comparison: egypt, value: "No", color: table_success},
            {comparison: gibraltar, value: "No", color: table_success},
            {comparison: guernsey, value: "No", color: table_success},
            {comparison: hong_kong, value: "No", color: table_success},
            {comparison: ireland, value: "No", color: table_success},
            {comparison: isle_of_man, value: "No", color: table_success},
            {comparison: jersey, value: "No", color: table_success},
            {comparison: liechtenstein, value: "Yes", color: table_danger},
            {comparison: luxembourg, value: "No", color: table_success},
            {comparison: lithuania, value: "No", color: table_success},
            {comparison: malta, value: "No", color: table_success},
            {comparison: mauritius, value: "No", color: table_success},
            {comparison: netherlands, value: "No", color: table_success},
            {comparison: panama, value: "No", color: table_success},
            {comparison: seychelles, value: "-", color: table_danger},
            {comparison: singapore, value: "No", color: table_success},
            {comparison: dubai, value: "Yes", color: table_danger},
            {comparison: ras_al_khaimah, value: "No", color: table_success},
            {comparison: switzerland, value: "No", color: table_success}
        ],
        topic: "Net worth tax",
        comparison: country
    }
    return jsonify(context)


# Get information about free_mobile_operator
@app.route("/free_mobile_operator")
def free_mobile_operator():
    context = {
        "data": [
            {comparison: bahamas, value: "Yes", color: table_success},
            {comparison: barbados, value: "No", color: table_danger},
            {comparison: andorra, value: "Yes", color: table_success},
            {comparison: belize, value: "No", color: table_danger},
            {comparison: bermuda, value: "Yes", color: table_success},
            {comparison: british_virgin_islands, value: "No", color: table_danger},
            {comparison: cayman_islands, value: "Yes", color: table_success},
            {comparison: cyprus, value: "Yes", color: table_success},
            {comparison: egypt, value: "No", color: table_danger},
            {comparison: gibraltar, value: "Yes", color: table_success},
            {comparison: guernsey, value: "Yes", color: table_success},
            {comparison: hong_kong, value: "Yes", color: table_success},
            {comparison: ireland, value: "Yes", color: table_success},
            {comparison: isle_of_man, value: "Yes", color: table_success},
            {comparison: jersey, value: "Yes", color: table_success},
            {comparison: liechtenstein, value: "Yes", color: table_success},
            {comparison: luxembourg, value: "Yes", color: table_success},
            {comparison: lithuania, value: "Yes", color: table_success},
            {comparison: malta, value: "Yes", color: table_success},
            {comparison: mauritius, value: "No", color: table_danger},
            {comparison: netherlands, value: "Yes", color: table_success},
            {comparison: panama, value: "Yes", color: table_success},
            {comparison: seychelles, value: "No", color: table_danger},
            {comparison: singapore, value: "Yes", color: table_success},
            {comparison: dubai, value: "No", color: table_danger},
            {comparison: ras_al_khaimah, value: "No", color: table_danger},
            {comparison: switzerland, value: "Yes", color: table_success}
        ],
        topic: "Free mobile operator",
        comparison: country
    }
    return jsonify(context)


# Get information about become_permanent_resident
@app.route("/become_permanent_resident")
def become_permanent_resident():
    context = {
        "data": [
            {comparison: bahamas, value: "20", color: table_danger},
            {comparison: barbados, value: "16", color: table_danger},
            {comparison: andorra, value: "20", color: table_danger},
            {comparison: belize, value: "1", color: table_success},
            {comparison: bermuda, value: "20", color: table_danger},
            {comparison: british_virgin_islands, value: "20", color: table_danger},
            {comparison: cayman_islands, value: "9", color: table_danger},
            {comparison: cyprus, value: "2", color: table_success},
            {comparison: egypt, value: "3", color: table_success},
            {comparison: gibraltar, value: "0", color: table_success},
            {comparison: guernsey, value: "6", color: table_danger},
            {comparison: hong_kong, value: "7", color: table_danger},
            {comparison: ireland, value: "5", color: table_danger},
            {comparison: isle_of_man, value: "Difficult", color: table_danger},
            {comparison: jersey, value: "5", color: table_danger},
            {comparison: liechtenstein, value: "5", color: table_danger},
            {comparison: luxembourg, value: "7", color: table_danger},
            {comparison: lithuania, value: "5", color: table_danger},
            {comparison: malta, value: "1", color: table_success},
            {comparison: mauritius, value: "Difficult", color: table_danger},
            {comparison: netherlands, value: "5", color: table_danger},
            {comparison: panama, value: "1", color: table_success},
            {comparison: seychelles, value: "Difficult", color: table_danger},
            {comparison: singapore, value: "Investors", color: table_danger},
            {comparison: dubai, value: "5", color: table_danger},
            {comparison: ras_al_khaimah, value: "Difficult", color: table_danger},
            {comparison: switzerland, value: "Difficult", color: table_danger}
        ],
        topic: "Become permanent resident",
        comparison: country
    }
    return jsonify(context)


# Get information about social_security_rate_for_corporations
@app.route("/social_security_rate_for_corporations")
def social_security_rate_for_corporations():
    context = {
        "data": [
            {comparison: bahamas, value: "5,9", color: table_danger},
            {comparison: barbados, value: "11,25", color: table_danger},
            {comparison: andorra, value: "14,5", color: table_danger},
            {comparison: belize, value: "-", color: table_danger},
            {comparison: bermuda, value: "-", color: table_danger},
            {comparison: british_virgin_islands, value: "Social Security: 4,5 ; National Health Insurance: 3,75", color: table_danger},
            {comparison: cayman_islands, value: "0", color: table_success},
            {comparison: cyprus, value: "7,8", color: table_danger},
            {comparison: egypt, value: "26", color: table_danger},
            {comparison: gibraltar, value: "GIP 36,50 per week", color: table_danger},
            {comparison: guernsey, value: "6,6", color: table_danger},
            {comparison: hong_kong, value: "0", color: table_success},
            {comparison: ireland, value: "10,75", color: table_danger},
            {comparison: isle_of_man, value: "-", color: table_danger},
            {comparison: jersey, value: "6.5% on earnings up to £4,180 per month, plus an additional 2% on earnings over £4,180 and under £13,828 per month", color: table_danger},
            {comparison: liechtenstein, value: "-", color: table_danger},
            {comparison: luxembourg, value: "12,67", color: table_danger},
            {comparison: lithuania, value: "30,98", color: table_danger},
            {comparison: malta, value: "10", color: table_danger},
            {comparison: mauritius, value: "6", color: table_danger},
            {comparison: netherlands, value: "18,69", color: table_danger},
            {comparison: panama, value: "12,5", color: table_danger},
            {comparison: seychelles, value: "0", color: table_success},
            {comparison: singapore, value: "17", color: table_danger},
            {comparison: dubai, value: "12,5", color: table_danger},
            {comparison: ras_al_khaimah, value: "12,5", color: table_danger},
            {comparison: switzerland, value: "6,23", color: table_danger}
        ],
        topic: "Social security rate for corporations",
        comparison: country
    }
    return jsonify(context)


# Get information about social_security_rate_for_employees
@app.route("/social_security_rate_for_employees")
def social_security_rate_for_employees():
    context = {
        "data": [
            {comparison: bahamas, value: "3,9", color: table_danger},
            {comparison: barbados, value: "10,1", color: table_danger},
            {comparison: andorra, value: "9", color: table_danger},
            {comparison: belize, value: "-", color: table_danger},
            {comparison: bermuda, value: "-", color: table_danger},
            {comparison: british_virgin_islands, value: "Social Scurity: 4 ; National Health Insurance: 3,75", color: table_danger},
            {comparison: cayman_islands, value: "0", color: table_success},
            {comparison: cyprus, value: "7,8", color: table_danger},
            {comparison: egypt, value: "14", color: table_danger},
            {comparison: gibraltar, value: "GIP 27,50 per week", color: table_danger},
            {comparison: guernsey, value: "6,6", color: table_danger},
            {comparison: hong_kong, value: "0", color: table_success},
            {comparison: ireland, value: "4", color: table_danger},
            {comparison: isle_of_man, value: "-", color: table_danger},
            {comparison: jersey, value: "6", color: table_danger},
            {comparison: liechtenstein, value: "-", color: table_danger},
            {comparison: luxembourg, value: "12,45", color: table_danger},
            {comparison: lithuania, value: "11", color: table_danger},
            {comparison: malta, value: "10", color: table_danger},
            {comparison: mauritius, value: "3", color: table_danger},
            {comparison: netherlands, value: "27,65", color: table_danger},
            {comparison: panama, value: "9,75", color: table_danger},
            {comparison: seychelles, value: "0", color: table_success},
            {comparison: singapore, value: "20", color: table_danger},
            {comparison: dubai, value: "5", color: table_danger},
            {comparison: ras_al_khaimah, value: "5", color: table_danger},
            {comparison: switzerland, value: "6,23", color: table_danger}
        ],
        topic: "Social security rate for employees",
        comparison: country
    }
    return jsonify(context)


# Get information about post_office_box_for_private_person
@app.route("/post_office_box_for_private_person")
def post_office_box_for_private_person():
    context = {
        "data": [
            {comparison: bahamas, value: "MailNetwork / Nassau", color: table_success},
            {comparison: barbados, value: "The General Post Office / Reef road, Bridgetown, Barbade", color: table_success},
            {comparison: andorra, value: "-", color: table_success},
            {comparison: belize, value: "Belize Postal Service / 150 North Front Street, Belize City, Belize", color: table_success},
            {comparison: bermuda, value: "Mailboxes Unlimited / 48 Par - La - Ville Road, Hamilton, Bermuda, HM11", color: table_success},
            {comparison: british_virgin_islands, value: "-", color: table_success},
            {comparison: cayman_islands, value: "Cayman Islands Postal Service / George Town Post Office 14 Edward Street, Grand Cayman, Cayman Islands Ky1-1100", color: table_success},
            {comparison: cyprus, value: "Cyprus Post / 100, Prodromou Street, 2063 Strovolos", color: table_success},
            {comparison: egypt, value: "Egypt Post / Al Seka Al Hadid, Mansheya El-Bakry, Heliopolis, Cairo Governorate, Égypte", color: table_success},
            {comparison: gibraltar, value: "Royal Gibraltar Post Office / Royal Gibraltar Post Office Postal Headquarters 104 Main Street GX11 1AA GIBRALTAR", color: table_success},
            {comparison: guernsey, value: " Guernsey Post Office / Guernsey Post Ltd Envoy House La Vrangue St Peter Port GUERNSEY GY1 1AA", color: table_success},
            {comparison: hong_kong, value: "Hong Kong Post Office / Revenue Tower, 5 Gloucester Rd, Wan Chai, Hong Kong", color: table_success},
            {comparison: ireland, value: "Nethouse / NetHouse, 113 Lower Rathmines Road, Dublin 6, Ireland", color: table_success},
            {comparison: isle_of_man, value: "Isle Of Man Post Office / Isle of Man Post Office Postal Headquarters Spring Valley Industrial Estate Douglas, IM2 1AA", color: table_success},
            {comparison: jersey, value: "Jersey Post / Jersey Post Postal Headquarters JERSEY JE1 1AA", color: table_success},
            {comparison: liechtenstein, value: "-", color: table_success},
            {comparison: luxembourg, value: "-", color: table_success},
            {comparison: lithuania, value: "Lithuania Post / AB Lietuvos paštas J. Jasinskio g. 16, 03500 Vilnius", color: table_success},
            {comparison: malta, value: "Malta Post / MaltaPost p.l.c Customer Care Department 305, Triq Hal-Qormi, Marsa  MTP 1001", color: table_success},
            {comparison: mauritius, value: "Mauritius Post / Attn. OIC. Boxes The Mauritius Post Ltd 3, Dumas Street Port Louis", color: table_success},
            {comparison: netherlands, value: "Post NL / Postbox 99180 8900 NA Leeuwarden", color: table_success},
            {comparison: panama, value: "", color: table_success},
            {comparison: seychelles, value: "Seychelles Postal Services / Seychelles Postal Services P.O.Box 60, Victoria, Mahé, Seychelles", color: table_success},
            {comparison: singapore, value: "Singapore Post / Singapore Post Limited 10 Eunos Road 8 Singapore Post Centre Singapore 408600", color: table_success},
            {comparison: dubai, value: "Emirates Post Group / Marrakech Street, Garhoud, Next to Al Mawakeb School POBOX: 99999 Dubai, United Arab Emirates", color: table_success},
            {comparison: ras_al_khaimah, value: "Emirates Post Group / Marrakech Street, Garhoud, Next to Al Mawakeb School POBOX: 99999 Dubai, United Arab Emirates", color: table_success},
            {comparison: switzerland, value: "Swiss Post / Poste CH SA Contact Center Poste Wankdorfallee 4 3030 Berne", color: table_success}
        ],
        topic: "Post office box for private person",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_treaties
@app.route("/tax_treaties")
def tax_treaties():
    context = {
        "data": [
            {comparison: andorra,
             value: '''
            France	(In-force) / 
            Germany (Pending) / 
            Liechtenstein (Pending) / 
            Luxembourg (Pending) / 
            Malta (Pending) / 
            Portugal (Pending) / 
            Spain (Pending) / 
            United Arab Emirates (Pending)
            ''', color: table_success},
            {comparison: bahamas,
             value: '''
             -
             ''', color: table_success},
            {comparison: barbados,
             value: '''
            Austria	(In-force) / 
            Bahrain	(In-force) / 
            Botswana	(In-force) / 
            Canada	(In-force) / 
            China	(In-force) / 
            Cuba	(In-force) / 
            Czech Republic	(In-force) / 
            Finland	(In-force) / 
            Ghana	(Pending) /
            Iceland	(In-force) / 
            Italy	(Pending) /
            Luxembourg	(In-force) / 
            Malta	(In-force) / 
            Mauritius	(In-force) / 
            Mexico	(In-force) / 
            Netherlands	(In-force) / 
            Norway	(In-force) / 
            Panama	(In-force) / 
            Portugal	(Pending) /
            Qatar	(Pending) /
            San Marino	(Pending) /
            Seychelles	(In-force) / 
            Singapore	(In-force) / 
            Slovakia	(Pending) /
            Spain	(In-force) / 
            Sweden	(In-force) / 
            Switzerland	(In-force) / 
            United Arab Emirates	(Pending) /
            United Kingdom	(In-force) / 
            United States	(In-force) / 
            Venezuela	(In-force)
             ''', color: table_success},
            {comparison: belize,
             value: '''
            Austria	(In-force) / 
            United Arab Emirates (Pending)
            ''', color: table_success},
            {comparison: bermuda, value: "-", color: table_success},
            {comparison: british_virgin_islands, value: "-", color: table_success},
            {comparison: cayman_islands, value: "-", color: table_success},
            {comparison: cyprus, value: '''
            Armenia	(In-force) / 
            Austria	(In-force) / 
            Bahrain	(Pending) /
            Belarus	(In-force) / 
            Belgium	(In-force) / 
            Bosnia and Herzegovina	(In-force) / 
            Bulgaria	(In-force) / 
            Canada	(In-force) / 
            China	(In-force) / 
            Czech Republic	(In-force) / 
            Denmark	(In-force) / 
            Egypt	(In-force) / 
            Estonia	(In-force) / 
            Ethiopia	(Pending) /
            Finland	(In-force) / 
            France	(In-force) / 
            Georgia	(In-force) / 
            Germany	(In-force) / 
            Greece	(In-force) / 
            Guernsey	(In-force) / 
            Hungary	(In-force) / 
            Iceland	(In-force) / 
            India	(In-force) / 
            Iran	(Pending) /
            Ireland	(In-force) / 
            Italy	(In-force) / 
            Jersey	(Pending) /
            Kuwait	(In-force) / 
            Latvia	(In-force) / 
            Lebanon	(In-force) / 
            Lithuania	(In-force) / 
            Malta	(In-force) / 
            Mauritius	(In-force) / 
            Moldova	(In-force) / 
            Montenegro	(In-force) / 
            Norway	(In-force) / 
            Poland	(In-force) / 
            Portugal	(In-force) / 
            Qatar	(In-force) / 
            Romania	(In-force) / 
            Russia	(In-force) / 
            San Marino	(In-force) / 
            Serbia	(In-force) / 
            Seychelles	(In-force) / 
            Singapore	(In-force) / 
            Slovakia	(In-force) / 
            Slovenia	(In-force) / 
            South Africa	(In-force) / 
            Spain	(In-force) / 
            Sweden	(In-force) / 
            Switzerland	(In-force) / 
            Syria	(In-force) / 
            Thailand	(In-force) / 
            Ukraine	(In-force) / 
            United Arab Emirates	(In-force) / 
            United Kingdom	(In-force) / 
            United States	(In-force)
            ''', color: table_success},
            {comparison: egypt, value: '''
            Albania	(In-force) / 
            Algeria	(In-force) / 
            Austria	(In-force) / 
            Bahrain	(In-force) / 
            Belarus	(In-force) / 
            Belgium	(In-force) / 
            Bulgaria	(In-force) / 
            Canada	(In-force) / 
            China	(In-force) / 
            Cyprus	(In-force) / 
            Czech Republic	(In-force) / 
            Denmark	(In-force) / 
            FYROM	(In-force) / 
            Finland	(In-force) / 
            France	(In-force) / 
            Georgia	(In-force) / 
            Germany	(In-force) / 
            Greece	(In-force) / 
            Hungary	(In-force) / 
            India	(In-force) / 
            Indonesia	(In-force) / 
            Iraq	(In-force) / 
            Ireland	(Pending) /
            Italy	(In-force) / 
            Japan	(In-force) / 
            Jordan	(In-force) / 
            Kuwait	(In-force) / 
            Lebanon	(In-force) / 
            Libya	(In-force) / 
            Malaysia	(In-force) / 
            Malta	(In-force) / 
            Mauritius	(Pending) /
            Morocco	(In-force) / 
            Netherlands	(In-force) / 
            Norway	(In-force) / 
            Oman	(In-force) / 
            Pakistan	(In-force) / 
            Palestine	(In-force) / 
            Poland	(In-force) / 
            Romania	(In-force) / 
            Russia	(In-force) / 
            Serbia	(In-force) / 
            Singapore	(In-force) / 
            South Africa	(In-force) / 
            South Korea	(In-force) / 
            Spain	(In-force) / 
            Sudan	(In-force) / 
            Sweden	(In-force) / 
            Switzerland	(In-force) / 
            Syria	(In-force) / 
            Tunisia	(In-force) / 
            Turkey	(In-force) / 
            Ukraine	(In-force) / 
            United Arab Emirates	(In-force) / 
            United Kingdom	(In-force) / 
            United States	(In-force) / 
            Yemen	(In-force)
            ''', color: table_success},
            {comparison: gibraltar, value: '''
            -
            ''', color: table_success},
            {comparison: guernsey, value: '''
            Cyprus	(In-force) /
            Hong Kong	(In-force) /
            Isle of Man	(In-force) /
            Jersey	(In-force) /
            Luxembourg	(In-force) /
            Malta	(In-force) /
            Mauritius	(In-force) /
            Monaco	(In-force) /
            Qatar	(In-force) /
            Seychelles	(In-force) /
            Singapore	(In-force)
            ''', color: table_success},
            {comparison: hong_kong, value: '''
            Austria	(In-force) /
            Belgium	(In-force) /
            Brunei	(In-force) /
            Canada	(In-force) /
            China	(In-force) /
            Czech Republic	(In-force) /
            France	(In-force) /
            Guernsey	(In-force) /
            Hungary	(In-force) /
            Indonesia	(In-force) /
            Ireland	(In-force) /
            Italy	(Pending) /
            Japan	(In-force) /
            Jersey	(In-force) /
            Kuwait	(In-force) /
            Liechtenstein	(In-force) /
            Luxembourg	(In-force) /
            Malaysia	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Romania	(Pending) /
            Russia	(In-force) /
            South Africa	(In-force) /
            South Korea	(Pending) /
            Spain	(In-force) /
            Switzerland	(In-force) /
            Thailand	(In-force) /
            United Arab Emirates	(Pending) /
            United Kingdom	(In-force) /
            Vietnam	(In-force)
            ''', color: table_success},
            {comparison: ireland, value: '''
            Albania	(In-force) /
            Armenia	(In-force) /
            Australia	(In-force) /
            Austria	(In-force) /
            Bahrain	(In-force) /
            Belarus	(In-force) /
            Belgium	(In-force) /
            Bosnia and Herzegovina	(In-force) /
            Botswana	(In-force) /
            Bulgaria	(In-force) /
            Canada	(In-force) /
            Chile	(In-force) /
            China	(In-force) /
            Croatia	(In-force) /
            Cyprus	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Egypt	(Pending) /
            Estonia	(In-force) /
            Ethiopia	(Pending) /
            FYROM	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Georgia	(In-force) /
            Germany	(In-force) /
            Greece	(In-force) /
            Hong Kong	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Israel	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Kuwait	(In-force) /
            Latvia	(In-force) /
            Lithuania	(In-force) /
            Luxembourg	(In-force) /
            Malaysia	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Moldova	(In-force) /
            Montenegro	(In-force) /
            Morocco	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Pakistan	(In-force) /
            Panama	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Romania	(In-force) /
            Russia	(In-force) /
            Saudi Arabia	(In-force) /
            Serbia	(In-force) /
            Singapore	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Thailand	(In-force) /
            Turkey	(In-force) /
            Ukraine	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force) /
            Uzbekistan	(In-force) /
            Vietnam	(In-force) /
            Zambia	(In-force)
            ''', color: table_success},
            {comparison: isle_of_man, value: '''
            Bahrain	(In-force) /
            Belgium	(Pending) /
            Estonia	(In-force) /
            Guernsey	(In-force) /
            Jersey	(In-force) /
            Luxembourg	(In-force) /
            Malta	(In-force) /
            Qatar	(In-force) /
            Seychelles	(In-force) /
            Singapore	(In-force)
            ''', color: table_success},
            {comparison: jersey, value: '''
            Cyprus	(Pending) /
            Estonia	(In-force) /
            Guernsey	(In-force) /
            Hong Kong	(In-force) /
            Isle of Man	(In-force) /
            Luxembourg	(In-force) /
            Malta	(In-force) /
            Qatar	(In-force) /
            Rwanda	(In-force) /
            Seychelles	(Pending) /
            Singapore	(In-force)
            ''', color: table_success},
            {comparison: liechtenstein, value: '''
            Andorra	(Pending) /
            Austria	(In-force) /
            Czech Republic	(In-force) /
            Germany	(In-force) /
            Hong Kong	(In-force) /
            Hungary	(In-force) /
            Luxembourg	(In-force) /
            Malta	(In-force) /
            San Marino	(In-force) /
            Singapore	(In-force) /
            Switzerland	(In-force) /
            United Arab Emirates	(Pending) /
            United Kingdom	(In-force) /
            Uruguay	(In-force)
            ''', color: table_success},
            {comparison: luxembourg, value: '''
            Albania	(Pending) /
            Andorra	(Pending) /
            Armenia	(In-force) /
            Austria	(In-force) /
            Azerbaijan	(In-force) /
            Bahrain	(In-force) /
            Barbados	(In-force) /
            Belgium	(In-force) /
            Brazil	(In-force) /
            Brunei	(Pending) /
            Bulgaria	(In-force) /
            Canada	(In-force) /
            China	(In-force) /
            Croatia	(Pending) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Estonia	(In-force) /
            FYROM	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Georgia	(In-force) /
            Germany	(In-force) /
            Greece	(In-force) /
            Guernsey	(In-force) /
            Hong Kong	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Indonesia	(In-force) /
            Ireland	(In-force) /
            Isle of Man	(In-force) /
            Israel	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Jersey	(In-force) /
            Kazakhstan	(In-force) /
            Kuwait	(Pending) /
            Laos	(In-force) /
            Latvia	(In-force) /
            Liechtenstein	(In-force) /
            Lithuania	(In-force) /
            Malaysia	(In-force) /
            Malta	(In-force) /
            Mauritius	(In-force) /
            Mexico	(In-force) /
            Moldova	(In-force) /
            Monaco	(In-force) /
            Morocco	(In-force) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Panama	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Romania	(In-force) /
            Russia	(In-force) /
            San Marino	(In-force) /
            Saudi Arabia	(In-force) /
            Senegal	(Pending) /
            Serbia	(Pending) /
            Seychelles	(In-force) /
            Singapore	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Taiwan	(In-force) /
            Tajikistan	(In-force) /
            Thailand	(In-force) /
            Trinidad and Tobago	(In-force) /
            Tunisia	(In-force) /
            Turkey	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force) /
            Uruguay	(Pending) /
            Uzbekistan	(In-force) /
            Vietnam	(In-force)
            ''', color: table_success},
            {comparison: lithuania, value: '''
            Austria	(In-force) /
            Azerbaijan	(In-force) /
            Belarus	(In-force) /
            Belgium	(In-force) /
            Bulgaria	(In-force) /
            Canada	(In-force) /
            China	(In-force) /
            Croatia	(In-force) /
            Cyprus	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Estonia	(In-force) /
            FYROM	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Georgia	(In-force) /
            Germany	(In-force) /
            Greece	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Ireland	(In-force) /
            Israel	(In-force) /
            Italy	(In-force) /
            Kazakhstan	(In-force) /
            Kuwait	(Pending) /
            Kyrgyzstan	(In-force) /
            Latvia	(In-force) /
            Luxembourg	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Moldova	(In-force) /
            Morocco	(Pending) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Romania	(In-force) /
            Russia	(In-force) /
            Serbia	(In-force) /
            Singapore	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Turkey	(In-force) /
            Turkmenistan	(In-force) /
            Ukraine	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force) /
            Uzbekistan	(In-force)
            ''', color: table_success},
            {comparison: malta, value: '''
            Albania	(In-force) /
            Andorra	(Pending) /
            Australia	(In-force) /
            Austria	(In-force) /
            Azerbaijan	(Pending) /
            Bahrain	(In-force) /
            Barbados	(In-force) /
            Belgium	(In-force) /
            Bulgaria	(In-force) /
            Canada	(In-force) /
            China	(In-force) /
            Croatia	(In-force) /
            Curacao	(Pending) /
            Cyprus	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Egypt	(In-force) /
            Estonia	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Georgia	(In-force) /
            Germany	(In-force) /
            Greece	(In-force) /
            Guernsey	(In-force) /
            Hong Kong	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Ireland	(In-force) /
            Isle of Man	(In-force) /
            Israel	(In-force) /
            Italy	(In-force) /
            Jersey	(In-force) /
            Jordan	(In-force) /
            Kuwait	(In-force) /
            Latvia	(In-force) /
            Lebanon	(In-force) /
            Libya	(In-force) /
            Liechtenstein	(In-force) /
            Lithuania	(In-force) /
            Luxembourg	(In-force) /
            Malaysia	(In-force) /
            Mauritius	(In-force) /
            Mexico	(In-force) /
            Moldova	(In-force) /
            Montenegro	(In-force) /
            Morocco	(In-force) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Pakistan	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Romania	(In-force) /
            Russia	(In-force) /
            San Marino	(In-force) /
            Saudi Arabia	(In-force) /
            Serbia	(In-force) /
            Singapore	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Syria	(In-force) /
            Tunisia	(In-force) /
            Turkey	(In-force) /
            Ukraine	(Pending) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force) /
            Uruguay	(In-force)
            ''', color: table_success},
            {comparison: mauritius, value: '''
            Bangladesh	(In-force) /
            Barbados	(In-force) /
            Belgium	(In-force) /
            Botswana	(In-force) /
            China	(In-force) /
            Congo	(Pending) /
            Croatia	(In-force) /
            Cyprus	(In-force) /
            Egypt	(Pending) /
            France	(In-force) /
            Germany	(In-force) /
            Guernsey	(In-force) /
            India	(In-force) /
            Italy	(In-force) /
            Kenya	(Pending) /
            Kuwait	(In-force) /
            Lesotho	(In-force) /
            Luxembourg	(In-force) /
            Madagascar	(In-force) /
            Malaysia	(In-force) /
            Malta	(In-force) /
            Monaco	(Pending) /
            Mozambique	(In-force) /
            Namibia	(In-force) /
            Nepal	(In-force) /
            Nigeria	(Pending) /
            Oman	(In-force) /
            Pakistan	(In-force) /
            Qatar	(In-force) /
            Russia	(Pending) /
            Rwanda	(In-force) /
            Senegal	(In-force) /
            Seychelles	(In-force) /
            Singapore	(In-force) /
            South Africa	(In-force) /
            Sri Lanka	(In-force) /
            Swaziland	(In-force) /
            Sweden	(In-force) /
            Thailand	(In-force) /
            Tunisia	(In-force) /
            Uganda	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            Zambia	(In-force) /
            Zimbabwe	(In-force)
            ''', color: table_success},
            {comparison: netherlands, value: '''
            Albania	(In-force) /
            Argentina	(In-force) /
            Armenia	(In-force) /
            Aruba	(In-force) /
            Australia	(In-force) /
            Austria	(In-force) /
            Azerbaijan	(In-force) /
            Bahrain	(In-force) /
            Bangladesh	(In-force) /
            Barbados	(In-force) /
            Belarus	(In-force) /
            Belgium	(In-force) /
            Bosnia and Herzegovina	(In-force) /
            Brazil	(In-force) /
            Bulgaria	(In-force) /
            Canada	(In-force) /
            China	(In-force) /
            Croatia	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Egypt	(In-force) /
            Estonia	(In-force) /
            Ethiopia	(Pending) /
            FYROM	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Georgia	(In-force) /
            Germany	(In-force) /
            Ghana	(In-force) /
            Greece	(In-force) /
            Hong Kong	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Indonesia	(In-force) /
            Ireland	(In-force) /
            Israel	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Jordan	(In-force) /
            Kazakhstan	(In-force) /
            Kuwait	(In-force) /
            Latvia	(In-force) /
            Lithuania	(In-force) /
            Luxembourg	(In-force) /
            Malawi	(Pending) /
            Malaysia	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Moldova	(In-force) /
            Morocco	(In-force) /
            New Zealand	(In-force) /
            Nigeria	(In-force) /
            Norway	(In-force) /
            Oman	(In-force) /
            Pakistan	(In-force) /
            Panama	(In-force) /
            Philippines	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Romania	(In-force) /
            Russia	(In-force) /
            Saudi Arabia	(In-force) /
            Serbia	(In-force) /
            Singapore	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sri Lanka	(In-force) /
            Suriname	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Taiwan	(In-force) /
            Thailand	(In-force) /
            Tunisia	(In-force) /
            Turkey	(In-force) /
            Uganda	(In-force) /
            Ukraine	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force) /
            Uzbekistan	(In-force) /
            Venezuela	(In-force) /
            Vietnam	(In-force) /
            Zambia	(In-force) /
            Zimbabwe	(In-force)
            ''', color: table_success},
            {comparison: panama, value: '''
            Barbados	(In-force) /
            Czech Republic	(Pending) /
            France	(In-force) /
            Ireland	(In-force) /
            Israel	(In-force) /
            Italy	(Pending) /
            Luxembourg	(In-force) /
            Mexico	(In-force) /
            Netherlands	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Singapore	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force)
            ''', color: table_success},
            {comparison: seychelles, value: '''
            Bahrain	(In-force) /
            Barbados	(In-force) /
            Belgium	(Pending) /
            Botswana	(In-force) /
            China	(In-force) /
            Cyprus	(In-force) /
            Guernsey	(In-force) /
            Indonesia	(In-force) /
            Isle of Man	(In-force) /
            Jersey	(Pending) /
            Kenya	(Pending) /
            Luxembourg	(In-force) /
            Malaysia	(In-force) /
            Mauritius	(In-force) /
            Monaco	(In-force) /
            Oman	(In-force) /
            Qatar	(In-force) /
            San Marino	(Pending) /
            Singapore	(In-force) /
            South Africa	(In-force) /
            Thailand	(In-force) /
            United Arab Emirates	(In-force) /
            Vietnam	(In-force) /
            Zambia	(In-force) /
            Zimbabwe	(In-force)
            ''', color: table_success},
            {comparison: singapore, value: '''
            Albania	(In-force) /
            Australia	(In-force) /
            Austria	(In-force) /
            Bahrain	(In-force) /
            Bangladesh	(In-force) /
            Barbados	(In-force) /
            Belarus	(In-force) /
            Belgium	(In-force) /
            Brunei	(In-force) /
            Bulgaria	(In-force) /
            Cambodia	(Pending) /
            Canada	(In-force) /
            China	(In-force) /
            Cyprus	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Ecuador	(In-force) /
            Egypt	(In-force) /
            Estonia	(In-force) /
            Fiji	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Georgia	(In-force) /
            Germany	(In-force) /
            Guernsey	(In-force) /
            Hungary	(In-force) /
            India	(In-force) /
            Indonesia	(In-force) /
            Ireland	(In-force) /
            Isle of Man	(In-force) /
            Israel	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Jersey	(In-force) /
            Kazakhstan	(In-force) /
            Kuwait	(In-force) /
            Laos	(Pending) /
            Latvia	(In-force) /
            Libya	(In-force) /
            Liechtenstein	(In-force) /
            Lithuania	(In-force) /
            Luxembourg	(In-force) /
            Malaysia	(In-force) /
            Malta	(In-force) /
            Mauritius	(In-force) /
            Mexico	(In-force) /
            Mongolia	(In-force) /
            Morocco	(In-force) /
            Myanmar	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Oman	(In-force) /
            Pakistan	(In-force) /
            Panama	(In-force) /
            Papua New Guinea	(In-force) /
            Philippines	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Qatar	(In-force) /
            Romania	(In-force) /
            Russia	(In-force) /
            Rwanda	(In-force) /
            San Marino	(In-force) /
            Saudi Arabia	(In-force) /
            Seychelles	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sri Lanka	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Taiwan	(In-force) /
            Thailand	(In-force) /
            Turkey	(In-force) /
            Ukraine	(In-force) /
            United Arab Emirates	(In-force) /
            United Kingdom	(In-force) /
            Uzbekistan	(In-force) /
            Vietnam	(In-force)
            ''', color: table_success},
            {comparison: dubai, value: '''
            Albania	(Pending) /
            Algeria	(In-force) / 
            Andorra	(Pending) /
            Armenia	(In-force) / 
            Austria	(In-force) / 
            Azerbaijan	(In-force) / 
            Barbados	(Pending) /
            Belarus	(In-force) / 
            Belgium	(In-force) / 
            Belize	(Pending) /
            Bosnia and Herzegovina	(In-force) / 
            Bulgaria	(In-force) / 
            Canada	(In-force) / 
            China	(In-force) / 
            Cyprus	(In-force) / 
            Czech Republic	(In-force) / 
            Egypt	(In-force) / 
            Estonia	(In-force) / 
            Ethiopia	(Pending) /
            FYROM	(Pending) /
            Fiji	(Pending) /
            Finland	(In-force) / 
            France	(In-force) / 
            Georgia	(In-force) / 
            Germany	(In-force) / 
            Greece	(Pending) /
            Hong Kong	(Pending) /
            Hungary	(In-force) / 
            India	(In-force) / 
            Indonesia	(In-force) / 
            Ireland	(In-force) / 
            Italy	(In-force) / 
            Japan	(Pending) /
            Jordan	(Pending) /
            Kazakhstan	(In-force) / 
            Kosovo	(Pending) /
            Latvia	(In-force) / 
            Lebanon	(In-force) / 
            Libya	(Pending) /
            Liechtenstein	(Pending) /
            Lithuania	(In-force) / 
            Luxembourg	(In-force) / 
            Malaysia	(In-force) / 
            Malta	(In-force) / 
            Mauritania	(Pending) /
            Mauritius	(In-force) / 
            Mexico	(Pending) /
            Morocco	(In-force) / 
            Mozambique	(In-force) / 
            Netherlands	(In-force) / 
            New Zealand	(In-force) / 
            Pakistan	(In-force) / 
            Panama	(In-force) / 
            Philippines	(In-force) / 
            Poland	(In-force) / 
            Portugal	(In-force) / 
            Romania	(In-force) / 
            Senegal	(Pending) /
            Serbia	(Pending) /
            Seychelles	(In-force) / 
            Singapore	(In-force) / 
            Slovakia	(Pending) /
            Slovenia	(In-force) / 
            South Korea	(In-force) / 
            Spain	(In-force) / 
            Sri Lanka	(In-force) / 
            Sudan	(In-force) / 
            Switzerland	(In-force) / 
            Syria	(In-force) / 
            Tajikistan	(In-force) / 
            Thailand	(In-force) / 
            Tunisia	(In-force) / 
            Turkey	(In-force) / 
            Turkmenistan	(In-force) / 
            Uganda	(Pending) /
            Ukraine	(In-force) / 
            Uzbekistan	(In-force) / 
            Venezuela	(In-force) / 
            Vietnam	(In-force) / 
            Yemen	(In-force)
            ''', color: table_success},
            {comparison: ras_al_khaimah, value: '''
            Albania	(Pending) /
            Algeria	(In-force) / 
            Andorra	(Pending) /
            Armenia	(In-force) / 
            Austria	(In-force) / 
            Azerbaijan	(In-force) / 
            Barbados	(Pending) /
            Belarus	(In-force) / 
            Belgium	(In-force) / 
            Belize	(Pending) /
            Bosnia and Herzegovina	(In-force) / 
            Bulgaria	(In-force) / 
            Canada	(In-force) / 
            China	(In-force) / 
            Cyprus	(In-force) / 
            Czech Republic	(In-force) / 
            Egypt	(In-force) / 
            Estonia	(In-force) / 
            Ethiopia	(Pending) /
            FYROM	(Pending) /
            Fiji	(Pending) /
            Finland	(In-force) / 
            France	(In-force) / 
            Georgia	(In-force) / 
            Germany	(In-force) / 
            Greece	(Pending) /
            Hong Kong	(Pending) /
            Hungary	(In-force) / 
            India	(In-force) / 
            Indonesia	(In-force) / 
            Ireland	(In-force) / 
            Italy	(In-force) / 
            Japan	(Pending) /
            Jordan	(Pending) /
            Kazakhstan	(In-force) / 
            Kosovo	(Pending) /
            Latvia	(In-force) / 
            Lebanon	(In-force) / 
            Libya	(Pending) /
            Liechtenstein	(Pending) /
            Lithuania	(In-force) / 
            Luxembourg	(In-force) / 
            Malaysia	(In-force) / 
            Malta	(In-force) / 
            Mauritania	(Pending) /
            Mauritius	(In-force) / 
            Mexico	(Pending) /
            Morocco	(In-force) / 
            Mozambique	(In-force) / 
            Netherlands	(In-force) / 
            New Zealand	(In-force) / 
            Pakistan	(In-force) / 
            Panama	(In-force) / 
            Philippines	(In-force) / 
            Poland	(In-force) / 
            Portugal	(In-force) / 
            Romania	(In-force) / 
            Senegal	(Pending) /
            Serbia	(Pending) /
            Seychelles	(In-force) / 
            Singapore	(In-force) / 
            Slovakia	(Pending) /
            Slovenia	(In-force) / 
            South Korea	(In-force) / 
            Spain	(In-force) / 
            Sri Lanka	(In-force) / 
            Sudan	(In-force) / 
            Switzerland	(In-force) / 
            Syria	(In-force) / 
            Tajikistan	(In-force) / 
            Thailand	(In-force) / 
            Tunisia	(In-force) / 
            Turkey	(In-force) / 
            Turkmenistan	(In-force) / 
            Uganda	(Pending) /
            Ukraine	(In-force) / 
            Uzbekistan	(In-force) / 
            Venezuela	(In-force) / 
            Vietnam	(In-force) / 
            Yemen	(In-force)
            ''', color: table_success},
            {comparison: switzerland, value: '''
            Albania	(In-force) /
            Algeria	(In-force) / 
            Argentina	(Pending) /
            Armenia	(In-force) / 
            Australia	(In-force) / 
            Austria	(In-force) / 
            Azerbaijan	(In-force) / 
            Bangladesh	(In-force) / 
            Barbados	(In-force) / 
            Belarus	(In-force) / 
            Belgium	(In-force) / 
            Bulgaria	(In-force) / 
            Canada	(In-force) / 
            Chile	(In-force) / 
            China	(In-force) / 
            Colombia	(In-force) / 
            Costa Rica	(Pending) /
            Croatia	(In-force) / 
            Cyprus	(In-force) / 
            Czech Republic	(In-force) / 
            Denmark	(In-force) / 
            Ecuador	(In-force) / 
            Egypt	(In-force) / 
            Estonia	(In-force) / 
            FYROM	(In-force) / 
            Finland	(In-force) / 
            France	(In-force) / 
            Georgia	(In-force) / 
            Germany	(In-force) / 
            Ghana	(In-force) / 
            Greece	(In-force) / 
            Hong Kong	(In-force) / 
            Hungary	(In-force) / 
            Iceland	(In-force) / 
            India	(In-force) / 
            Indonesia	(In-force) / 
            Iran	(In-force) / 
            Ireland	(In-force) / 
            Israel	(In-force) / 
            Italy	(In-force) / 
            Ivory Coast	(In-force) / 
            Jamaica	(In-force) / 
            Japan	(In-force) / 
            Kazakhstan	(In-force) / 
            Kuwait	(In-force) / 
            Kyrgyzstan	(In-force) / 
            Latvia	(In-force) / 
            Liechtenstein	(In-force) / 
            Lithuania	(In-force) / 
            Luxembourg	(In-force) / 
            Malaysia	(In-force) / 
            Malta	(In-force) / 
            Mexico	(In-force) / 
            Moldova	(In-force) / 
            Mongolia	(In-force) / 
            Montenegro	(In-force) / 
            Morocco	(In-force) / 
            Netherlands	(In-force) / 
            New Zealand	(In-force) / 
            Norway	(In-force) / 
            Oman	(Pending) /
            Pakistan	(In-force) / 
            Peru	(In-force) / 
            Philippines	(In-force) / 
            Poland	(In-force) / 
            Portugal	(In-force) / 
            Qatar	(In-force) / 
            Romania	(In-force) / 
            Russia	(In-force) / 
            Serbia	(In-force) / 
            Singapore	(In-force) / 
            Slovakia	(In-force) / 
            Slovenia	(In-force) / 
            South Africa	(In-force) / 
            South Korea	(In-force) / 
            Spain	(In-force) / 
            Sri Lanka	(In-force) / 
            Sweden	(In-force) / 
            Taiwan	(In-force) / 
            Tajikistan	(In-force) / 
            Thailand	(In-force) / 
            Trinidad and Tobago	(In-force) / 
            Tunisia	(In-force) / 
            Turkey	(In-force) / 
            Turkmenistan	(In-force) / 
            Ukraine	(In-force) / 
            United Arab Emirates	(In-force) / 
            United Kingdom	(In-force) / 
            United States	(In-force) / 
            Uruguay	(In-force) / 
            Uzbekistan	(In-force) / 
            Venezuela	(In-force) / 
            Vietnam	(In-force) / 
            Zimbabwe	(Pending)
            ''', color: table_success}
        ],
        topic: "Tax treaties",
        comparison: country
    }
    return jsonify(context)


# Get information about tax_information_exchange_agreements
@app.route("/tax_information_exchange_agreements")
def tax_information_exchange_agreements():
    context = {
        "data": [
            {comparison: bahamas, value: '''
            Argentina	(In-force) /
            Australia	(In-force) /
            Belgium	(In-force) /
            Canada	(In-force) /
            China	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greenland	(In-force) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Indonesia	(Pending) /
            Ireland	(Pending) /
            Japan	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Monaco	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(Pending) /
            Norway	(In-force) /
            Poland	(In-force) /
            San Marino	(In-force) /
            South Africa	(In-force) /
            South Korea	(In-force) /
            Spain	(In-force) /
            Sweden	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: barbados, value: '''
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Greenland	(In-force)
            ''', color: table_success},
            {comparison: andorra, value: '''
            Argentina	(In-force) /
            Australia	(In-force) /
            Austria	(In-force) /
            Belgium	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greenland	(In-force) /
            Iceland	(In-force) /
            Italy	(Pending) /
            Liechtenstein	(In-force) /
            Luxembourg	(In-force) /
            Monaco	(In-force) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            San Marino	(In-force) /
            South Korea	(Pending) /
            Spain	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force)
            ''', color: table_success},
            {comparison: belize, value: '''
            Australia	(Pending) /
            Belgium	(In-force) /
            Czech Republic	(Pending) /
            Denmark	(In-force) /
            Faroe Islands	(Pending) /
            Finland	(In-force) /
            France	(In-force) /
            Greenland	(Pending) /
            Iceland	(Pending) /
            India	(In-force) /
            Ireland	(In-force) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Poland	(Pending) /
            Portugal	(Pending) /
            South Africa	(In-force) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            United Kingdom	(In-force)
            ''', color: table_success},
            {comparison: bermuda, value: '''
            Belgium	(Pending) /
            Canada	(In-force) /
            Czech Republic	(Pending) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(Pending) /
            Greenland	(Pending) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Ireland	(In-force) /
            Italy	(Pending) /
            Malta	(In-force) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Singapore	(In-force) /
            South Korea	(In-force) /
            Sweden	(In-force) /
            Turkey	(In-force) /
            United Kingdom	(In-force)
            ''', color: table_success},
            {comparison: british_virgin_islands, value: '''
            Aruba	(In-force) /
            Canada	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(Pending) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greenland	(Pending) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Ireland	(In-force) /
            Isle of Man	(In-force) /
            Netherlands	(In-force) /
            Netherlands Antilles	(Pending) /
            Norway	(In-force) /
            Poland	(Pending) /
            Portugal	(Pending) /
            South Korea	(In-force) /
            Sweden	(In-force) /
            United Kingdom	(In-force)
            ''', color: table_success},
            {comparison: cayman_islands, value: '''
            Argentina	(In-force) /
            Aruba	(In-force) /
            Australia	(In-force) /
            Belgium	(Pending) /
            Brazil	(Pending) /
            Canada	(In-force) /
            China	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greece	(Pending) /
            Greenland	(In-force) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Ireland	(In-force) /
            Isle of Man	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Qatar	(Pending) /
            Seychelles	(Pending) /
            South Africa	(In-force) /
            Sweden	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: cyprus, value: "-", color: table_success},
            {comparison: egypt, value: "-", color: table_success},
            {comparison: gibraltar, value: '''
            Australia	(In-force) /
            Austria	(In-force) /
            Belgium	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greece	(Pending) /
            Greenland	(In-force) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Ireland	(In-force) /
            Italy	(In-force) /
            Malta	(In-force) /
            Mexico	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            South Africa	(In-force) /
            Sweden	(In-force) /
            Turkey	(Pending) /
            United Kingdom	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: guernsey, value: '''
            Argentina	(In-force) /
            Australia	(In-force) /
            Austria	(In-force) /
            Bahamas	(In-force) /
            Belgium	(Pending) /
            Bermuda	(In-force) /
            Botswana	(Pending) /
            Brazil	(Pending) /
            British Virgin Islands	(In-force) /
            Bulgaria	(Pending) /
            Canada	(In-force) /
            Cayman Islands	(In-force) /
            Chile	(In-force) /
            China	(In-force) /
            Costa Rica	(Pending) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Gibraltar	(In-force) /
            Greece	(In-force) /
            Greenland	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Indonesia	(Pending) /
            Ireland	(In-force) /
            Italy	(Pending) /
            Japan	(In-force) /
            Latvia	(In-force) /
            Lesotho	(In-force) /
            Liechtenstein	(In-force) /
            Lithuania	(Pending) /
            Macau	(In-force) /
            Mauritius	(In-force) /
            Mexico	(In-force) /
            Montserrat	(Pending) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(Pending) /
            Romania	(In-force) /
            Saint Kitts and Nevis	(In-force) /
            San Marino	(In-force) /
            Seychelles	(In-force) /
            Slovakia	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            Spain	(Pending) /
            Swaziland	(In-force) /
            Sweden	(In-force) /
            Switzerland	(Pending) /
            Turkey	(Pending) /
            Turks and Caicos Islands	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force) /
            Uruguay	(Pending)
            ''', color: table_success},
            {comparison: hong_kong, value: '''
            Denmark	(Pending) /
            Faroe Islands	(In-force) /
            Greenland	(In-force) /
            Iceland	(In-force) /
            Norway	(In-force) /
            Sweden	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: ireland, value: '''
            Anguilla	(In-force) /
            Antigua and Barbuda	(In-force) /
            Argentina	(Pending) /
            Bahamas	(Pending) /
            Belize	(In-force) /
            Bermuda	(In-force) /
            British Virgin Islands	(In-force) /
            Cayman Islands	(In-force) /
            Cook Islands	(In-force) /
            Dominica	(In-force) /
            Gibraltar	(In-force) /
            Grenada	(In-force) /
            Guernsey	(In-force) /
            Isle of Man	(In-force) /
            Jersey	(In-force) /
            Liechtenstein	(In-force) /
            Marshall Islands	(In-force) /
            Montserrat	(Pending) /
            Saint Kitts and Nevis	(Pending) /
            Saint Lucia	(In-force) /
            Saint Vincent and the Grenadines	(In-force) /
            Samoa	(In-force) /
            San Marino	(In-force) /
            Turks and Caicos Islands	(Pending) /
            Vanuatu	(In-force)
            ''', color: table_success},
            {comparison: isle_of_man, value: '''
            Argentina	(In-force) /
            Australia	(In-force) /
            Botswana	(Pending) /
            British Virgin Islands	(In-force) /
            Canada	(In-force) /
            Cayman Islands	(In-force) /
            China	(In-force) /
            Czech Republic	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greenland	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Indonesia	(In-force) /
            Ireland	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Lesotho	(In-force) /
            Mexico	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Slovenia	(In-force) /
            Swaziland	(Pending) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Turkey	(Pending) /
            United Kingdom	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: jersey, value: '''
            Argentina	(In-force) /
            Australia	(In-force) /
            Austria	(In-force) /
            Belgium	(Pending) /
            Brazil	(Pending) /
            Canada	(In-force) /
            China	(In-force) /
            Czech Republic	(In-force) /
            e	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greenland	(In-force) /
            Hungary	(In-force) /
            Iceland	(In-force) /
            India	(In-force) /
            Indonesia	(In-force) /
            Ireland	(In-force) /
            Italy	(In-force) /
            Japan	(In-force) /
            Latvia	(In-force) /
            Mexico	(In-force) /
            Netherlands	(In-force) /
            New Zealand	(In-force) /
            Norway	(In-force) /
            Poland	(In-force) /
            Portugal	(In-force) /
            Romania	(In-force) /
            Slovenia	(In-force) /
            South Africa	(In-force) /
            South Korea	(Pending) /
            Spain	(Pending) /
            Sweden	(In-force) /
            Switzerland	(In-force) /
            Turkey	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: liechtenstein, value: '''
            Andorra	(In-force) /
            Antigua and Barbuda	(In-force) /
            Australia	(In-force) /
            Belgium	(Pending) /
            Canada	(In-force) /
            China	(In-force) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            France	(In-force) /
            Germany	(In-force) /
            Greenland	(In-force) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(Pending) /
            Ireland	(In-force) /
            Italy	(Pending) /
            Japan	(In-force) /
            Mexico	(Pending) /
            Monaco	(In-force) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Saint Kitts and Nevis	(In-force) /
            Saint Vincent and the Grenadines	(In-force) /
            South Africa	(In-force) /
            Sweden	(In-force) /
            United Kingdom	(In-force) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: luxembourg, value: '''
            Andorra	(In-force)
            ''', color: table_success},
            {comparison: lithuania, value: '''
            Georgia	(Pending) /
            Guernsey	(Pending) /
            Kazakhstan	(Pending)
            ''', color: table_success},
            {comparison: malta, value: '''
            Bahamas	(In-force) /
            Bermuda	(In-force) /
            Cayman Islands	(In-force) /
            Gibraltar	(In-force) /
            Macau	(Pending)
            ''', color: table_success},
            {comparison: mauritius, value: '''
            Australia	(In-force) /
            Austria	(Pending) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            Greenland	(Pending) /
            Guernsey	(In-force) /
            Iceland	(Pending) /
            Norway	(In-force) /
            United States	(Pending)
            ''', color: table_success},
            {comparison: netherlands, value: '''
            -
            ''', color: table_success},
            {comparison: panama, value: '''
            Canada	(In-force) /
            Denmark	(Pending) /
            Faroe Islands	(Pending) /
            Finland	(Pending) /
            Greenland	(Pending) /
            Iceland	(Pending) /
            Norway	(Pending) /
            Sweden	(Pending) /
            United States	(In-force)
            ''', color: table_success},
            {comparison: seychelles, value: '''
            Cayman Islands	(Pending) /
            Denmark	(In-force) /
            Faroe Islands	(In-force) /
            Finland	(In-force) /
            Georgia	(In-force) /
            Greenland	(In-force) /
            Guernsey	(In-force) /
            Iceland	(In-force) /
            India	(Pending) /
            Netherlands	(In-force) /
            Norway	(In-force) /
            Sweden	(In-force) /
            Switzerland	(Pending)
            ''', color: table_success},
            {comparison: singapore, value: '''
            Bermuda	(In-force)
            ''', color: table_success},
            {comparison: dubai, value: '''
            Denmark	(Pending) /
            Norway	(Pending) /
            Sweden	(Pending)
            ''', color: table_success},
            {comparison: ras_al_khaimah, value: '''
            Denmark	(Pending) /
            Norway	(Pending) /
            Sweden	(Pending)
            ''', color: table_success},
            {comparison: switzerland, value: '''
            Andorra	(In-force) /
            Belize	(In-force) /
            Greenland	(Pending) /
            Grenada	(Pending) /
            Guernsey	(Pending) /
            Isle of Man	(In-force) /
            Jersey	(In-force) /
            San Marino	(Pending) /
            Seychelles	(Pending)
            ''', color: table_success}
        ],
        topic: "Tax information exchange agreements",
        comparison: country
    }
    return jsonify(context)


# Get information about company_liability_of_shareholders
@app.route("/company_liability_of_shareholders")
def company_liability_of_shareholders():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Limited", color: table_active},
            {comparison: andorra_private_limited_company, value: "Limited", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Limited", color: table_active},
            {comparison: barbados_ibc, value: "Limited", color: table_active},
            {comparison: barbados_isrl, value: "Limited", color: table_active},
            {comparison: belize_ibc, value: "Limited", color: table_active},
            {comparison: bermuda_exempt_company, value: "Limited", color: table_active},
            {comparison: bvi_ibc, value: "Limited", color: table_active},
            {comparison: cayman_exempted_company, value: "Limited", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Limited", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Limited", color: table_active},
            {comparison: cyprus_private_company, value: "Limited", color: table_active},
            {comparison: cyprus_public_company, value: "Limited", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Limited", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Limited", color: table_active},
            {comparison: guernsey_limited_company, value: "Limited", color: table_active},
            {comparison: hong_kong_private_company, value: "Limited", color: table_active},
            {comparison: hong_kong_public_company, value: "Limited", color: table_active},
            {comparison: ireland_private_company, value: "Limited", color: table_active},
            {comparison: ireland_public_company, value: "Limited", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Limited", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Limited", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Limited", color: table_active},
            {comparison: jersey_private_company, value: "Limited", color: table_active},
            {comparison: jersey_public_company, value: "Limited", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Limited", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Limited", color: table_active},
            {comparison: luxembourg_private_company, value: "Limited", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Limited", color: table_active},
            {comparison: malta_private_company, value: "Limited", color: table_active},
            {comparison: malta_public_company, value: "Limited", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Limited", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Limited", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Limited", color: table_active},
            {comparison: panama_corporation, value: "Limited", color: table_active},
            {comparison: seychelles_ibc, value: "Limited", color: table_active},
            {comparison: seychelles_csl, value: "Limited", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Limited", color: table_active},
            {comparison: singapore_private_company, value: "Limited", color: table_active},
            {comparison: singapore_public_company, value: "Limited", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Limited", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Limited", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Limited", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Limited", color: table_active},
            {comparison: rak_offshore_ibc, value: "Limited", color: table_active},
        ],
        topic: "Liability of shareholders",
        comparison: company
    }
    return jsonify(context)


# Get information about company_minimum_number_of_shareholders
@app.route("/company_minimum_number_of_shareholders")
def company_minimum_number_of_shareholders():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "1.0", color: table_active},
            {comparison: andorra_private_limited_company, value: "1.0", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "1.0", color: table_active},
            {comparison: barbados_ibc, value: "1.0", color: table_active},
            {comparison: barbados_isrl, value: "1.0", color: table_active},
            {comparison: belize_ibc, value: "1.0", color: table_active},
            {comparison: bermuda_exempt_company, value: "1.0", color: table_active},
            {comparison: bvi_ibc, value: "1.0", color: table_active},
            {comparison: cayman_exempted_company, value: "1.0", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "2.0", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "1.0", color: table_active},
            {comparison: cyprus_private_company, value: "1.0", color: table_active},
            {comparison: cyprus_public_company, value: "7.0", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "1.0", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "3.0", color: table_active},
            {comparison: guernsey_limited_company, value: "1.0", color: table_active},
            {comparison: hong_kong_private_company, value: "1.0", color: table_active},
            {comparison: hong_kong_public_company, value: "50.0", color: table_active},
            {comparison: ireland_private_company, value: "1.0", color: table_active},
            {comparison: ireland_public_company, value: "7.0", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "1.0", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "1.0", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "2.0", color: table_active},
            {comparison: jersey_private_company, value: "1.0", color: table_active},
            {comparison: jersey_public_company, value: "2.0", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "1.0", color: table_active},
            {comparison: lithuania_private_limited_company, value: "1.0", color: table_active},
            {comparison: luxembourg_private_company, value: "1.0", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "1.0", color: table_active},
            {comparison: malta_private_company,
             value: "1 if the company director is a natural person or 2 if the director is corporate body",
             color: table_active},
            {comparison: malta_public_company, value: "2.0", color: table_active},
            {comparison: mauritius_gbc1_company, value: "1.0", color: table_active},
            {comparison: mauritius_gbc2_company, value: "1.0", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "1.0", color: table_active},
            {comparison: panama_corporation, value: "2.0", color: table_active},
            {comparison: seychelles_ibc, value: "1.0", color: table_active},
            {comparison: seychelles_csl, value: "2.0", color: table_active},
            {comparison: singapore_private_exempt_company, value: "1.0", color: table_active},
            {comparison: singapore_private_company, value: "1.0", color: table_active},
            {comparison: singapore_public_company, value: "1.0", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "1.0", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "1.0", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "1.0", color: table_active},
            {comparison: dubai_difc_llc_company, value: "1.0", color: table_active},
            {comparison: rak_offshore_ibc, value: "1.0", color: table_active},
        ],
        topic: "Minimum number of shareholders",
        comparison: company
    }
    return jsonify(context)


# Get information about company_maximum_number_of_shareholders
@app.route("/company_maximum_number_of_shareholders")
def company_maximum_number_of_shareholders():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Unlimited", color: table_active},
            {comparison: andorra_private_limited_company, value: "Unlimited", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Unlimited", color: table_active},
            {comparison: barbados_ibc, value: "Unlimited", color: table_active},
            {comparison: barbados_isrl, value: "Unlimited", color: table_active},
            {comparison: belize_ibc, value: "Unlimited", color: table_active},
            {comparison: bermuda_exempt_company, value: "Unlimited", color: table_active},
            {comparison: bvi_ibc, value: "Unlimited", color: table_active},
            {comparison: cayman_exempted_company, value: "Unlimited", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Unlimited", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Unlimited", color: table_active},
            {comparison: cyprus_private_company, value: "50.0", color: table_active},
            {comparison: cyprus_public_company, value: "Unlimited", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Unlimited", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Unlimited", color: table_active},
            {comparison: guernsey_limited_company, value: "Unlimited", color: table_active},
            {comparison: hong_kong_private_company, value: "50.0", color: table_active},
            {comparison: hong_kong_public_company, value: "Unlimited", color: table_active},
            {comparison: ireland_private_company, value: "99.0", color: table_active},
            {comparison: ireland_public_company, value: "Unlimited", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Unlimited", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Unlimited", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Unlimited", color: table_active},
            {comparison: jersey_private_company, value: "30.0", color: table_active},
            {comparison: jersey_public_company, value: "Unlimited", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Unlimited", color: table_active},
            {comparison: lithuania_private_limited_company, value: "249.0", color: table_active},
            {comparison: luxembourg_private_company, value: "40.0", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Unlimited", color: table_active},
            {comparison: malta_private_company, value: "50.0", color: table_active},
            {comparison: malta_public_company, value: "Unlimited", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Unlimited", color: table_active},
            {comparison: mauritius_gbc2_company, value: "25.0", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Unlimited", color: table_active},
            {comparison: panama_corporation, value: "Unlimited", color: table_active},
            {comparison: seychelles_ibc, value: "Unlimited", color: table_active},
            {comparison: seychelles_csl, value: "Unlimited", color: table_active},
            {comparison: singapore_private_exempt_company, value: "20.0", color: table_active},
            {comparison: singapore_private_company, value: "50.0", color: table_active},
            {comparison: singapore_public_company, value: "Unlimited", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Unlimited", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Unlimited", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Unlimited", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Unlimited", color: table_active},
            {comparison: rak_offshore_ibc, value: "Unlimited", color: table_active},
        ],
        topic: "Maximum number of shareholders",
        comparison: company
    }
    return jsonify(context)


# Get information about company_restriction_on_nationality_residency_of_shareholders
@app.route("/company_restriction_on_nationality_residency_of_shareholders")
def company_restriction_on_nationality_residency_of_shareholders():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "None", color: table_active},
            {comparison: andorra_private_limited_company, value: "None", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "None", color: table_active},
            {comparison: barbados_ibc,
             value: "Yes, local or Caricom resident shareholders restricted to less than 10%",
             color: table_active},
            {comparison: barbados_isrl,
             value: "Yes, local or Caricom resident shareholders restricted to less than 10%",
             color: table_active},
            {comparison: belize_ibc, value: "None", color: table_active},
            {comparison: bermuda_exempt_company, value: "None", color: table_active},
            {comparison: bvi_ibc, value: "None", color: table_active},
            {comparison: cayman_exempted_company, value: "None", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "None", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "None", color: table_active},
            {comparison: cyprus_private_company, value: "None", color: table_active},
            {comparison: cyprus_public_company, value: "None", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes, cannot be residents of Gibraltar",
             color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "None", color: table_active},
            {comparison: guernsey_limited_company, value: "None", color: table_active},
            {comparison: hong_kong_private_company, value: "None", color: table_active},
            {comparison: hong_kong_public_company, value: "None", color: table_active},
            {comparison: ireland_private_company, value: "None", color: table_active},
            {comparison: ireland_public_company, value: "None", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "None", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "None", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "None", color: table_active},
            {comparison: jersey_private_company, value: "None", color: table_active},
            {comparison: jersey_public_company, value: "None", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "None", color: table_active},
            {comparison: lithuania_private_limited_company, value: "None", color: table_active},
            {comparison: luxembourg_private_company, value: "None", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "None", color: table_active},
            {comparison: malta_private_company, value: "None", color: table_active},
            {comparison: malta_public_company, value: "None", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Should not be resident of Mauritius",
             color: table_active},
            {comparison: mauritius_gbc2_company, value: "Should not be resident of Mauritius",
             color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "None", color: table_active},
            {comparison: panama_corporation, value: "None", color: table_active},
            {comparison: seychelles_ibc, value: "None", color: table_active},
            {comparison: seychelles_csl, value: "None", color: table_active},
            {comparison: singapore_private_exempt_company, value: "None", color: table_active},
            {comparison: singapore_private_company, value: "None", color: table_active},
            {comparison: singapore_public_company, value: "None", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "None", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "None", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "None", color: table_active},
            {comparison: dubai_difc_llc_company, value: "None", color: table_active},
            {comparison: rak_offshore_ibc, value: "None", color: table_active},
        ],
        topic: "Restriction on nationality residency of shareholders",
        comparison: company
    }
    return jsonify(context)


# Get information about company_corporate_shareholders_allowed
@app.route("/company_corporate_shareholders_allowed")
def company_corporate_shareholders_allowed():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company,
             value: "Yes - provided that at least 1 director is natural person", color: table_active},
            {comparison: hong_kong_public_company, value: "No", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "No", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "No", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Corporate shareholders allowed",
        comparison: company
    }
    return jsonify(context)


# Get information about company_minimum_number_of_directors
@app.route("/company_minimum_number_of_directors")
def company_minimum_number_of_directors():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "1.0", color: table_active},
            {comparison: andorra_private_limited_company, value: "1.0", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "1.0", color: table_active},
            {comparison: barbados_ibc, value: "1.0", color: table_active},
            {comparison: barbados_isrl, value: "1.0", color: table_active},
            {comparison: belize_ibc, value: "1.0", color: table_active},
            {comparison: bermuda_exempt_company, value: "1.0", color: table_active},
            {comparison: bvi_ibc, value: "1.0", color: table_active},
            {comparison: cayman_exempted_company, value: "1.0", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "1.0", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "1.0", color: table_active},
            {comparison: cyprus_private_company, value: "1.0", color: table_active},
            {comparison: cyprus_public_company, value: "1.0", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "1.0", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "1.0", color: table_active},
            {comparison: guernsey_limited_company, value: "1.0", color: table_active},
            {comparison: hong_kong_private_company, value: "1.0", color: table_active},
            {comparison: hong_kong_public_company, value: "1.0", color: table_active},
            {comparison: ireland_private_company, value: "2.0", color: table_active},
            {comparison: ireland_public_company, value: "2.0", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "2.0", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "1.0", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "2.0", color: table_active},
            {comparison: jersey_private_company, value: "1.0", color: table_active},
            {comparison: jersey_public_company, value: "2.0", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "1.0", color: table_active},
            {comparison: lithuania_private_limited_company, value: "1.0", color: table_active},
            {comparison: luxembourg_private_company, value: "1.0", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "3, but if single shareholder company then 1",
             color: table_active},
            {comparison: malta_private_company, value: "1.0", color: table_active},
            {comparison: malta_public_company, value: "1.0", color: table_active},
            {comparison: mauritius_gbc1_company, value: "1.0", color: table_active},
            {comparison: mauritius_gbc2_company, value: "1.0", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "1.0", color: table_active},
            {comparison: panama_corporation, value: "3.0", color: table_active},
            {comparison: seychelles_ibc, value: "1.0", color: table_active},
            {comparison: seychelles_csl, value: "2.0", color: table_active},
            {comparison: singapore_private_exempt_company, value: "1.0", color: table_active},
            {comparison: singapore_private_company, value: "1.0", color: table_active},
            {comparison: singapore_public_company, value: "1.0", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "1.0", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "1.0", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "2.0", color: table_active},
            {comparison: dubai_difc_llc_company, value: "1.0", color: table_active},
            {comparison: rak_offshore_ibc, value: "1.0", color: table_active},
        ],
        topic: "Minimum number of directors",
        comparison: company
    }
    return jsonify(context)


# Get information about company_restriction_on_nationality_residency_of_directors
@app.route("/company_restriction_on_nationality_residency_of_directors")
def company_restriction_on_nationality_residency_of_directors():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "None", color: table_active},
            {comparison: andorra_private_limited_company, value: "None", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "None", color: table_active},
            {comparison: barbados_ibc, value: "Yes, corporate directors need to be Registered Barbados Companies",
             color: table_active},
            {comparison: barbados_isrl, value: "Yes, corporate directors need to be Registered Barbados Companies",
             color: table_active},
            {comparison: belize_ibc, value: "None", color: table_active},
            {comparison: bermuda_exempt_company, value: "No, but a quorum should be formed in Bermuda",
             color: table_active},
            {comparison: bvi_ibc, value: "None", color: table_active},
            {comparison: cayman_exempted_company, value: "None", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "None", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "None", color: table_active},
            {comparison: cyprus_private_company, value: "None", color: table_active},
            {comparison: cyprus_public_company, value: "None", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "None", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "None", color: table_active},
            {comparison: guernsey_limited_company, value: "None", color: table_active},
            {comparison: hong_kong_private_company, value: "None", color: table_active},
            {comparison: hong_kong_public_company, value: "None", color: table_active},
            {comparison: ireland_private_company,
             value: "Yes, at least 1 director should be an individual resident in an EEA Member State",
             color: table_active},
            {comparison: ireland_public_company,
             value: "Yes, at least 1 director should be an individual resident in an EEA Member State",
             color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "None", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "None", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "None", color: table_active},
            {comparison: jersey_private_company, value: "None", color: table_active},
            {comparison: jersey_public_company, value: "None", color: table_active},
            {comparison: liechtenstein_stock_company_ag,
             value: "At least 1 director should be individual, resident in Liechtenstein and qualified to act",
             color: table_active},
            {comparison: lithuania_private_limited_company, value: "None", color: table_active},
            {comparison: luxembourg_private_company, value: "None", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "None", color: table_active},
            {comparison: malta_private_company, value: "None", color: table_active},
            {comparison: malta_public_company, value: "None", color: table_active},
            {comparison: mauritius_gbc1_company,
             value: "Majority of Mauritius resident directors is needed to obtain GBC1 license",
             color: table_active},
            {comparison: mauritius_gbc2_company, value: "None", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "None", color: table_active},
            {comparison: panama_corporation, value: "None", color: table_active},
            {comparison: seychelles_ibc, value: "None", color: table_active},
            {comparison: seychelles_csl, value: "None", color: table_active},
            {comparison: singapore_private_exempt_company,
             value: at_least_one_director_should_be_an_individual_resident_in_singapore, color: table_active},
            {comparison: singapore_private_company,
             value: at_least_one_director_should_be_an_individual_resident_in_singapore, color: table_active},
            {comparison: singapore_public_company,
             value: at_least_one_director_should_be_an_individual_resident_in_singapore, color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Majority of Swiss resident directors",
             color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Majority of Swiss resident directors",
             color: table_active},
            {comparison: dubai_difc_ltd_company, value: "None", color: table_active},
            {comparison: dubai_difc_llc_company, value: "None", color: table_active},
            {comparison: rak_offshore_ibc, value: "None", color: table_active},
        ],
        topic: "Restriction on nationality residency of directors",
        comparison: company
    }
    return jsonify(context)


# Get information about company_local_director_requirement
@app.route("/company_local_director_requirement")
def company_local_director_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes if corporate directors", color: table_active},
            {comparison: barbados_isrl, value: "Yes if corporate directors", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes, a quorum should be formed in Bermuda",
             color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "No", color: table_active},
            {comparison: cyprus_public_company, value: "No", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "No", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: yes_at_least_one, color: table_active},
            {comparison: guernsey_limited_company, value: "No", color: table_active},
            {comparison: hong_kong_private_company, value: "No", color: table_active},
            {comparison: hong_kong_public_company, value: "No", color: table_active},
            {comparison: ireland_private_company, value: "Yes, at least 1 EEA-resident", color: table_active},
            {comparison: ireland_public_company, value: "Yes, at least 1 EEA-resident", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "No", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "No", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "No", color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "No", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes, at least 1 director should be local",
             color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "No", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "No", color: table_active},
            {comparison: malta_private_company, value: "No", color: table_active},
            {comparison: malta_public_company, value: "No", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: yes_at_least_one, color: table_active},
            {comparison: singapore_private_company, value: yes_at_least_one, color: table_active},
            {comparison: singapore_public_company, value: yes_at_least_one, color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: yes_at_least_one, color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: yes_at_least_one, color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Local director requirement",
        comparison: company
    }
    return jsonify(context)


# Get information about company_corporate_directors_allowed
@app.route("/company_corporate_directors_allowed")
def company_corporate_directors_allowed():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes but need to be registered in Barbados", color: table_active},
            {comparison: barbados_isrl, value: "Yes but need to be registered in Barbados", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company,
             value: "Currently yes but under new Companies Ordinance at least 1 director should be natural person",
             color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "No", color: table_active},
            {comparison: ireland_public_company, value: "No", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "No", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes, but should hold fiduciary license",
             color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "No", color: table_active},
            {comparison: jersey_private_company, value: "Yes, under conditions", color: table_active},
            {comparison: jersey_public_company, value: "Yes, under conditions", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes, if more than 1 directors", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: "No", color: table_active},
            {comparison: singapore_private_company, value: "No", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Corporate directors allowed",
        comparison: company
    }
    return jsonify(context)


# Get information about company_shareholders__meeting_requirement
@app.route("/company_shareholders__meeting_requirement")
def company_shareholders__meeting_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes but can be waived", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes but can be dispensed", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes, if more than 1 shareholder", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes if more than 25 shareholders",
             color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes, but can be waived", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Shareholders  meeting requirement",
        comparison: company
    }
    return jsonify(context)


# Get information about company_shareholders__meetings_location
@app.route("/company_shareholders__meetings_location")
def company_shareholders__meetings_location():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Anywhere", color: table_active},
            {comparison: andorra_private_limited_company, value: "Andorra", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Andorra", color: table_active},
            {comparison: barbados_ibc, value: "Anywhere", color: table_active},
            {comparison: barbados_isrl, value: "Anywhere", color: table_active},
            {comparison: belize_ibc, value: "Anywhere", color: table_active},
            {comparison: bermuda_exempt_company, value: "Anywhere", color: table_active},
            {comparison: bvi_ibc, value: "Anywhere", color: table_active},
            {comparison: cayman_exempted_company, value: "Anywhere", color: table_active},
            {comparison: cayman_exempted_limited_duration_company,
             value: "N/A - no requirement for shareholder meeting", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Cayman Islands", color: table_active},
            {comparison: cyprus_private_company, value: "Anywhere", color: table_active},
            {comparison: cyprus_public_company, value: "Anywhere", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Anywhere except Gibraltar",
             color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Egypt", color: table_active},
            {comparison: guernsey_limited_company, value: "Anywhere", color: table_active},
            {comparison: hong_kong_private_company, value: "Anywhere", color: table_active},
            {comparison: hong_kong_public_company, value: "Anywhere", color: table_active},
            {comparison: ireland_private_company, value: "Anywhere", color: table_active},
            {comparison: ireland_public_company, value: "Anywhere", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Anywhere", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Anywhere", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Anywhere", color: table_active},
            {comparison: jersey_private_company, value: "Anywhere", color: table_active},
            {comparison: jersey_public_company, value: "Anywhere", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Anywhere", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Anywhere", color: table_active},
            {comparison: luxembourg_private_company, value: "Anywhere", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Anywhere", color: table_active},
            {comparison: malta_private_company, value: "Anywhere", color: table_active},
            {comparison: malta_public_company, value: "Anywhere", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Anywhere", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Anywhere", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Netherlands", color: table_active},
            {comparison: panama_corporation, value: "Anywhere", color: table_active},
            {comparison: seychelles_ibc, value: "Anywhere", color: table_active},
            {comparison: seychelles_csl, value: "Anywhere", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Anywhere", color: table_active},
            {comparison: singapore_private_company, value: "Anywhere", color: table_active},
            {comparison: singapore_public_company, value: "Anywhere", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Switzerland", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Switzerland", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Dubai DIFC", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Dubai DIFC", color: table_active},
            {comparison: rak_offshore_ibc, value: "N/A - no requirement for shareholder meetings",
             color: table_active},
        ],
        topic: "Shareholders  meetings location",
        comparison: company
    }
    return jsonify(context)


# Get information about company_minimum_capital_requirement
@app.route("/company_minimum_capital_requirement")
def company_minimum_capital_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "B$1", color: table_active},
            {comparison: andorra_private_limited_company, value: "3.0", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "60.0", color: table_active},
            {comparison: barbados_ibc, value: "US$1", color: table_active},
            {comparison: barbados_isrl, value: "US$1", color: table_active},
            {comparison: belize_ibc, value: "US$1", color: table_active},
            {comparison: bermuda_exempt_company, value: "US$1", color: table_active},
            {comparison: bvi_ibc, value: "US$1", color: table_active},
            {comparison: cayman_exempted_company, value: "CI$1", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "CI$1", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "CI$1", color: table_active},
            {comparison: cyprus_private_company, value: "1.0", color: table_active},
            {comparison: cyprus_public_company, value: "26.629", color: table_active},
            {comparison: gibraltar_non_resident_company, value: gbp_one, color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "EGP 250,000", color: table_active},
            {comparison: guernsey_limited_company, value: gbp_one, color: table_active},
            {comparison: hong_kong_private_company, value: "HK$1", color: table_active},
            {comparison: hong_kong_public_company, value: "HK$1", color: table_active},
            {comparison: ireland_private_company, value: "1.0", color: table_active},
            {comparison: ireland_public_company, value: "€38,092 (25% should be fully paid-up)",
             color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: gbp_one, color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: gbp_one, color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: gbp_one, color: table_active},
            {comparison: jersey_private_company, value: gbp_one, color: table_active},
            {comparison: jersey_public_company, value: gbp_one, color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "CHF 50,000", color: table_active},
            {comparison: lithuania_private_limited_company, value: "2.5", color: table_active},
            {comparison: luxembourg_private_company, value: "12.395", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "30.987", color: table_active},
            {comparison: malta_private_company, value: "1165.0", color: table_active},
            {comparison: malta_public_company, value: "46587.0", color: table_active},
            {comparison: mauritius_gbc1_company, value: "US$1", color: table_active},
            {comparison: mauritius_gbc2_company, value: "US$1", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "€18,000 ���", color: table_active},
            {comparison: panama_corporation, value: "US$1", color: table_active},
            {comparison: seychelles_ibc, value: "US$1", color: table_active},
            {comparison: seychelles_csl, value: "US$1", color: table_active},
            {comparison: singapore_private_exempt_company, value: "S$1", color: table_active},
            {comparison: singapore_private_company, value: "S$1", color: table_active},
            {comparison: singapore_public_company, value: "S$1", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "CHF 20,000", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: chf_100000, color: table_active},
            {comparison: dubai_difc_ltd_company, value: "US$1", color: table_active},
            {comparison: dubai_difc_llc_company, value: "US$1", color: table_active},
            {comparison: rak_offshore_ibc, value: "None", color: table_active},
        ],
        topic: "Minimum capital requirement",
        comparison: company
    }
    return jsonify(context)


# Get information about company_can_the_capital_be_denominated_in_foreign_currency
@app.route("/company_can_the_capital_be_denominated_in_foreign_currency")
def company_can_the_capital_be_denominated_in_foreign_currency():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes, USD only", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "No", color: table_active},
            {comparison: ireland_public_company, value: "No", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes, in € and US$", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes, except MURs", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes, except MURs", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes, except SCR", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Can the capital be denominated in foreign currency",
        comparison: company
    }
    return jsonify(context)


# Get information about company_non_par_value_shares_allowed
@app.route("/company_non_par_value_shares_allowed")
def company_non_par_value_shares_allowed():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "N/A - ISRLs issue quotas rather than shares", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "No", color: table_active},
            {comparison: cyprus_public_company, value: "No", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes - only non-par value shares are allowed",
             color: table_active},
            {comparison: hong_kong_public_company, value: "Yes - only non-par value shares are allowed",
             color: table_active},
            {comparison: ireland_private_company, value: "No", color: table_active},
            {comparison: ireland_public_company, value: "No", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "No", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "No", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "No", color: table_active},
            {comparison: malta_public_company, value: "No", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: "No", color: table_active},
            {comparison: singapore_private_company, value: "No", color: table_active},
            {comparison: singapore_public_company, value: "No", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Non-par value shares allowed",
        comparison: company
    }
    return jsonify(context)


# Get information about company_bearer_shares_allowed
@app.route("/company_bearer_shares_allowed")
def company_bearer_shares_allowed():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "No", color: table_active},
            {comparison: barbados_isrl, value: "N/A - ISRLs issue quotas rather than shares",
             color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "No", color: table_active},
            {comparison: cyprus_public_company, value: "No", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "No", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "No", color: table_active},
            {comparison: hong_kong_private_company, value: "No", color: table_active},
            {comparison: hong_kong_public_company, value: "No", color: table_active},
            {comparison: ireland_private_company, value: "No", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "No", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "No", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "No", color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "No", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "No", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "No", color: table_active},
            {comparison: malta_public_company, value: "No", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: "No", color: table_active},
            {comparison: singapore_private_company, value: "No", color: table_active},
            {comparison: singapore_public_company, value: "No", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Bearer shares allowed",
        comparison: company
    }
    return jsonify(context)


# Get information about company_capital_duty_on_issurance_of_shares
@app.route("/company_capital_duty_on_issurance_of_shares")
def company_capital_duty_on_issurance_of_shares():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes but IBC is exempt", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "No", color: table_active},
            {comparison: barbados_isrl, value: "No", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: yes_ci_dollar_fifty, color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: yes_ci_dollar_fifty, color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: yes_ci_dollar_fifty, color: table_active},
            {comparison: cyprus_private_company, value: "Yes, starting from €103 depending on capital structure",
             color: table_active},
            {comparison: cyprus_public_company, value: "Yes, starting from €103 depending on capital structure",
             color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes, GBP£10", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "No", color: table_active},
            {comparison: hong_kong_private_company, value: "No", color: table_active},
            {comparison: hong_kong_public_company, value: "No", color: table_active},
            {comparison: ireland_private_company, value: "No", color: table_active},
            {comparison: ireland_public_company, value: "No", color: table_active},
            {comparison: isle_of_man_private_company_act_1931,
             value: yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands,
             color: table_active},
            {comparison: isle_of_man_limited_company_act_2006,
             value: yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands,
             color: table_active},
            {comparison: isle_of_man_public_company_act_1931,
             value: yes_gbp_seventeen_per_gbp_one_thousand_of_capital_above_gbp_two_thousands_with_a_maximum_duty_of_gbp_five_thousands,
             color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "No", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes, 1% on contributions over CHF1million",
             color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "No", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "No", color: table_active},
            {comparison: malta_private_company, value: "No", color: table_active},
            {comparison: malta_public_company, value: "No", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Capital duty on issurance of shares",
        comparison: company
    }
    return jsonify(context)


# Get information about company_registered_office_needs_to_be_in_the_country
@app.route("/company_registered_office_needs_to_be_in_the_country")
def company_registered_office_needs_to_be_in_the_country():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes (within UAE)", color: table_active},
        ],
        topic: "Registered office needs to be in the country",
        comparison: company
    }
    return jsonify(context)


# Get information about company_company_secretary_registered_agent_requirement
@app.route("/company_company_secretary_registered_agent_requirement")
def company_company_secretary_registered_agent_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "No", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "No", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Company secretary registered agent requirement",
        comparison: company
    }
    return jsonify(context)


# Get information about company_restrictions_to_foreign_investors
@app.route("/company_restrictions_to_foreign_investors")
def company_restrictions_to_foreign_investors():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "None", color: table_active},
            {comparison: andorra_private_limited_company, value: "None", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "None", color: table_active},
            {comparison: barbados_ibc, value: "None", color: table_active},
            {comparison: barbados_isrl, value: "None", color: table_active},
            {comparison: belize_ibc, value: "None", color: table_active},
            {comparison: bermuda_exempt_company, value: "None", color: table_active},
            {comparison: bvi_ibc, value: "None", color: table_active},
            {comparison: cayman_exempted_company, value: "None", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "None", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "None", color: table_active},
            {comparison: cyprus_private_company, value: "None", color: table_active},
            {comparison: cyprus_public_company, value: "None", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "None", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "None", color: table_active},
            {comparison: guernsey_limited_company, value: "None", color: table_active},
            {comparison: hong_kong_private_company, value: "None", color: table_active},
            {comparison: hong_kong_public_company, value: "None", color: table_active},
            {comparison: ireland_private_company, value: "None", color: table_active},
            {comparison: ireland_public_company, value: "None", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "None", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "None", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "None", color: table_active},
            {comparison: jersey_private_company, value: "None", color: table_active},
            {comparison: jersey_public_company, value: "None", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "None", color: table_active},
            {comparison: lithuania_private_limited_company, value: "None", color: table_active},
            {comparison: luxembourg_private_company, value: "None", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "None", color: table_active},
            {comparison: malta_private_company, value: "Yes, for holding Maltese real estate",
             color: table_active},
            {comparison: malta_public_company, value: "Yes, for holding Maltese real estate",
             color: table_active},
            {comparison: mauritius_gbc1_company, value: "None", color: table_active},
            {comparison: mauritius_gbc2_company, value: "None", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "None", color: table_active},
            {comparison: panama_corporation, value: "None", color: table_active},
            {comparison: seychelles_ibc, value: "None", color: table_active},
            {comparison: seychelles_csl, value: "None", color: table_active},
            {comparison: singapore_private_exempt_company, value: "None", color: table_active},
            {comparison: singapore_private_company, value: "None", color: table_active},
            {comparison: singapore_public_company, value: "None", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "None", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "None", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "None", color: table_active},
            {comparison: dubai_difc_llc_company, value: "None", color: table_active},
            {comparison: rak_offshore_ibc, value: "None", color: table_active},
        ],
        topic: "Restrictions to foreign investors",
        comparison: company
    }
    return jsonify(context)


# Get information about company_time_needed_for_registration
@app.route("/company_time_needed_for_registration")
def company_time_needed_for_registration():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: two_five_days, color: table_active},
            {comparison: andorra_private_limited_company, value: "50 days", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "50 days", color: table_active},
            {comparison: barbados_ibc, value: five_ten_days, color: table_active},
            {comparison: barbados_isrl, value: five_ten_days, color: table_active},
            {comparison: belize_ibc, value: "24 hours", color: table_active},
            {comparison: bermuda_exempt_company, value: "10 - 15 days", color: table_active},
            {comparison: bvi_ibc, value: one_two_days, color: table_active},
            {comparison: cayman_exempted_company, value: three_four_days, color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: three_four_days, color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: three_four_days, color: table_active},
            {comparison: cyprus_private_company, value: "7 - 10 days", color: table_active},
            {comparison: cyprus_public_company, value: "7 - 10 days", color: table_active},
            {comparison: gibraltar_non_resident_company, value: five_ten_days, color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "8 days", color: table_active},
            {comparison: guernsey_limited_company, value: "2 - 24 hours", color: table_active},
            {comparison: hong_kong_private_company, value: "4 - 7 days", color: table_active},
            {comparison: hong_kong_public_company, value: "4 - 7 days", color: table_active},
            {comparison: ireland_private_company, value: five_ten_days, color: table_active},
            {comparison: ireland_public_company, value: five_ten_days, color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: one_five_days, color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: one_five_days, color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: one_five_days, color: table_active},
            {comparison: jersey_private_company, value: "2 hours - 2 days", color: table_active},
            {comparison: jersey_public_company, value: "2 hours - 2 days", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "3 - 5 days", color: table_active},
            {comparison: lithuania_private_limited_company, value: "3 days", color: table_active},
            {comparison: luxembourg_private_company, value: "3 days", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "2 - 3 days", color: table_active},
            {comparison: malta_private_company, value: "2 - 4 days", color: table_active},
            {comparison: malta_public_company, value: "2 - 4 days", color: table_active},
            {comparison: mauritius_gbc1_company, value: "15 - 20 days", color: table_active},
            {comparison: mauritius_gbc2_company, value: two_five_days, color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "4 - 8 weeks", color: table_active},
            {comparison: panama_corporation, value: two_five_days, color: table_active},
            {comparison: seychelles_ibc, value: one_two_days, color: table_active},
            {comparison: seychelles_csl, value: "10 days", color: table_active},
            {comparison: singapore_private_exempt_company, value: one_two_days, color: table_active},
            {comparison: singapore_private_company, value: one_two_days, color: table_active},
            {comparison: singapore_public_company, value: one_two_days, color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "10 - 20 days", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "10 - 20 days", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "4 - 6 weeks", color: table_active},
            {comparison: dubai_difc_llc_company, value: "4 - 6 weeks", color: table_active},
            {comparison: rak_offshore_ibc, value: "24 hours", color: table_active},
        ],
        topic: "Time needed for registration",
        comparison: company
    }
    return jsonify(context)


# Get information about company_shelf_companies_available
@app.route("/company_shelf_companies_available")
def company_shelf_companies_available():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "No", color: table_active},
            {comparison: barbados_isrl, value: "No", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "No", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "No, due to speedy registration", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company,
             value: "Yes, but difficult to find due to high minimum capital requirement", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "No, due to beneficial ownership disclosure",
             color: table_active},
            {comparison: jersey_public_company, value: "No, due to beneficial ownership disclosure",
             color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes, but rare due to high minimum requirement",
             color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company,
             value: "Yes but difficult to find due to high minimum capital requirement", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No, due to the high minimum capital requirement",
             color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes but not easily found due to high cost",
             color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes but not easily found due to high cost",
             color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Shelf companies available",
        comparison: company
    }
    return jsonify(context)


# Get information about company_publicly_accessible_records_of_directors
@app.route("/company_publicly_accessible_records_of_directors")
def company_publicly_accessible_records_of_directors():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: no_but_filed_with_the_authorities, color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Publicly accessible records of directors",
        comparison: company
    }
    return jsonify(context)


# Get information about company_publicly_accessible_records_of_shareholders
@app.route("/company_publicly_accessible_records_of_shareholders")
def company_publicly_accessible_records_of_shareholders():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "No", color: table_active},
            {comparison: barbados_isrl, value: "No", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "No", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "No", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "No", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "No", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "No", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes if 1 shareholder only",
             color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: no_but_filed_with_the_authorities, color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Publicly accessible records of shareholders",
        comparison: company
    }
    return jsonify(context)


# Get information about company_publicly_accessible_financial_statements
@app.route("/company_publicly_accessible_financial_statements")
def company_publicly_accessible_financial_statements():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "No", color: table_active},
            {comparison: barbados_isrl, value: "No", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "No", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "No", color: table_active},
            {comparison: hong_kong_private_company, value: "No", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "No", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "No", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "No", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "No", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "No", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "No", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: no_but_filed_with_the_authorities, color: table_active},
            {comparison: singapore_private_exempt_company, value: "No", color: table_active},
            {comparison: singapore_private_company, value: "No", color: table_active},
            {comparison: singapore_public_company, value: "No", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Publicly accessible financial statements",
        comparison: company
    }
    return jsonify(context)


# Get information about company_beneficial_ownership_disclosure
@app.route("/company_beneficial_ownership_disclosure")
def company_beneficial_ownership_disclosure():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: yes_to_service_provider, color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes, to service providers and authorities",
             color: table_active},
            {comparison: andorra_private_anonymous_company,
             value: "Yes, to the service provider and the authorities", color: table_active},
            {comparison: barbados_ibc, value: "Yes, to Authorities", color: table_active},
            {comparison: barbados_isrl, value: "Yes, to Authorities", color: table_active},
            {comparison: belize_ibc, value: yes_to_service_provider, color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes, to service provide and Authorities",
             color: table_active},
            {comparison: bvi_ibc, value: yes_to_service_provider, color: table_active},
            {comparison: cayman_exempted_company, value: yes_to_service_provider, color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: yes_to_service_provider,
             color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: yes_to_service_provider,
             color: table_active},
            {comparison: cyprus_private_company, value: yes_to_service_provider, color: table_active},
            {comparison: cyprus_public_company, value: yes_to_service_provider, color: table_active},
            {comparison: gibraltar_non_resident_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: guernsey_limited_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: hong_kong_private_company, value: yes_to_service_provider, color: table_active},
            {comparison: hong_kong_public_company, value: yes_to_service_provider, color: table_active},
            {comparison: ireland_private_company, value: yes_to_service_provider, color: table_active},
            {comparison: ireland_public_company, value: yes_to_service_provider, color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: yes_to_service_provider,
             color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: yes_to_service_provider,
             color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: yes_to_service_provider,
             color: table_active},
            {comparison: jersey_private_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: jersey_public_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: yes_to_service_provider,
             color: table_active},
            {comparison: lithuania_private_limited_company, value: yes_to_service_provider,
             color: table_active},
            {comparison: luxembourg_private_company, value: yes_to_service_provider, color: table_active},
            {comparison: luxembourg_public_company_sa, value: yes_to_service_provider, color: table_active},
            {comparison: malta_private_company, value: yes_to_service_provider, color: table_active},
            {comparison: malta_public_company, value: yes_to_service_provider, color: table_active},
            {comparison: mauritius_gbc1_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: mauritius_gbc2_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: yes_to_service_provider,
             color: table_active},
            {comparison: panama_corporation, value: yes_to_service_provider, color: table_active},
            {comparison: seychelles_ibc, value: yes_to_service_provider, color: table_active},
            {comparison: seychelles_csl, value: "Yes, to service provider and Authorities.",
             color: table_active},
            {comparison: singapore_private_exempt_company, value: yes_to_service_provider,
             color: table_active},
            {comparison: singapore_private_company, value: yes_to_service_provider, color: table_active},
            {comparison: singapore_public_company, value: yes_to_service_provider, color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: yes_to_service_provider,
             color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: yes_to_service_provider,
             color: table_active},
            {comparison: dubai_difc_ltd_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: dubai_difc_llc_company, value: yes_to_service_provider_and_authorities,
             color: table_active},
            {comparison: rak_offshore_ibc, value: yes_to_service_provider, color: table_active},
        ],
        topic: "Beneficial ownership disclosure",
        comparison: company
    }
    return jsonify(context)


# Get information about company_nominee_shareholder_allowed
@app.route("/company_nominee_shareholder_allowed")
def company_nominee_shareholder_allowed():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl,
             value: "Yes but by law the shareholder would be treated as the real shareholder and beneficial owner",
             color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Nominee shareholder allowed ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_annual_return_requirement
@app.route("/company_annual_return_requirement")
def company_annual_return_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Annual return requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_tax_return_requirement
@app.route("/company_tax_return_requirement")
def company_tax_return_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "No", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Tax return requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_requirement_to_maintain_accounting_records
@app.route("/company_requirement_to_maintain_accounting_records")
def company_requirement_to_maintain_accounting_records():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes, for 5 years", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Requirement to maintain accounting records ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_foreign_currency_accounting_allowed
@app.route("/company_foreign_currency_accounting_allowed")
def company_foreign_currency_accounting_allowed():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes, in USD only", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "No", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Foreign currency accounting allowed ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_accounting_records_can_be_held_outside_the_country
@app.route("/company_accounting_records_can_be_held_outside_the_country")
def company_accounting_records_can_be_held_outside_the_country():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "No", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "No", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "Yes", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes", color: table_active},
            {comparison: cayman_exempted_company, value: "Yes", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "Yes", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "Yes", color: table_active},
            {comparison: seychelles_ibc, value: "Yes", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "No", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "No", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Accounting records can be held outside the country ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_financial_statements_requirement
@app.route("/company_financial_statements_requirement")
def company_financial_statements_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "Yes - need to maintain accounts", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Financial statements requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_financial_statements_filing_requirement
@app.route("/company_financial_statements_filing_requirement")
def company_financial_statements_filing_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "No", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "No", color: table_active},
            {comparison: hong_kong_private_company, value: "No", color: table_active},
            {comparison: hong_kong_public_company, value: "No", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "No", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "No", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No, only financial summary", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "No", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Financial statements filing requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_accounting_principles_for_financial_statements
@app.route("/company_accounting_principles_for_financial_statements")
def company_accounting_principles_for_financial_statements():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "IFRS", color: table_active},
            {comparison: andorra_private_limited_company, value: "Andorran accounting laws",
             color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Andorran accounting laws",
             color: table_active},
            {comparison: barbados_ibc, value: "IFRS", color: table_active},
            {comparison: barbados_isrl, value: "IFRS", color: table_active},
            {comparison: belize_ibc, value: "N/A - no financial statements required", color: table_active},
            {comparison: bermuda_exempt_company, value: "IFRS", color: table_active},
            {comparison: bvi_ibc, value: "IFRS", color: table_active},
            {comparison: cayman_exempted_company, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: cayman_exempted_limited_duration_company,
             value: n_a_no_requirement_for_financial_statements, color: table_active},
            {comparison: cayman_ordinary_non_resident_company,
             value: n_a_no_requirement_for_financial_statements, color: table_active},
            {comparison: cyprus_private_company, value: "IFRS", color: table_active},
            {comparison: cyprus_public_company, value: "IFRS", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "IFRS", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Egyptian GAAP", color: table_active},
            {comparison: guernsey_limited_company, value: uk_gaap_ias_ifrs, color: table_active},
            {comparison: hong_kong_private_company,
             value: "Hong Kong Financial Reporting Standards (in line with IFRS)", color: table_active},
            {comparison: hong_kong_public_company,
             value: "Hong Kong Financial Reporting Standards (in line with IFRS)", color: table_active},
            {comparison: ireland_private_company, value: "IFRS", color: table_active},
            {comparison: ireland_public_company, value: "IFRS", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "IFRS", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "IFRS", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "IFRS", color: table_active},
            {comparison: jersey_private_company, value: uk_gaap_ias_ifrs, color: table_active},
            {comparison: jersey_public_company, value: uk_gaap_ias_ifrs, color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "IFRS", color: table_active},
            {comparison: lithuania_private_limited_company, value: "IFRS", color: table_active},
            {comparison: luxembourg_private_company, value: "IFRS or Luxembourg GAAP", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "IFRS or Luxembourg GAAP", color: table_active},
            {comparison: malta_private_company, value: "IFRS", color: table_active},
            {comparison: malta_public_company, value: "IFRS", color: table_active},
            {comparison: mauritius_gbc1_company, value: "IFRS", color: table_active},
            {comparison: mauritius_gbc2_company, value: "IFRS", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "IFRS", color: table_active},
            {comparison: panama_corporation, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: seychelles_ibc, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: seychelles_csl, value: "GAAP", color: table_active},
            {comparison: singapore_private_exempt_company, value: "IFRS", color: table_active},
            {comparison: singapore_private_company, value: "IFRS", color: table_active},
            {comparison: singapore_public_company, value: "IFRS", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Swiss GAAP", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Swiss GAAP", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "IFRS", color: table_active},
            {comparison: dubai_difc_llc_company, value: "IFRS", color: table_active},
            {comparison: rak_offshore_ibc, value: "Discussed with local registered agent", color: table_active},
        ],
        topic: "Accounting principles for financial statements",
        comparison: company
    }
    return jsonify(context)


# Get information about company_consolidated_financial_statements_requirement
@app.route("/company_consolidated_financial_statements_requirement")
def company_consolidated_financial_statements_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "N/A", color: table_active},
            {comparison: cayman_exempted_company, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: cayman_exempted_limited_duration_company,
             value: n_a_no_requirement_for_financial_statements, color: table_active},
            {comparison: cayman_ordinary_non_resident_company,
             value: n_a_no_requirement_for_financial_statements, color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "Yes", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: seychelles_ibc, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "No", color: table_active},
        ],
        topic: "Consolidated financial statements requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_exemption_to_consolidated_financial_statements_requirement
@app.route("/company_exemption_to_consolidated_financial_statements_requirement")
def company_exemption_to_consolidated_financial_statements_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "Yes", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes", color: table_active},
            {comparison: barbados_isrl, value: "Yes", color: table_active},
            {comparison: belize_ibc, value: "N/A - no requirement for consolidated financial statements",
             color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes", color: table_active},
            {comparison: bvi_ibc, value: "N/A", color: table_active},
            {comparison: cayman_exempted_company, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: cayman_exempted_limited_duration_company,
             value: n_a_no_requirement_for_financial_statements, color: table_active},
            {comparison: cayman_ordinary_non_resident_company,
             value: n_a_no_requirement_for_financial_statements, color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "Yes", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "Yes", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "Yes", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: seychelles_ibc, value: n_a_no_requirement_for_financial_statements,
             color: table_active},
            {comparison: seychelles_csl, value: "N/A", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "N/A", color: table_active},
        ],
        topic: "Exemption to consolidated financial statements requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_audit_requirement
@app.route("/company_audit_requirement")
def company_audit_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: "No", color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc, value: "Yes but exemption available", color: table_active},
            {comparison: barbados_isrl, value: "Yes but exemption available", color: table_active},
            {comparison: belize_ibc, value: "No", color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes but can be waived", color: table_active},
            {comparison: bvi_ibc, value: "No", color: table_active},
            {comparison: cayman_exempted_company, value: "No", color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: "No", color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: "No", color: table_active},
            {comparison: cyprus_private_company, value: "Yes", color: table_active},
            {comparison: cyprus_public_company, value: "Yes", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes", color: table_active},
            {comparison: hong_kong_public_company, value: "Yes", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "Yes", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: "No", color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "Yes", color: table_active},
            {comparison: jersey_private_company, value: "No", color: table_active},
            {comparison: jersey_public_company, value: "Yes", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "Yes", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes (but still need an audit for tax return purposes)",
             color: table_active},
            {comparison: malta_public_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc1_company, value: "Yes", color: table_active},
            {comparison: mauritius_gbc2_company, value: "No", color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: "No", color: table_active},
            {comparison: seychelles_ibc, value: "No", color: table_active},
            {comparison: seychelles_csl, value: "Yes", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "Yes", color: table_active},
            {comparison: singapore_public_company, value: "Yes", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "Yes", color: table_active},
            {comparison: dubai_difc_llc_company, value: "Yes", color: table_active},
            {comparison: rak_offshore_ibc, value: "Yes", color: table_active},
        ],
        topic: "Audit requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about company_exemptions_to_audit_requirement
@app.route("/company_exemptions_to_audit_requirement")
def company_exemptions_to_audit_requirement():
    context = {
        "data": [
            {comparison: bahamas_ibc, value: n_a_no_audit_requirement, color: table_active},
            {comparison: andorra_private_limited_company, value: "Yes", color: table_active},
            {comparison: andorra_private_anonymous_company, value: "Yes", color: table_active},
            {comparison: barbados_ibc,
             value: "Yes. Audit is required only if assets or gross revenue exceed US$500,000",
             color: table_active},
            {comparison: barbados_isrl,
             value: "Yes. Audit is required only if assets or gross revenue exceed US$500,000",
             color: table_active},
            {comparison: belize_ibc, value: n_a_no_audit_requirement, color: table_active},
            {comparison: bermuda_exempt_company, value: "Yes, audit can be waived", color: table_active},
            {comparison: bvi_ibc, value: n_a_no_audit_requirement, color: table_active},
            {comparison: cayman_exempted_company, value: n_a_no_audit_requirement, color: table_active},
            {comparison: cayman_exempted_limited_duration_company, value: n_a_no_audit_requirement,
             color: table_active},
            {comparison: cayman_ordinary_non_resident_company, value: n_a_no_audit_requirement,
             color: table_active},
            {comparison: cyprus_private_company, value: "No", color: table_active},
            {comparison: cyprus_public_company, value: "No", color: table_active},
            {comparison: gibraltar_non_resident_company, value: "Yes", color: table_active},
            {comparison: egypt_limited_liability_company_llc, value: "No", color: table_active},
            {comparison: guernsey_limited_company, value: "Yes", color: table_active},
            {comparison: hong_kong_private_company, value: "Yes - if dormant company", color: table_active},
            {comparison: hong_kong_public_company, value: "No", color: table_active},
            {comparison: ireland_private_company, value: "Yes", color: table_active},
            {comparison: ireland_public_company, value: "No", color: table_active},
            {comparison: isle_of_man_private_company_act_1931, value: "Yes", color: table_active},
            {comparison: isle_of_man_limited_company_act_2006, value: n_a_no_audit_requirement,
             color: table_active},
            {comparison: isle_of_man_public_company_act_1931, value: "No", color: table_active},
            {comparison: jersey_private_company, value: n_a_no_audit_requirement, color: table_active},
            {comparison: jersey_public_company, value: "No", color: table_active},
            {comparison: liechtenstein_stock_company_ag, value: "No", color: table_active},
            {comparison: lithuania_private_limited_company, value: "Yes", color: table_active},
            {comparison: luxembourg_private_company, value: "Yes", color: table_active},
            {comparison: luxembourg_public_company_sa, value: "Yes", color: table_active},
            {comparison: malta_private_company, value: "Yes", color: table_active},
            {comparison: malta_public_company, value: "No", color: table_active},
            {comparison: mauritius_gbc1_company, value: "No", color: table_active},
            {comparison: mauritius_gbc2_company, value: n_a_no_audit_requirement, color: table_active},
            {comparison: netherlands_bv_company_dutch_bv, value: "Yes", color: table_active},
            {comparison: panama_corporation, value: n_a_no_audit_requirement, color: table_active},
            {comparison: seychelles_ibc, value: n_a_no_audit_requirement, color: table_active},
            {comparison: seychelles_csl, value: "No", color: table_active},
            {comparison: singapore_private_exempt_company, value: "Yes", color: table_active},
            {comparison: singapore_private_company, value: "No", color: table_active},
            {comparison: singapore_public_company, value: "No", color: table_active},
            {comparison: swiss_limited_company_sarl_gmbh, value: "Yes", color: table_active},
            {comparison: swiss_stock_corporation_ag_sa, value: "Yes", color: table_active},
            {comparison: dubai_difc_ltd_company, value: "No", color: table_active},
            {comparison: dubai_difc_llc_company, value: "No", color: table_active},
            {comparison: rak_offshore_ibc, value: "N/A", color: table_active},
        ],
        topic: "Exemptions to audit requirement ",
        comparison: company
    }
    return jsonify(context)


# Get information about trust_registration_requirement
@app.route("/trust_registration_requirement")
def trust_registration_requirement():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "No, unless it holds Bahamian real estate",
             color: table_active},
            {comparison: barbados_international_trust, value: "Yes", color: table_active},
            {comparison: belize_international_trust, value: "Yes", color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust, value: "Yes", color: table_active},
            {comparison: gibraltar_trust, value: "No, registration is optional", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "No", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: "No, registration is optional", color: table_active},
            {comparison: malta_trust, value: "No", color: table_active},
            {comparison: mauritius_non_resident_trust, value: "No", color: table_active},
            {comparison: panama_trust, value: "No, unless it owns Panama real estate", color: table_active},
            {comparison: seychelles_international_trust, value: "Yes", color: table_active},
            {comparison: singapore_foreign_trust, value: "No", color: table_active},
        ],
        topic: "Registration requirement",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_settlor_residency_requirement
@app.route("/trust_settlor_residency_requirement")
def trust_settlor_residency_requirement():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust,
             value: "Yes, should not be a permanent resident of the Bahamas", color: table_active},
            {comparison: barbados_international_trust,
             value: "Yes, should not be a permanent resident of Barbados", color: table_active},
            {comparison: belize_international_trust,
             value: "Yes, should not be a permanent resident of Belize. Persons resident under the Belize Retirement Program can be settlors.",
             color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust,
             value: "Yes, but may not be a Cyprus permanent resident in the year preceding the year of creation",
             color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "No", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: "No", color: table_active},
            {comparison: malta_trust, value: "No", color: table_active},
            {comparison: mauritius_non_resident_trust,
             value: "Yes, should not be a permanent resident of the Mauritius", color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust, value: "No", color: table_active},
            {comparison: singapore_foreign_trust, value: "Yes, should not be a permanent resident of Singapore",
             color: table_active},
        ],
        topic: "Settlor residency requirement",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_beneficiary_residency_requirement
@app.route("/trust_beneficiary_residency_requirement")
def trust_beneficiary_residency_requirement():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust,
             value: "Yes, should not be a permanent resident of the Bahamas", color: table_active},
            {comparison: barbados_international_trust,
             value: "Yes, should not be a permanent resident of Barbados", color: table_active},
            {comparison: belize_international_trust,
             value: "Yes, should not be a permanent resident of Belize. Persons resident under the Belize Retirement Program can be beneficiaries.",
             color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust,
             value: "Yes, but may not be a Cyprus permanent resident in the year preceding the year of creation",
             color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "No", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: "No", color: table_active},
            {comparison: malta_trust, value: "No", color: table_active},
            {comparison: mauritius_non_resident_trust,
             value: "Yes, should not be a permanent resident of the Mauritius", color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust, value: "No", color: table_active},
            {comparison: singapore_foreign_trust, value: "Yes, should not be a permanent resident of Singapore",
             color: table_active},
        ],
        topic: "Beneficiary residency requirement",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_trustee_residency_requirement
@app.route("/trust_trustee_residency_requirement")
def trust_trustee_residency_requirement():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "Yes", color: table_active},
            {comparison: barbados_international_trust, value: yes_at_least_one, color: table_active},
            {comparison: belize_international_trust,
             value: "No, but a Belize resident and licensed Trust Agent is required.", color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust, value: yes_at_least_one, color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "Yes", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: yes_at_least_one, color: table_active},
            {comparison: malta_trust, value: yes_at_least_one, color: table_active},
            {comparison: mauritius_non_resident_trust, value: yes_at_least_one, color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust, value: "Yes", color: table_active},
            {comparison: singapore_foreign_trust, value: "Yes", color: table_active},
        ],
        topic: "Trustee residency requirement",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_should_the_trustee_be_licensed
@app.route("/trust_should_the_trustee_be_licensed")
def trust_should_the_trustee_be_licensed():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "Yes", color: table_active},
            {comparison: barbados_international_trust, value: "No", color: table_active},
            {comparison: belize_international_trust, value: "Yes, if a corporate trustee",
             color: table_active},
            {comparison: bermuda_trust, value: "Yes", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust, value: "Yes", color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "Yes", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "Yes", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: "Yes", color: table_active},
            {comparison: malta_trust, value: yes_at_least_one, color: table_active},
            {comparison: mauritius_non_resident_trust, value: yes_at_least_one, color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust, value: "Yes", color: table_active},
            {comparison: singapore_foreign_trust, value: "Yes", color: table_active},
        ],
        topic: "Should the trustee be licensed",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_protector_allowed
@app.route("/trust_protector_allowed")
def trust_protector_allowed():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "Yes", color: table_active},
            {comparison: barbados_international_trust, value: "Yes", color: table_active},
            {comparison: belize_international_trust, value: "Yes", color: table_active},
            {comparison: bermuda_trust, value: "Yes", color: table_active},
            {comparison: bvi_trust, value: "Yes", color: table_active},
            {comparison: cayman_ordinary_trust, value: "Yes", color: table_active},
            {comparison: cyprus_international_trust, value: "Yes", color: table_active},
            {comparison: gibraltar_trust, value: "Yes", color: table_active},
            {comparison: guernsey_trust, value: "Yes", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "Yes", color: table_active},
            {comparison: isle_of_man_trust, value: "Yes", color: table_active},
            {comparison: jersey_international_trust, value: "Yes", color: table_active},
            {comparison: liechtenstein_trust, value: "Yes", color: table_active},
            {comparison: malta_trust, value: "Yes", color: table_active},
            {comparison: mauritius_non_resident_trust, value: "Yes", color: table_active},
            {comparison: panama_trust, value: "Yes", color: table_active},
            {comparison: seychelles_international_trust, value: "Yes", color: table_active},
            {comparison: singapore_foreign_trust, value: "Yes", color: table_active},
        ],
        topic: "Protector allowed",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_protector_requirement
@app.route("/trust_protector_requirement")
def trust_protector_requirement():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "No", color: table_active},
            {comparison: barbados_international_trust, value: "No", color: table_active},
            {comparison: belize_international_trust, value: "No", color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust, value: "No", color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "No", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: "No", color: table_active},
            {comparison: malta_trust, value: "No", color: table_active},
            {comparison: mauritius_non_resident_trust, value: "No", color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust, value: "No", color: table_active},
            {comparison: singapore_foreign_trust, value: "No", color: table_active},
        ],
        topic: "Protector requirement",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_perpetuity_period
@app.route("/trust_perpetuity_period")
def trust_perpetuity_period():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: hundred_fifty_years, color: table_active},
            {comparison: barbados_international_trust, value: hundred_years, color: table_active},
            {comparison: belize_international_trust, value: "120 years", color: table_active},
            {comparison: bermuda_trust, value: hundred_years, color: table_active},
            {comparison: bvi_trust, value: "360 years", color: table_active},
            {comparison: cayman_ordinary_trust, value: hundred_fifty_years, color: table_active},
            {comparison: cyprus_international_trust, value: no_maximum_duration, color: table_active},
            {comparison: gibraltar_trust, value: hundred_years, color: table_active},
            {comparison: guernsey_trust, value: no_maximum_duration, color: table_active},
            {comparison: hong_kong_foreign_trust, value: "80 years", color: table_active},
            {comparison: isle_of_man_trust, value: hundred_fifty_years, color: table_active},
            {comparison: jersey_international_trust, value: no_maximum_duration, color: table_active},
            {comparison: liechtenstein_trust, value: no_maximum_duration, color: table_active},
            {comparison: malta_trust, value: hundred_years, color: table_active},
            {comparison: mauritius_non_resident_trust, value: "99 years", color: table_active},
            {comparison: panama_trust, value: no_maximum_duration, color: table_active},
            {comparison: seychelles_international_trust, value: hundred_years, color: table_active},
            {comparison: singapore_foreign_trust, value: hundred_years, color: table_active},
        ],
        topic: "Perpetuity period",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_restriction_on_trust_property
@app.route("/trust_restriction_on_trust_property")
def trust_restriction_on_trust_property():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust,
             value: "Yes, should not include Bahamian real estate or shares in a company owning Bahamian real estate",
             color: table_active},
            {comparison: barbados_international_trust, value: "Yes, should not include Barbados real estate",
             color: table_active},
            {comparison: belize_international_trust,
             value: "Yes, should not include Belize real estate or shares in a company owning Belize real estate",
             color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust, value: "No", color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "No", color: table_active},
            {comparison: jersey_international_trust,
             value: "Yes, should not include Jersey real estate or shares in a company owning Jersey real estate",
             color: table_active},
            {comparison: liechtenstein_trust, value: "No", color: table_active},
            {comparison: malta_trust,
             value: "Yes, should not include Maltese real estate or shares in a company owning Maltese real estate",
             color: table_active},
            {comparison: mauritius_non_resident_trust, value: "No", color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust,
             value: "Yes, should not include Seychelles real estate or shares in a company owning Seychelles real estate",
             color: table_active},
            {comparison: singapore_foreign_trust, value: "No", color: table_active},
        ],
        topic: "Restriction on trust property",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_taxation
@app.route("/trust_taxation")
def trust_taxation():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "Exempt", color: table_active},
            {comparison: barbados_international_trust, value: "Exempt", color: table_active},
            {comparison: belize_international_trust, value: "Exempt", color: table_active},
            {comparison: bermuda_trust, value: "Exempt", color: table_active},
            {comparison: bvi_trust, value: "Exempt", color: table_active},
            {comparison: cayman_ordinary_trust, value: "Exempt", color: table_active},
            {comparison: cyprus_international_trust, value: "Exempt, except for income generated in Cyprus",
             color: table_active},
            {comparison: gibraltar_trust, value: "Exempt", color: table_active},
            {comparison: guernsey_trust, value: "Exempt", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "Exempt", color: table_active},
            {comparison: isle_of_man_trust, value: "Exempt", color: table_active},
            {comparison: jersey_international_trust, value: "Exempt", color: table_active},
            {comparison: liechtenstein_trust, value: "Exempt", color: table_active},
            {comparison: malta_trust, value: "Exempt", color: table_active},
            {comparison: mauritius_non_resident_trust, value: "Exempt", color: table_active},
            {comparison: panama_trust, value: "Exempt", color: table_active},
            {comparison: seychelles_international_trust, value: "Exempt", color: table_active},
            {comparison: singapore_foreign_trust, value: "Exempt", color: table_active},
        ],
        topic: "Taxation",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_confidentiality
@app.route("/trust_confidentiality")
def trust_confidentiality():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: barbados_international_trust,
             value: "Names of Settlor and Beneficiaries are not publicly available", color: table_active},
            {comparison: belize_international_trust,
             value: "The names of the Settlor(s) and the Beneficiary(ies) are not reported and the Register of Trusts is not open for public inspection.",
             color: table_active},
            {comparison: bermuda_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: bvi_trust, value: no_information_is_declosed_to_any_person, color: table_active},
            {comparison: cayman_ordinary_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: cyprus_international_trust,
             value: "The names of Settlor and Beneficiaries are not disclosed to Authorities",
             color: table_active},
            {comparison: gibraltar_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: guernsey_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: hong_kong_foreign_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: isle_of_man_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: jersey_international_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: liechtenstein_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: malta_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: mauritius_non_resident_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: panama_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
            {comparison: seychelles_international_trust,
             value: "The names of Settlor and Beneficiaries are not disclosed to Authorities",
             color: table_active},
            {comparison: singapore_foreign_trust, value: no_information_is_declosed_to_any_person,
             color: table_active},
        ],
        topic: "Confidentiality",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_asset_protection
@app.route("/trust_asset_protection")
def trust_asset_protection():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "Yes", color: table_active},
            {comparison: barbados_international_trust, value: "Yes", color: table_active},
            {comparison: belize_international_trust, value: "Yes", color: table_active},
            {comparison: bermuda_trust, value: "Yes", color: table_active},
            {comparison: bvi_trust, value: n_a_no_specific_legislation_for_asset_protection,
             color: table_active},
            {comparison: cayman_ordinary_trust, value: "Yes", color: table_active},
            {comparison: cyprus_international_trust, value: "Yes", color: table_active},
            {comparison: gibraltar_trust, value: "Yes if the Trust is registered", color: table_active},
            {comparison: guernsey_trust, value: n_a_no_specific_legislation_for_asset_protection,
             color: table_active},
            {comparison: hong_kong_foreign_trust, value: n_a_no_specific_legislation_for_asset_protection,
             color: table_active},
            {comparison: isle_of_man_trust, value: "Yes", color: table_active},
            {comparison: jersey_international_trust, value: n_a_no_specific_legislation_for_asset_protection,
             color: table_active},
            {comparison: liechtenstein_trust, value: "Yes", color: table_active},
            {comparison: malta_trust, value: "Yes", color: table_active},
            {comparison: mauritius_non_resident_trust, value: "Yes", color: table_active},
            {comparison: panama_trust, value: "Yes", color: table_active},
            {comparison: seychelles_international_trust, value: "Yes", color: table_active},
            {comparison: singapore_foreign_trust, value: "Yes", color: table_active},
        ],
        topic: "Asset protection",
        comparison: trust
    }
    return jsonify(context)


# Get information about trust_reporting_requirement
@app.route("/trust_reporting_requirement")
def trust_reporting_requirement():
    context = {
        "data": [
            {comparison: bahamas_non_resident_trust, value: "No", color: table_active},
            {comparison: barbados_international_trust, value: "No", color: table_active},
            {comparison: belize_international_trust, value: "No", color: table_active},
            {comparison: bermuda_trust, value: "No", color: table_active},
            {comparison: bvi_trust, value: "No", color: table_active},
            {comparison: cayman_ordinary_trust, value: "No", color: table_active},
            {comparison: cyprus_international_trust, value: "No", color: table_active},
            {comparison: gibraltar_trust, value: "No", color: table_active},
            {comparison: guernsey_trust, value: "No", color: table_active},
            {comparison: hong_kong_foreign_trust, value: "No", color: table_active},
            {comparison: isle_of_man_trust, value: "No", color: table_active},
            {comparison: jersey_international_trust, value: "No", color: table_active},
            {comparison: liechtenstein_trust, value: "No", color: table_active},
            {comparison: malta_trust, value: "No", color: table_active},
            {comparison: mauritius_non_resident_trust, value: "No", color: table_active},
            {comparison: panama_trust, value: "No", color: table_active},
            {comparison: seychelles_international_trust, value: "No", color: table_active},
            {comparison: singapore_foreign_trust,
             value: "Yes, annual declaration of compliance with exemption criteria", color: table_active},
        ],
        topic: "Reporting requirement",
        comparison: trust
    }
    return jsonify(context)
