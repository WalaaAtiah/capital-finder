from asyncio import exceptions
from distutils.log import error
from http.server import BaseHTTPRequestHandler
from locale import currency
from logging import exception
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)
        print(dictionary)

        try:
            if 'capital' in dictionary and 'country' in dictionary:
                print("hi")
                capital=dictionary['capital']
                url = 'https://restcountries.com/v3.1/capital/'
                r = requests.get(url + capital).json()
                # print (1,r[0]["name"]["common"])
                country=r[0]["name"]["common"]
                if country.lower()==dictionary['country'].lower():
                    message=f" correct .^^ the capital of {country} is {capital}"
                else :
                    country2=dictionary['country']
                    url2 = 'https://restcountries.com/v3.1/name/'
                    r2 = requests.get(url2 + country2).json()
                    print (2,r2[0]["capital"][0])
                    capital2=r2[0]["capital"][0]
                    message=f"{capital} is the capital of {country} && The capital of {country2} is {capital2} "
    
            elif 'capital' in dictionary:
                print (dictionary['capital'])
                capital=dictionary['capital']
                url = 'https://restcountries.com/v3.1/capital/'
                r = requests.get(url + capital).json()
                languages= [i for i in r[0]["languages"].values()]
                currency=[i for i in r[0]["currencies"].keys()]
                currency_name=[i for i in r[0]["currencies"].values()]
                x=currency_name[0]["name"]
                country=r[0]["name"]["common"]
                message=f"{capital} is the capital of {country} ,its currency {x} ({currency[0]}) and its language {languages[0]}"
    
            elif 'country' in dictionary:
                print (dictionary['country'])
                country=dictionary['country']
                url = 'https://restcountries.com/v3.1/name/'
                r = requests.get(url + country).json()
                languages= [i for i in r[0]["languages"].values()]
                currency=[i for i in r[0]["currencies"].keys()]
                currency_name=[i for i in r[0]["currencies"].values()]
                x=currency_name[0]["name"]
                print (2,r[0]["capital"][0])
                capital=r[0]["capital"][0]
                message=f"The capital of {country} is {capital},its currency {x} ({currency[0]}) and its language {languages[0]}"
    
            else :
                message="please provide me with a country name or capital name " 
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
        except:
            pass
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write("you enter wrong value".encode())
    
        return
