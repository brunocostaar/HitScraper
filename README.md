-----

# 🎵 HitScraper

This Python script retrieves the **Billboard Hot 100** chart from any specific date you choose. It then searches for those songs on Spotify and automatically creates a new private playlist in your account with the top hits from that day.

## 🚀 Features

  * **Web Scraping:** Fetches historical data from Billboard.com using `BeautifulSoup`.
  * **Spotify Integration:** Uses `Spotipy` to interact with the Spotify Web API.
  * **Automatic Playlist Creation:** Creates a playlist named "Músicas mais populares no dia [YYYY-MM-DD]" and adds the songs. (You can change the playlist name to whatever you prefer)

## 📋 Prerequisites

  * Python 3.x
  * A Spotify Account

## ⚙️ Configuration & Environment Variables

This project uses **Environment Variables** to keep sensitive data (like your API keys) secure and out of the source code. The code looks for `CLIENT_ID`, `CLIENT_SECRET`, and `USER_AGENT`.

### Step 1: Get Spotify API Credentials

1.  Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
2.  Click **"Create An App"**. Give it a name and description.
3.  Once created, you will see your **Client ID**. Click "Show Client Secret" to see your **Client Secret**. Save these.
4.  Click **"Edit Settings"**.
5.  Scroll down to **Redirect URIs** and add:
    `http://127.0.0.1:8888/callback`
    *(Note: This must match the URI in the Python script exactly)*.
6.  Click **Save**.

### Step 2: Set the Environment Variables

You need to set these variables on your computer before running the script so `os.getenv` can read them.

## 📦 Installation

Install the required Python libraries using pip:

```bash
pip install beautifulsoup4 requests spotipy
```

## ▶️ Usage

1.  Run the script:
    ```bash
    python main.py
    ```
2.  The script will prompt you for a date:
    ```text
    Input a date (YYYY-MM-DD): 2000-08-12
    ```
3.  **First Run Only:** A browser window will open asking you to authorize the app to access your Spotify account. Click **Agree**.
4.  The script will scrape Billboard, find the songs, and generate your playlist\!

## ⚠️ Disclaimer

This project is for educational purposes. Web scraping behavior is subject to the Terms of Service of the website being scraped (Billboard). Use responsibly.

-----
