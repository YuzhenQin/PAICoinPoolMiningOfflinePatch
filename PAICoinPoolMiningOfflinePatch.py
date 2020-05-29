# -*- coding: UTF-8 -*-
# Auth by "Gtihub/YuzhenQin|PAICoinPool/qqqqq|PAIForum/QQQQQ"
# in 2020/5/29
# Init repository : http://github.com/YuzhenQin/PAICoinPoolMiningOfflinePatch (This is a git repo).
# If you want to sponsor me, please transfer to PAI address:Pkkxw26PEvPx5zaWDSNBFqrseYsKvy7qXU
# For Chinese Version of this "code readme" or other details,please view "readme.me" on Git Repo!
# 欲要知晓更多细节或中文版，请查看Git仓库中的Readme.md!
import win32gui
import win32con
import pyautogui
import os,sys
import time
try:
    PCPConfig = open('config.txt')
except:
    print('无法读取config.txt')
    os.system('pause')
    exit(0)
i = 0
username = ''
password = ''
for eachline in PCPConfig:
    i=i+1
    if i==2:
        password = eachline
    elif i==3:
        username = eachline
if username=='' or password=='':
    print('用户名或密码为空|Username or Password is blank')
    os.system('pause')
    exit(0)
print('Config文件读取完毕，正在检索PAI Miner窗口')
hwnd = ''
try:
    hwnd = win32gui.FindWindow('Qt5QWindowIcon','PAI Miner')
except:
    print('无法检索到PAI Miner窗口')
    os.system('pause')
    exit(0)
print('开始进入主循环')
left,top,right,bottom = win32gui.GetWindowRect(hwnd)
while 1:
    templ,tempt,tempr,tempb = win32gui.GetWindowRect(hwnd)
    if left!=templ or top!=tempt or right!=tempr or bottom!=tempb:
        print('窗口坐标发生变化，开始进行自动操作')
        left,top,right,bottom = win32gui.GetWindowRect(hwnd)
        pyautogui.moveTo(x=left+(right-left)/2,y=top+230,duration=0.1,tween=pyautogui.linear)
        pyautogui.click()
        pyautogui.moveTo(x=left+(right-left)/2,y=top+200,duration=0.1,tween=pyautogui.linear)
        pyautogui.click()
        pyautogui.typewrite(message=username,interval=0.1)
        #pyautogui.hotkey('ctrl','v')
        pyautogui.moveTo(x=left+(right-left)/2,y=top+230,duration=0.1,tween=pyautogui.linear)
        pyautogui.click()
        pyautogui.typewrite(message=password,interval=0.1)
        #pyautogui.moveTo(x=left+(right-left)/2,y=top+290,duration=0.1,tween=pyautogui.linear)
        #pyautogui.click()
        time.sleep(5)
        left,top,right,bottom = win32gui.GetWindowRect(hwnd)
        for i in range(5,20):
            pyautogui.moveTo(x=left+(right-left)/2,y=top+i*20,duration=0.001,tween=pyautogui.linear)
            pyautogui.click()
        print('done!')
    time.sleep(10)