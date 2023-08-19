from xml.etree.ElementTree import XMLParser
maxdepth = 0
def depth(elem, level):
    class MaxDepth:                     # The target object of the parser
        maxDepth = 0
        depth = 0
        def start(self, tag, attrib):   # Called for each opening tag.
            self.depth += 1
            if self.depth > self.maxDepth:
                self.maxDepth = self.depth
        def end(self, tag):             # Called for each closing tag.
            self.depth -= 1
        def close(self):    # Called when all data has been parsed.
            return self.maxDepth
    
    target = MaxDepth()
    parser = XMLParser(target=target)
    parser.feed(etree.tostring(elem))
    global maxdepth
    maxdepth = parser.close() - 1
