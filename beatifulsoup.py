#Beatifulsoup #pip3 install bs4
from bs4 import BeautifulSoup

#Macht aus dem hässlichen HTML-Code von requests einen schönen HTML-Code, der sich einfacher lesen lässt
def bs4_convert(html_code):

    #Bekommt den Hässlichen HTML-Code und packt ihn für Soup in die Variable soup
    soup = BeautifulSoup(html_code, 'html.parser')         #soup ist eine classe aus BS4

    #Packt den HTML-Code in Schön in die Variable beatiful_Soup
    beatiful_Soup = soup.prettify()                        #nearly_beatiful_Soup ist ein String      

    #Gibt den schönen, für BS4 les und durchsuchbaren HTML-Code zurück
    #Wir können aber nur Soup durchsuchen, deswegen geben wir das auch zurück
    return soup, beatiful_Soup