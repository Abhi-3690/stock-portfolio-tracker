# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}


def calculate_investment(stock, quantity):
    """Calculate investment for a stock."""
    return stock_prices[stock] * quantity


def main():
    print("=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    total_investment = 0
    portfolio = []

    print("\nAvailable stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        investment = calculate_investment(stock, quantity)
        total_investment += investment

        portfolio.append((stock, quantity, stock_prices[stock], investment))

        print(f"✅ Added {quantity} shares of {stock}.")
        print(f"Investment: ${investment:,.2f}")

    print("\n" + "=" * 45)
    print("             PORTFOLIO SUMMARY")
    print("=" * 45)

    if not portfolio:
        print("No stocks were added.")

    else:
        print(f"{'Stock':<10}{'Qty':<10}{'Price':<12}{'Value':<12}")
        print("-" * 45)

        for stock, quantity, price, investment in portfolio:
            print(
                f"{stock:<10}"
                f"{quantity:<10}"
                f"${price:<11,.2f}"
                f"${investment:<11,.2f}"
            )

        print("-" * 45)
        print(f"Total Investment: ${total_investment:,.2f}")

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()