import requests
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import sqlite3
import webbrowser
from database import save_to_database

from gui import create_gui

def searchGithub(github_user):
    url = 'https://github.com/' + github_user + "?tab=repositories"

    r = requests.get(url)
    soup = bs(r.text, 'html.parser')

    li = soup.findAll('div', class_='d-inline-block mb-1')

    base_url = 'https://github.com/'
    number = []
    repositories = []
    url = []

    for _, i in enumerate(li):
        for a in i.findAll('a'):
            newUrl = base_url + a["href"]
        number.append(_)
        repositories.append(i.text.strip())
        url.append(newUrl)

    tem = list(zip(number, repositories, url))
    df = pd.DataFrame(data=tem, columns=["No", "Repo", "URL"])
    
    #Guardar en la base de datos
    save_to_database(df)

root, tree = create_gui(searchGithub)

  
root.mainloop()













