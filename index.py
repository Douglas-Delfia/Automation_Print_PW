import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import os



def wait_element(driver,element_xpath):
    wait = WebDriverWait(driver, 30)
    return wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))


def print_tables():

    driver = webdriver.Edge()
    url = "https://app.powerbi.com/groups/me/reports/d6f77dfe-838c-4032-8f56-0b65597b289a/ReportSectiondacfff9c1a264aa612e3?ctid=9744600e-3e04-492e-baa1-25ec245c6f10&experience=power-bi"
    driver.get(url)
    
    #Espera pelo carregamento da pagina
    wait_element(driver,"/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/div/div[1]/tri-shell/tri-extension-page-outlet/div[2]/report/exploration-container/div/div/docking-container/div/div/div/section/app-bar/div/div[2]/button[3]")

    n = 0
    tables = len( driver.find_elements(By.CLASS_NAME,"mat-ripple"))


    ##Altere o caminho "../../just/" para o caminho desejado
    data = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists("../../just/" + data):
        os.mkdir("../../just/" + data)
    

    while n != tables:
        n = n + 1

        wait_element(driver,f"/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/div/div[1]/tri-shell/tri-extension-page-outlet/div[2]/report/exploration-container/div/div/docking-container/div/div/exploration-fluent-navigation/section/mat-action-list/button[{n}]").click()
        
        nome_planilha = driver.find_element(By.CLASS_NAME,"textRun").text.replace(" ","_")
        
        #Ajusta o tamanho da tela
        wait_element(driver,"/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/div/div[1]/tri-shell/tri-extension-page-outlet/div[2]/report/exploration-container/div/div/docking-container/div/div/div/section/app-bar/div/div[2]/button[3]").click()
        wait_element(driver,"/html/body/div[2]/div[4]/div/div/div/button[2]").click()

        #Zoom
        wait_element(driver,"/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/div/div[1]/tri-shell/tri-extension-page-outlet/div[2]/report/exploration-container/div/div/docking-container/div/div/div/section/app-bar/div/div[2]/button[3]").click()
        wait_element(driver,"/html/body/div[2]/div[4]/div/div/div/button[1]").click(),sleep(1)

        #Altere o caminho "../../just/" para o caminho desejado
        hora_formatada = datetime.now().strftime("%H-%M")
        driver.save_screenshot(filename=f"../../just/{data}/{hora_formatada}_{nome_planilha}.png"),sleep(1)

        body_element = driver.find_element(By.TAG_NAME,"body")
        body_element.send_keys(Keys.ESCAPE)

    driver.quit()


'''schedule.every().day.at("09:10").do(print_tables)
while True:
    schedule.run_pending()
    sleep(15)'''

print_tables()