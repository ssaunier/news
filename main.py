from client import News

def print_articles(articles):
    for article in articles:
        print(f"- {article}")

def main():
    news = News()

    choice = input("Country headlines [default] or Search [hit s]?")
    if choice == "s":
        print("What do you to search?")
        keyword = input("> ")
        print_articles(news.search(keyword))
    else:
        print("Country?")
        country = input("> ")
        print_articles(news.headlines(country))

if __name__ == '__main__':
    main()
