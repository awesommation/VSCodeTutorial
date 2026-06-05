// Frontend calculator logic for the static UI.
// It assembles button presses into a math expression and sends the expression to the API.
const display = document.getElementById('display');
const buttons = document.querySelectorAll('[data-value]');
const clearButton = document.getElementById('clear');
const calculateButton = document.getElementById('calculate');

// Keep the current expression as a string while the user presses buttons.
let expression = '';

// Update the calculator display with the current expression or result.
function updateDisplay(value) {
  display.textContent = value || '0';
}

// Append button values to the expression when the user clicks any calculator button.
buttons.forEach((button) => {
  button.addEventListener('click', () => {
    expression += button.dataset.value;
    updateDisplay(expression);
  });
});

// Clear the expression and reset the display.
clearButton.addEventListener('click', () => {
  expression = '';
  updateDisplay('0');
});

// Send the expression to the backend API and display the returned result.
calculateButton.addEventListener('click', async () => {
  if (!expression.trim()) {
    return;
  }

  const payload = { expression };

  try {
    const response = await fetch('/api/calc', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    const result = await response.json();

    if (!response.ok) {
      updateDisplay(result.error || 'Error');
      return;
    }

    // Replace the current expression with the evaluated result.
    expression = String(result.result);
    updateDisplay(expression);
  } catch (error) {
    updateDisplay('Network error');
  }
});
