import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

####################### SOUP FUNCTION ####################################

def give_soup(link):
	url = 'https://www.androidcentral.com'+link
	page = requests.get(url)
	soup = BeautifulSoup(page.content,'html.parser')
	return soup

############################ lINKS ########################################
soup = give_soup('')

tags = soup.find_all('a', class_='bullet__link', href=True)

links = []
i=1
for tag in tags:
	links.append(tag['href'])
	i+=1
	if i==5: #number of articles
		break
############################ OPEN LINKS ###################################

for link in links :
	soup = give_soup(link)
	title = soup.find('h1', class_='article-header__title').text
	intro = soup.find('span', class_='article-header__intro').text
	article = soup.find('div', class_='article-body col-3of3 col-2of3@tablet').text

	title_ar = translator.translate(title,dest='ar').text
	intro_ar = translator.translate(intro,dest='ar').text
	article_ar = translator.translate(article,dest='ar').text

	with open('news.txt','a') as f:
		f.write('*'*25+'\n')
		f.write('Link = https://www.androidcentral.com{}\n'.format(link))
		f.write(title_ar.strip()+'\n')
		f.write(intro_ar.strip()+'\n')
		f.write(article_ar.strip()+'\n')




