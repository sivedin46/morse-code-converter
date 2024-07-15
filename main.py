import pandas as pd

morse = pd.read_csv("morse.csv")
my_dict = dict(zip(morse.Letter, morse.Morse))
print(my_dict)


def converter():
    while True:
        my_string = input(f"Please enter the sentences that you want to convert for morse.A-Z,0-9 enter 'q' for quit: ").upper()
        output_list = []
        if my_string == "Q":
            break
        else:
            for letter in my_string:
                try:
                    output_list.append(my_dict[letter])
                except KeyError:
                    output_list.append('/')
            print(output_list)

converter()
