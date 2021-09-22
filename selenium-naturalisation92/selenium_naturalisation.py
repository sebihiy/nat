import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from win10toast import ToastNotifier

TIME_OUT = 60 * 60 * 2  # time out for trying to get a booking (2 hours)
SLEEP_TIME = 60 * 60 * 2  # sleep time after reaching the page for booking (2 hours)

HAUTS_DE_SEINE_GOUV_FR = "http://www.hauts-de-seine.gouv.fr/booking/create/4462/2"


def selenium_naturalisation():
    browser = webdriver.Chrome()

    send_notification = False
    timeout = time.time() + TIME_OUT
    while (not send_notification and time.time() < timeout):
        browser.get(HAUTS_DE_SEINE_GOUV_FR)

        # refresh while the page does not load
        condition_element = None
        while condition_element is None:
            try:
                condition_element = browser.find_element_by_id("condition")
            except NoSuchElementException:
                pass

        position = condition_element.location

        # issue with chrome driver, need to scroll manually to the location
        browser.execute_script("window.scrollTo(" + str(position['x']) + ", " + str(position['y']) + ")")
        # click on check box to accept condition
        condition_element.click()

        # click on next
        browser.find_element_by_name("nextButton").click()

        # check if that there are no booking date
        try:
            form = browser.find_element_by_id("FormBookingCreate")
            if not form or not("Veuillez recommencer" in form.text or "Please try later" in form.text):
                # no form? or not the annoying message? send notification
                send_notification = True
            else:
                # retry in 1 second
                time.sleep(1)
        except NoSuchElementException:
            # the element does not exist? notify
            send_notification = True

    if send_notification:
        toaster = ToastNotifier()
        toaster.show_toast("Selenium naturalisation","Go check chrome!!!", duration=60)
        time.sleep(SLEEP_TIME)  # wait until the user has finished using the browser


if __name__ == '__main__':
    selenium_naturalisation()
