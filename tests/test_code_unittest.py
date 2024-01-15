import unittest
import json
from utils.func import load_operations, mask_card_number, mask_account_number, format_date, prepare_operation_data


class TestYourFunctions(unittest.TestCase):

    def test_load_operations(self):

        data = [{"key": "value"}]
        with open('test_operations.json', 'r', encoding='utf-8') as file:
            json.dump(data, file)

        # Проверьте, что функция load_operations возвращает ожидаемые данные
        loaded_data = load_operations('test_operations.json')
        self.assertEqual(loaded_data, data)

    def test_mask_card_number(self):

        card_number = "1234567890123456"
        masked_number = mask_card_number(card_number)
        self.assertEqual(masked_number, "XXXX XX** **** 3456")

    def test_mask_account_number(self):

        account_number = "123456789"
        masked_number = mask_account_number(account_number)
        self.assertEqual(masked_number, "**6789")

    def test_format_date(self):

        date_str = "2022-01-15T12:30:45.678"
        formatted_date = format_date(date_str)
        self.assertEqual(formatted_date, "15.01.2022")

    def test_prepare_operation_data(self):

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

        self.assertEqual(formatted_operation, expected_result)


if __name__ == '__main__':
    unittest.main()
