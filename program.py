import os
import csv
from class_file import Purchase
import statistics



def main():
    print_header()
    #user_input=get_user_input()

    filepath=get_file_path()
    data=get_real_estate_data(filepath)
    search_data(data)
    # display_results()
    #     pass


def print_header():
    print("---------------------------------------")
    print("           REAL ESTATE APP")
    print("---------------------------------------")

def get_user_input():
    user_input=input("What state would you like to search?")
    pass

def get_file_path():
    base_folder=os.path.dirname(__file__)
    return os.path.join(base_folder, 'SacramentoRealEstateTransactions2008.csv')

def get_real_estate_data(filepath):
    with open (filepath, 'r', encoding='utf-8' ) as fin:
        reader=csv.DictReader(fin)
        purchases=[]
        for row in reader:
            p=Purchase.create_from_dict(row)
            purchases.append(p)
    return purchases



def search_data(data):

    data.sort(key=lambda p: p.price)

    high_purchase= data[-1]
    low_purchase= data[0]
    print('The most expensive house is ${} and has {} beds and {} baths'.format(high_purchase.price, high_purchase.beds, high_purchase.baths))
    print('The least expensive house is ${} and has {} beds and {} baths'.format(low_purchase.price, low_purchase.beds, low_purchase.baths))

    home_prices=(
        pur.price
        for pur in data

    )
    ave_price=statistics.mean(home_prices)
    print('The average home price is {}'.format(round(ave_price)))


if __name__=='__main__':
    main()