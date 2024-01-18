def calculate_total_price(selected_items):
    total_price = 0

    for item in selected_items:
        # Assuming each item in selected_items has a 'price' attribute
        total_price += item.get('price', 0)

    return total_price

