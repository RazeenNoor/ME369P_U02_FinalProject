import requests
from bs4 import BeautifulSoup

class Cities:
    def __init__(self,city):
        if city.lower()=="austin":
            self.city="Austin"
        if city.lower()=="boston":
            self.city="Boston"
        if city.lower()=="chicago":
            self.city="Chicago"

    def weather(self):
        Weather_links={"Austin":"https://weather.com/weather/tenday/l/9f4a74658d953c0535b91dd11ef8e2779b3f5a2bbff41bef1a1f655c92f3523df757f8b8ec8701792e72bf435f22a158",
                       "Boston":"https://weather.com/weather/tenday/l/9eccff5ba3b3b7655fd03a7fcc4158de1ec1cfbd4121d113068e6ce3a0632ba0",
                       "Chicago":"https://weather.com/weather/tenday/l/c1e7235c2dd7a3c88782c770be746ec65ec1d7b568ef19e8ead1e256c8ba74a8"}
        
        url=Weather_links[self.city]
        html= requests.get(url)
        s= BeautifulSoup(html.content, 'html.parser')
        city_temp = s.find("span",attrs={"class":"styles--temperature--3YaGV"}).text
        city_rain=s.find("span", attrs={"data-testid":"PercentageValue", "class":"DailyContent--value--1Jers"}).text
        city_description=s.find('p', attrs={"data-testid":"wxPhrase", "class":"DailyContent--narrative--3Ti6_"}).text
        Weather={'temp':city_temp, 'precip':city_rain, 'conditions':city_description}

        #Returns a dictionary with current temp, chance of rain, and a description of current conditions
        return Weather

        
    def news(self):
        Headlines=[]
        if self.city=="Austin":
            url2= "https://www.statesman.com/news/"
            html2= requests.get(url2)
            s2= BeautifulSoup(html2.content, 'html.parser')
            Austin_news = s2.find_all('a', {'class':'gnt_m_th_a'})
            for headline in Austin_news:
                Headlines.append(headline.text)
                # news_type=headline.find('div')
                # if news_type.get('data-c-ms')=="NEWS" or news_type.get('data-c-ms')=="LOCAL" or news_type.get('data-c-ms')=="CRIME" :
                #     print(headline.text)
        if self.city=="Boston":
            url2b='https://whdh.com/'
            html2b= requests.get(url2b)
            s2b= BeautifulSoup(html2b.content, 'html.parser')
            Boston_headlines=s2b.find('div',{'class':'wp-block-article-grid is-style-columns'}).find_all('a')
            for headline in Boston_headlines:
                Headlines.append(headline.text)
            
        if self.city=="Chicago":
            url2c='https://www.chicagotribune.com/news/breaking/'
            html2c= requests.get(url2c)
            s2c= BeautifulSoup(html2c.content, 'html.parser')
            c=s2c.find('div',{'class':"primary-font__PrimaryFontStyles-o56yd5-0 gVBMpi"})
            headlines=c.find_all('a')
            for title in headlines:
                headline=title.find('h2',{'class':"primary-font__PrimaryFontStyles-o56yd5-0 gVBMpi font_20_custom font_mobile_custom font_normal"})
                Headlines.append(headline.text)

        #Returns a list of news headlines associated with the city
        return Headlines
                  

    def events(self):
        Events={}
        Event_link={"Austin":"https://seatgeek.com/cities/austin",
                    "Boston":"https://seatgeek.com/cities/boston",
                    "Chicago":"https://seatgeek.com/cities/chicago"}

        url=Event_link[self.city]
        html=requests.get(url)
        s3c=BeautifulSoup(html.content,'html.parser')
        c2=s3c.find('ul',{"class","EventList__BaseEventList-sc-27d91e34-2 iDIABp"})
        c3=c2.find_all('li')
        for tag in c3[:4]:
            event=tag.find('p',{'data-testid':"event-item-title", 'class':"EventItem__Title-sc-6323af75-1 rmJCb"}).text 
            date=tag.find('p',{'data-testid':"date", 'class':"EventItem__Title-sc-6323af75-1 rmJCb"}).text
            time=tag.find('div', {'data-testid':"time","class":"EventItem__Subtitle-sc-6323af75-3 exfQxM"}).text.replace("·","")
            # print(f'{event.text}\n{date.text} \n{time.text.replace("·","")}')
            Events[event]=(date,time)

        #Returns dictionary of events with date and time of event in tuple
        return Events
  

    def landmarks(self):
        landmark_links={"Austin":'https://en.wikipedia.org/wiki/Austin,_Texas',
                        "Boston":"https://en.wikipedia.org/wiki/Boston",
                        "Chicago":"https://en.wikipedia.org/wiki/Chicago"}
        url=landmark_links[self.city]

        html= requests.get(url)
        s= BeautifulSoup(html.content, 'html.parser')
        landmark_img=s.find("tr",{"class":"mergedtoprow"}).find_all('img')
        landmark_caption=s.find_all("div",{'class':'thumbcaption text-align-center'})
        Landmarks={}
        for img,landmark in zip(landmark_img[:5],landmark_caption[:5]):
            Landmarks[landmark.text]=img['src']

        #Returns dictionary of five landmark names with associated url to image 
        return Landmarks
    


if __name__ == '__main__':
    pass
    A=Cities('auStin')        #Pass the city name
    # A.landmarks()
    # A.weather()
    # A.news()
    # print(A.events())
    # B=Cities('BosTon')
    # B.landmarks()
    # B.weather()
    # B.news()
    # B.events()
    # C=Cities('Chicago')
    # print(C.landmarks())
    # C.weather()
    # C.events()

