from news.fetch import fetch_news
from news.filter import filter_all_articles
from emailer.format_html import format_articles_to_html
from emailer.send import send_email

# ------------------------------
# 1. Fetch Articles for Each Topic
# ------------------------------
all_articles = {}

# NVIDIA news
all_articles.update(fetch_news(
    query='NVIDIA AND (AI OR CUDA OR GPU OR TensorRT OR Jetson)',
    domains='techcrunch.com,venturebeat.com,tomshardware.com,anandtech.com,nvidia.com,arstechnica.com,thenextweb.com',
    label='NVIDIA',
    
))

# Generative AI tools
all_articles.update(fetch_news(
    query='LangChain OR LLM OR RAG OR ChatGPT OR transformers OR huggingface',
    domains='techcrunch.com,venturebeat.com,thenextweb.com,huggingface.co,arxiv.org',
    label='GenAI',
    
))

# Deep Learning & ML Research
all_articles.update(fetch_news(
    query='deep learning OR machine learning OR AI research OR neural networks',
    domains='arxiv.org,science.org,nature.com,venturebeat.com',
    label='ML Research',
    
))

# ------------------------------
# 2. Filter & Clean the Articles
# ------------------------------
filtered_articles = filter_all_articles(all_articles)

# ------------------------------
# 3. Format to Styled HTML
# ------------------------------
html_content = format_articles_to_html(filtered_articles)

# ------------------------------
# 4. Send the Email
# ------------------------------
send_email("🧠 Your Daily AI Digest", html_content)
