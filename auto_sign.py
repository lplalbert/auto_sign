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
import user


def sign_in(uid, pwd):

    # 浏览器驱动设置
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    # 打开浏览器
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0") # 打开健康打卡系统

    # 输入学号密码
    print("Inputting the UID and Password of User {0}".format(uid))
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"mt_5\"]/div[2]/div[3]/input"))).send_keys(uid)
    browser.find_element(by=By.XPATH,value="//*[@id=\"mt_5\"]/div[3]/div[3]/input").send_keys(pwd)

    print("Signing in for User {0}".format(uid))
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'zzj_top_6s')))
    browser.switch_to.frame('zzj_top_6s')
    browser.find_element(By.XPATH, '/html/body/form/div/div[11]/div[3]/div[4]/span').click() # 点击本人填报

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='bak_0']/div[7]/div[2]")))

    try:
        browser.find_element(By.XPATH, '/html/body/form/div/div[7]/div[4]').click()
    except:
        browser.find_element(By.XPATH, '/html/body/form/div/div[7]/div[2]/div[2]/div[6]/div[4]').click() # 点击确认

    time.sleep(2)
    browser.get_screenshot_as_file('screenshot.png') # 截图

    # 关闭浏览器
    print("Singing in for User {0} is finished".format(uid))
    browser.quit()


if __name__ == "__main__":

    sign_in(user.UID, user.PWD)

    now = time.localtime() # 当前时间
    nowt = time.strftime("%Y-%m-%d/%H: %M: %S", now)  # 这一步就是对时间进行格式化

    img_path = os.path.split(os.path.abspath(__file__))[0] + '\\screenshot.png' # 截图所在位置
    system(img_path) # 打开截图
    time.sleep(1)
    send_keys('^c') #将图片复制到剪切板
    time.sleep(1)

    system(user.wechat_path)  # 打开微信
    time.sleep(1)

    send_keys('^f')  # 按下查找快捷键
    send_keys(user.group)  # 查找聊天对象

    time.sleep(1)
    send_keys('{ENTER}')  # 按下回车键-进入聊天窗口
    time.sleep(1)
    send_keys('^v')  # 将截图粘贴进去
    send_keys(nowt+' 已完成健康打卡')
    send_keys('{ENTER}')  # 按下回车键  点击发送
    send_keys('{VK_ESCAPE}')  # 关闭窗口
    send_keys('{VK_ESCAPE}')  # 关闭窗口
    send_keys('^w')  # 关闭窗口