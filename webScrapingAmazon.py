from re import I
from attr import attr
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1024,768')

url = webdriver.Chrome(options=options)

url.get("https://www.amazon.com.br/gp/bestsellers/books/ref=sv_b_1?pf_rd_r=9JNHFE5EJRVNVRNNWDCH&pf_rd_p=1714fbf5-98d9-40d3-afe2-4c5513980b24&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_s=merchandised-search-2&pf_rd_t=30901&pf_rd_i=6740748011")

site = BeautifulSoup(url.page_source, 'html.parser')

livro = site.findAll("div", attrs = {'class':'a-column a-span12 a-text-center _p13n-zg-list-grid-desktop_style_grid-column__2hIsc'})

livrosmaisvendidos = []
for livros in livro: 
    
    titulo = livros.find('div', attrs = {'class':'_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y'})

    print(titulo.text)

    autor = livros.find('div', attrs ={'class':'a-row a-size-small'})
    #print(autor.text)

    preco = livros.find('span', attrs={'class':'_p13n-zg-list-grid-desktop_price_p13n-sc-price__3mJ9Z'})
    #print(preco.text)
    link = livros.find('a', attrs = {'class':'a-link-normal a-text-normal'})
    print(link['href'])

    livrosmaisvendidos.append([titulo.text,autor.text,preco.text, link['href']])
AmazonLivros = pd.DataFrame(livrosmaisvendidos, columns=["Título", "Autor", "Preço","Link"])
AmazonLivros.to_csv('AmazonLivros.xlsx', index=False)