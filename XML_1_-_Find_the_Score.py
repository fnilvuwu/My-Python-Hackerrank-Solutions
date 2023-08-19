
def get_attr_number(node):
    attr_num = 0
    attr_num += len(node.attrib)
    for i in node:
        attr_num += len(i.attrib)
        for j in i:
            attr_num += len(j.attrib)
    return attr_num