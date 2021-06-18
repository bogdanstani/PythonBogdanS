import pprint
from datetime import datetime
from random import choice, randint, uniform
from countrygroups import EUROPEAN_UNION


def get_random_element_from_list(random_list):
    return choice(random_list)


def get_random_tuple_statistic():
    random_country = get_random_element_from_list(EUROPEAN_UNION.names)
    random_year = randint(1990, datetime.now().year)
    random_genre = get_random_element_from_list(['M', 'F'])
    random_health_index = round(uniform(0, 100), 1)

    random_tuple = (random_country, random_year, random_genre, random_health_index)

    return random_tuple


def get_random_list_of_tuple_elements(n=30):
    list_for_statistic = []

    for x in range(n):
        tuple_for_append = get_random_tuple_statistic()
        list_for_statistic.append(tuple_for_append)

    return list_for_statistic


def get_dictionary_by_year(list_of_tuples):
    return {
        year: {
            country: [sex, health_index]
            for country, _, sex, health_index in list_of_tuples if _ == year
        }
        for country, year, sex, health_index in list_of_tuples
    }


def get_country_by_year(list_of_tuples, country_name):
    return {
        year: [sex, health_index]
        for _, year, sex, health_index in list_of_tuples if _ == str(country_name)
    }


def get_country_and_year_same_key(list_of_tuples):
    return {
        country + str(f'_{year}'): [sex, health_index]
        for country, year, sex, health_index in list_of_tuples
    }


def get_dict_with_health_index_greater(list_of_tuples, index_value):
    return {
        health_index: [country, year, sex]
        for country, year, sex, health_index in list_of_tuples if health_index > index_value
    }


def get_health_index_greater_and_genre(list_of_tuples, index_value, genre):
    return {
        health_index: [country, year, sex]
        for country, year, sex, health_index in list_of_tuples if
        health_index > index_value and sex == genre
    }


if __name__ == '__main__':
    list_of_tuples_for_statistic = get_random_list_of_tuple_elements(55)
    print(f'list of tuples is:{list_of_tuples_for_statistic}\n')
    pretty_printer = pprint.PrettyPrinter()

    dict_by_year = get_dictionary_by_year(list_of_tuples_for_statistic)
    print(f'dict by year : ')
    pretty_printer.pprint(dict_by_year)

    dict_Germany_by_year = get_country_by_year(list_of_tuples_for_statistic, 'Germany')
    print(f'Germany : {dict_Germany_by_year}\n')

    dict_Country_and_year = get_country_and_year_same_key(list_of_tuples_for_statistic)
    print(f'Country and year : {dict_Country_and_year}\n')

    dict_health_index_greater_than_5 = get_dict_with_health_index_greater(list_of_tuples_for_statistic, 5)
    print(f'dict_health_index_greater_than_5 : {dict_health_index_greater_than_5}\n')

    dict_health_index_greater_than_5_and_female = get_health_index_greater_and_genre(list_of_tuples_for_statistic, 5,
                                                                                     'F')
    print(f'dict_health_index_greater_than_5_and_female : {dict_health_index_greater_than_5_and_female}')

    print('\nSETS ************************************ \n')

    set1 = {1, 7, 2, 7, 6, 8, 2, 2, 9, 0}
    set2 = {4, 7, 3, 7, 5, 8, 2, 2, 9, 5}

    print(f'set1: {set1}')
    print(f'set2: {set2}\n')

    print(f'union: {set1.union(set2)}')
    print(f'intersection: {set1.intersection(set2)}')
    print(f'difference: {set1.difference(set2)}')
    print(f'symmetric difference: {set1.symmetric_difference(set2)}')