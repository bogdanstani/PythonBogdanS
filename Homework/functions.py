import pprint
import pycountry

description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '
])
raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]


def generate_dict_from_raw_data():
    tuple_country = []

    for country_index, list_of_values_of_coverage in raw_data:
        zipping_list = list(zip(description[1], list_of_values_of_coverage))
        list_of_dict = []

        for year, coverage in zipping_list:
            list_of_dict.append({'year': year, 'coverage': coverage})

        try:
            string_country_index = pycountry.countries.get(alpha_2=country_index).name
        except:
            string_country_index = country_index

        tuple_country.append((string_country_index, list_of_dict))

    return dict(tuple_country)


def get_year_data(dataset_dict, year):
    list_of_tuple_data = []

    for key in dataset_dict.keys():
        for each_dict in dataset_dict[key]:

            if each_dict.get('year').strip() == year.strip():
                # print((key, each_dict.get('coverage')))
                list_of_tuple_data.append((key, each_dict.get('coverage')))

    # print(list_of_tuple_data)
    return {year: list_of_tuple_data}


def get_country_data(dataset_dict, country):
    # print(dataset.get(country))
    list_of_tuple_data = []

    for each_dict in dataset_dict.get(country):
        list_of_tuple_data.append((each_dict.get('year'), each_dict.get('coverage')))
        # print(each_dict.get('coverage'))

    # print(list_of_tuple_data)

    return {country: list_of_tuple_data}


def perform_average(country_dictionary):
    sum_of_coverage_of_the_country = 0

    for each_tuple_in_list in country_dictionary:
        sum_of_coverage_of_the_country += float(each_tuple_in_list[1])

    return sum_of_coverage_of_the_country / len(country_dictionary)


# Functions for decorators homework ******************************

print_registry = []


def register(func):
    """Register a function as a plug-in"""
    print_registry.append(func.__name__)
    return func


@register
def uppercase_decorator(fnc):
    def wrapper(string):

        return fnc(string).upper()

    return wrapper


@uppercase_decorator
def string_word(string):
    return string


@register
def safe_addition(fnc):
    def wrapper(no1, no2):
        if not (isinstance(no1, int) or isinstance(no1, float) and isinstance(no2, int) or isinstance(no1, float)):
            print('the numbers are not ok for addition')
        else:
            return fnc(no1, no2)

    return wrapper


@register
@safe_addition
def addition(number1, number2):
    return number1 + number2


@register
def some_function_one():
    pass


@register
def some_function_two():
    pass


if __name__ == '__main__':
    dataset = generate_dict_from_raw_data()
    pretty_printer = pprint.PrettyPrinter()
    print('Dataset is:')
    pprint.PrettyPrinter().pprint(dataset)

    print('data for each year:')
    pprint.PrettyPrinter().pprint(get_year_data(dataset, '2019'))

    country_data = get_country_data(dataset, 'Romania')
    print('data for a specific country:')
    pprint.PrettyPrinter().pprint(country_data)

    print('Average for the specific data:')
    print(perform_average(country_data['Romania']))

    print('\nDecorators ***********************************\n')

    print(string_word('heLLo World'))
    print(f'the sum is:', addition(4, 1))
    print(f'the sum is:', addition('jk', 1))
    print(f'the list of functions with register as decorator is: ', print_registry)