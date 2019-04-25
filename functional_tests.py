#!/usr/bin/env python
import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit();

    def check_for_row_in_list_table(self, row_text):
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( row_text, [row.text for row in rows])

    def type_todo_item_text(self, item_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys(item_text)
        inputbox.send_keys(Keys.ENTER)


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool online to-do app. She goes
        # to check its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do list
        self.assertIn( 'To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do straight away
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        self.type_todo_item_text('Buy peacock feathers')
        self.check_for_row_in_list_table( '1: Buy peacock feathers')

        # WHen she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edit is very methodical)
        self.type_todo_item_text('Use peacock feathers to make a fly')
        self.check_for_row_in_list_table( '1: Buy peacock feathers')
        self.check_for_row_in_list_table( '2: Use peacock feathers to make a fly')


        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # She visits that URL - her to-do list is still there

        #Satisfied she goes back to sleep
        self.fail("Finish the test!")

if __name__ == '__main__':
    unittest.main()