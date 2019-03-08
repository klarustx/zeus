#!/usr/bin/env python
# coding: utf-8

import urllib2

class AlarmHelper :
    def alarm(self,token,msg,phone_list) :
        url = "https://oapi.dingtalk.com/robot/send?access_token=" +  token
        templete = """
        {
            "msgtype": "text",
            "text": {
                "content": "%s"
            },
            "at": {
                "atMobiles": [
                    %s
                ],
                "isAtAll": false
            }
        }
        """
        at_str = ""
        for phone in phone_list :
            at_str += "\"%d\"," % (phone,)
        msg = templete % (msg,at_str,)
        print(msg)
        headers = {"Content-type": "application/json"}
        request =  urllib2.Request(url,data=msg,headers=headers)
        response =  urllib2.urlopen(request, timeout=15)
        print(response.read())

if __name__ == "__main__" :
    objAlarm = AlarmHelper()
    objAlarm.alarm("c85a0a07c228f03d80c8ad2de003f4f1abd4e809882adef89bbcbe81310c0fa8","hello,world!!!I was born!!!",[phone_numbers])


