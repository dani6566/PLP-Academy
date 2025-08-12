def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price_after_discount = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price_after_discount == original_price:
    print(f"No discount applied. Original price: ${original_price:.2f}")
else:
    print(f"Final price after discount: ${final_price_after_discount:.2f}")
