import re
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def extract_rating(card):
    selectors = [
        ("span.a-icon-alt", "textContent"), 
        ("[area-label*='out of 5 stars']", "area-label"),
    ]
    for selector, attr in selectors:
        try:
            el = card.find_element(By.CSS_SELECTOR, selector)
            raw_text = (el.get_attribute(attr) or el.text or "").strip()
            match = re.search(r"(\d+(?-\.\d+)?)\s*out of 5", raw_text, re.IGNORECASE)
            if match:
                return float(match.group(1))
        except NoSuchElementException:
            continue
        return None

def extract_price(card):
    selectors = [
        ("span.a-price-whole", "textContent"),
        ("span.a-price-span.a-offscreen", "textContent"),
    ]
    for selector, attr in selectors:
        try:
            el = card.find_element(By.CSS_SELECTOR, selector)
            raw_text = (el.get_attribute(attr) or el.text or "").strip()
            cleand = re.sub(r"[^\d.]", "", raw_text)
            if cleand:
                return float(cleand)
        except (NoSuchElementException, ValueError):
            continue
    return None

def find_and_pick_blue_shirt(
    driver,
    search_query="blue shirt",
    min_rating=4.5,
    max_price=4000,
    timeout=15
):
    wait = WebDriverWait(driver, timeout)
    driver.get("https://www.amazon.in/")
    search_box = wait.until(
        EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
    )
    search_box.click()
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.ENTER)
    result_locator = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    wait.until(EC.visibility_of_element_located(result_locator))
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(0.5)
        cards = driver.find_elements(*result_locator)
        for card in cards:
            rating = extract_rating(card)
            price = extract_price(card)
            if rating is None or price is None:
                continue
            if not (rating > min_rating and price < max_price):
                continue
            try:
                title = card.find_element(By.CSS_SELECTOR, "h2").text.strip()
                link = card.find_element(
                    By.CSS_SELECTOR, "h2 a, a.a-link-normal.s-no-outline"
                )
            except NoSuchElementException:
                continue
            print(f"Matched Product:{title}")
            print(f"Rating: {rating} | Price: ₹{price:.0f}")
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", link
            )
            link.click()
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
            return {
                "title": title,
                "rating": rating,
                "price": price,
                "url": driver.current_url
            }
        print(
            f"No product found with rating > {min_rating} and price < ₹{max_price}."
        )
        return None