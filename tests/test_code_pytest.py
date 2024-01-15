from utils.func import mask_card_number, format_date, prepare_operation_data


def test_mask_card_number():
    card_number = "1234567890123456"
    masked_number = mask_card_number(card_number)
    assert masked_number == "XXXX XX** **** 3456"


def test_format_date():
    date_str = "2022-01-15T12:30:45.678"
    formatted_date = format_date(date_str)
    assert formatted_date == "15.01.2022"


def test_prepare_operation_data():
    operation = {
        "date": "2022-01-15T12:30:45.678",
        "from": "1234567890123456",
        "to": "987654321",
        "operationAmount": {"amount": "100.0", "currency": {"name": "USD"}},
        "description": "Sample Operation"
    }

    formatted_operation = prepare_operation_data(operation)
    expected_result = (
        "15.01.2022 Sample Operation\n"
        "XXXX XX** **** 3456 -> **4321\n"
        "100.0 USD\n"
    )

    assert formatted_operation == expected_result
