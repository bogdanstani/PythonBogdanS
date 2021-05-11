from random import choice, random, randint


def get_random_type_article():
    article = ['shirt', 'scarf', 'glove', 'heat', 'pants']
    return choice(article)


def get_random_size_article():
    size = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
    return choice(size)


def get_random_list_of_articles(n):
    list_articles = []

    for x in range(n):
        list_articles.append([get_random_type_article(), get_random_size_article()])

    return list_articles


def sell_last_article(list_for_delete_last_element):
    list_for_delete_last_element.pop()

    return list_for_delete_last_element


def sell_any_article_by_type_and_size(list_for_delete_any_element, article_type, size):
    if [article_type, size] in list_for_delete_any_element:
        list_for_delete_any_element.remove([article_type, size])
    else:
        print(f'the article', [article_type, size], 'was not found to be deleted')

    return list_for_delete_any_element


def sell_any_article_by_position(list_for_delete_any_position_element, n):
    if 0 <= n < len(list_for_delete_any_position_element):
        list_for_delete_any_position_element.pop(n)

    return list_for_delete_any_position_element


def add_article(list_for_add_article, article_type, size):
    list_for_add_article.append([article_type, size])

    return list_for_add_article


if __name__ == '__main__':
    print(get_random_type_article())
    print(get_random_size_article())

    try:
        number_of_articles = int(input('Please insert the number of articles (should be an positive integer)'))

    except:
        number_of_articles = randint(10, 20)
        print('you have not enter an integer , so the number of articles was chosen randomly and it is :' + str(
            number_of_articles))

    list_of_elements = get_random_list_of_articles(number_of_articles)

    print(f'the list of articles is :', list_of_elements)
    print(f'the list of articles after selling the last one is:', sell_last_article(list_of_elements))
    print(f'selling ',
          sell_any_article_by_type_and_size(list_of_elements, get_random_type_article(), get_random_size_article()))
    # print(sell_any_article_by_position(list_of_elements, -3))
    # print(sell_any_article_by_position(list_of_elements, 0))

    list_of_elements = add_article(list_of_elements, get_random_type_article(), get_random_size_article())
    print(f'final list of elements after add', list_of_elements)








