from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://datasus.saude.gov.br/")
element = driver.find_element_by_xpath('//*[@id="menu-item-449"]/a').click() # acesso_à_informação.
element = driver.find_element_by_xpath('/html/body/div[1]/div/div/section[6]/div/div/div[4]/div/div/div/div/div/figure/a/img').click() # informações_de_saúde-tabnet.
element = driver.find_element_by_xpath('//*[@id="elementor-tab-title-2152"]').click() # assistência_à_saúde.
element = driver.find_element_by_xpath('//*[@id="elementor-tab-content-2152"]/ul/li[1]/span/a/span').click() # produção_hospitalar_(SIH/SUS).
element = driver.find_element_by_xpath('//*[@id="infesq"]/input[6]').click() # dados_detalhados_de_AIH_(SP)_por_local_de_internação_2008_em_diante.
element = driver.find_element_by_xpath('//*[@id="mySelect"]').click() # abrangência_geográfica.
#element = driver.find_element_by_xpath('').click()
#element = driver.find_element_by_xpath('').click()
