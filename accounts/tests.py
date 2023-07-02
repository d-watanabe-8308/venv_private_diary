from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='/Users/d_watanabe/Downloads/chromedriver_mac64/chromedriver')

    def test_login(self):
        # ログインページを開く
        self.selenium.get(self.live_server_url + reverse_lazy('account_login'))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('pitagora.3.swich@gmail.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('09025638348dw')
        self.selenium.find_element_by_name('btn').click()

        # ページタイトルの検証
        self.assertEqual('日記一覧 | Private Diary', self.selenium.title)