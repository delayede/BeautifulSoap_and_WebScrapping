from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


URL = ["http://www.data.gov/","http://maps.googleapis.com/maps/api/geocode/json"]



def Task_3():
	
	def get_html(url):
		r = requests.get(url)
		return r
  
	def parser():
		html =  get_html(URL[0])
		print(get_content_3(html.text))


	def get_content_3(html):
		bs = BeautifulSoup(html, 'html.parser')
		number_of_datasets  = bs.find(href="/metrics").text
		return number_of_datasets

	parser()


