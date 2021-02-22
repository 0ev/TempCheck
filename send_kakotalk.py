from kaling import Kakao

KakaoLink = Kakao('87d3bd176110c4c614b5a877cbdf6eee','https://dfsdfsdfsdf.pythonanywhere.com')
KakaoLink.login('10andyye.jongcye@gmail.com', 'kakao123@B')


def send_kakaotalk(name,number):
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
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&"+str(number)+"&0",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&"+str(number)+"&0"
                        }
                    },
                    {
                        "title": "37.5℃ 이상 및 발열감",
                        "link": {
                            "web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&"+str(number)+"&1",
                            "mobile_web_url": "https://dfsdfsdfsdf.pythonanywhere.com/check/"+name+"&"+str(number)+"&1"
                        }
                    }]
                }
            })

send_kakaotalk("예상우",1)