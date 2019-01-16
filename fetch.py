import requests
from pprint import pprint


def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    pprint(r.json())


if __name__ == '__main__':
    main()
