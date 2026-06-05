# Flask Weather App

A small Flask application that allows users to enter a city name and view the current weather with an icon.

## Overview

- `app.py` contains the Flask server, city form handling, OpenWeatherMap API integration, and result rendering.
- `templates/index.html` renders the search form, error messages, and weather result card.
- `static/flask_weather/styles.css` stores the Flask app-specific stylesheet.
- `requirements.txt` lists the Python dependencies.

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenWeatherMap API key:
   - Windows PowerShell:
     ```powershell
     $env:WEATHER_API_KEY = "your_api_key_here"
     ```
   - Or create a `.env` file in the project root with:
     ```text
     WEATHER_API_KEY=your_api_key_here
     ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open the app in a browser:
   ```text
   http://127.0.0.1:5000/
   ```

## Usage

- Enter a city name and click `Search`.
- If the city is found, the app displays current temperature, weather description, and an icon.
- If the city is invalid or the lookup fails, an error message is shown.

## Notes

- The Flask app uses a dedicated static subfolder at `static/flask_weather/` so existing top-level `static/` assets are preserved.
- Weather icons are loaded from OpenWeatherMap’s icon service.
- The app is intentionally server-rendered for simplicity.
