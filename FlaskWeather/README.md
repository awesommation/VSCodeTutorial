# Flask Weather App

A simple Flask-based weather lookup application that queries the OpenWeatherMap API.

## Features

- Search weather by city name
- Optional state/region and country code for disambiguation
- Support for Celsius and Fahrenheit temperature units
- Real-time weather display with OpenWeatherMap icons

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your OpenWeatherMap API key:
   - Create a `.env` file in this directory
   - Add: `WEATHER_API_KEY=your_api_key_here`

3. Run the app:
   ```bash
   python app.py
   ```

4. Open `http://localhost:5000` in your browser

## Project Structure

- `app.py` - Flask application with weather lookup route
- `templates/` - HTML templates
- `static/` - CSS and other static assets

## API Details

The app uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch current weather data.
