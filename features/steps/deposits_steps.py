from asyncio import sleep
from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from json import loads
from urllib.parse import urlparse, urljoin

EMAIL = "luishcl@outlook.com"
PASSWORD = "1Bees-pass2"
DEPOSIT_URL = "https://test-bees.herokuapp.com/deposits"
DEFAULT_URL = "https://test-bees.herokuapp.com/"
SUCCESSFUL_MSG_CREATE = 'Deposit was successfully created.'
SUCCESSFUL_MSG_UPDATE = 'Deposit was successfully updated.'
SUCCESSFUL_MSG_DELETE = 'Deposit was successfully destroyed.'
DEPOSIT_ID = "deposits/128"

@given('stay on "{deposit_page}" session')
def go_to_page(context, deposit_page):
    context.browser.get(DEPOSIT_URL)
    title = context.browser.find_element(By.TAG_NAME, 'h1').text
    assert title in deposit_page


@given('stay "{deposit_edit}" session')
def step_impl(context, deposit_edit):
    context.browser.get(DEPOSIT_URL)
    
    # to-do locate and Pick up the deposit that was created
    



    base_url_deposit = DEPOSIT_URL
    relative_path_deposit = DEPOSIT_ID
    final_url = urljoin(base_url_deposit, relative_path_deposit)
    print(final_url)  # Output: 
    context.browser.get(final_url)

    edit_deposit_button = context.browser.find_element(By.XPATH, '/html/body/div/div[2]/a[1]')
    edit_deposit_button.click()
    
    #assert Title from Edit page
    title = context.browser.find_element(By.TAG_NAME, 'h1').text
    assert title in deposit_edit

    
@given('pick up a deposits')
def step_given(context):
    # Navigate default
    context.browser.get(DEPOSIT_URL)

    # Locate the table element (e.g., by ID, class, XPath, etc.)
    # my_table = context.browser.find_element(By.ID, 'deposits')

    # Extract rows and columns from the table
    # rows = my_table.find_elements(By.TAG_NAME, 'tr')
    # for row in rows:
    #     columns = row.find_elements(By.TAG_NAME, 'td')
    #     for col in columns:
    #         print(col.text)  # Print the text content of each cell
    
    # Localize o elemento na coluna A (por exemplo, "João")
    target_text = 'Deposit_A'
    # Localize todas as células da primeira linha (cabeçalhos das colunas)
    header_cells = context.browser.find_elements(By.XPATH, '//table//tr[1]/th')

    # Obtenha o número de colunas
    number_of_columns = len(header_cells)
    print(number_of_columns)

    # Localize todas as células da tabela
    cells = context.browser.find_elements(By.XPATH, '//table//td')

    # Varra as células para encontrar a posição do texto alvo
    for i, cell in enumerate(cells):
        if target_text in cell.text:
            line = i // number_of_columns  # Calcula o número da linha
            column = i % number_of_columns  # Calcula o número da coluna
            print(f"Texto encontrado na linha {line + 1}, coluna {column + 1}")
            break  # Saia do loop quando encontrar o texto

    # Reference target text  Deposits_A
    xpath_reference = f"html/body/div/div/table/tbody/tr[{line + 1}]/td[{column + 1}]"
    print(xpath_reference)
    # # Encontre o elemento com base no XPath
    element_reference = context.browser.find_element(By.XPATH, xpath_reference)
    print(element_reference)
    # Encontre o último elemento da mesma linha (próxima célula na mesma linha)
    element_action = element_reference.find_element(By.XPATH, './following-sibling::td/a')
    # # Clique no elemento de ação
    element_action.click()



@when('create a new deposit')
def create_deposit(context):
    
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    create_new_deposit_link = context.browser.find_element(By.LINK_TEXT, 'New deposit')
    create_new_deposit_link.click()

    info_deposits = loads(context.text)
    deposit_imput_name = context.browser.find_element(By.ID, 'deposit_name')
    deposit_imput_name.send_keys(info_deposits['name'])

    deposit_imput_address = context.browser.find_element(By.ID, 'deposit_address')
    deposit_imput_address.send_keys(info_deposits['address'])

    deposit_imput_city = context.browser.find_element(By.ID, 'deposit_city')
    deposit_imput_city.send_keys(info_deposits['city'])

    deposit_imput_state = context.browser.find_element(By.ID, 'deposit_state')
    deposit_imput_state.send_keys(info_deposits['state'])

    deposit_imput_zipcode = context.browser.find_element(By.ID, 'deposit_zipcode')
    deposit_imput_zipcode.send_keys(info_deposits['zipcode'])

    create_deposit_button = context.browser.find_element(By.CLASS_NAME, 'btn-primary')
    create_deposit_button.click()
    


@when(u'edit a deposit')
def step_impl(context):


    edit_deposits = loads(context.text)
    # name
    deposit_edit_name = context.browser.find_element(By.ID, 'deposit_name')
    deposit_edit_name.clear()
    deposit_edit_name.send_keys(edit_deposits['name'])

    #address
    deposit_edit_address = context.browser.find_element(By.ID, 'deposit_address')
    deposit_edit_address.clear()
    deposit_edit_address.send_keys(edit_deposits['address'])

    #city
    deposit_edit_city = context.browser.find_element(By.ID, 'deposit_city')
    deposit_edit_city.clear()
    deposit_edit_city.send_keys(edit_deposits['city'])

    #state
    deposit_edit_state = context.browser.find_element(By.ID, 'deposit_state')
    deposit_edit_state.clear()
    deposit_edit_state.send_keys(edit_deposits['state'])

    #zipcode
    deposit_edit_zipcode = context.browser.find_element(By.ID, 'deposit_zipcode')
    deposit_edit_zipcode.clear()
    deposit_edit_zipcode.send_keys(edit_deposits['zipcode'])

    #Apply update
    update_deposit_button = context.browser.find_element(By.XPATH, '/html/body/div/form/div[2]/input')
    update_deposit_button.click()



@when('destroy it')
def do_destroy_deposit(context):
    destroy_button_element = context.browser.find_element(By.XPATH, '/html/body/div/div[2]/form/button')
    destroy_button_element.click()


@then('the deposits were created successful')
def verify_deposit(context):
    
    message_created_successful = context.browser.find_element(By.XPATH, '/html/body/div/p').text()
    assert message_created_successful in SUCCESSFUL_MSG_CREATE
    print(message_created_successful)
    sleep(3)
    # Capture path from actual URL to use on deposits manager
    url_parseada = urlparse(context.browser.current_url).path
    print(url_parseada)
    
    back_to_deposit_link = context.browser.find_element(By.LINK_TEXT, 'Back to deposits')
    back_to_deposit_link.click()



@then('the deposits were edited successful')
def step_impl(context):
    successful_msg_deposit_update = context.browser.find_element(By.XPATH, '/html/body/div/p').text()
    assert successful_msg_deposit_update in SUCCESSFUL_MSG_UPDATE
    print(successful_msg_deposit_update)
    
    back_to_deposit_link = context.browser.find_element(By.LINK_TEXT, 'Back to deposits')
    back_to_deposit_link.click()




@then('deposit is removed')
def step_then(context):
    message_destroyed_sucessfull = context.browser.find_element(By.XPATH, '/html/body/div/p').text()
    assert message_destroyed_sucessfull in SUCCESSFUL_MSG_DELETE
    print(message_destroyed_sucessfull)