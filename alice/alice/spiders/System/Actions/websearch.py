
def websearch(self, find, session):
    session.driver.get("https://duckduckgo.com")
    search_form = session.driver.find_element_by_id('search_form_input_homepage')
    self.results = []
    search_form.send_keys(find)
    search_form.submit()
    #self.os_make_web_directories("duckduckgo/search", find)
    return session.driver.page_source

