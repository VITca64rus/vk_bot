import vk
import time
#Васин токен
#session = vk.Session(access_token='d2c6fbed1ca379b65428f9187dfd191cd9eb3812336d0c08a483d521a06a6f33802e7c93ec8bee255d630')
#Мой токен



def get_friends(token, id):
    session = vk.Session(access_token=token)
    api = vk.API(session)
    try:
        id_user = (api.users.get(user_ids=id, v=5.71)[0]['id'])
        friends_id=(api.friends.get(user_id=id_user,v=5.71)['items'])
    except:
        members = api.groups.getMembers(group_id=id,v=5.71)
        count = members['count']
        offset = 1000
        members = members['items']
        while offset < count:
            members.extend(api.groups.getMembers(group_id=group_id, count=1000, offset=offset, v=5.71)['items'])
            offset += 1000
        friends_id=members
    return(friends_id)

def send_message(token, id_for_send, msg):
    session = vk.Session(access_token=token)
    api = vk.API(session)
    id_for_send = int(api.users.get(user_ids=id_for_send, v=5.71)[0]['id'])
    #try:
    api.messages.send(user_id=id_for_send,message=msg,random_id=0,v=5.71)
    #except:
     #   print('Избежал капчу')

def invite_to_group(token, group_id, user_id):
    session = vk.Session(access_token=token)
    api = vk.API(session)
    group_id=int(api.groups.getById(group_id=group_id, v=5.71)[0]['id'])
    user_id = int(api.users.get(user_ids=user_id, v=5.71)[0]['id'])
    try:
        api.groups.invite(group_id=group_id, user_id=user_id, v=5.71)
    except:
        print('некая ошибка')

def save_fotos(token, p_id):
    session = vk.Session(access_token=token)
    api = vk.API(session)
    p_id = int(api.users.get(user_ids=p_id, v=5.71)[0]['id'])
    imgs = []
    i=0
    can = True
    while can:
        last_i=i
        photos = api.messages.getHistoryAttachments(peer_id=p_id, media_type='photo', start_from=i, count=200, v=5.71,photo_sizes=0,preserve_order=1)['items']
        print ('*' * 10)
        print (i)
        print(photos)
        for photo in photos:
            try:
                i=photo['message_id']
                dict = photo ['attachment'] ['photo']
                del dict ['album_id']
                del dict ['date']
                del dict ['id']
                del dict ['owner_id']
                del dict ['has_tags']
                del dict ['access_key']
                del dict ['height']
                del dict ['text']
                del dict ['width']
                keys = list (dict.keys ())
                razm = []
                for key in keys:
                    razm.append (int (key [6:]))
                imgs.append (photo ['attachment'] ['photo'] ['photo_{}'.format (max (razm))])
                print(photo ['attachment'] ['photo'] ['photo_{}'.format (max (razm))])
            except:
                pass
        if i==last_i:
            can=False
    return(imgs)
#invite_to_group('203465624', 'vasyatk_a')

#send_message('miss_korogodskaya','Ты красная подруга?')

#print(api.messages.getHistory(peer_id=13116147,v=5.71))
#send_message('miss_korogodskaya','Я же умный кот)')
