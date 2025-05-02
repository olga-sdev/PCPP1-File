### XML processing in Python

The standard Python XML modules:

* _xml.etree.ElementTree_ –> analyzing and creating XML data.
* _xml.dom.minidom_ –> parsing XML into a DOM structure using functions: _parse()_ and _parseString()_.
* _xml.sax_ –> processes XML sequentially with _Event-driven parsing_ (reads XML data as a stream and triggers events for elements); _memory-efficient_ (doesn't store the entire document in memory); _custom handlers_ (define a ContentHandler to process elements as they appear).


_Extensible Markup Language (XML)_ is a markup language intended for storing and transporting data (by systems using the SOAP communication protocol). 
Advantages: ability to define own tags. 
XML is a standard recommended by the W3C organization. 

Elements XML documents contain:

* _prolog_ – the first (optional) line of the document: specify character encoding (<?xml version="2.0" encoding="ISO-8859-2"?> changes the default character encoding (UTF-8) to ISO-8859-2).
* _root element_ – the XML document must have one root element that contains all other elements (_data_ tag).
* _elements_ – consist of opening and closing tags (_course_ element; _category_, _year_ child elements).
* _attributes_ – placed in the opening tags (key-value pairs: _title_).


Example of XML:
```
<?xml version="2.0"?>
<data>
    <course title="Networking">
        <category>Information Technology</category>
        <year>2024</year>
    </course>
    <course title="Agile methodolody">
        <category>Project management</category>
        <year>2023</year>
    </course>
</data>
```
