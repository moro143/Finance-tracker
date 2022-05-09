from src import main
import argparse

parser = argparse.ArgumentParser(description='Finance tracker')
parser.add_argument('-u', '--users', action='store_true', help='Shows users')
parser.add_argument('-c', '--categories', action='store_true', help='Shows categories')
parser.add_argument('-t', '--transactions', action='store_true', help='Shows transactions')

args = vars(parser.parse_args())

if __name__=="__main__":
    if args['users']:
        main.get_users()
    if args['categories']:
        main.get_categories()
    if args['transactions']:
        main.get_transactions()