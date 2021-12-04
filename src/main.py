import numpy as np
import requests
import subprocess
from bs4 import BeautifulSoup
from Python import Python

def return_license(link):
    #print(link[link.find('.com')+4:])
    license_link = 'https://raw.githubusercontent.com'+link[link.find('.com')+4:]+'/master/LICENSE'

    r = requests.get(license_link)
    f = open("license.txt", "w")
    f.write(r.text)
    f.close()
    return r.text

def find_number_of_contributors_in_json_header(text):
    link = str([line for line in text.split('\n') if "Link" in line])
    link_split = link.split("page=")
    n = link_split[-1].split(">")
    return (n[0])

def return_contributors_number(link):
    # print(link[link.find('.com')+4:])
    contributors_json_link = 'https://api.github.com/repos'+link[link.find('.com')+4:-1]+'/contributors?per_page=1&anon=true'
    #print(contributors_json_link)

    print(contributors_json_link)
    r = requests.get(contributors_json_link)
    f = open("contributors.json", "w")
    f.write(str(r.headers))

    print(find_number_of_contributors_in_json_header(str(r.headers)))

    f.close()
    contributors_number = 0

    return contributors_number

def make_safety_check():
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    result.stdout.decode('utf-8')

def search_for_package_web(query):
    query+= ' python github'
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    
    # to search  
    link = []
    name = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        link.append(j)
        name.append(j[j[19:].find("/")+20:])
    return link, name

def main():
    # # Language = Python()
    # # Language.find_in_database()
    # # Language.find_in_internet()

    # # file = open("new_links.txt","r")
    # # links = file.readlines()
    # # print(links[0])
    # # print(links[0][links[0].find('.com')+4:])
    # return_license(links[14])
    # return_contributors_number(links[14])

    # print(links[10])
    # # reqs = requests.get('https://api.github.com/repos/faif/python-patterns/contributors?per_page=1&anon=true')
    # # reqs = requests.get('https://api.github.com/repos/pytransitions/transitions/contributors?per_page=1&anon=true')
    # # print(reqs.headers)

    # link, name = search_for_package_web('audio')
    # print(link[0])
    # print(name[0])

    # # print(link[0][19:].find("/"))
    # # print(link[0][link[0][19:].find("/")+20:])
    query = 'pandas'
    link, name = search_for_package_web(query)
    print(name[0], link[0], return_license(link[0]))
    print(return_contributors_number(link[0]))
        




    # soup = BeautifulSoup(reqs.text, 'html.parser')
    # print(soup.find_all('a'))
    # for link in soup.find_all('a'):
    #     print(link.get('href'))





if __name__=='__main__':
    main()


