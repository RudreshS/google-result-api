import unittest
import os
from googleapi.google_api import GoogleApi

class TestSearchApi(unittest.TestCase):

		def setUp(self):
			key ="AIzaSyB9AwAVyahkHS0cqflG1Aepwn5LQ_moZ14"
			GoogleApi.key = os.getenv("API_KEY", key)

		def test_get_json(self):
				search = GoogleApi({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_json()
				self.assertEqual(data["search_metadata"]["status"], "Success")
				self.assertIsNotNone(data["search_metadata"]["google_url"])
				self.assertIsNotNone(data["search_metadata"]["id"])
				self.assertIsNotNone(data['local_results']['places'][0])

		def test_get_json(self):
				search = GoogleApi({"q": "Coffee", "engine": "google_scholar"})
				data = search.get_json()
				self.assertIsNotNone(data["organic_results"][0]["title"])

		def test_get_dict(self):
				search = GoogleApi({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_dict()
				self.assertIsNotNone(data.get('local_results'))

		def test_get_dictionary(self):
				search = GoogleApi({"q": "Coffee", "location": "Austin,Texas"})
				data = search.get_dictionary()
				self.assertIsNotNone(data.get('local_results'))


		def test_get_html(self):
				search = GoogleApi({"q": "Coffee", "location": "Berlin, Germany"}, engine= "google")
				data = search.get_html()
				self.assertGreater(len(data), 10)

if __name__ == '__main__':
		unittest.main()
