import urllib

file_path = #put the file path of the .txt file you would like to read

def read_text():
	text = open("file_path")
	contents = text.read()
	print(contents)
	text.close()
	check_profanity(contents)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()


read_text()