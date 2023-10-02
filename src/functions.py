import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filter_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_sort_data(data):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:5]


def get_format_data(data):
    format_data = []
    for value in data:
        value["date"] = value["date"].replace("T", " ")
        value["date"] = datetime.strptime(value["date"], "%Y-%m-%d %H:%M:%S.%f")
        value["date"] = value["date"].strftime('%d.%m.%Y')
        if 'from' in value:
            if len([int(i) for i in value['from'] if i.isdigit()]) == 16:
                from_card = value['from'].split()[-1]
                secret_card = value['from'].split()[0] + ' ' + from_card[:4] + ' ' + from_card[5:7] + '**' + ' ' + '****' + ' ' + from_card[-4:]
            else:
                from_card = value['from'].split()[-1]
                secret_card = value['from'].split()[0] + ' ' + '*' * len(from_card[6:-4]) + from_card[-4:]
            if len([int(i) for i in value['to'] if i.isdigit()]) == 16:
                to_from_card = value['to'].split()[-1]
                to_secret_card = value['to'].split()[0] + ' ' + to_from_card[:6] + '*' * len(to_from_card[6:-4]) + to_from_card[-4:]
            else:
                to_from_card = value['to'].split()[-1]
                to_secret_card = value['to'].split()[0] + ' ' + '*' * len(to_from_card[6:-4]) + to_from_card[-4:]
            format_data.append(f"""\
{value["date"]} {value["description"]}
{secret_card} -> {to_secret_card}
{value["operationAmount"]["amount"]} {value["operationAmount"]["currency"]["name"]}""")
        else:
            if len([int(i) for i in value['to'] if i.isdigit()]) == 16:
                 to_from_card = value['to'].split()[-1]
                 to_secret_card = value['to'].split()[0] + to_from_card[:6] + '*' * len(to_from_card[6:-4]) + to_from_card[-4:]
            else:
                 to_from_card = value['to'].split()[-1]
                 to_secret_card = value['to'].split()[0] + ' ' + '*' * len(to_from_card[6:-4]) + to_from_card[-4:]
            format_data.append(f"""\
{value["date"]} {value["description"]}
{to_secret_card}
{value["operationAmount"]["amount"]} {value["operationAmount"]["currency"]["name"]}""")
    return format_data




