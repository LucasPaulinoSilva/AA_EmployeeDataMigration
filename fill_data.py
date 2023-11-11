from playwright.sync_api import sync_playwright
from subprocess import Popen
from pywinauto import Desktop
from requests_api import requestsApi
import config
import httpx


def fillData():
    # Concatena caminho da pasta com o nome do arquivo e extensão
    path_file_exe = config.PATH_FILE + config.NAME_PROGRAM + '.exe'

    with sync_playwright() as p:
        # Abre página do formulário no edge
        browser = p.chromium.launch(channel='msedge', headless=False)
        page = browser.new_page()
        page.goto(config.LINK_CHALLENGE)

        # Abre o programa desktop
        Popen(path_file_exe, shell=True)
        program = Desktop(backend='uia').EmployeeList
        program.wait('visible')

        # Comando para identificar todos os itens e funcionalidades do programa
        # program.print_control_identifiers()

        for employees in range(0, 10):
            # Captura o ID do site
            employee_ID = page.input_value('#employeeID')
            # Informa o ID para API e retorna os valores encontrados
            phone_number, start_date = requestsApi(employee_ID)

            # Pesquisa o ID no programa
            program.child_window(auto_id="txtEmpId").set_text(employee_ID)
            program.child_window(auto_id="btnSearch").click()

            # Captura os valores no programa
            first_name = program.child_window(
                auto_id='txtFirstName').get_value()
            last_name = program.child_window(auto_id='txtLastName').get_value()
            email_id = program.child_window(auto_id='txtEmailId').get_value()
            city = program.child_window(auto_id='txtCity').get_value()
            state = program.child_window(auto_id='txtState').get_value()
            zip_code = program.child_window(auto_id='txtZip').get_value()
            job_title = program.child_window(auto_id='txtJobTitle').get_value()
            department = program.child_window(
                auto_id='txtDepartment').get_value()
            manager = program.child_window(auto_id='txtManager').get_value()

            # Preenche os dados no site
            page.locator('#firstName').fill(first_name)
            page.locator('#lastName').fill(last_name)
            page.locator('#phone').fill(phone_number)
            page.locator('#email').fill(email_id)
            page.locator('#city').fill(city)
            page.select_option('#state', value=state)
            page.locator('#zip').fill(zip_code)
            page.locator('#title').fill(job_title)
            page.select_option('#department', value=department)
            page.locator('#startDate').fill(start_date)
            page.locator('#manager').fill(manager)

            # Clica no botão enviar do site
            page.locator('#submitButton').click()

        input('STOP para poder ver o resultado. Pressione qualquer tecla para finalizar.')

        # Fecha o programa
        program.close()


if __name__ == '__main__':
    fillData()
