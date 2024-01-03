from xml import sax


class opendrivehandler(sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""

    # 开始标签时调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "road":
            r_id = attributes["id"]
            r_length = attributes["length"]
            print("*****Road*****")
            print("the length of road {0} is {1}m".format(r_id, r_length))

    # 结束标签时调用
    def endElement(self, tag):
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        pass


if __name__ == "__main__":
    # 创建一个新的XMLReader
    parser = sax.make_parser()
    # 关闭namespaces
    parser.setFeature(sax.handler.feature_namespaces, 0)
    # 重写Handler
    Handler = opendrivehandler()
    parser.setContentHandler(Handler)
    parser.parse("one road.xodr")
