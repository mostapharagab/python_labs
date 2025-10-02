import json



def run_product_data_transform():
    def user_input():
        while True:
            try:
                products_names_list = input("Enter product names (comma-separated): ").split(",")
            except Exception:
                print("Invalid product names list. Try again.")
                continue

            try:
                products_prices_list = list(map(float, input("Enter product prices (comma-separated): ").split(",")))
                if len(products_prices_list) != len(products_names_list):
                    raise Exception("Lists have different lengths.")
                return products_names_list, products_prices_list
            except Exception:
                print("Invalid product prices list. Try again.")

    product_names, product_prices = user_input()


    pairs = list(zip(product_names, product_prices))
    pairs = list(filter(lambda x: x[1] > 0, pairs))

    products_lst = list(map(lambda x: {
        "product": x[0].strip(),
        "price": x[1],
        "discounted": round(x[1] * 0.9, 2)
    }, pairs))


    with open("products.json", "w") as file:
        json.dump(products_lst, file, indent=2)


    print("\nPreview of first 5 products:")
    print(json.dumps(products_lst[:5], indent=2))
