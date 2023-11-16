# PDF.py

import Scrape
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


class BuildPDF:
    def __init__(self, city):
        self.city = city.lower()
        if self.city == "austin":
            self.generate_pdf('Austin.pdf')
        elif self.city == "boston":
            self.generate_pdf('Boston.pdf')
        elif self.city == "chicago":
            self.generate_pdf('Chicago.pdf')
        else:
            print(f"City '{city}' is not supported.")

    def generate_pdf(self, filename):
        city_instance = Scrape.Cities(self.city)
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Generate PDF content using the city_instance
        pdf_content = f"Information for {self.city.capitalize()} as of {current_date_time}\n\n"
        pdf_content += f"Weather: {city_instance.weather()['temp']}, {city_instance.weather()['precip']}, {city_instance.weather()['conditions']}\n\n"
        pdf_content += "Current News:\n"
        for headline in city_instance.news():
            pdf_content += f"- {headline}\n"
        pdf_content += "\nEvents:\n"
        for event, (date, time) in city_instance.events().items():
            pdf_content += f"- {event} on {date} at {time}\n"
        pdf_content += "\nLandmarks:\n"
        for landmark, img_url in city_instance.landmarks().items():
            pdf_content += f"- {landmark}\n"

        # formatting
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # font and size
        c.setFont("Helvetica", 12)

        # margins
        margin = 50
        # usable_width = width - 2 * margin
        # usable_height = height - 2 * margin

        # Draw text with proper line spacing
        lines = pdf_content.split('\n')
        line_height = 14  # Adjust as needed
        current_height = height - margin
        for line in lines:
            if current_height - line_height < margin:
                # Start a new page if the text exceeds the page height
                c.showPage()
                current_height = height - margin
            c.drawString(margin, current_height, line)
            current_height -= line_height

        c.save()

if __name__ == '__main__':
    BuildPDF("Austin")
    BuildPDF("Boston")
    BuildPDF("Chicago")
