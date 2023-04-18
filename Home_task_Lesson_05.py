var1 = "verylongstring"

reverse_string = "Desserts" [::-1]
print(reverse_string)

var2 = len(var1)

var3 = list(var1.strip(" "))
print(var3)

var4 = "|".join(var3[2::3])
print(var4)

def func_count(var1): #count method
    dict = {}
    for symbol in var1:
        dict[symbol] = var1.count(symbol)
    return dict

def func_no_count(var1): #no count method
    dict = {}
    for symbol in var1:
        if symbol not in dict:
            dict[symbol] = 0
        dict[symbol] += 1
    return dict

print(func_count(var1))
print(func_no_count(var1))



s1 = "short string"
s2 = "medium string"
s3 = "loooooong string"
list_of_strings = [s1, s2, s3]

def func_str_list(list_of_strings):
    longest_str = ""
    for s in list_of_strings:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str

longest = func_str_list(list_of_strings)
print(f"The longest string is a: {longest}")



string = "1/3/2"
divider = "/"
def divide_and_glue(string, divider):
    word_list = string.split(divider)
    sorted_list = sorted(word_list)
    return divider.join(sorted_list)

print(divide_and_glue(string, divider))



provided_list = [104, 114, 121, 115, 116, 111, 115, 32, 118, 111, 115, 107, 114, 101, 115]

def ascii_to_string(provided_list):
    x = ''.join(chr(num) for num in provided_list)
    return (x)

print(ascii_to_string(provided_list))






