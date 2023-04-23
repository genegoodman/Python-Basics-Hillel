lst = [
    1, 2, [3, 4, [5, 6]]
]
def sum_of_numbers(lst):
    sum = 0
    for item in lst:
        if isinstance(item, int):
            sum += item
        else:
            sum += sum_of_numbers(item)
    return sum

print(sum_of_numbers(lst))


words =  ['one', 'two', 'three', 'four']
length = 7
def repeat_words(words, length):
    repetitions = length // len(words)
    remainder = length % len(words)
    result = [words[i] for i in range(len(words))] * repetitions
    result += [words[i] for i in range(remainder)]
    return result

print(repeat_words(words, length))



import random
import string
import time


PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))
print("Generated password:", PASSWORD)


def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return

        time.sleep(0.1)

def password_cracker():
    alphabet = string.ascii_letters
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    guess = a + b + c + d
                    if guess == PASSWORD:
                        return guess

print(f"Cracked password: {password_cracker()}")









