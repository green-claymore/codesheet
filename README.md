# codesheet
Hide your crypto seed phrase or master passwords in a sheet full of randomized words.

Inspired from the colorized notes used in Denmark to help you remember your PIN for your credit cards (https://i.imgur.com/LIpSWu0.jpg).

Instead of just directly writing down your seed phrase for your crypto wallet on a piece of paper, or a password consisting of multiple words (which are safer than conventional passwords, as explained in https://xkcd.com/936/), you can hide the words in a pattern on a sheet full of other random seed words. This way, someone gaining access to your seed note does not mean they will know your seed. You can use the vertical A-Z and horizontal numbering on the sheet as help for forming a pattern which is more easy to remember.

The script requires that you download a words.txt list of seed words which it will then use. Upon running the script, it takes a number of seed words from you as input, in order to remove them from the list of random words, so you can put in your own seed words in the spreadsheet after, without worrying about any doubles.

After running the script the codesheet.xlsx spreadsheet will be available in the folder of the script. You can now open it and format it to landscape, put in your own seed words, and perhaps add a footer with the derivation path, hint or note.

