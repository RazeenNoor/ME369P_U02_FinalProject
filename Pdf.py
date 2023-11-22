import Scrape
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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
                        f"<T>Information for {self.city.capitalize()}<TT>\nas of {current_date_time}\n\n" #Title
                       
                        f"<H>Current Weather:<HH>\n" #Heading
                        f"-Temperature: {current_weather['temp']}\n"
                        f"-Precipitation: {current_weather['precip']}\n"
                        f"-Current Conditions:\n{current_weather['conditions']}\n"
                       )

        # 3-Day Forecast 
        pdf_content += "\n<H>3-Day Forecast:<HH>\n" #Heading
        for date, details in forecast.items():
            pdf_content += (f"- {date}:\n"
                            f"     High/Low: {details[0]}\n"
                            f"     Chance of Rain: {details[1]}\n"
                            f"     Description: {details[2]}\n"
                            )
          
        # Current News
        pdf_content += "\n<H>Current News:<HH>\n" #Heading
        for headline in city_instance.news():
            pdf_content += f"- {headline}\n"
        
        # Events
        pdf_content += "\n<H>Events:<HH>\n" #Heading
        for event, (date, time) in city_instance.events().items():
            pdf_content += f"- {event} on {date} at {time}\n"
        
        # Landmarks
        pdf_content += "\n<H>Landmarks:<HH>\n" #Heading
        for landmark, img_url in city_instance.landmarks().items():
            pdf_content += f"- {landmark} {img_url}\n"

        # formatting
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        margin = 50
        
        #Fonts
        Tfont,Tsize="Helvetica-Bold",20
        Hfont,Hsize="Courier-Bold",16
        tfont,tsize="Helvetica",12
        
        #Font colors
        Hcolor = (0, 0, 1)  # RGB (0-1)
        Tcolor = (1, 0, 0)
        tcolor = (0, 0, 0)

        # line spacing
        lines = pdf_content.split('\n')
        line_height = 14 
        max_line_width = width - 2 * margin  # Maximum width for a line
        current_height = height - margin

        for line in lines:
            if "<T>" in line:
                # Title line
                c.setFillColor(Tcolor)
                c.setFont(Tfont, Tsize)
                title = line.replace("<T>", "").replace("<TT>", "")
                c.drawString(margin, current_height, title)
                current_height -= line_height
            elif "<H>" in line:
                # Heading line
                c.setFillColor(Hcolor)
                c.setFont(Hfont, Hsize)
                heading = line.replace("<H>", "").replace("<HH>", "")
                c.drawString(margin, current_height, heading)
                current_height -= line_height
            else:
                c.setFillColor(tcolor)
                c.setFont(tfont, tsize)
                
                # Wrapping
                # Split the line into words
                words = line.split()
                current_line = ""

                for word in words:
                    # Check if next word exceeds max_line_width
                    if c.stringWidth(current_line + word, tfont, tsize) < max_line_width:
                        current_line += word + " "
                    else:
                        # start a new line
                        c.drawString(margin, current_height, current_line.strip())
                        current_height -= line_height
                        current_line = word + " "

                # Draw rest of line
                c.drawString(margin, current_height, current_line.strip())
                current_height -= line_height

        c.save()

if __name__ == '__main__':
    BuildPDF("Austin")
    BuildPDF("Boston")
    BuildPDF("Chicago")
