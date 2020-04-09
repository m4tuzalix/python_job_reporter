import unittest
from PageModels.manual_fetch_model import ManualFetch
from Selectors.page_selectors import justJoinIt as selector

class TestManualModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.link = "https://justjoin.it/wroclaw"
        cls.model = ManualFetch(link=cls.link, 
            all_links=selector.all_links, 
            city_name=selector.city, 
            bar_scroll=selector.bar_scroll, 
            date_posted=selector.date_posted)
        cls.model.open_web()
    @classmethod
    def tearDownClass(cls):
        cls.model.close_web()

    def test00_open_web(self):
        self.assertNotEqual(self.model.open_web(), False)

    def test01_get_all_links(self):
        links = self.model.get_all_links()
        self.assertIsInstance(links, list)
        self.assertGreater(len(links), 0)
    
    def test02_validation(self):
        link = self.model.get_all_links()
        validation = self.model.link_validation(link[0])
        self.assertEqual(validation, True)
        self.assertIsInstance(self.model.links_array, list)

    def test03_scrolling(self):
        scrolling = self.model.scroll_down(700)
        self.assertNotEqual(scrolling, False)
        