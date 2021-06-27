import requests, bs4

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip','DNT':'1','Connection':'close'}

class Covid:
    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/"
        self.response = response = requests.get(self.url, headers=header)
        self.text_data = response.content
        self.soup = bs4.BeautifulSoup(self.text_data, "lxml")
    def total(self):
        data = self.soup.find_all("div", {"class": "maincounter-number"}) 
        return {"name" : "World", "cases" : int(data[0].get_text().strip().replace(",", "")), "deaths" : int(data[1].get_text().strip().replace(",", "")), "recovered" : int(data[2].get_text().strip().replace(",", ""))}
    def country(self, country):
        data = self.soup.find("tbody")
        data = data.find_all("tr")
        for i in data:
            dat = i.find_all("td")
            if dat[1].get_text().strip().lower() == country.lower().strip(): 
                return {"name" : dat[1].get_text().strip(), "cases" : int(dat[2].get_text().strip().replace(",", "")), "deaths" : int(dat[4].get_text().strip().replace(",", "")), "recovered" : int(dat[6].get_text().strip().replace(",", ""))}
