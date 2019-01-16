import requests


def main():
    URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    res = requests.get(url=URL)

    print(res)


if __name__ == '__main__':
    main()
    