# codesheet

Hide your crypto seed phrase or master passwords in a sheet full of randomized words for better security.

Inspired from the colorized notes used in Denmark to help you remember your PIN for your credit cards: https://i.imgur.com/LIpSWu0.jpg.

Instead of just directly writing down your seed phrase for your crypto wallet or password manager on a piece of paper, you can hide the words in a pattern of your choice on a sheet full of other random seed words. This way, someone gaining access to your seed note will not necessarily know your seed. You can use the vertical A-Z and horizontal numbering on the sheet as help for forming a pattern you can remember.

When running the Python script, it takes your seed words as inputs (in no particular order), in order to remove them from the list of random words, so you can put in your seed words manually afterward and avoid duplicate words. It also gives you the option of adding a custom note in the footer, which could be useful for stating the crypto's derivation path, or which wallet the seed has worked with before.

After running the script, the generated codesheet.xlsx spreadsheet will be ready in the folder of the script. You can now open it and put in your own seed words.

Default formatting of the codesheet is landscape, with grid on.
