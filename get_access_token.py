import webbrowser


def main():
    url = (f'https://oauth.vk.com/authorize?'
           f'client_id=7867290'
           f'&redirect_uri=https://oauth.vk.com/blank.hmtl'
           f'&scope=friends,photos'
           f'&response_type=token'
           f'&display=page'
           f'&revoke=1'
           f'&version=5.131')
    webbrowser.open(url)


if __name__ == '__main__':
    main()
