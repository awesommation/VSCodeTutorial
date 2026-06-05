# Modern Calculator

A modern, fast calculator built with FastAPI and a responsive frontend.

## Features

- Real-time calculation display
- Supports basic arithmetic operations: +, −, ×, ÷, ^, %
- Safe expression evaluation using Python's AST module
- Clean, modern UI with dark theme
- JSON API for calculation backend

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open `http://localhost:8000` in your browser

## Project Structure

- `app.py` - FastAPI application with calculator API
- `static/index.html` - Main calculator UI
- `static/app.js` - Frontend JavaScript logic
- `static/styles.css` - Styling

## API Endpoint

### POST `/api/calc`

Evaluates a mathematical expression and returns the result.

**Request:**
```json
{
  "expression": "2 + 2 * 3"
}
```

**Response:**
```json
{
  "result": 8
}
```

## Supported Operations

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `**`
- Modulo: `%`
- Negation: `-x`
