from typing import Dict, List

def format_articles_to_html(all_articles: Dict[str, List[Dict]]) -> str:
    html = """
    <html>
    <head>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          padding: 20px;
          color: #333;
        }
        .topic {
          margin-bottom: 40px;
        }
        .topic h2 {
          color: #2c3e50;
          border-bottom: 2px solid #ccc;
          padding-bottom: 5px;
        }
        .article {
          background-color: #fff;
          border-radius: 8px;
          padding: 15px;
          margin-bottom: 10px;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .article a {
          font-size: 16px;
          color: #2980b9;
          text-decoration: none;
          font-weight: bold;
        }
        .article a:hover {
          text-decoration: underline;
        }
        .description {
          font-size: 14px;
          margin-top: 5px;
          color: #555;
        }
      </style>
    </head>
    <body>
      <h1>🗞️ Your Daily AI Digest</h1>
    """

    for topic, articles in all_articles.items():
        html += f'<div class="topic"><h2>{topic}</h2>'
        for article in articles:
            title = article.get("title", "No title")
            url = article.get("url", "#")
            desc = article.get("description", "No description available.")
            html += f'''
              <div class="article">
                <a href="{url}" target="_blank">{title}</a>
                <div class="description">{desc}</div>
              </div>
            '''
        html += '</div>'

    html += "</body></html>"
    return html
