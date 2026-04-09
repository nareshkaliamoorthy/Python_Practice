import playwright
from playwright.sync_api import sync_playwright

def intercept_api():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.route("https:\\amazon.in", "*/user/api", "*jpg, *png")
        page.goto("https://www.amazon.in/")


    
    
    

