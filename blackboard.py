- from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import datetime

root = Tk()
root.title("BlackBoard Login System")

# Functionality start
def blackboard():
    driver = webdriver.Chrome(executable_path="D:\shareble\drivers\chromedriver.exe")
    driver.get("https://cuchd.blackboard.com/")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.find_element_by_id("user_id").send_keys(username.get())
    driver.find_element_by_id("password").send_keys(password.get())
    driver.find_element_by_id("entry-login").click()
    x = datetime.datetime.now()
    times = re.search("((\d{2}[:])+\d{2})",str(x)).group(0)
    print(times)
    day = datetime.datetime.today().weekday()
    print(type(day))

    if day == 0:
        if times >= "10:00:00" and times <= "12:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[7]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "13:30:00" and times < "14:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[5]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "14:30:00" and times <="15:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
    elif day == 1:
        if times >= "10:00:00" and times < "11:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[3]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "11:45:00" and times <="12:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[8]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "13:30:00" and times <"15:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[9]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
    elif day == 2:
        if times >= "10:00:00" and times < "10:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[8]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "10:45:00" and times < "11:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[5]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "12:00:00" and times <"12:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[8]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "12:45:00" and times <= "15:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[2]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)

    elif day ==3 :
        if times >= "14:30:00" and times <"15:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[4]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
    elif day == 4:
        if times >= "14:30:00" and times <"15:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[4]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
    elif day == 5:
        if  times >= "10:00:00" and times < "11:45:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[6]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "13:30:00" and times <"14:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[5]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)
        elif times >= "14:30:00" and times <"15:30:00":
            pbj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[4]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView()",pbj)

## GUI DESIGN
usernamelabel = Label(root,text="Username : ")
usernamelabel.grid(row=0,column=0)
username = Entry(root,width=50)
username.grid(row = 0,column=1)

passwordlabel = Label(root,text="Password : ")
passwordlabel.grid(row=1,column=0)
password = Entry(root,width=50)
password.grid(row=1,column=1,columnspan=2)

submit = Button(root,text="Enter",command=blackboard)
submit.grid(row=2,column=0)

#GUI END
root.mainloop()
