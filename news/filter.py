def remove_duplicates(articles):
    seen = set()
    unique_articles = []
    for article in articles:
        title = article['title'].strip().lower()
        if title not in seen:
            unique_articles.append(article)
            seen.add(article['title'])
    return unique_articles

def remove_no_title_description_url(articles):
    return [article for article in articles if article['title'] and article['description'] and article['url']]

def limit_articles(articles, max=5):
    return articles[:max]
def filter_all_articles(all_articles):
    new_articles = {}
    for label, articles in all_articles.items():
        new_articles[label] = remove_duplicates(articles)
        new_articles[label] = remove_no_title_description_url(new_articles[label])
        new_articles[label] = limit_articles(new_articles[label], max=5)

    return new_articles