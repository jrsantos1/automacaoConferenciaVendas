from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time
import pandas

navegator = webdriver.Chrome()

navegator.get("http://erpb.orsa.mx:31470/psp/cpfb91pr/EMPLOYEE/ERP/?&cmd=login&languageCd=POR&")

navegator.find_element_by_xpath('//*[@id="userid"]').send_keys('JSANTOS')

navegator.find_element_by_xpath('//*[@id="pwd"]').send_keys('987654321%')

navegator.find_element_by_xpath('//*[@id="login"]/div/div[1]/div[8]/input').click()

navegator.get('https://erpb.orsa.mx:31475/psp/cpfb91pr/EMPLOYEE/ERP/c/REQUISITION_ITEMS.REQUISITIONS.GBL?FolderPath=PORTAL_ROOT_OBJECT.EPPO_PURCHASING.EPCO_REQUISITIONS.EP_REQUISITIONS_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')

navegator.switch_to.frame('TargetContent')

navegator.find_element_by_xpath('//*[@id="REQ_ADD_SRCH_BUSINESS_UNIT"]').clear()

navegator.find_element_by_xpath('//*[@id="REQ_ADD_SRCH_BUSINESS_UNIT"]').send_keys('21212')

navegator.find_element_by_xpath('//*[@id="#ICSearch"]').click()

#navegator.switch_to.frame('TargetContent')
time.sleep(5)

navegator.find_element_by_xpath('//*[@id="REQ_HDR_REQ_NAME"]').send_keys('Titulo')

navegator.find_element_by_xpath('//*[@id="CPLPO_REQ_DFLT_BUYER_ID"]').send_keys('COMPRADOR_BRASIL') #selecione comprador

navegator.find_element_by_xpath('//*[@id="CPLPO_PRMPT1_WK_DESCR"]').send_keys('SP - 58.731.662/0001-11') # cnpj fornecedor

time.sleep(5)

navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_INV_ITEM_ID$0"]').send_keys('1301010324') #preencher com item

time.sleep(4)

navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_INV_ITEM_ID$0"]').send_keys('1301010324') #preencher com item

navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').clear() #preencher quantidade

navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').send_keys('1') #preencher quantidade

time.sleep(3)

navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').clear() #preencher quantidade

navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').send_keys('1') #preencher quantidade

#navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_SCHEDULE_PB$0"]/img').click()

time.sleep(3)

#navegator.switch_to.window()

navegator.switch_to.active_element()

navegator.switch_to.window('pt_modalMask')

WebDriverWait(navegator, 5)

navegator.find_element_by_xpath('//*[@id="#ICOK"]').click()










