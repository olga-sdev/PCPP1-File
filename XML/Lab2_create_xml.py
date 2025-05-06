"""
Objectives
improving the student's skills in building an XML document;
using the Element class and the SubElement function.

Scenario
You are a programmer working for an online store.
Your task is to build an XML document containing information about the three vegan products available in the store:

<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>

Save the document to the shop.xml file.
Use UTF-8 character encoding and don't forget to add the prolog to the beginning of the file. Good luck!
"""
import xml.etree.ElementTree as ET


root = ET.Element('shop')

category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

product_1 = ET.SubElement(category, 'product', {'name': 'Tomato Veganietto'})
type_1 = ET.SubElement(product_1, 'type')
type_1.text = 'tomato'
producer_1 = ET.SubElement(product_1, 'producer')
producer_1.text = 'Programmers Eat Tomato'
price_1 = ET.SubElement(product_1, 'price')
price_1.text = '7'
currency_1 = ET.SubElement(product_1, 'currency')
currency_1.text = 'EUR'

product_2 = ET.SubElement(category, 'product', {'name': 'Water'})
type_2 = ET.SubElement(product_2, 'type')
type_2.text = 'water'
producer_2 = ET.SubElement(product_2, 'producer')
producer_2.text = 'Drinks4Coders Inc.'
price_2 = ET.SubElement(product_2, 'price')
price_2.text = '1'
currency_2 = ET.SubElement(product_2, 'currency')
currency_2.text = 'USD'

ET.dump(root)

tree = ET.ElementTree(root)

tree.write('grocery_shop.xml', 'UTF-8', True)

"""
<?xml version='1.0' encoding='UTF-8'?>
<shop>
    <category name="Vegan Products">
        <product name="Tomato Veganietto">
            <type>tomato</type>
            <producer>Programmers Eat Tomato</producer>
            <price>7</price>
            <currency>EUR</currency>
        </product><product name="Water">
            <type>water</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>1</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>
"""
