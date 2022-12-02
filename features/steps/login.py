from behave import *
from selenium import webdriver

@given('Inicio el Navegador Brave')
def step_impl(context):

    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    context.driver= webdriver.Chrome(chrome_options=options, 
    executable_path="C:/Users/the_f/Resumenes/Universidad/6toSemestre/Ingenieria-requisitos/Ayudantias/Codes/chromedriver.exe")
    context.driver.maximize_window()

@when('Entro a GitHub')
def step_impl(context):
    context.driver.get("https://github.com/")

@when('Busco el botón sign in')
def step_impl(context):
    sign = context.driver.find_element_by_xpath('//div//div//a[@class="HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0"]').is_displayed()
    assert sign is True
    
@then('Se cierra el navegador')
def step_impl(context):
    context.driver.close()

