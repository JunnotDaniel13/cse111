import math


manufactured_items = int(input("Enter the manufactured items: "))
items_in_box = int(input("Enter the number of items in a box: "))

boxes = manufactured_items / items_in_box

print(math.ceil(boxes))
