#Requests - Zum anfordern des HTML-Codes für BS4 
#pip3 install requests
import requests

#Request bekommt eine URL und ermittelt damit ein HTML_
def request_website(url):

    #html_antwort gibt hoffentlich <Response [200]> zurück, was bedeutet das die Anfrage erfolgreich verarbeitet wurde.
    html_antwort = requests.get(url)

    #html_code enthält den HTML-Code der Website, welcher dann im folgenden von BeatifulSoup genutzt werden kann
    html_code = html_antwort.content

    #Gibt den HTML-Code zurück
    return html_code

