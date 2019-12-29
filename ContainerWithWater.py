def ContainerWithWater(arr):
    if len(arr) < 2:
        return -1
    start = 0
    end = len(arr) - 1
    max_product = 0
    while(start < end):
        prod = min(arr[end], arr[start]) * (end - start)
        # max_product = max(max_product, prod)
        if prod > max_product:
            max_product = prod
        if arr[end] < arr[start]:
            end -= 1
        else:
            start += 1
    return max_product
    
