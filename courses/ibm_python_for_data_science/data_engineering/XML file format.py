import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ET
import pandas as pd

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)


# Reading with xml.etree.ElementTree


tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building", "room"]

datatframe = pd.DataFrame(columns=columns)

for node in root:

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text

    title = node.find("title").text

    division = node.find("division").text

    building = node.find("building").text

    room = node.find("room").text

    datatframe = datatframe.append(pd.Series(
        [firstname, lastname, title, division, building, room], index=columns), ignore_index=True)

print(datatframe)

df = pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details")
datatframe.to_csv("employee.csv", index=False)


# | Data Formate  | Read           | Save             |
# | ------------- |:--------------:| ----------------:|
# | csv           | `pd.read_csv()`  |`df.to_csv()`     |
# | json          | `pd.read_json()` |`df.to_json()`    |
# | excel         | `pd.read_excel()`|`df.to_excel()`   |
# | hdf           | `pd.read_hdf()`  |`df.to_hdf()`     |
# | sql           | `pd.read_sql()`  |`df.to_sql()`     |
# | ...           |   ...          |       ...        |
