import requests
import json

GOOGLE_ENGINE = 'google'

class GoogleApi(object):
    """SerpApiClient enables to query google search engine supported and parse the result.

    search = GoogleApi({
        "q": "Coffee",
        "location": "Austin,Texas",
        "engine": "google",
        "api_key": "<your private key>"
        })
	data = search.get_json()
    """

    BACKEND = "https://customsearch.googleapis.com/customsearch/v1?"
    num = str(10)
    key ="AIzaSyB9AwAVyahkHS0cqflG1Aepwn5LQ_moZ14"
    path = "cx=59c893957269aa6d7&" + num + "&key=" + key


    def __init__(self, params_dict, engine = None):
        self.params_dict = params_dict
        self.engine = engine

    def construct_url(self, path = path):
        "Create url to post request."

        if self.key:
            self.params_dict['api_key'] = self.key
        if self.engine:
            if not 'engine' in self.params_dict:
                self.params_dict['engine'] = self.engine
        if not 'engine' in self.params_dict:
            raise ValueError('"engine must be defined in params_dict or engine".')

        return self.BACKEND + path, self.params_dict

    def get_results(self, path = path):
        "Apply post request to the given url."
        url = 'https://customsearch.googleapis.com/customsearch/v1?cx=59c893957269aa6d7&num=10&q=Coffee&location=Berlin%2C+Berlin%2C+Germany&hl=de&gl=de&google_domain=google.d&key=AIzaSyB9AwAVyahkHS0cqflG1Aepwn5LQ_moZ14'
        data={"userId": 1, "title": "Best coffee", "country": "ethiopia"}
        try:
            url, parameter = self.construct_url(path)
            #response = requests.get(url, parameter, timeout=60000)
            response =requests.post(url, json=data)
            return response
        except requests.HTTPError as e:
            print("fail: " + url)
            print(e, e.response.status_code)
            raise e

    def get_html(self):
        """Returns:
            Raw HTML search result from Gooogle
        """
        return self.get_results()

    def get_json(self):
        """Returns:
            Formatted JSON search result
        """
        self.params_dict["output"] = "json"
        return json.loads(self.get_results())

    def get_raw_json(self):
        """Returns:
            Formatted JSON search result as string
        """
        self.params_dict["output"] = "json"
        return self.get_results()

    def get_dictionary(self):
        """Returns:
            Dict with the formatted response content
        """
        return dict(self.get_json())

    def get_dict(self):
        """Returns:
            Dict with the formatted response content
            (alias for get_dictionary)
        """
        return self.get_dictionary()

    def get_search_archive(self, search_id, format = 'json'):
        """Retrieve search result from the Search Archive API
        Parameters:
            search_id (int): unique identifier for the search provided by metadata.id
            format (string): search format: json or html [optional]
        Returns:
            dict|string: search result from the archive
        """
        result = self.get_results("/searches/{0}.{1}".format(search_id, format))
        if format == 'json':
            result = json.loads(result)
        return result

    def get_account(self):
        """Get account information using Account API
        Returns:
            dict: account information
        """
        return json.loads(self.get_results("/account"))

    def get_location(self, q, limit = 10):
        """Get location using Location API
        Parameters:
            q (string): location (like: city name..)
            limit (int): number of matches returned
        Returns:
            dict: Location matching q
        """
        self.params_dict = {}
        self.params_dict["output"] = "json"
        self.params_dict["q"] = q
        self.params_dict["limit"] = limit
        return json.loads(self.get_results('/locations.json'))

if __name__ == "__main__":
    search = GoogleApi({"q": "Coffee", "location": "Berlin, Germany"}, engine="google")
    data = search.get_html()
    print(data.text)