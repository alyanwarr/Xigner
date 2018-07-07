import os
import unittest
import xmldsig
import sys

def sign(XML):

	result=xmldsig.sign(XML.replace("\n",""),'certs/file.key')
	print result
	
	#print xmldsig.verify(result,'certs/file.key')

if __name__ == '__main__':
    with open("temp.txt", "r") as f:
   
    #for debugging purposes :) 
    
	XML = f.read()

    sign(XML)
