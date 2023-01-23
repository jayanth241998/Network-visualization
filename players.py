import tweepy
import pandas as pd
import time
api_key= "HIdjAPlrhJinYeJl6kXmyIQaQ"
api_secretkey = "UEYpynFWlqGa8VGHlcNXCKhy4hKAmYHcfMpWsuON6w2N0CAKGJ"
access_token = "925025173778063361-jGd0OuDv9rWjEk0CXrDJ3xBiUn3kJJZ"
access_secretoken = "yQb23gm1HCy3hoL0ZraZVNgU1Tgx1RngWP8SvRIi82DsW"
#auth = tweepy.OAuthHandler(api_key,api_secretkey)
#auth.set_access_token(access_token,access_secretoken)
#api = tweepy.API(auth)
bearer_token = "AAAAAAAAAAAAAAAAAAAAABIOlQEAAAAABrJGIdCFEwrdJhiAXSsWFDjmH%2F0%3DvIiXXdwkboDzOcRwFNnAw71lmY2DbdFHaOfCFbFjI09rQEujJr"  # BEARER_TOKEN
client = tweepy.Client(bearer_token)
user = client.get_user(username="NBA")
NBALists = client.get_owned_lists(user.data.id)
response = NBALists.data
NBAListID = [x for x in response if x.name=="NBA Players"][0]
players = []
token = None
endoflist = False
while(True):
    playersResponse = client.get_list_members(NBAListID.id,pagination_token=token)
    players.extend(playersResponse.data)
    meta = playersResponse.meta
    token = meta.get('next_token')
    if(token == None):
        break

players1 = players[0:4]
print("number of players: ",len(players))

playerdf = pd.DataFrame(players1)

writer = pd.ExcelWriter('NBAPlayers.xlsx', engine='xlsxwriter')

playerdf.to_excel(writer)

writer.close()
edges = []

for x in players1:
    followingList = client.get_users_following(x.id).data
    for y in followingList:
        if y in players:
            edges.append((x.username,y.username))


print(edges)

playerdf = pd.DataFrame(edges)

writer = pd.ExcelWriter('NBAfollow.xlsx', engine='xlsxwriter')

playerdf.to_excel(writer)

writer.close()




#data = json.loads(followers.data)
##print(followers)

