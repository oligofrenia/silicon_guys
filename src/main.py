import numpy as np
import requests
from bs4 import BeautifulSoup
from Python import Python

def return_license(link):
    # print(link[link.find('.com')+4:])
    license_link = 'https://raw.githubusercontent.com'+link[link.find('.com')+4:-1]+'/master/LICENSE'

    r = requests.get(license_link)
    f = open("license.txt", "w")
    f.write(r.text)
    f.close()
    return r.text

def return_contributors_number(link):
    # print(link[link.find('.com')+4:])
    contributors_json_link = 'https://api.github.com/repos'+link[link.find('.com')+4:-1]+'/contributors?per_page=1&anon=true'

    print(contributors_json_link)
    r = requests.get(contributors_json_link)
    f = open("contributors.json", "w")
    f.write(str(r.headers))
    f.close()
    contributors_number = 0

    return contributors_number

def main():
    Language = Python()
    Language.find_in_database()
    Language.find_in_internet()

    file = open("new_links.txt","r")
    links = file.readlines()
    # print(links[0])
    # print(links[0][links[0].find('.com')+4:])
    return_license(links[14])
    return_contributors_number(links[14])

    print(links[10])
    # reqs = requests.get('https://api.github.com/repos/faif/python-patterns/contributors?per_page=1&anon=true')
    reqs = requests.get('https://api.github.com/repos/pytransitions/transitions/contributors?per_page=1&anon=true')
    print(reqs.headers)




    # soup = BeautifulSoup(reqs.text, 'html.parser')
    # print(soup.find_all('a'))
    # for link in soup.find_all('a'):
    #     print(link.get('href'))





if __name__=='__main__':
    main()


