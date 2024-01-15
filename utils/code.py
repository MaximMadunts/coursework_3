from utils.func import load_operations, prepare_operation_data


def main():
    '''основной код'''
    operations_data = load_operations("../operations.json")
    executed_operations = [op for op in operations_data if "state" in op and op["state"] == "EXECUTED"]

    last_five_operations = sorted(executed_operations, key=lambda x: x["date"], reverse=True)[:5]

    formatted_operations = [prepare_operation_data(op) for op in last_five_operations]
    formatted_output = "\n\n".join(formatted_operations)

    print(formatted_output)


if __name__ == "__main__":
    main()
