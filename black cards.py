from PIL import Image, ImageFont, ImageDraw
#make image
img = Image.new('RGBA',(818,1170),color = 'black')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("helvetica bold.ttf", 80)
#collect input
inputText = input("Type here what should go on the card: ")
#test

splitTextBySpaceList = inputText.split()
splitTextBySpaceString = ''
splitTextAfterSort = [] #array that holds the words that were split

#wrap around
for x in range(len(splitTextBySpaceList)):
	if (len(splitTextBySpaceString + splitTextBySpaceList[x]) < 16):
		splitTextBySpaceString = splitTextBySpaceString + splitTextBySpaceList[x] + ' ' #when the amount of characters in the current array is less than 16, add them together

	else:
		splitTextAfterSort.append(splitTextBySpaceString)								#else add them to the splitted text array
		splitTextBySpaceString = splitTextBySpaceList[x] + ' '

	if x == len(splitTextBySpaceList) - 1:												#if this is the last loop, append it
		splitTextAfterSort.append(splitTextBySpaceString)

#put all text into one string
cardText = ''
for i in range(len(splitTextAfterSort)):
	if i == 0:
		cardText = splitTextAfterSort[i] + '\n'
	else:
		cardText = cardText + splitTextAfterSort[i] + '\n'

#draw text
draw.text((50, 50),cardText,(255,255,255),font=font)
table = str.maketrans(dict.fromkeys('\/:*"\<>|?'))
titleText = inputText.translate(table)
img.save("cards/" + titleText + '.png')
