var_1 = 3
var_2 = 2
var_3 = var_1 == var_2
print(var_3)
PI = "3.14"

line = float(PI),str(var_1 - var_2)
print(line)

list = [(var_1),(var_2), (var_3), (PI)]
print(list)

my_set = set(list)
print(my_set)

tuple_1 = ("uno", "dos", "tres")
tuple_2 = ("ein", "zwei", "drei")
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

tuple_to_list = [*tuple_3]
print(tuple_to_list)

print()
dict = {
    "Date": 1996,
    150:200,
    100: "Score",
    True: None,
    False: ['l', 'i', 's', 't'],
    3.15: {'key': 'value', 1: 2},
    ("uno", "dos", "tres"):("ein", "zwei", "drei")
}

print(dict)