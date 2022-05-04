# -*- coding: UTF-8 -*- #
"""
@filename :auto_sign.py
@author :lplalbert
@time :2022-04-22
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from os import system
from pywinauto.keyboard import send_keys#键盘
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UID = "202024100711" #学号
PWD = ".200222Lpl\n" #密码
wechat_path = r'D:\WeChat\WeChat.exe' #微信位置

def sign_in(uid, pwd):

    # set to no-window
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")

    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    print("Inputting the UID and Password of User {0}".format(uid))
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"mt_5\"]/div[2]/div[3]/input"))).send_keys(uid)
    browser.find_element(by=By.XPATH,value="//*[@id=\"mt_5\"]/div[3]/div[3]/input").send_keys(pwd)

    print("Signing in for User {0}".format(uid))
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'zzj_top_6s')))
    browser.switch_to.frame('zzj_top_6s')
    browser.find_element(By.XPATH, '/html/body/form/div/div[11]/div[3]/div[4]/span').click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='bak_0']/div[7]/div[2]")))

    try:
        browser.find_element(By.XPATH, '/html/body/form/div/div[7]/div[4]').click()
    except:
        browser.find_element(By.XPATH, '/html/body/form/div/div[7]/div[2]/div[2]/div[6]/div[4]').click()

    time.sleep(2)
    browser.get_screenshot_as_file('screenshot.png')

    # quit the browser
    print("Singing in for User {0} is finished".format(uid))
    browser.quit()


if __name__ == "__main__":

    # For Single User
    sign_in(UID, PWD)
    print("Emailing to User {0} for notification".format(UID))

    now = time.localtime()
    nowt = time.strftime("%Y-%m-%d/%H: %M: %S", now)  # 这一步就是对时间进行格式化

    img_path = os.path.split(os.path.abspath(__file__))[0] + '\\screenshot.png'
    print(img_path)
    system(img_path)
    time.sleep(1)
    send_keys('^c') #将图片复制到剪切板
    time.sleep(1)
    # 微信安装路径----------=====----=================自行修改=======
    # wechat_path = r'D:\WeChat\WeChat.exe'  # ===自行修改========
    system(wechat_path)  # 打开微信
    time.sleep(1)

    send_keys('^f')  # 按下查找快捷键
    send_keys('文件传输助手')  # 查找聊天对象=================自行修改========

    time.sleep(1)
    send_keys('{ENTER}')  # 按下回车键-进入聊天窗口
    time.sleep(1)
    send_keys('^v')  # 将截图粘贴进去
    send_keys(nowt+' 已完成健康打卡')
    send_keys('{ENTER}')  # 按下回车键  点击发送
    send_keys('{VK_ESCAPE}')  # 关闭窗口
    send_keys('{VK_ESCAPE}')  # 关闭窗口
    send_keys('^w')  # 关闭窗口