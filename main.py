# Find the index of elements that meet a condition in Python

my_list = [4, 8, 12, 16, 25]

indexes = [
    index for index in range(len(my_list))
    if my_list[index] > 10
]

print(indexes)  # 👉️ [2, 3, 4]