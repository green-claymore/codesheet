import xlsxwriter
import string

# /// Take seed words as input from user, in no particular order
print("Please enter the LENGTH of your seed phrase as a number:")
seed_length = int(input())

seed = list()
print("Please enter your " + str(seed_length) + " seed words one by one, in no particular order:")
for n in range(0, seed_length):
    seed.append(input())

if len(seed) != len(set(seed)):
    print("You inputted at least one of your seed words twice! \nPlease try again")
    exit()
print("Thank you, " + str(len(seed)) + " seed words were recorded. They are:")
print(seed)

# /// Start spreadsheet

workbook = xlsxwriter.Workbook('codesheet.xlsx')
worksheet = workbook.add_worksheet()

# generate numbers and letters

string_letters = list(string.ascii_uppercase)
string_numbers = list(range(len(string_letters)))

# enter numbers in top row
for x in range(len(string_numbers) - 1):
    worksheet.write(str(string_letters[x + 1]) + '1', str(string_numbers[x]))

# enter letters in left column
for y in range(len(string_letters)):
    worksheet.write('A' + str(string_numbers[y] + 2), str(string_letters[y]))

# collect bip39 seed words from online
# words_url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'


# import local words.txt file as list, this works

with open('words.txt', 'r') as f:
    words_import = [line.rstrip() for line in f]

words_set = set(words_import)
words = list(words_set)

# /// Check and remove your inputted seed words from list of words ///

words_cleaned = [entry for entry in words if entry not in seed]

print("Removed " + str(len(words) - len(words_cleaned)) + " of the inputted seed word(s) from list of seed words.")

seed.clear()


# /// Enter random seed words in rest of spreadsheet ///

d = 0
for b in range(1, len(string_letters)):
    for c in range(len(string_numbers)):
        worksheet.write(string_letters[b] + str(string_numbers[c] + 2), words_cleaned[d])  # + '-' + str(ran_num[d]))
        d = d + 1

workbook.close()

print("Code sheet generated!")
print("You can now open the generated codesheet.xlsx file and put in your own seed words in a pattern you can remember.")
print("Feel free to format the spreadsheet to your liking (landscape A4, font size, etc.) before printing.")
