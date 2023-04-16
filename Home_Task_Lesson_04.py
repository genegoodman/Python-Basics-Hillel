def func_a(*names):
    list_a = []
    for name in names:
        if name not in names:
            list_a.append(name)
    return list_a

def func_b(**kwargs):
    quantity_of_args = len(kwargs)
    print(quantity_of_args)
    user_type = kwargs.get("user_type", "Student")
    print(user_type)

func_b(name = "Gene")
func_b(name = "Mykyta", user_type = "Teacher")


def func_c(a, b, c=None, *, d, e="Default", f="Default"):
    pass

def func_d(x):
    def func_d_int(y):
        return x * y
    return func_d_int

def print_square(lines, *args):
    print("****")
    if lines == 4:
        return
    else:
        print_square(lines + 1)


print_square(1)






