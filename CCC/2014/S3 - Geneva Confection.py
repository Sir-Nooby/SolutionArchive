#Problem S3: The Geneva Confection - 2014 (SirNooby)
tests = int(input())

for i in range(tests):
    
    cart_order = []

    stack = []

    current = 1
    
    carts = int(input())
    
    for v in range(carts):
        cart = int(input())
        cart_order.append(cart)
    
    while True:
        if len(cart_order) == 0 and len(stack) == 0:
            print("Y")
            break
        elif cart_order and cart_order[-1] == current: #Pass the cart in
            cart_order.pop(-1)
            current += 1
        elif stack and stack[-1] == current: #Pass from storage
            stack.pop(-1)
            current += 1
        elif cart_order and cart_order[-1] != current: #Storage
            stack.append(cart_order[-1])
            cart_order.pop(-1)
        else:
            print("N")
            break
        
        