from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print("->", i[0],">", i[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print("->", i[0],">", i[1])

# instantiate the parser and fed it some HTML
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
