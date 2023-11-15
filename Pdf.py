import Scrape

#Build Pdf or markdown to view scraped information
##example
class buildpdf:
    def __init__(self, city):
        if city.lower()=="austin":
            self.Austin()
        if city.lower()=="boston":
            self.Boston()
        if city.lower()=="chicago":
            self.Chicago()

    def Austin(self):
        A=Scrape.Cities('auSTin')
        print(A.weather())
        pass
    
    def Boston(self):
        pass

    def Chicago(self):
        pass

    

if __name__ == '__main__':
    buildpdf("Austin")