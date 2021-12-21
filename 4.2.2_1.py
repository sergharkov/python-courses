def make_country(country_name, capital_name):
    try:
        userFloat1 = str(country_name)
        userFloat2 = str(capital_name)
    except ValueError:
        return print("TypeError")
    finally:
        make_country = {}
        make_country['country_name'] = country_name
        make_country['capital_name'] = capital_name
    return make_country
#----------------------------
def show_country_info(country_dict):
    capital = country_dict['capital_name']
    country = country_dict['country_name'] 
    return (f"Country: {country}, Capital: {capital}.")
print(show_country_info(make_country('Gondor', 'Minas Tirith')))
