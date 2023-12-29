import os
import requests
import unittest

class RESTBook(unittest.TestCase):

    def setUp(self):
        self.baseUrl_get = "https://api.github.com/events"

        self.header = {
                        "content-type": "application/x-www-form-urlencoded",
                        "Accept-Encoding": "application/gzip",
                        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
                        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
                      }
        self.payload = { "q": "English is hard, but detectably so" }


    def test_makeRestCall_get(self):
        req = requests.get(self.baseUrl_get)
        outJSON = req.json()
        assert req.status_code == 200

    def test_makeRestCall_post(self):
         req = requests.post('https://httpbin.org/post', params={'key':'value'})
         outJSON = req.json()
         text = req.text
         assert req.status_code == 200
#
# def makeRestCall_delete(self):
#     # do something
#
# def makeRestCall_put(self):
#     # do something
#
# def makeRestCall_head(self):
#     # do something
