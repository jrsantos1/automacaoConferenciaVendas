from selenium import webdriver
import time
import pandas as pd
from IPython.display import display

navegator = webdriver.Chrome()

navegator.get("http://erpb.orsa.mx:31470/psp/cpfb91pr/EMPLOYEE/ERP/?&cmd=login&languageCd=POR&")

navegator.find_element_by_xpath('//*[@id="userid"]').send_keys('JSANTOS')

navegator.find_element_by_xpath('//*[@id="pwd"]').send_keys('987654321%')

navegator.find_element_by_xpath('//*[@id="login"]/div/div[1]/div[8]/input').click()

tabela = pd.read_excel("requisicoes.xlsx")

for i, buu in enumerate(tabela['BU']):
    if(tabela.loc[i, "ID_requisicao"] == ""):
        continue
    print(tabela.loc[i, "Titulo"])
    BU = tabela.loc[i, "BU"]
    titulo = tabela.loc[i, "Titulo"]
    comprador = tabela.loc[i, "Comprador"]
    CNPJ_fornecedor = tabela.loc[i, "CNPJ_fornecedor"]
    item = tabela.loc[i, "ID_item"]
    quantidade = tabela.loc[i, "Quantidade"]
    budge_unidade = tabela.loc[i, "Budge_unidade"]
    valor = tabela.loc[i, "Valor"]
    id_requisicao = tabela.loc[i, "ID_requisicao"]

    time.sleep(3)

    navegator.get('https://erpb.orsa.mx:31475/psp/cpfb91pr/EMPLOYEE/ERP/c/REQUISITION_ITEMS.REQUISITIONS.GBL?FolderPath=PORTAL_ROOT_OBJECT.EPPO_PURCHASING.EPCO_REQUISITIONS.EP_REQUISITIONS_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder')

    navegator.switch_to.frame('TargetContent')

    navegator.find_element_by_xpath('//*[@id="REQ_ADD_SRCH_BUSINESS_UNIT"]').clear()

    navegator.find_element_by_xpath('//*[@id="REQ_ADD_SRCH_BUSINESS_UNIT"]').send_keys(str(BU))

    navegator.find_element_by_xpath('//*[@id="#ICSearch"]').click()

#navegator.switch_to.frame('TargetContent')
    time.sleep(5)

    navegator.find_element_by_xpath('//*[@id="REQ_HDR_REQ_NAME"]').send_keys(titulo)

    navegator.find_element_by_xpath('//*[@id="CPLPO_REQ_DFLT_BUYER_ID"]').send_keys(comprador) #selecione comprador

    navegator.find_element_by_xpath('//*[@id="CPLPO_PRMPT1_WK_DESCR"]').send_keys(CNPJ_fornecedor) # cnpj fornecedor

    time.sleep(5)

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_INV_ITEM_ID$0"]').send_keys(str(item)) #preencher com item

    time.sleep(4)

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_INV_ITEM_ID$0"]').send_keys(str(item)) #preencher com item

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').clear() #preencher quantidade

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').send_keys(len(str(quantidade)))#preencher quantidade

    time.sleep(3)

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').clear() #preencher quantidade

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_QTY_REQ$0"]').send_keys(len(str(quantidade))) #preencher quantidade

    time.sleep(4)

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_SCHEDULE_PB$0"]/img').click()

    time.sleep(3)

    #navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_SCHEDULE_PB$0"]/img').click()

    #navegator.switch_to.window()

    navegator.switch_to.default_content()

    navegator.find_element_by_xpath('//*[@id="#ICOK"]').click()

    time.sleep(3)

    navegator.switch_to.frame('TargetContent')

    time.sleep(1)

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_SHIP_SHIPTO_ID$0"]').clear() # Entrega

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_SHIP_SHIPTO_ID$0"]').send_keys(str(budge_unidade)) # Entrega

    time.sleep(3)

    #navegator.find_element_by_xpath('//*[@id="REQ_LINE_SHIP_SHIPTO_ID$0"]').send_keys('21212') # Entrega

    navegator.find_element_by_xpath('//*[@id="REQ_SCHED_WRK_DISTRIBUTE_PB$0"]/img').click() # Navegar para centrod e custo

    navegator.switch_to.default_content()

    time.sleep(3)

    navegator.find_element_by_xpath('//*[@id="#ICYes"]').click()# confirmar e seguir

    time.sleep(2)

    navegator.find_element_by_xpath('//*[@id="#ICOK"]').click() #confirmar e seguir
    navegator.find_element_by_xpath('//*[@id="#ICOK"]').click() #confirmar e seguir

    time.sleep(3)

    navegator.switch_to.frame('ptModFrame_2')

    time.sleep(5)

    navegator.find_element_by_xpath('//*[@id="OPERATING_UNIT$0"]').clear()

    navegator.find_element_by_xpath('//*[@id="OPERATING_UNIT$0"]').send_keys(str(budge_unidade)) #preenchendo unidade de distribuição orçamentaria

    #navegator.switch_to.frame('ptModFrame_5')

    time.sleep(3)

    navegator.find_element_by_xpath('//*[@id="#ICSave"]').click()

    time.sleep(3)

    navegator.switch_to.frame('TargetContent')

    time.sleep(3)

    navegator.find_element_by_xpath('//*[@id="REQ_PNLS_WRK_RETURN_PB"]').click() #voltar para tela inicial

    time.sleep(3)

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_PRICE_REQ_C$0"]').clear()

    navegator.find_element_by_xpath('//*[@id="REQ_LINE_WRK_PRICE_REQ_C$0"]').send_keys(str(valor))

    tabela.loc[i, "ID_requisicao"] = "feito"

