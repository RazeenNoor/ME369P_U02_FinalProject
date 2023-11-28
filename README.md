# ME369P U02 Final Project
By: Jason Rivas, Razeen Noor, and Isabella Gomez

This project aims to provide travelers with convenient access to real time information about their travel destination. This project consitsts of three main components: detecting ArUco markers that are associated with the travel destination, generating the pdf with the scraped information, and scraping the information from real-time sources. 
![](https://github.com/RazeenNoor/ME369P_U02_LightningTalk/blob/2dbd3e1347439c818766b9efcd29dbfc10fc3973/Images/Program%20Architecture.png)


## ArUco Marker Detection 
OpenCV Package Installation:
* `pip install opencv-python`
* `conda install -c conda-forge opencv`
  
This file utilizes OpenCV to detect ArUco markers and is the main file for the project. ArUco markers are 5x5 black and white binary squares that provide a fast and simple detection. 

Below are the associated ArUco markers of the supported cities.
![](https://github.com/RazeenNoor/ME369P_U02_LightningTalk/blob/f0d2379ab93900487e0a105cc1b1c3166f3b4523/Images/ArUco%20Markers.png)


## Generating the pdf
ReportLab Package Installation
* `pip install reportlab`
* `conda install -c anaconda reportlab`

The `Pdf.py` file utilizes the datetime (built-in) and the reportlab packages. Once the `BuildPDF` class is called, the program will create an instance of the desired destination in the `Scrape.py` file and call associated attributes to obtain real-time information. As information is returned, this file will arrange it into a readable format and generate the pdf.

## Scraping the Information
Requests and BeautifulSoup Package Installation
* `pip install requests`
* `conda install -c anaconda requests`
* `pip install bs4`
* `conda install -c conda-forge bs4`

This file consists of a class called `Cities` that creates an instance for the desired travel destination and has the following attributes: `weather()`, `.news()`, `.events()` and `.landmarks()` where the BeautifulSoup and Request packages are utilized to open the website and scrape text from the html code. For a crashcourse in html scraping click [here](https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-find/).

## Utilizing this Project
To utilize this project the user will need to download the following files from our github: `ArucoMarkerDetection.py`, `Pdf.py`, `Scrape.py` and the aforementioned packages used in the files. Once this is complete users will only need to run `ArucoMarkerDetection.py`.

> Note:  The `ArucoMarkerDetection.py`, `Pdf.py`, and `Scrape.py` files should all be in the same working directory. 

Start by scanning an ArUco marker associated with your selected city. The ArUco marker can be a digital image or printed. Run the `ArucoMarkerDetection.py` to open your computer's camera and show your computer camera an image of the ArUco marker. The main program will then detect and identify the marker which is associated with a destination, subsequently triggering the `Pdf.py` and the `Scrape.py` files to scrape real-time information about the destination and generate the pdf in the working directory. 


  
