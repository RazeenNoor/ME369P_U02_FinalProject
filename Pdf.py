import Scrape
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime


class BuildPDF:
    def __init__(self, city):
        self.city = city.lower()
        filename = f"{self.city.capitalize()}.pdf"
        if self.city in ["austin", "boston", "chicago"]:
            self.generate_pdf(filename)
        else:
            print(f"City '{city}' is not supported.")

    def generate_pdf(self, filename):
        city_instance = Scrape.Cities(self.city)
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_weather, forecast = city_instance.weather()
        
        # Title and Current Weather
        pdf_content = (
                        f"<T>Information for {self.city.capitalize()}\n as of {current_date_time}\n\n" #Title
                       
                        f"<H>Current Weather:\n" #Heading
                        f"- The current temperature is {current_weather['temp']}\n"
                        f"- There is a {current_weather['precip']} chance of rain\n"
                        f"- Current Conditions:\n{current_weather['conditions']}\n"
                       )

        # 3 Day Forecast 
        pdf_content += "\n<H>3 Day Forecast:\n" #Heading
        for date, details in forecast.items():
            pdf_content += (f"<h>- {date}:\n"
                            f"     High / Low: {details[0]}\n"
                            f"     Chance of Rain: {details[1]}\n"
                            f"     Description: {details[2]}\n\n"
                            )
        
        # Current News
        pdf_content += "<H>Current News:\n" #Heading
        for headline in city_instance.news():
            pdf_content += f"- {headline}\n"
        
        # Events
        pdf_content += "\n<H>Events:\n" #Heading
        for event, (date, time) in city_instance.events().items():
            pdf_content += f"- {event} on {date} at {time}\n"
        
        # Landmarks
        pdf_content += "\n<H>Landmarks:\n" #<HH> Heading
        landmark_imgs=[]
        for landmark, img_url in city_instance.landmarks().items():
            landmark_imgs.append(ImageReader(img_url))
            pdf_content += f"- {landmark} \n"


        # create canvas
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        
        #Fonts and size
        Tfont,Tsize="Helvetica-Bold",20
        Hfont,Hsize="Helvetica-Bold",16
        tfont,tsize="Helvetica",12
        
        #Font colors
        Hcolor = (.2, .5, 1)  # RGB values from 0-1
        Tcolor = (1, 0, 0)
        tcolor = (0, 0, 0)

        # line spacing
        margin = 50
        lines = pdf_content.split('\n')
        line_height = 15 
        max_width = width - 2 * margin  # Maximum width for a line
        current_height = height - margin

        # line formating
        for line in lines:
            if "<T>" in line:
                # Title 
                c.setFillColor(Tcolor)
                c.setFont(Tfont, Tsize)
                title = line.replace("<T>", "")
                c.drawString(margin, current_height, title)
                current_height -= line_height
            elif "<H>" in line:
                # Heading 
                c.setFillColor(Hcolor)
                c.setFont(Hfont, Hsize)
                heading = line.replace("<H>", "")
                c.drawString(margin, current_height, heading)
                current_height -= line_height
            elif "<h>" in line:
                # Subheading 
                c.setFillColor(tcolor)
                c.setFont(tfont+'-Bold', 14)
                subheading = line.replace("<h>", "")
                c.drawString(margin, current_height, subheading)
                current_height -= line_height
            else:
                # Rest of Text
                c.setFillColor(tcolor)
                c.setFont(tfont, tsize)
                
                # line wrapping
                words = line.split()
                current_line = ""

                for word in words:
                    # Check if next word exceeds max_line_width
                    if c.stringWidth(current_line + word, tfont, tsize) < max_width:
                        current_line += word + " "
                    else:
                        # start a new line
                        c.drawString(margin, current_height, current_line.strip())
                        current_height -= line_height
                        current_line = word + " "

                # Draw rest of line
                c.drawString(margin, current_height, current_line.strip())
                current_height -= line_height
        
        # Adding Images
        x=50
        for landmark in landmark_imgs:
            c.drawImage(landmark,x,10, width=100, height=80,mask='auto')
            x+=105

        c.save()

if __name__ == '__main__':
    pass
    # BuildPDF("Austin")
    # BuildPDF("Boston")
    # BuildPDF("Chicago")
