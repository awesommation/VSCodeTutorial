# VSCode Tutorial - Independent Apps

This repository contains two independent web applications as separate projects:

## Projects

### 1. [FlaskWeather](./FlaskWeather)
A Flask-based weather lookup application that queries the OpenWeatherMap API.

**Features:**
- Search weather by city, state, and country
- Real-time temperature display in Celsius or Fahrenheit
- Weather icons from OpenWeatherMap
- Error handling for invalid locations

**Quick Start:**
```bash
cd FlaskWeather
pip install -r requirements.txt
# Set WEATHER_API_KEY in .env or environment
python app.py
# Open http://localhost:5000
```

### 2. [Calculator](./Calculator)
A modern calculator built with FastAPI and a responsive frontend.

**Features:**
- Real-time calculation display
- Supports +, −, ×, ÷, ^, % operations
- Safe expression evaluation
- Clean dark-themed UI
- JSON API backend

**Quick Start:**
```bash
cd Calculator
pip install -r requirements.txt
python app.py
# Open http://localhost:8000
```

## Project Structure

```
VSCodeTutorial/
├── FlaskWeather/           # Flask weather app
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── requirements.txt
│   ├── README.md
│   └── .env.example
├── Calculator/             # FastAPI calculator app
│   ├── app.py
│   ├── static/
│   ├── requirements.txt
│   └── README.md
└── README.md              # This file
```

## Each App Is Independent

Each application has its own:
- Python dependencies (`requirements.txt`)
- Static files and assets
- Documentation (`README.md`)
- Configuration files

You can run each app separately or both at different ports.

## Requirements

- Python 3.8+
- Each app specifies its dependencies in its own `requirements.txt`

Refer to each app's `README.md` for detailed setup and usage instructions.

## Notes

- The Flask app uses a dedicated static subfolder at `static/flask_weather/` so existing top-level `static/` assets are preserved.
- Weather icons are loaded from OpenWeatherMap’s icon service.
- The app is intentionally server-rendered for simplicity.
