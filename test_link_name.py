from selenium import webdriver

try:

    browser = webdriver.Chrome()
    browser.get('http://blog.csssr.ru/qa-engineer/')

    graphs_errors = browser.find_element_by_css_selector('.graphs-errors a')
    graphs_errors.click()
    soft_link = browser.find_element_by_css_selector('li a')
    soft_link.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    link_name = browser.current_url

    assert link_name == 'https://monosnap.com/', "Link would be https://monosnap.com/" #https://app.prntscr.com/ru/

finally:

    browser.quit()
