from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page

url = "http://www.ibm.com"

data = requests.get(url).text

# create a soup object using the variable 'data'
soup = BeautifulSoup(data, "html5lib")

# in html anchor/link is represented by the tag <a>
for link in soup.find_all('a', href=True):
    print(link.get('href'))

# in html image is represented by the tag <img>
for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")

# get the contents of the webpage in text format and store in a variable called data
table = soup.find('table')

# Get all rows from the table
# in html table row is represented by the tag <tr>
for row in table.find_all('tr'):
    # Get all columns in each row.
    # in html a column is represented by the tag <td>
    cols = row.find_all('td')
    color_name = cols[2].string  # store the value in column 3 as color_name
    color_code = cols[3].text  # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))
