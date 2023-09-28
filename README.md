# The only Playwright Test Automation using Python Cheatsheet you need



Playwright is a Python library that provides a high-level API for automating web browsers like Chromium, Firefox, and WebKit. Here's a cheatsheet highlighting the most common opperations in a Playwright Python Test Project.

Have a look at this [Playwright Test Example]() from this repository

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Initializing Playwright & Launching a Browser](#initializing-playwright)
- [Basic Navigation](#basic-navigation)
- [Interacting With Elements](#interacting-with-elements)
- [Handling Screenshots and PDFs](#screenshots-and-pdfs)
- [Handling Cookies](#handling-cookies)
- [Handling Alerts & Dialogs](#handling-alerts-and-dialogs)
- [Keyboard & Mouse Inputs](#keyboard-input)
- [Evaluating Javascript](#evaluating-javascript)
- [Working With Frames](#working-with-frames)


### Installation:

You need to install Playwright for Python first:

```bash
pip install playwright
playwright install
```

Install a test runner. Pytest is popular for python
```bash
pip install pytest
```

### Project structure:
When organizing a Playwright Python project, it's essential to create a structured and maintainable directory layout. Here's a common project structure for a Playwright Python project:

```plaintext
project_name/
│
├── tests/
│   ├── __init__.py
│   ├── test_my_feature.py
│   └── test_another_feature.py
```


`tests/`: This directory contains your Playwright test scripts. Each test script should focus on testing a specific feature or scenario.

### Initializing Playwright and Lanching a Browser:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # Your automation code here
    browser.close()
```

### Basic Navigation:

```python
# Navigate to a URL
page.goto('https://example.com')

# Reload the page
page.reload()

# Go back and forward in history
page.goBack()
page.goForward()
```

### Interacting with Elements:

```python
# Click an element
page.click('button')

# Type text into an input field
page.type('input[name="username"]', 'your_username')

# Press Enter key
page.press('input[name="password"]', 'Enter')

# Get text content of an element
text = page.text_content('h1')

# Select an option in a dropdown
page.select_option('select', label='Option 1')

# Waiting for elements to appear or become visible
page.wait_for_selector('div#my-element', state='visible')

# Check if an element exists
assert page.locator("button").is_visible()

# Check the page title
assert page.title() == "Expected Title"
```

### Screenshots and PDFs:

```python
# Take a screenshot
page.screenshot(path='screenshot.png')

# Generate a PDF
page.pdf(path='document.pdf')
```

### Handling Cookies:

```python
# Get all cookies
cookies = page.cookies()

# Set a cookie
page.set_cookie(name='my_cookie', value='cookie_value')

# Delete a cookie
page.delete_cookie(name='my_cookie')
```

### Handling Alerts and Dialogs:

```python
# Handle a JavaScript alert
page.on('dialog').accept()
page.on('dialog').dismiss()
```

### Keyboard and Mouse Input:

```python
# Type text
page.type('input', 'Hello, Playwright!')

# Press and release keyboard keys
page.keyboard.press('Enter')
page.keyboard.release('Shift')

# Move the mouse and click
page.mouse.move(100, 100)
page.mouse.click()
```

### Evaluating JavaScript:

```python
# Evaluate JavaScript in the context of the page
result = page.evaluate('1 + 2')
```

### Working with Frames:

```python
# Switch to a frame by name, id, or index
page.frame(name='frameName')
page.frame(index=0)

# Execute code in the context of a frame
frame = page.frame(index=0)
frame.evaluate('console.log("Hello from frame!")')
```

### Run your tests
Run your Playwright tests using the test runner you've chosen. If you're using pytest, you can run your tests from the command line like this
```bash
pytest tests/
```

<details>
  <summary>Run this Playwight Python Test Example</summary>

  1. Clone this repository
  
  2. Open folder in your preferred Editor or IDE

  3. Install Playwright and Pytest
  ```bash
  pip install playwright pytest
  playwright install
  ```

  4. Run the test
  ```bash
  pytest tests/
  ```

  5. Results will be in terminal
  
</details>
