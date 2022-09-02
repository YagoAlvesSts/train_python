from seleniumSystem import ChromeAuto
from time import sleep


if __name__ == '__main__':
    
    options = ('--disable-gpu', '--no-sandbox',)
    chrome = ChromeAuto()
    browser = chrome.make_chrome_browser(*options)
    chrome.acessa('https://www.google.com')

    # TODO: Refactor this
    # input_element = browser.find_element(By.NAME, 'q')
    # input_element.send_keys('Python')
    # sleep(3)
    # input_element.send_keys(Keys.ENTER)
    # sleep(3)
    # browser.quit()
    
    
    # chrome.clica_perfil()
    # chrome.faz_logout()

    # chrome.clica_sign_in()
    # chrome.faz_login()

    # chrome.clica_perfil()
    # chrome.verifica_usuario('otaviomirandabr')

    sleep(5)
    chrome.sair()
