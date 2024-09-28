USD = "USD"
EUR = "EUR"
CAD = "CAD"
currencies = (USD, EUR, CAD)
exchange_rates = {
    USD: { EUR: 0.74, CAD: 1.31 },
    EUR: { USD: 1.36, CAD: 1.48 },
    CAD: { USD: 0.76, EUR: 0.68 }
}

def select_currency(target: str) -> str:
    while True:
        message = f"{target} currency (USD/EUR/CAD): "
        selected_currency = input(message).upper()
        if selected_currency in currencies:
            return selected_currency
        else:
            print("Invalid currency")

def select_amount() -> int:
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount")
    
    
def convert_currency(amount, source_currency, target_currency) -> float:
    if source_currency == target_currency:
        return amount
    exchange_rate = exchange_rates[source_currency][target_currency]
    
    if exchange_rate:
        return amount * exchange_rate
    else:
        return "Exchange rate not available"
    

def main():
    amount = select_amount()
    source_currency = select_currency(target="Source")
    print(source_currency)
    target_currency = select_currency(target="Target")
    result = convert_currency(amount=amount, source_currency=source_currency, target_currency=target_currency)
    print(f"{amount} {source_currency} is equal to {result:.2f} {target_currency}")
    
    
if __name__ == "__main__":
    main()