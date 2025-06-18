"""
Get the Middle Character --> 7kyu
"""
# def get_middle(s):
#     if len(s) % 2 == 0:
#         middle = int(len(s) / 2)
#         return s[middle-1:middle+1]
#     return s[len(s) // 2]
#
# print(get_middle("test"))
# print(get_middle("testing"))

""" 
Consecutive strings --> 6kyu
"""
# def longest_consec(strarr, k):
#     if k <= 0 or k > len(strarr):
#         return ""
#     max_len = 0
#     longest = ""
#     for i in range(len(strarr) - k + 1):
#         current = ''.join(strarr[i:i + k])
#         if len(current) > max_len:
#             max_len = len(current)
#             longest = current
#     return longest
# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],2))

"""
Invert values --> 8kyu
"""
# def invert(lst):
#     result = []
#     for item in lst:
#         if item > 0:
#             result.append(int(f"-{item}"))
#         else:
#             r = ""
#             for i in str(item):
#                 if i != "-":
#                     r += i
#             result.append(int(r))
#     return result
# print(invert([1,2,3,4,5,-6,7]))

"""
Snail --> 4kyu
"""
# def snail(snail_map):
#     res = []
#     while snail_map:
#         res += snail_map.pop(0)
#         for row in snail_map:
#             if row:
#                 res.append(row.pop())
#         if snail_map:
#             res += snail_map.pop()[::-1]
#         for row in reversed(snail_map):
#             if row:
#                 res.append(row.pop(0))
#     return res
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# print(snail(array))
