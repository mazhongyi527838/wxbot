# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
import library

list_send_data = ["111","2222","3333"]
class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "mazhongyi14789" #请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            print Argument
            return Argument
    def POST(self):
        try:
            webData = web.data()
            #print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            #print recMsg.content
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                msgId = recMsg.MsgId
                content = list_send_data[int(msgId)%2]
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif recMsg.MsgType == "image":
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            elif recMsg.MsgType == "event":
                if recMsg.Event == "subscribe":
                    content = library.event_dict["subscribe"]
                    print content
                    print toUser
                    print fromUser
                    print content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                else :
                    pass


            elif recMsg.MsgType == "image":
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            print "出现异常"
            return Argment
