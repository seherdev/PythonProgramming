def calculate_pyramid_height(number_of_blocks):
    height = 0
    remaining_blocks = number_of_blocks


    while remaining_blocks >= height + 1:
        height = height + 1 
        remaining_blocks = remaining_blocks - height 


    return height

print(calculate_pyramid_height(9))
print(calculate_pyramid_height(10))
print(calculate_pyramid_height(11))
print(calculate_pyramid_height(18))