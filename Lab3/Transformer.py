import json

def get_product_names():
    while True:
        user_input = input("Enter product names (comma-separated): ").strip()
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue
        names = [name.strip() for name in user_input.split(',')]
        names = [name for name in names if name]
        if len(names) == 0:
            print("Error: No valid product names entered. Please try again.")
            continue
        return names

def get_product_prices(count):
    while True:
        user_input = input(f"Enter {count} product prices (comma-separated): ").strip()
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue
        try:
            prices = [float(price.strip()) for price in user_input.split(',')]
            if len(prices) != count:
                print(f"Error: Expected {count} prices, but got {len(prices)}. Please try again.")
                continue
            return prices
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers separated by commas.")

def process_products(names, prices):
    paired_products = list(zip(names, prices))
    print(f"Paired {len(paired_products)} products with prices")
    filtered_products = list(filter(lambda x: x[1] > 0, paired_products))
    print(f"Filtered to {len(filtered_products)} valid products (price > 0)")
    def transform_func(x):
        return {
            "product": x[0],
            "price": x[1],
            "discounted": round(x[1] * 0.9, 2)
        }
    transformed_products = list(map(transform_func, filtered_products))
    print("Applied 10% discount to all products")
    return transformed_products

def save_to_json(products):
    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(products, file, indent=2)
    print(f"Saved {len(products)} products to 'products.json'")

def preview_products(products, limit=5):
    print(f"Preview of first {min(limit, len(products))} products:")
    print("="*60)
    for i, product in enumerate(products[:limit], 1):
        print(f"{i}. {product['product']}")
        print(f"   Original Price: ${product['price']:.2f}")
        print(f"   Discounted Price: ${product['discounted']:.2f}")
        print("-"*60)

def execute_task():
    print("PRODUCT DATA TRANSFORMER")
    names = get_product_names()
    print(f"Received {len(names)} product names")
    prices = get_product_prices(len(names))
    print(f"Received {len(prices)} product prices")
    products = process_products(names, prices)
    save_to_json(products)
    if products:
        preview_products(products, limit=5)
    else:
        print("No valid products to display (all prices were <= 0)")
