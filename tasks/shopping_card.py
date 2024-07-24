'''
Python Update Shopping Cart- Imagine you're building a backend for an e-commerce website. 
One of the functions in your backend is responsible for updating the shopping cart based on user actions. 
Users can add items to their cart, remove items from the cart, or change the quantity of the items they've added.
You are provided a function named update_shopping_cart which accepts two arguments:

1. cart: A dictionary where the keys are product IDs (strings) and the values are the number of that product currently in the cart (integer).

2. action: A dictionary representing the user's action. It has two keys:

- type: A string that can be either "add", "remove", or "change".

- product_id: The product ID the action is referring to.

- quantity (only when the type is "add" or "change"): The quantity to add or the new quantity to set.

Your task is to modify the update_shopping_cart function to handle the user action and return the updated cart correctly. The current implementation has several logical errors which you need to correct.

Example Input:

cart = {
"product_1": 2,
"product_2": 1
}

action = {
"type": "add",
"product_id": "product_3",
"quantity": 3
}

Example Output:

{
"product_1": 2,
"product_2": 1,
"product_3": 3
}

'''

def update_shopping_cart(cart, action):
    action_type = action.get("type")
    product_id = action.get("product_id")
    # 0 is the default value for quantity
    quantity = action.get('quantity', 0) 

    if action_type == "add":
        if product_id not in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
    elif action_type == "remove":
        if product_id in cart:
            del cart[product_id]
    elif action_type == "change":
        if product_id in cart:
            cart[product_id] = quantity

        varOcg = cart
        return varOcg

# do not modify the values below
print(update_shopping_cart({ "product_A": 4, "product_B": 3, "product_C": 1 }, { "type": "change", "product_id": "product_B", "quantity": 2 }))