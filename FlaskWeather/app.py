import os
from flask import Flask, render_template, request
import requests

# Load a local .env file when available so the WEATHER_API_KEY can be set locally during development.
# This is optional and will silently continue if dotenv is not installed.
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

# The OpenWeatherMap API key must be stored in the environment as WEATHER_API_KEY.
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")


class WeatherError(Exception):
    """Custom exception type for weather lookup failures."""
    pass


def get_weather(city: str, state: str = "", country: str = "", units: str = "metric") -> dict:
    """Fetch current weather from OpenWeatherMap.

    Args:
        city: The name of the city to look up.
        state: Optional state or region code to disambiguate the city.
        country: Optional country code to disambiguate the city.
        units: Unit system to request from the API ('metric' or 'imperial').

    Returns:
        A dictionary containing display-friendly weather data.

    Raises:
        WeatherError: When the API key is missing, the request fails, or the city is invalid.
    """
    if not WEATHER_API_KEY:
        raise WeatherError(
            "Weather API key not configured. Set WEATHER_API_KEY in your environment."
        )

    if units not in {"metric", "imperial"}:
        units = "metric"

    location_parts = [city]
    if state:
        location_parts.append(state)
    if country:
        location_parts.append(country)
    location_query = ",".join(location_parts)

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location_query,
        "appid": WEATHER_API_KEY,
        "units": units,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        # If the API returns JSON with a specific message, include it in the error.
        if hasattr(exc, "response") and exc.response is not None:
            try:
                error_data = exc.response.json()
                message = error_data.get("message")
                if message:
                    raise WeatherError(message.capitalize()) from exc
            except ValueError:
                pass
        raise WeatherError("Unable to fetch weather data. Try again later.") from exc

    data = response.json()

    if data.get("cod") != 200:
        message = data.get("message", "City not found.")
        raise WeatherError(message.capitalize())

    weather_info = data["weather"][0]
    main_info = data["main"]

    unit_label = "°C" if units == "metric" else "°F"

    return {
        "city": f"{data.get('name')}, {data.get('sys', {}).get('country', '')}".strip(", "),
        "description": weather_info.get("description", "").title(),
        "temperature": round(main_info.get("temp", 0)),
        "feels_like": round(main_info.get("feels_like", 0)),
        "unit_label": unit_label,
        "icon_url": f"https://openweathermap.org/img/wn/{weather_info.get('icon')}@2x.png",
    }


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the weather lookup page and handle city form submissions."""
    weather = None
    error = None
    city = ""
    state = ""
    country = ""
    units = "metric"

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        country = request.form.get("country", "").strip()
        units = request.form.get("units", "metric")

        if not city:
            error = "Please enter a city name."
        else:
            try:
                weather = get_weather(city, state=state, country=country, units=units)
            except WeatherError as exc:
                error = str(exc)

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        city=city,
        state=state,
        country=country,
        units=units,
    )


if __name__ == "__main__":
    # Start the Flask development server.
    app.run(debug=True)
