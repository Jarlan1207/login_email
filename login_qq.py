# -*- coding:utf-8 -*-
from splinter import Browser

username = '******' # qq邮箱
password = '******' # qq密码
password2 = '******' # qq邮箱独立密码

b = Browser('chrome')
b.visit('https://mail.qq.com/')

with b.get_iframe('login_frame') as iframe:
    iframe.find_by_name('u').fill(username)
    iframe.find_by_name('p').fill(password)
    iframe.find_by_id('login_button').click()
    iframe.find_by_name('pp').fill(password2)
    iframe.find_by_id('btlogin').click()

print u'登陆qq邮箱成功'

b.find_by_id('composebtn').click()
# b.find_by_id('to').fill(username)

with b.get_iframe('mainFrame') as frame1:
    # frame1.find_by_id('toAreaCtrl').fill('123')
    frame1.find_by_id('subject').fill('hello')
    frame1.find_by_id('toAreaCtrl').fill('hello')


    # frame1.find_by_id('subject').fill(username)


