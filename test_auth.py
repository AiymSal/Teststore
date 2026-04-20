import random
import string
from playwright.sync_api import expect


def test_successful_registration(page):
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    login_name = f"user_{random_suffix}"
    email = f"{login_name}@example.com"
    password = "Password123!" # Вынесли пароль в переменную

   
    page.goto("https://automationteststore.com/")
    page.get_by_text("Login or register").click()
    page.locator("button[title='Continue']").click()

    
    
    page.locator("#AccountFrm_firstname").fill("Ivan")
    page.locator("#AccountFrm_lastname").fill("Tester")
    page.locator("#AccountFrm_email").fill(email)
    page.locator("#AccountFrm_address_1").fill("Test Street 123")
    page.locator("#AccountFrm_city").fill("Almaty")
    
   
   
    page.locator("#AccountFrm_zone_id").select_option(label="Greater London")
    
    page.locator("#AccountFrm_postcode").fill("123456")
    page.locator("#AccountFrm_loginname").fill(login_name)
    page.locator("#AccountFrm_password").fill(password)
    page.locator("#AccountFrm_confirm").fill(password) # Используем ту же переменную

   
    page.locator("#AccountFrm_agree").check()
    page.locator("button[title='Continue']").click()

   
    expect(page.get_by_text("Your Account Has Been Created!")).to_be_visible()

    
    with open("auth_creds.md", "a") as f:
        f.write(f"{login_name} | {password} | {email}\n")
    
    
    print(f"\n--- ТЕСТ ПРОЙДЕН ---")
    print(f"\nДанные добавлены в лог auth_creds.md")
