from playwright.sync_api import sync_playwright

def test_my_website():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://google.com')
        assert page.title() == 'Google'
        browser.close()