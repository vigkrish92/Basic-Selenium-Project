from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get('https://www.nseindia.com/products/content/equities/equities/eq_security.htm')


select_series = Select(driver.find_element_by_id('series'))
select_time_range = Select(driver.find_element_by_id('dateRange'))
symbol = driver.find_element_by_id('symbol')

select_series.select_by_visible_text('EQ')
select_time_range.select_by_visible_text('3 months')

select_series.select_by_value('EQ')
select_time_range.select_by_value('3month')

symbol.send_keys("YES BANK")

driver.find_element_by_xpath("//*[@id=\"submitMe\"]").submit()

y = driver.find_element_by_xpath("/html/body/table/tbody").text

print(y)

driver.quit()
