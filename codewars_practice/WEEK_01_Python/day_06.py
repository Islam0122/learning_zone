"""
Is this a triangle? --> 7kyu
"""
# def is_triangle(a, b, c):
#     return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

"""
Directions Reduction --> 5kyu
"""
# def dir_reduc(arr):
#     opposite = {
#         "NORTH": "SOUTH",
#         "SOUTH": "NORTH",
#         "EAST": "WEST",
#         "WEST": "EAST"
#     }
#
#     stack = []
#
#     for direction in arr:
#         if stack and stack[-1] == opposite[direction]:
#             stack.pop()
#         else:
#             stack.append(direction)
#
#     return stack


