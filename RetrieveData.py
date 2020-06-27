from webbrowser import browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import DBManager

chrome_options = Options()
# incognito window
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome('C:/Users/user/chromedriver', chrome_options= chrome_options)

driver.get("https://www.politifact.com/factchecks/list/?page=393&")

next_button_exists = True
page = 393
while next_button_exists is True:
    page += 1
    element = driver.find_element_by_id("top")
    element = element.find_element_by_class_name("global-content")

    next_button = None

    try:
        button_elements = element.find_elements_by_class_name("t-row")[1]\
            .find_element_by_class_name("o-platform__content")\
            .find_element_by_class_name("m-list")
        button_elements = button_elements.find_elements_by_class_name("m-list__item")
        for button_element in button_elements:
            button = button_element.find_element_by_class_name("c-button")
            if button.get_attribute("innerText") == "Next":
                next_button = button
        next_button_exists = True
    except:
        next_button_exists = False
        next_button = None

    try:
        content_row = element.find_elements_by_class_name("t-row")[0]\
            .find_element_by_class_name("m-textblock").find_element_by_class_name("o-listicle")\
            .find_element_by_class_name("o-listicle__inner").find_element_by_class_name("o-listicle__content")\
            .find_element_by_class_name("o-listicle__list")

        news_items = content_row.find_elements_by_class_name("o-listicle__item")

        i = 1
        facts = []
        for news_element in news_items:
            if i % 10 == 0:
                print(str(i) + "\\" + str(len(news_items)))
            i = i + 1
            articleElement = news_element.find_element_by_tag_name("article")

            tag = articleElement.get_attribute("class").split(" ")[2].split("--")[1]

            author_element = articleElement.find_element_by_class_name("m-statement__author")
            author_data = author_element.find_element_by_class_name("m-statement__meta")
            author = author_data.find_element_by_class_name("m-statement__name").get_attribute("title")
            publish_info = author_data.find_element_by_class_name("m-statement__desc").get_attribute("innerText")

            content_element = articleElement.find_element_by_class_name("m-statement__content")\
                .find_element_by_class_name("m-statement__body").find_element_by_class_name("m-statement__quote-wrap")\
                .find_element_by_class_name("m-statement__quote").find_element_by_tag_name("a").get_attribute("href")
            # Open a new window
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(content_element)

            global_content = driver.find_element_by_id("top").find_element_by_class_name("global-content")
            text_to_be_verified = global_content.find_element_by_class_name("o-stage").find_element_by_class_name("o-stage__inner")\
                .find_element_by_class_name("m-statement").find_element_by_class_name("m-statement__content")\
                .find_element_by_class_name("m-statement__body").find_element_by_class_name("m-statement__quote-wrap")\
                .find_element_by_class_name("m-statement__quote").get_attribute("innerText")

            text_elements = None

            ok = True
            rows = global_content.find_elements_by_class_name("t-row")
            for x in range(0, len(rows)):
                try:
                    text_elements = rows[x].find_element_by_class_name("t-row__center")\
                        .find_element_by_class_name("m-textblock")
                    ok = True
                    break
                except:
                    ok = False
            if ok is True:
                text_elements = text_elements.find_elements_by_tag_name("p")
                text = ""
                for text_element in text_elements:
                    try:
                        txt_ = text_element.get_attribute("innerText")
                    except:
                        txt_ = None
                    if txt_ is not None:
                        text = text + " " + txt_
                        text = text + "\\n"
                fact = {
                    "fact": text_to_be_verified,
                    "tag": tag,
                    "author": author,
                    "publish_info": publish_info,
                    "data": text
                }
                facts.append(fact)
            else:
                print("Skipping " + str(i - 1))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        if len(facts) > 0:
            # write to db
            DBManager.insert_documents(facts)
        print("Page:" + str(page))
        next_button.click()
    except:
        next_button.click()

driver.close()
