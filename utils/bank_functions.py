import json
from datetime import datetime


def open_file():
    with open('../operations.json') as f:
        data = json.load(f)
        return data


def filter_and_sort_transactions(data):
    filtered_list = [
        dictionary for dictionary in data
        if dictionary.get('state') is not None and dictionary.get('state') == 'EXECUTED'
    ]

    last_transactions = sorted(
        filtered_list,
        key=lambda x: datetime.strptime(x.get('date', '2018-01-21T01:10:28'), '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=True
    )[:5]
    return last_transactions


def print_transactions(last_transactions):
    for tx in last_transactions:
        value = tx.get('from') if tx.get('from') is not None else ''
        if value == '':
            from_masked = ''
        else:
            if value.startswith('Счет'):
                from_masked = mask_bill(value)
            else:
                from_masked = mask_from(value)
        to_masked = mask_bill(tx.get('to'))
        operation_date = datetime.strptime(tx['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        print("{} {}".format(operation_date, tx['description']))
        print("{} -> {}".format(from_masked, to_masked))
        print("{} {}\n".format(tx['operationAmount']['amount'], tx['operationAmount']['currency']['name']))


def mask_bill(value):
    return "Счет **{}".format(value[-4:])


def mask_from(value):
    words = ''.join([i for i in value if not i.isdigit()])
    card_number = ''
    for m in value:
        if m.isdigit():
            card_number = card_number + m
    masked_card_number = '{} {}{} **** {}'.format(card_number[:4], card_number[4:6], '**', card_number[-4:])
    masked_from = words + masked_card_number
    return masked_from


def main():
    data = open_file()
    last_transactions = filter_and_sort_transactions(data)
    print_transactions(last_transactions)


if __name__ == '__main__':
    main()
