# ME369P U02 Final Project
By: Jason Rivas, Razeen Noor, and Isabella Gomez

This project aims to provide travelers with convenient access to real time information about their destination. This projetct consitst of three main components: detecting ArUco markers that are associated with the travel destination, generating the pdf with the scraped information, and scraping the information from real-time sources. 

# ArUco Marker Detection 
OpenCV Package Installation:
* ``
* ``
This file utilizes OpenCV to detect ArUco markers. ArUco markers are 5x5 black and white binary squares that provide a fast and simple detection. To utilize this project the user will need to show their computer camera an image of the ArUco marker. The program will detect and identify the marker which is associated with a destination, subsequently triggering the `pdf.py` and the `Scrape.py` files to generate the pdf. 

Below are the associated ArUco marekers of the supported cities.
**insert images
![caption]()

# Generating the pdf
ReportLab package Installation
* ``
* ``

The `pdf.py` file utilizes the datetime (built-in) and the reportlab packages. Once the `BuildPDF` class is called, the program will create an instance of the desired destination in the `Scrape.py` file and call associated attributes to obtain real-time information. As information is returned, this file will arrange it into a readable format and generate the pdf.

# Scraping the Information
Requests and BeautifulSoup package Installation
* ``
* ``
* ``
* ``

This file consists of a class called `Cities` that creates an instance for the desired travel destination and has the following attributes: `weather()`, `.news()`, `.events()` and `.landmarks()` where the beautifulSoup and request are utilized to open the website and scrape text from the html code. For a crashcourse in html scraping click [here](*link)
  
