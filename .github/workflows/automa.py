
import csv
import random
import time

import requests

def send_message():

    token = os.getenv('credentials')
    quotes = []
    with open('Quotes.csv', 'r', newline='') as reader:
        lines = csv.DictReader(reader)

        for line in lines:
           quotes.append(line['Quotes'])

    message = random.choice(quotes)

    url = os.getenv('url')
    chatId = os.getenv('chatId')

    payload = {
        "chatId": chatId,
        "message": message
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


def main():
  send_message()

if __name__ == '__main__' :

  main()




