import itchat

#注册个人消息
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

    if u'作者' in msg['Text'] or u'主人' in msg['Text']:
        return u'xie'
        # itchat.send('@img@applaud.gif', msg['FromUserName'])
        #  there should be a picture
    elif u'回复' in msg['Text']:
        return u'我是机器人'
    elif u'这么快' in msg['Text']:
        return u'我是机器人'
    else:
        #return get_response(msg['Text']) or u'' + msg['Text']
        return msg['Text']
    # return  实现自动回复给发消息的人

#注册群消息
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        #msg.user.send(u'@%s\u2005I received: %s' % ( msg.actualNickName, msg.text))
        print(msg['Text'])
    else:
        print(msg['Text'])


def send_news():
    itchat.auto_login(hotReload=True)
    myfriends = itchat.get_friends()
    count = 0
    message = '群发测试信息'
    for myfriends in myfriends:
        # print(myfriends)
        if myfriends['RemarkName']:
            print(myfriends['RemarkName'])
            print(myfriends["UserName"])
            # itchat.send(message, toUserName=myfriends["UserName"])
            # time.sleep(0.5)
            count += 1
            print('发送成功')
    print(count)

def main():
    send_news()
# hotReload(热加载),短时间内不需要再次扫码登陆
#为了能方便的关掉，所以没有使用热加载，需要热加载的可以参考注释代码
itchat.auto_login(hotReload=True)
#itchat.auto_login()
itchat.run()

if __name__ == '__main__':
    main()