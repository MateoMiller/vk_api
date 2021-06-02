import requests
import argparse


class Vk_Methods:
    def __init__(self, token, user_id):
        self.token = token
        self.used_id = user_id

    def get_friends(self):
        url = self.get_friends_url()
        print(url)
        info = self.get_info(url)
        if 'error' in info:
            self.print_error(info)
        else:
            self.print_friends(info)

    def get_photo_albums(self):
        url = self.get_photo_albums_url()
        print(url)
        info = self.get_info(url)
        if 'error' in info:
            self.print_error(info)
        else:
            self.print_albums(info)

    def get_friends_url(self):
        url = (f"https://api.vk.com/method/friends.get?"
               f"user_id={self.used_id}"
               f"&order=name"
               f"&count=500"
               f"&fields=nickname"
               f"&access_token={self.token}"
               f"&v=5.131"
               )
        return url

    def get_photo_albums_url(self):
        url = (f"https://api.vk.com/method/photos.getAlbums?"
               f"owner_id={self.used_id}"
               f"&count=500"
               f"&access_token={self.token}"
               f"&v=5.131"
               )
        return url

    def get_info(self, url):
        return requests.get(url).json()

    def print_error(self, json_response):
        error = json_response['error']
        print(f"Возникла ошибка {error['error_msg']}")

    def print_albums(self, json_response):
        albums = json_response["response"]["items"]
        print(f"количество альбомов={len(albums)}")
        for album in albums:
            print(f"id={album['id']}, name={album['title']}")

    def print_friends(self, json_response):
        friends = json_response["response"]["items"]
        print(f"количество друзей={len(friends)}")
        for friend in friends:
            print(f"id={friend['id']} {friend['first_name']} {friend['last_name']}")


def main():
    args = parse_args()
    print(args)
    user_id = args.id
    with open('token', 'r') as file:
        token = file.read()
    method = args.type
    vk_methods = Vk_Methods(token, user_id)
    if method == 'friends':
        vk_methods.get_friends()
    elif method == 'albums':
        vk_methods.get_photo_albums()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='Тип запроса', choices=['friends', 'albums'])
    parser.add_argument('id', help='Id пользователя, про которого хотите узнать информацию', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    main()
