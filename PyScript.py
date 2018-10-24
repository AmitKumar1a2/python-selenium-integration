
import time
from datetime import datetime
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")	
driver = None
#reading data from file into array
def readFromFile(fileName):
    array = []
    with open(fileName) as f:
        for line in f:
            array.append(line.strip('\n'))
    f.close()
    return array
def hitSite(array):
    i=0
    file= open('PathWhereYouWantToCreateLogFile','a')
    for line in array:
        tempArray = line.split(',')
        name = tempArray[0]
        email = tempArray[1]
        number = tempArray[2]
        try:
            driver = webdriver.Chrome(executable_path='PathOfCromeDriverExecutable', chrome_options=chrome_options)
            driver.get('https://www.surveymonkey.com/s/<SurveyID>')
            time.sleep(1) 
            nxt_btn = driver.find_element_by_name('ElementIDForNameField')
            nxt_btn.send_keys(name)
            nxt_btn = driver.find_element_by_name('ElementIDForEmailField')
            nxt_btn.send_keys(email)
			#you can add as many Fields as you required
            nxt_btn = driver.find_element_by_name('ElementIDForNumberField')
            nxt_btn.send_keys(number)
            vote_check = driver.find_element_by_id('160992479_1133482491')
            driver.execute_script("arguments[0].click();",vote_check)
            send_bt = driver.find_element_by_class_name('done-button')
            send_bt.click() 
            driver.quit()
            print("successed")
			#Logging 
            out = "Survey No:"+str(i)+" :with data: "+line+"\n"
            file.write(out)
            i=i+1
        except:
			#Logging 
            out= "Survey Not Done for: "+str(i)+" :with data: "+line+"\n"
            file.write(out)
            i=i+1
            driver.quit()
            print("failed")
            continue
	file.close()
hitSite(readFromFile('FileName.txt'))
