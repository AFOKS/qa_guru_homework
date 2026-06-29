from selene import browser, be, have, by


browser.open('https://google.com')
#if browser.element(by.text('Accept all')).matching(be.visible):
   #browser.element(by.text('Accept all')).click()
browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
browser.element('html').should(have.text('About this page'))


#browser.element('[id="search"]').should(have.text('QA.GURU: Курсы тестировщиков'))