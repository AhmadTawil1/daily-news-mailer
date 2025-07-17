import requests
import pprint
import sys
from datetime import datetime, timedelta
from config.settings import NEWS_API_KEY

sys.stdout.reconfigure(encoding='utf-8')

API_KEY = NEWS_API_KEY

def fetch_news(query, domains, label, days_back=1):
    date_from = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'domains': domains,
        'from': date_from,
        'sortBy': 'popularity',
        'language': 'en',
        'apiKey': API_KEY
    }

    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    return {label: articles}

if __name__ == '__main__':
    all_articles = {}

    # 1. NVIDIA AI News
    all_articles.update(fetch_news(
        query='NVIDIA AND (AI OR CUDA OR GPU OR TensorRT OR Jetson)',
        domains='nvidia.com',
        label='NVIDIA'
    ))

    # 2. Generative AI News (LLMs, LangChain, RAG, etc.)
    all_articles.update(fetch_news(
        query='(LangChain OR LLM OR RAG OR ChatGPT OR transformers OR huggingface)',
        domains='techcrunch.com,venturebeat.com,thenextweb.com,huggingface.co,arxiv.org',
        label='GenAI'
    ))

    # 3. ML/DL Research News
    all_articles.update(fetch_news(
        query='(deep learning OR machine learning OR AI research OR neural networks)',
        domains='arxiv.org,science.org,nature.com,venturebeat.com',
        label='ML Research'
    ))

    pprint.pprint(all_articles, sort_dicts=False, width=140)
    
