# def is_odd(n):
#     return n % 2 == 1
#
# print(is_odd(12))

# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(is_leapyear(2100))

# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i,total)
#
# print_triangular_numbers(5)

# def is_prime(n):
#     if n < 2:
#         return False
#
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(13))

# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("helloworld"))


# def remove_all(text, remove):
#     return text.replace(remove, "")
#
# print(remove_all("Hello world", "l"))

# def substitute(message,key):
#     alphabet = "abcdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtgdjeopwmkunbhsğiştuqertnzxs"
# print(substitute("Hello, World", key))

# def remove_dups(text):
#     result = ""
#     for ch in text:
#         if ch not in result.lower():
#             result = result + ch
#     return result
#
# print(remove_dups("Hello World"))

