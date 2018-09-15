# -*- coding:utf-8 -*-
from splinter import Browser
import time

username = '*******' # 163邮箱
password = '*******' # 163密码
# password2 = '******' # 邮箱独立密码

b = Browser('chrome')
b.visit('https://mail.163.com/')

with b.get_iframe('x-URS-iframe') as iframe:
    iframe.find_by_name('email').fill(username)
    iframe.find_by_name('password').fill(password)
    iframe.find_by_id('dologin').click()
    iframe.find_by_id('_mail_component_67_67').click()
    time.sleep(2)
    # iframe.find_by_id('_mail_link_22_210').click()
    iframe.find_by_id('_mail_input_3_213').fill('815723755@qq.com')


    # iframe.find_by_name('pp').fill(password2)
    # iframe.find_by_id('btlogin').click()

print u'登陆163邮箱成功'

# b.find_by_id('composebtn').click()
# b.find_by_id('to').fill(username)

# with b.get_iframe('leftFrame') as iframe1:
    # iframe1.find_by_name('toAreaCtrl').fill(username)
    # iframe1.find_by_id('subject').fill(username)


