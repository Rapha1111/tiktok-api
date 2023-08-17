import requests, json

def getUserInfo(username):
  #on obtiens l'user id de countik
  user_info = requests.get("https://countik.com/api/exist/"+username).json()
  user_id=user_info["id"]
  nickname=user_info["nickname"]
  #on obtiens maintenant les donnés de l'utilisateur
  user_data = requests.get("https://countik.com/api/userinfo/"+user_id).json()
  user_data["nickname"]=nickname
  return user_data


def getUserVideo(username):
  #on obtiens l'user id de countik
  user_info = requests.get("https://countik.com/api/exist/"+username).json()
  user_secuid=user_info["sec_uid"]
  #on obtiens tt les donnés
  user_data = requests.get("https://countik.com/api/analyze/?sec_user_id="+user_secuid).json()
  return user_data["videos"]
  
def getVideo(video):
  if "tiktok.com" in video: #est-ce que c'est l'url ?
    video_url=video
  else: #on a que l'id de la video
    try:
      m=int(video) #est ce que l'id de la video est sous la forme chiffre ?
      return requests.get("https://countik.com/api/videoinfo/"+video).json()
    except: #id de type lettre
      video_url="https://vm.tiktok.com/"+video
  return requests.post("https://countik.com/api/video/exist", data=json.dumps({"url":video_url}), headers={"Content-Type": "application/json"}
).json()

#https://countik.com/api/videoinfo/7267055581465218336
#https://countik.com/api/videoinfo/