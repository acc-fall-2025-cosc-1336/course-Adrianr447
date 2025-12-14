class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    # Table 1 data
    return [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft"),
    ]


def display_stock_list(stocks):
    print("\nStock Report")
    print(f"{'Company':<15} {'Symbol':<10}")
    for s in stocks:
        print(f"{s.get_company_name():<15} {s.get_symbol():<10}")


def main():
    while True:
        stocks = get_stock_list()

        print("\n1-Display stock purchase history")
        print("2-Exit")
        option = input("Select option: ").strip()

        if option == "1":
            display_stock_list(stocks)
        elif option == "2":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
