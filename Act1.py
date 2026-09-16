USD_TO_EUR_RATE = 0.87
usd_prices = [12.99, 25.50, 5.00, 99.99, 45.00, 15.75]

print("--- Product Price Conversion (USD to EUR) ---")
for i, usd_price in enumerate(usd_prices, start=1):
    eur_price = usd_price * USD_TO_EUR_RATE
    print(f"Product #{i}: ${usd_price:.2f} USD  -->  €{eur_price:.2f} EUR")
