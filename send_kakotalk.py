from kaling import Kakao

KakaoLink = Kakao('9f7088d9cbae02c3a17e64fbf7c69329','https://dfsdfsdfsdf.pythonanywhere.com')
KakaoLink.login('10andyye.jongcye@gmail.com', 'kakao123@B')


def send_kakaotalk_1(name,number):
    KakaoLink.send(name,{
                "link_ver": "4.0",
                "template_object": {
                    "object_type": "feed",
                    "button_title": "",
            
                    "content": {
                        "title": "몸에 열이 있나요?",
                        "image_url": "https://dfsdfsdfsdf.pythonanywhere.com/static/fever.png",
                        "link": {
                            "web_url": "",
                            "mobile_web_url": ""
                        },
                        "description": "made by 상우 in IDEV"
                    },
            
                    "buttons": [{
                        "title": "37.5℃ 미만",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&1&0",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&1&0"
                        }
                    },
                    {
                        "title": "37.5℃ 이상",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&1&1",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&1&1"
                        }
                    }]
                }
            })


def send_kakaotalk_2(name,number):
    KakaoLink.send(name,{
                "link_ver": "4.0",
                "template_object": {
                    "object_type": "feed",
                    "button_title": "",
            
                    "content": {
                        "title": "감염이 의심되는 증상이 있나요?",
                        "image_url": "https://dfsdfsdfsdf.pythonanywhere.com/static/infected.png",
                        "link": {
                            "web_url": "",
                            "mobile_web_url": ""
                        },
                        "description": "made by 상우 in IDEV"
                    },
            
                    "buttons": [{
                        "title": "아니오",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&2&0",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&2&0"
                        }
                    },
                    {
                        "title": "예",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&2&1",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&2&1"
                        }
                    }]
                }
            })

def send_kakaotalk_3(name,number):
    KakaoLink.send(name,{
                "link_ver": "4.0",
                "template_object": {
                    "object_type": "feed",
                    "button_title": "",
            
                    "content": {
                        "title": "본인 또는 동거인이 방역당국에 의해 현재 자가격리가 이루어지고 있나요?",
                        "image_url": "https://dfsdfsdfsdf.pythonanywhere.com/static/isolation.png",
                        "link": {
                            "web_url": "",
                            "mobile_web_url": ""
                        },
                        "description": "made by 상우 in IDEV"
                    },
            
                    "buttons": [{
                        "title": "아니오",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&3&0",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&3&0"
                        }
                    },
                    {
                        "title": "예",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&3&1",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&3&1"
                        }
                    }]
                }
            })



send_kakaotalk_1("예상우",1)
send_kakaotalk_2("예상우",1)
send_kakaotalk_3("예상우",1)