import random
import string
import pytest
from playwright.sync_api import expect

@pytest.fixture
def user_creds(page):
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    login_name = f"user_{random_suffix}"
    email = f"{login_name}@example.com"
    password = "Password123!"


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
    page.locator("#AccountFrm_confirm").fill(password) 

   
    page.locator("#AccountFrm_agree").check()
    page.locator("button[title='Continue']").click()

   
    expect(page.get_by_text("Your Account Has Been Created!")).to_be_visible()

           
    
    with open("auth_creds.md", "a") as f:
        f.write(f"{login_name} | {password} | {email}\n")

    return {"login": login_name, "password": password}



def test_registration_only(user_creds):
    print(f"\n--- Тест регистрации пройден для: {user_creds['login']} ---")



def test_login_after_registration(user_creds, page):
    
    page.locator(".side_account_list").get_by_text("Logoff").click()
    # expect(page.get_by_text("Account Logout")).to_be_visible()

    page.get_by_text("Login or register").click()
    
    page.locator("#loginFrm_loginname").fill(user_creds["login"])
    page.locator("#loginFrm_password").fill(user_creds["password"])
    page.locator("button[title='Login']").click()

    expect(page.get_by_text("Welcome back")).to_be_visible()
    print(f"\n--- Тест логина пройден для: {user_creds['login']} ---")

