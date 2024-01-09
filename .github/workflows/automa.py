import os
import csv
from random import choice 
import time

import requests

messanger = '.github/workflows/wish.txt'

def new_year(messanger):   
      with open(messanger, mode='r') as fd:          
          lines = fd.readlines()
          line =  [line.strip() for line in lines]
          sentence = choice(line)
          return sentence     

def send_message():

    token = os.getenv('credentials')
    quotes = []
    with open('.github/workflows/Quotes.csv', 'r', newline='') as reader:
        lines = csv.DictReader(reader)

        for line in lines:
           quotes.append(line['Quotes'])

    message = choice(quotes)
    


    url = os.getenv('url')
    chatId = os.getenv('chatId')

    payload = {
        "chatId": chatId,
        "mediaUrl": new_year(messanger),
        "mediaCaption": message,
        "mediaName": "james.png"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        
        print('successful')
    else:
        
        print('failed')

    # print(response.text)


def main():
  send_message()

if __name__ == '__main__' :

  main()




