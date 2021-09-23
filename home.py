from selenium import webdriver
import time
import pandas as pd
from IPython.display import display

tabela = pd.read_excel("requisicoes.xlsx")
display(tabela)

quit()

navegator = webdriver.Chrome()

navegator.get("http://erpb.orsa.mx:31470/psp/cpfb91pr/EMPLOYEE/ERP/?&cmd=login&languageCd=POR&")

navegator.find_element_by_xpath('//*[@id="userid"]').send_keys('')

navegator.find_element_by_xpath('//*[@id="pwd"]').send_keys('')

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

time.sleep(4)

navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_SCHEDULE_PB$0"]/img').click()

time.sleep(3)

#navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_SCHEDULE_PB$0"]/img').click()

#navegator.switch_to.window()

navegator.switch_to.default_content()

time.sleep(3)

navegator.find_element_by_xpath('//*[@id="#ICOK"]').click()

navegator.switch_to.frame('TargetContent')

navegator.find_element_by_xpath('//*[@id="REQ_LINE_SHIP_SHIPTO_ID$0"]').clear() # Entrega

navegator.find_element_by_xpath('//*[@id="REQ_LINE_SHIP_SHIPTO_ID$0"]').send_keys('2120012') # Entrega

time.sleep(3)

#navegator.find_element_by_xpath('//*[@id="REQ_LINE_SHIP_SHIPTO_ID$0"]').send_keys('21212') # Entrega

navegator.find_element_by_xpath('//*[@id="REQ_SCHED_WRK_DISTRIBUTE_PB$0"]/img').click() # Navegar para centrod e custo

navegator.switch_to.default_content()

time.sleep(3)

navegator.find_element_by_xpath('//*[@id="#ICYes"]').click() # confirmar e seguir

time.sleep(10)

navegator.find_element_by_xpath('//*[@id="#ICOK"]').click() #confirmar e seguir
navegator.find_element_by_xpath('//*[@id="#ICOK"]').click() #confirmar e seguir

time.sleep(3)

navegator.switch_to.frame('ptModFrame_2')

time.sleep(5)

navegator.find_element_by_xpath('//*[@id="OPERATING_UNIT$0"]').clear()

navegator.find_element_by_xpath('//*[@id="OPERATING_UNIT$0"]').send_keys('2120012') #preenchendo unidade de distribuição orçamentaria

#navegator.switch_to.frame('ptModFrame_5')

time.sleep(3)

navegator.find_element_by_xpath('//*[@id="#ICSave"]').click()

time.sleep(3)

navegator.switch_to.frame('TargetContent')

time.sleep(3)

navegator.find_element_by_xpath('//*[@id="REQ_PNLS_WRK_RETURN_PB"]').click() #voltar para tela inicial

time.sleep(3)

navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_PRICE_REQ_C$0"]').clear()

navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_PRICE_REQ_C$0"]').send_keys(400)


quit()
