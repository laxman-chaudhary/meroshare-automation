from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import json
from mail import send_email
content=open("/opt/script/meroshare/alex/creadential.json","r")

config=json.load(content)
key_list = list(config.keys())




def datatdo():


    CHROMEDRIVER_PATH = '/opt/chromedriver/chromedriver'

    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                            chrome_options=chrome_options
                         )


    # path='/usr/bin/chromedriver'

    # driver = webdriver.Chrome(path)

    driver.get("https://meroshare.cdsc.com.np/#/login")



    def login(username,password,depositpartner):
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]').click()
        driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input').send_keys(depositpartner)
        driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li').click()
        time.sleep(3)








        #username input
        driver.find_element(By.ID,'username').send_keys(username)

        #password input
        driver.find_element(By.ID,'password').send_keys(password)



        #login click button
        driver.find_element(By.XPATH,'/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button').click()
        time.sleep(2)

        #redirect to apply share
        driver.get("https://meroshare.cdsc.com.np/#/asba")

        time.sleep(2)



    def check_the_share_list(crnNumber,email,transactionpin,value):

        def __init__(self,crnNumber,email,transactionpin,i):
            self.crnNumber=crnNumber
            self.transactionpin=transactionpin
            self.email=email
            self.value=value







        def if_apply_button_exist(i):
            time.sleep(5)
            try:
                test=f"//*[@id='main']/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{i+1}]/div/div[2]/div/div[4]/button"
                driver.find_element(By.XPATH,test)

                companynames=f'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{i+1}]/div/div[1]/div/span[1]'
                companyName=driver.find_element(By.XPATH,companynames)
                sharet=f'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{i+1}]/div/div[1]/div/span[4]'
                sharetype=driver.find_element(By.XPATH,sharet)
                shareg=f'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{i+1}]/div/div[1]/div/span[5]'
                shareGROUP=driver.find_element(By.XPATH,shareg)



                applied_time = datetime.now()
                d1 = applied_time.strftime("%d/%m/%Y %H:%M:%S")
                company_names={
                    "company":companyName.text,
                    "share_type":sharetype.text,
                    "share group":shareGROUP.text,
                    'email':email,
                    'applied_time':d1,

                }
                return company_names
            except NoSuchElementException:
                return







        def application_form():

            time.sleep(1)

            bankname=Select(driver.find_element(By.ID,'selectBank'))
            values=f"2: {value}"
            bankname.select_by_value(values)

            minimum_share=20

            time.sleep(1)
            driver.find_element(By.ID,'appliedKitta').send_keys(minimum_share)
            print(minimum_share)

            time.sleep(1)
            driver.find_element(By.ID,'crnNumber').send_keys(crnNumber)
            driver.find_element(By.ID,'disclaimer').click()

            time.sleep(2)

            driver.find_element(By.XPATH,'//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]').click()

            time.sleep(2)

            driver.find_element(By.ID,'transactionPIN').send_keys(transactionpin)

            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]').click()

            return minimum_share

           # time.sleep(2)
            #driver.find_element(By.XPATH,'/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a').click()

            # /html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input

        time.sleep(5)

        a=driver.find_elements(By.CLASS_NAME,'company-list')


        try:


            listofcmpy=[]
            if len(a)==0:
                print("no share issued")

                time.sleep(2)
                driver.find_element(By.XPATH,'/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a').click()
                time.sleep(5)
            else:

                for i in range(len(a)):
                    cname=if_apply_button_exist(i)
                    listofcmpy.append(cname)
                for j in range(len(listofcmpy)):
                    print(listofcmpy[j])
                    if listofcmpy[j]==None:
                        print("share already filled")
                        if len(listofcmpy)==j+1:
                            time.sleep(2)
                            driver.find_element(By.XPATH,'/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a').click()
                            time.sleep(2)


                    elif (listofcmpy[j]['share_type']=="IPO" or listofcmpy[j]['share_type']=="FPO")  and listofcmpy[j]['share group']=="Ordinary Shares":
                            time.sleep(2)
                            btn=f'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{j+1}]/div/div[2]/div/div[4]/button'
                            time.sleep(5)
                            driver.find_element(By.XPATH,btn).click()

                            time.sleep(2)
                            a=application_form()
                            send_email(listofcmpy[j]['company'],listofcmpy[j]['share_type'],listofcmpy[j]['email'],listofcmpy[j]['applied_time'])
                            time.sleep(20)
                    
                            if len(listofcmpy)==j+1:
                                time.sleep(2)
                                driver.find_element(By.XPATH,'/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a').click()
                            # print("delay")
                            # time.sleep(2000)
                            # print(date.today())
            

                    else:
                        print("no share issued")
                        if len(listofcmpy)==j+1:
                                time.sleep(2)
                                driver.find_element(By.XPATH,'/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a').click()

                        time.sleep(2)

                    
                        



        except:

            print("error")

            time.sleep(2)
            driver.find_element(By.XPATH,'/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a').click()
            time.sleep(10)


    for i in key_list:
        try:
            login(config[i]['UserName'],config[i]['password'],config[i]['DepositerParticipaterID'])
            check_the_share_list(config[i]['CRN_Number'],config[i]['user_email'],config[i]['transaction_pin'],config[i]['selectbnkvalue'])
        except:
            print("other Errors")
            driver.get("https://meroshare.cdsc.com.np/#/login")
    driver.quit()

datatdo()
