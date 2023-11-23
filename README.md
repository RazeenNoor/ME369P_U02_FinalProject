# ME369P U02 Final Project
By: Jason Rivas, Razeen Noor, and Isabella Gomez

This project aims to provide travelers with convenient access to real time information about their destination. This project consitsts of three main components: detecting ArUco markers that are associated with the travel destination, generating the pdf with the scraped information, and scraping the information from real-time sources. 

## ArUco Marker Detection 
OpenCV Package Installation:
* `pip install opencv-python`
* `conda install -c conda-forge opencv`
  
This file utilizes OpenCV to detect ArUco markers. ArUco markers are 5x5 black and white binary squares that provide a fast and simple detection. 

Below are the associated ArUco marekers of the supported cities.
**insert images
![caption]()


## Generating the pdf
ReportLab Package Installation
* `pip install reportlab`
* `conda install -c anaconda reportlab`

The `pdf.py` file utilizes the datetime (built-in) and the reportlab packages. Once the `BuildPDF` class is called, the program will create an instance of the desired destination in the `Scrape.py` file and call associated attributes to obtain real-time information. As information is returned, this file will arrange it into a readable format and generate the pdf.

## Scraping the Information
Requests and BeautifulSoup Package Installation
* `pip install requests`
* `conda install -c anaconda requests`
* `pip install bs4`
* `conda install -c conda-forge bs4`

This file consists of a class called `Cities` that creates an instance for the desired travel destination and has the following attributes: `weather()`, `.news()`, `.events()` and `.landmarks()` where the beautifulSoup and request are utilized to open the website and scrape text from the html code. For a crashcourse in html scraping click [here](*link).

## Utilizing this Project
To utilize this project the user will need to download the following files from our github: `arUco file name?`, `pdf.py`, `Scrape.py` and the aforementioned packages used in the files. Once this is complete users will only need to run `arUco file name?`.

> Note:  The `arUco file name?`, `pdf.py`, and `Scrape.py` files should all be in the same working directory. 

Start by selecting a supported city and it's associated ArUco marker. It is recommended that the ArUco marker gets printed although a digital image will works as well. Run the `arUco file name?` to open your computer's camera and show your computer camera an image of the ArUco marker. The main program will then detect and identify the marker which is associated with a destination, subsequently triggering the `pdf.py` and the `Scrape.py` files to scrape real-time information about the destination and generate the pdf in the working directory. 


  
