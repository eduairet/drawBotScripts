# This scripts generates a 900px wide word with a color variation between each letter

# Handy linear interpolation function
def lerp(value1, value2, factor):
    return value1 + (value2 - value1)*factor

# Word design function
def wordDesign(word, myFont):
    #Check the size of the word to fit the canvas
    textSize = FormattedString(word, font=myFont, fontSize=1)
    #Defines the font size
    myFontSize = width() * .9 / textSize.size()[0]
    #Initialize a Formatted String for the word
    tx = FormattedString('', font=myFont, fontSize=myFontSize, align='center')
    # Appends each letter with a smooth color changing
    for i, letter in enumerate(word):
        tx.append(letter, fill=(lerp(0, 1, i/len(word)), 0, 1))
    # Text output
    text(tx, (width()/2, height()/2 + tx.fontDescender()))
    
# Call the function
wordDesign('Yout word', 'Arial')
# Output image
saveImage('~/Desktop/myword.png')
