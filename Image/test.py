#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,Image

if (len(sys.argv) != 4):
        print("usage: " + sys.argv[0] + \
                " maxSize_pixel input_img_dir output_img_dir")
        sys.exit(0)
else:
        maxSide = int(sys.argv[1])
        inputDir = sys.argv[2]
        outputDir = sys.argv[3]

def encodeChinese(msg):
	type = sys.getfilesystemencoding()
	return msg.decode('UTF-8').encode(type)

def judgeSize(im):
	#判断图片分辨率,如果最大边超过1024返回False,如果不超过返回True
        if (max(im.size) > maxSide):
                print("return false")
                return False
        else:
                return True

def changeSize(im):
        wid,hig = im.size
        zoomLevel = 1.0 * max(wid, hig) / maxSide

        if (wid > hig):
	        newimg = im.resize((maxSide, hig / zoomLevel), Image.ANTIALIAS)
        else:
	        newimg = im.resize((wid / zoomLevel, maxSide), Image.ANTIALIAS)
	return newimg

def main():
        errFile = open(outputDir + '/errFile.txt','w')
	for parent,dirnames,filenames in os.walk(inputDir):
		for filename in filenames:
			fName = filename
			filename = parent + os.sep + filename
			fPostfix = os.path.splitext(filename)[1]
			try:
				img = Image.open(filename)
			except:
				print filename
				print encodeChinese('open file error')
				continue
			#img.load()
			print filename
			print fPostfix
			if(fPostfix !='.jpg' and fPostfix !='.png' and fPostfix != '.JPG' and fPostfix != '.PNG'):
				errFile.write(str(filename) + '\n')
				errFile.write(encodeChinese('not a picture, please check again...') + '\n')
				errFile.write('\n')
			else:
				print 'judgeSize()'	
				if(judgeSize(img) == False):
					print 'judgeSize: size to big'
					newimg = changeSize(img)
					newimg.save(outputDir + os.sep + fName)
					print str(outputDir + os.sep + fName) 
					print encodeChinese('save')
	print encodeChinese('done')
	errFile.close()

main()
