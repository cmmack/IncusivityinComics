import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS():

    url = 'https://comicvine.gamespot.com/api/characters/?api_key=f034c37be925e4dfd8fec2fa76eed913ec24f61d&format=html'

    resp = requests.get(url)

    with open ('comicsdump.xml', 'wb') as f:

        f.write(resp.content)

def parseXML(comicsdump):

    tree = ET.parse(comicsdump)

    root = tree.getroot

    part1 =[]

    for part in root.findall('/character'):

        characters = {}

        for child in part:
            
            #if child.tag == '{http://search.yahoo.com/mrss/}content':
                #news['media'] = child.attrib['url']
            #else:
                #news[child.tag] = child.text.encode('utf8')
            part1.append(characters)

        return part1

def savetoCSV(part1, new):
    
    fields = ['1','2','3','4','5','6','7','8','9']

    with open(new, 'w') as csvfile:

        writer = csv.DictWriter(new, fieldnames = fields)

        writer.writerheader()

        writer.writerows(part1)

def main():

    loadRSS()

    part1 = parseXML('comicsdump.xml')

    savetoCSV(part1, 'new.csv')

if __name__ == "__main__":
  
    main()



    

