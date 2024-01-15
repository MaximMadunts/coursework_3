
from datetime import datetime
import json
from pip import main


def load_operations(file_path='operations.json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
    return operations_data


def mask_card_number(card_number):
    masked_number = f"XXXX XX** **** {card_number[-4:]}"
    return masked_number


def mask_account_number(account_number):
    masked_number = f"**{account_number[-4:]}"
    return masked_number


def format_date(date_str):
    date_object = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


def prepare_operation_data(operation):
    formatted_date = format_date(operation["date"])
    masked_from = mask_card_number(operation.get("from", ""))
    masked_to = mask_account_number(operation["to"])

    amount = float(operation["operationAmount"]["amount"])
    currency = operation["operationAmount"]["currency"]["name"]

    formatted_operation = (
        f"{formatted_date} {operation['description']}\n"
        f"{masked_from} -> {masked_to}\n"
        f"{amount} {currency}\n"
    )
    return formatted_operation


if __name__ == "__main__":
    main()
