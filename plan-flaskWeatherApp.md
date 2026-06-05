## Plan: Flask Weather App

TL;DR: Create a small Flask app that serves a city entry form, fetches current weather from an external API, and renders the result with a weather icon.

**Steps**
1. Create a Flask entrypoint at `app.py`.
   - Initialize `Flask(__name__)` and configure an API key from `WEATHER_API_KEY` environment variable.
   - Add a root route `/` that handles both GET and POST.
   - On POST, call a helper function to request current weather for the submitted city.
   - Return rendered HTML with weather data and an icon URL.
2. Add a `templates/` folder with `index.html`.
   - Build a form for city input.
   - Display a weather panel when data exists, including city name, temperature, description, and icon.
   - Include a simple error message area for invalid cities or API failures.
3. Use the existing `static/` folder for frontend assets.
   - Add or update `static/styles.css` to style the form, weather card, and icon.
   - Optionally add `static/app.js` if client-side behavior is desired, but the initial plan can remain server-rendered.
4. Add `requirements.txt`.
   - Include `Flask`, `requests`, and optionally `python-dotenv` for local environment loading.
5. Document usage in a short README or comments.
   - Explain how to install dependencies, set `WEATHER_API_KEY`, and run `python app.py`.

**Relevant files**
- `app.py` — new Flask app and weather-fetching logic.
- `templates/index.html` — city form and weather display.
- `static/styles.css` — page styling for form and icon presentation.
- `requirements.txt` — Python dependencies.

**Verification**
1. Install dependencies from `requirements.txt` in a virtual environment.
2. Set `WEATHER_API_KEY` to a valid OpenWeatherMap API key.
3. Run `python app.py` and open `http://127.0.0.1:5000/`.
4. Enter a city name and verify that the current weather and icon appear.
5. Test invalid city input and confirm an error message is shown gracefully.

**Decisions**
- Use server-side Flask rendering to keep the implementation simple and avoid extra frontend complexity.
- Use an external weather API like OpenWeatherMap via a configurable environment variable.
- Keep the existing `static/` directory for assets rather than creating a separate frontend-only app.

**Further Considerations**
1. If you want a richer UX later, add an AJAX flow with `static/app.js` so the page does not reload on submit.
2. If you prefer a specific weather provider, the helper function can be adapted to that API.
