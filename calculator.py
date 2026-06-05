from __future__ import annotations

import ast
import operator as op
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

# Create the FastAPI application instance.
app = FastAPI(title="Modern Calculator API")

# Serve files from the `static` directory at the `/static` URL path.
STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Define a safe subset of Python operators that the calculator can evaluate.
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
}


def evaluate_expression(expression: str) -> float:
    """Parse and evaluate a math expression safely using the AST module."""
    try:
        root = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid expression") from exc

    def _eval(node: ast.AST) -> float:
        """Recursively evaluate AST nodes that are allowed."""
        if isinstance(node, ast.Expression):
            return _eval(node.body)

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return float(node.value)
            raise ValueError("Unsupported constant")

        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in ALLOWED_OPERATORS:
                left = _eval(node.left)
                right = _eval(node.right)
                return ALLOWED_OPERATORS[op_type](left, right)
            raise ValueError("Unsupported operator")

        if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[type(node.op)](_eval(node.operand))

        raise ValueError("Unsupported syntax")

    result = _eval(root)
    if result == float("inf") or result == float("-inf"):
        raise ValueError("Division by zero")

    return result


@app.get("/", response_class=HTMLResponse)
async def read_index() -> HTMLResponse:
    """Return the main calculator UI page."""
    index_path = STATIC_DIR / "index.html"
    return HTMLResponse(index_path.read_text(encoding="utf-8"))


@app.post("/api/calc")
async def calculate(request: Request) -> JSONResponse:
    """Accept a JSON payload and return the evaluated result."""
    payload = await request.json()
    expression = payload.get("expression")

    if not isinstance(expression, str) or not expression.strip():
        raise HTTPException(status_code=400, detail="Expression is required")

    try:
        result = evaluate_expression(expression)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero")

    return JSONResponse({"result": result})


if __name__ == "__main__":
    # Start the development server when running this file directly.
    import uvicorn

    uvicorn.run("calculator:app", host="127.0.0.1", port=8000, reload=True)
