
from time import sleep
import warnings
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import init as colorama_init
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
colorama_init(autoreset=True)

def browser(): 
    option1 = Options()
    option1.add_argument("--disable-notifications")
    # warnings.simplefilter("ignore")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option1)
    driver.implicitly_wait(5)
    driver.minimize_window()
    return driver

def query(driver, dork):
    dork = dork.replace(' ', '+')
    URL = f'https://google.com/search?q={dork}'
    driver.get(URL)
    

def get_urls(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        site_urls = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/a")
        with open("sites.txt", "a+") as sites:
            for g in site_urls:
                try:
                    url = g.get_attribute('href')
                    print(url)
                    sites.write("%s\n" % url)
                except:
                    pass      
    except:
        pass   
            
def next_page(driver):
        
    try:  
        next = driver.find_element(By.ID, 'pnnext')   
        next.click()
    except:
        return 0
    
def capcha(driver):
    try:
        capcha = driver.find_element(By.ID, 'captcha-form') 
        print(f'{Fore.RED}Capcha Found!')
        while True:
            try:
                google = driver.find_element(By.ID, 'main') 
                break
            except:
                continue
    except:
        pass 
    

def dork_list():
    file_in = input("Enter File Name: ")
    file_in = file_in.strip()
    driver = browser()
    with open(file_in, 'r', encoding="utf-8") as file:
        
        line_no = 0
        for line in file:
            line_no = line_no + 1
            print(f'''
                {Fore.LIGHTCYAN_EX}*****************************************************************************
                                        {Fore.MAGENTA}[{line_no}] Search => {line}
                {Fore.LIGHTCYAN_EX}*****************************************************************************
                ''')
            dork = line.strip()
            query(driver, dork)
            print(f'{Fore.LIGHTBLUE_EX}***************************** {Fore.YELLOW}Trying on page 1 {Fore.LIGHTBLUE_EX}*****************************')
            capcha(driver)
            get_urls(driver)
            count = 2
            while True:
                capcha(driver)
                ext = next_page(driver)
                if ext == 0:
                    break
                capcha(driver)
                print(f'{Fore.LIGHTBLUE_EX}***************************** {Fore.YELLOW}Trying on page {count}{Fore.LIGHTBLUE_EX} *****************************')
                get_urls(driver)
                count = count + 1
                
def single_dork():
    dork = input("Enter dork: ")
    dork = dork.strip()
    driver = browser()
    query(driver, dork)
    print(f'{Fore.LIGHTBLUE_EX}***************************** {Fore.YELLOW}Trying on page 1 {Fore.LIGHTBLUE_EX}*****************************')
    capcha(driver)
    get_urls(driver)
    count = 2
    sleep(30)
    while True:
        capcha(driver)
        ext = next_page(driver)
        if ext == 0:
            driver.quit()
            print(f'{Fore.LIGHTGREEN_EX}Search Completed!')
            break
        capcha(driver)
        print(f'{Fore.LIGHTBLUE_EX}***************************** {Fore.YELLOW}Trying on page {count}{Fore.LIGHTBLUE_EX} *****************************')
        get_urls(driver)
        count = count + 1

print(f'''
         ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄          ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄         ▄ 
        ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌        ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌        ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌        ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌          ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌        ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌        ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌   ▀   ▐░▌▐░█▀▀▀▀█░█▀▀         ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌       ▐░▌▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌
        ▐░▌       ▐░▌▐░▌      ▐░▌  ▄      ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
        ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
         ▀         ▀  ▀         ▀  ▀       ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
         
                                                                                    {Fore.LIGHTGREEN_EX}A Next level Web Grabber
      ''')
print(f'''Your output file will be save as {Fore.LIGHTGREEN_EX}sites.txt''')
_enter = input(f'Press Enter to continue --> ')

print(f''''     
                {Fore.LIGHTWHITE_EX}* Choose one of them *
                
        {Fore.YELLOW}[1] Search by single dork
        [2] Search by list of dorks''')
input_var = int(input(f'--> '))


if input_var == 1:
    single_dork()
    
elif input_var == 2:
    dork_list()
    
else:
    print(f"{Fore.LIGHTRED_EX}Wrong input!")
