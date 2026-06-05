# FlaskWeather — User Stories and Implementation Plans

This document contains user stories and implementation plans for the current set of issues.

## 1) Add 5-day weather forecast support (Issue #8)

User story:
- As a user, I want to see a 5-day weather forecast for a searched location so that I can plan my activities for the coming days.

Implementation plan:
- Use OpenWeatherMap's 5 day / 3 hour forecast endpoint or the One Call API to fetch forecast data.
- Aggregate or extract daily summaries (date, high/low temperature, main weather condition, icon).
- Add a forecast panel to the existing `index.html` template showing 5 day cards with icon, date, high/low, and short summary.
- Keep the current weather card visible above or beside the forecast.
- Add error handling and loading states for the forecast request.
- Add unit tests for data aggregation logic.

---

## 2) Use a single comma-separated location field for city/state/country (Issue #9)

User story:
- As a user, I want to enter a location in a single field like "Seattle, WA, US" so that entering a search feels natural and compact.

Implementation plan:
- Replace the three separate inputs (`city`, `state`, `country`) in the template with one `location` input.
- Parse the `location` string on the server-side (split on commas, trim whitespace) into city, state, and country components.
- Reuse the existing `get_weather()` helper to accept parsed components.
- Update client-side validation and the server route to handle the new input.
- Add UI guidance (placeholder text and tooltip) showing example input formats.
- Update tests for form parsing.

---

## 3) Add autocomplete support for the location input (Issue #10)

User story:
- As a user, I want autocomplete suggestions when typing a location so I can select the correct city quickly and avoid misspelling.

Implementation plan:
- Add a lightweight autocomplete widget to the front-end (vanilla JS or small library).
- Use an external geocoding or location API (e.g., OpenWeatherMap's Geocoding API or Mapbox Places) to fetch suggestions.
- Debounce user input and request suggestions as the user types.
- Allow keyboard and mouse selection; populate the `location` field with the selected suggestion.
- Provide a fallback to allow manual text entry if suggestions fail or API quota is exceeded.
- Add tests/mocks for frontend behavior where practical.

---

## 4) Improve weather error handling and API key validation (Issue #11)

User story:
- As a user, I want clear and actionable error messages when something goes wrong (missing API key, invalid location, network error) so I know how to resolve or retry.

Implementation plan:
- Detect missing `WEATHER_API_KEY` at app startup and show an informative message in the UI when a lookup is attempted.
- Distinguish API errors (invalid location, API quota, bad API key) and network errors in `get_weather()` and raise descriptive exceptions.
- Update the Flask route to map those exceptions to friendly, actionable messages (e.g., "API key missing — add WEATHER_API_KEY to .env").
- Keep response structure stable for the template to avoid rendering errors.
- Add tests that mock API responses to verify error branches.

---

## 5) Add unit tests for weather lookup and route behavior (Issue #12)

User story:
- As a developer, I want automated tests for the weather lookup and route behavior so that future changes are safe and regressions are caught early.

Implementation plan:
- Add `pytest` to `requirements.txt` and create a `tests/` directory.
- Add tests for `get_weather()` covering successful response parsing and common error cases (invalid city, API error, missing key).
- Use `requests-mock` or `responses` to mock HTTP responses from OpenWeatherMap.
- Add tests for the Flask `index` route using Flask's `test_client()` to validate correct template rendering and error handling.
- Add a short note to the README describing how to run the tests: `pytest -q`.
