# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)

    elif msg_type == 'event':
        return EventMsg(xmlData)
class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        #self.MsgId = xmlData.find('MsgId').text

#接收到的为文字信息
class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")
        self.MsgId = xmlData.find('MsgId').text
#接收到的为图片信息
class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
        self.MsgId = xmlData.find('MsgId').text

#接收到的为事件信息，比如关注和取消关注等
class EventMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Event = xmlData.find('Event').text



