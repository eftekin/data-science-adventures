from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())

tag_object = soup.title
print("tag object: ", tag_object)
print("tag object type: ", type(tag_object))

tag_object = soup.h3
print(tag_object)

tag_child = tag_object.b
print(tag_child)

parent_tag = tag_child.parent
print(parent_tag)

print(tag_object.parent)

sibling1 = tag_object.next_sibling
print(sibling1)

sibling2 = sibling1.next_sibling
print(sibling2)

sibling3 = sibling2.next_sibling
print(sibling3)

print(tag_child['id'])
print(tag_child.attrs)
print(tag_child.get('id'))


tag_string = tag_child.string
print(tag_string)

print(type(tag_string))

unicode_string = str(tag_string)
print(unicode_string)

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')
table_rows = table_bs.find_all('tr')
print(table_rows)

first_row = table_rows[0]
print(first_row)

print(type(first_row))

print(first_row.td)

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('column', j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
print(list_input)

table_bs.find_all(id="flight")

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

print(table_bs.find_all(href=True))
# print(table_bs.find_all(href=False))
print(soup.find_all(id="boldest"))

print(table_bs.find_all(string="Florida"))


two_tables = "<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

two_tables_bs = BeautifulSoup(two_tables, "html.parser")

print(two_tables_bs.find("table"))
print(two_tables_bs.find("table", class_="pizza"))
