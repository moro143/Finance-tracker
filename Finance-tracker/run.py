from src import main
import argparse

parser = argparse.ArgumentParser(description='Finance tracker')
parser.add_argument('-O', '--Output', action='store_true', help='Outputs informations')
parser.add_argument('-I', '--Insert', action='store_true', help='Inserts new informations')
parser.add_argument('-u', '--users', action='store_true', help='Shows users')
parser.add_argument('-c', '--categories', action='store_true', help='Shows categories')
parser.add_argument('-t', '--transactions', action='store_true', help='Shows transactions')


args = vars(parser.parse_args())

if __name__=="__main__":
    if args['Output']:
        if args['users']:
            main.get_data('users', ['user_id', 'name', 'created_on'])
        if args['categories']:
            main.get_data('categories', ['category_id', 'name', 'created_on'])
        if args['transactions']:
            main.get_data('Finances', ['transaction_id', 'money', 'user_id', 'category_id', 'created_on'])
    elif args['Insert']:
        if args['users']:
            user = input('User name: ')
            main.insert_data('users', {'name': user})
        if args['categories']:
            category = input('Category name: ')
            main.insert_data('categories', {'name': category})
        if args['transactions']:
            user_id = input('User id: ')
            category_id = input('Category id: ')
            money = input('Money: ')
            main.insert_data('finances', {'money': money, 'user_id': user_id, 'category_id': category_id})