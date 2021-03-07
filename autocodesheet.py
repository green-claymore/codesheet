import xlsxwriter
import string
import urllib.request

# /// Input seed words as input from user, in no particular order
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
worksheet.set_landscape()
worksheet.hide_gridlines(0)
# worksheet.set_column(0, 0, 3)
# worksheet.set_column(1, 15, 8)

# Center first column and set its width
new_format = workbook.add_format()
new_format.set_align('center')
worksheet.set_column('A:A', 2, new_format)

# Decrease font size of words and set column width
cell_format = workbook.add_format()
cell_format.set_font_size(10)
worksheet.set_column('B:M', 7, cell_format)

# Center first row and return font size of it
cell_format = workbook.add_format()
cell_format.set_font_size(11)
cell_format.set_align('center')
worksheet.set_row(0, None, cell_format)


# /// Input footer note

print("Do you want to add a note in the footer of the codesheet? \n Enter y/n:")
footer_preference = str(input())
if footer_preference == "y":
    print("Please input your desired footer note:")
    footer_note = str(input())
    worksheet.set_footer(footer_note)

# generate numbers and letters

string_letters = list(string.ascii_uppercase)
string_numbers = list(range(len(string_letters)))
string_numbers_short = string_numbers[0:13]

# enter numbers in first row
for x in range(len(string_numbers_short) - 1):
    worksheet.write(str(string_letters[x + 1]) + '1', str(string_numbers_short[x]))

# enter letters in first column
for y in range(len(string_letters)):
    worksheet.write('A' + str(string_numbers[y] + 2), str(string_letters[y]))

# collect bip39 seed words from online

words_url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'

data = urllib.request.urlopen(words_url)
words = [line.rstrip() for line in data]

for x in range(len(words)):
    words[x] = words[x].decode('utf-8')

words_set = set(words)
words = list(words_set)

# /// Check and remove manually inputted seed words from list of words ///

words_cleaned = [entry for entry in words if entry not in seed]
print("Removed " + str(len(words) - len(words_cleaned)) + " of the inputted seed word(s) from list of seed words.")
seed.clear()


# /// Enter random seed words in rest of spreadsheet ///

d = 0
for b in range(1, len(string_numbers_short)):
    for c in range(len(string_numbers)):
        worksheet.write(string_letters[b] + str(string_numbers[c] + 2), words_cleaned[d])
        d = d + 1

workbook.close()

print("Code sheet generated!")
print("You can now open the generated codesheet.xlsx file and put in your own seed words in a pattern you can remember.")

# by green_claymore
# March 2021
#
# bitcoincash:qrzvg2sm7lhmzmy7h4qayr2mw2ju73aj0gt3kj8cz6
#
