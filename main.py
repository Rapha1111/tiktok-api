from flask import Flask
import api

app = Flask('app')

@app.route('/profile/<username>')
def profile(username):
  user_data = api.getUserInfo(username)
  #maintenant on met les data en forme pour coller a la demande
  data_a_return = {
  'userInfo': {
    'stats': {
    'followerCount': user_data["followerCount"],
    'followingCount': user_data["followingCount"],
    'heartCount': user_data["heartCount"],
  },
  'user': {
    'avatarMedium': user_data["avatarThumb"],
    'nickname': user_data["nickname"],
    'secUid': user_data["sec_uid"],
    'signature': '#pas obtenu'
  }
  }
}
  return data_a_return

@app.route("/profile/<username>/feed")
def feed(username):
  user_video = api.getUserVideo(username)
  user_data = api.getUserInfo(username)
  #maintenant on met les data en forme pour coller a la demande
  data_a_return = {"ItemList":[]}
  for i in user_video:
    video_data = {
      "id":i["id"],
      "author":{
        "avatarMedium":user_data["avatarThumb"]
      },
      "stats":{
        "playCount":i["plays"],
        "shareCount":i["shares"],
        "commentCount":i["comments"],
        "diggCount":"c'est quoi ?"
      },
      "video":{
        "cover":i["cover"],
        "description":i["desc"]
      }
    }
    data_a_return["ItemList"].append(video_data)
  return data_a_return

@app.route("/video/<videoid>")
def video(videoid):
  video=api.getVideo(videoid)
  video_data = {
      "id":video["id"],
      "author":{
        "avatarMedium":"pas obtenu"
      },
      "stats":{
        "playCount":video["plays"],
        "shareCount":video["shares"],
        "commentCount":video["comments"],
        "diggCount":"c'est quoi ?"
      },
      "video":{
        "cover":video["cover"],
        "description":video["desc"]
      }
    }
  return video_data
app.run(host='0.0.0.0', port=80)