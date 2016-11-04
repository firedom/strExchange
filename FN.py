import os

def replaceFoldername():
	fileName = os.listdir()
	for i in range(0, len(fileName)):
		print(fileName[i])
		if fileName[i].find(' ') > 0 :
			temp = fileName[i].split(' ')
			temp[0] = temp[0].strip('()')
			temp[1] = temp[1].strip('()')
			output = temp[1] + ' (' + temp[0] + ')'
			os.rename(fileName[i], output)

if __name__ == '__main__':
    replaceFoldername()
