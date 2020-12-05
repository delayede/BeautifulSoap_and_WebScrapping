from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

HOST ="https://www.python.org/"
URL = "https://www.python.org/"
HEADERS ={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36" 
}

def get_html(url):
    r = requests.get(url, headers = HEADERS)
    return r
  

def parser():
	html =  get_html(URL)
	print(get_content(html.text))


def get_content(html):
	bs = BeautifulSoup(html, 'html.parser')
	title = bs.find("title").text
	p = bs.find_all("p")
	p_len = len(bs.find_all("p"))
	p_text = bs.find("p").text
	h_text_len= len(bs.find("h2").text)
	c_text = bs.find("a").text
	a_href = bs.find("a").attrs['href']
	urls = []
	for s in bs.find_all('li'):
		a = s.find('a')
		urls.append(a.attrs['href'])

	h2= bs.find_all('h2')[0:4]
	a =	bs.find_all('a')[0:10]

	h1_to_h3 =[]
	for heading in bs.find_all(["h1", "h2", "h3"]):
		h1_to_h3.append(heading.name + ' ' + heading.text.strip())

	all_text = bs.get_text()

	tags = []
	for child in bs.recursiveChildGenerator():
		if child.name:
			tags.append(child.name)


	root_childs = [t.name for t in bs.html.descendants if t.name is not None]

	task_16 = (bs.title ,bs.title.text , bs.title.parent)

	"""
	str1 = bs.find_all(string=re.compile('Python'))
	for text in str1:
		print(" ".join(text.split()))
	"""
	id_19 = bs.find(id ="python-network")

	first_tag = bs.find(href="/dev/peps/peps.rss")
	beneath_tag = bs.select("html body h2")
	Tags_CSS = bs.select(".say-no-more")


	return Tags_CSS



parser()