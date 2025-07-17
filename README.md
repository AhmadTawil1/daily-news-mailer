# 📰 Daily News Mailer

A fully automated Python-based email digest that fetches, filters, formats, and sends daily AI/ML/NVIDIA news from trusted sources — straight to your inbox.

> Built for personal use now. Designed for multi-user Flask expansion later.

---

## 🚀 Features

- ✅ Curated topic-specific news (e.g., NVIDIA, GenAI, ML Research)
- ✅ Query + domain filtering using [NewsAPI.org](https://newsapi.org)
- ✅ Duplicate removal and article validation
- ✅ Clean, modern HTML formatting
- ✅ Secure email delivery via Gmail SMTP
- ✅ Fully automated with daily scheduling at `7:30 AM`
- ✅ Modular architecture (fetch → filter → format → send)

---

## 📁 Project Structure

```
daily-news-mailer/
│
├── main.py                  # Pipeline entry point
├── .env                     # Secrets: API key, email credentials
│
├── news/
│   ├── fetch.py             # Fetches articles per topic
│   └── filter.py            # Deduplicates and filters articles
│
├── emailer/
│   ├── format_html.py       # Converts articles to styled HTML
│   └── send.py              # Sends HTML email securely
│
├── scheduler/
│   └── job.py               # Runs `main.py` daily at 07:30
│
├── config/
│   └── settings.py          # Loads environment variables
│
├── requirements.txt         # Project dependencies
└── README.md                # You're here
```

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/daily-news-mailer.git
cd daily-news-mailer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up `.env`

```env
NEWS_API_KEY=your_newsapi_key
EMAIL_ADDRESS=your_gmail@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
```

> ⚠️ Make sure 2FA is enabled on your Gmail and you’re using an **App Password**.

---

## ⏰ Running the Scheduler

```bash
python -m scheduler.job
```

Keeps running and waits until 07:30 every day. You can deploy it as a background job or cloud task later.

---

## 🧠 Future Goals

> As this project evolves, I plan to expand it into a full Flask-based multi-user system.

### 🔜 Planned Features

- 🌐 Web interface with topic entry form (Flask)
- 👤 User accounts + preferences storage (SQLite or Firebase)
- 🧠 LLM-based article summarization
- ⭐ Relevance scoring or keyword ranking with AI
- 📊 Dashboard for reading history / most-clicked articles
- 📦 Dockerized deployment or cloud hosting (Render/Fly.io)
- 🕵️‍♂️ NLP-powered duplicate detection
- 🌍 Multilingual support (Arabic/Hebrew/English news feeds)
- 📁 Daily HTML archive storage (optional)

---

## 🧑‍💻 Built With

- Python 3.11+
- `requests` + `schedule` + `smtplib`
- `dotenv` for secure config
- `NewsAPI.org` for real-time headlines
- Gmail SMTP (TLS-secured)
- Clean modular architecture (no vibe-coding)

---

## 📬 Sample Email Preview

> _"🧠 Your Daily AI Digest"_  
> Includes 3 sections: `NVIDIA`, `GenAI`, and `ML Research` — formatted with modern HTML cards and safe links.

---

## 📄 License

MIT License. Use freely and modify for your own use cases.

---

## ✨ Author

**Ahmad Tawil**  
Backend & AI-focused Software Engineer  
[GitHub @AhmadTawil1](https://github.com/AhmadTawil1)