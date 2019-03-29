#!/usr/bin/env python
from core import console
from core import token
con = console.pyConsole()
import os, sys
try:
    import requests
except Exception as e:
    print con.Err(e.message + '!\n')

class FacebookUP:

    def __init__(self, title):
        self.title = title
        console.set_windowTitle(self.title)

    def post_toWall(self, message, token):
        self.message = str(message)
        self.message.replace(' ', '+')
        self.token = token
        if not message:
            print con.Err('please enter message to post !\n')
            sys.exit(1)
        else:
            try:
                print con.Proc('updating...!')
                requests.post('https://graph.facebook.com/me/feed/?message=' + self.message + '&access_token=' + self.token)
                print con.Succ('success !\n')
            except requests.exceptions.ConnectionError as e:
                print con.Err(str(e))
                print con.Err('failed !\n')
                sys.exit(1)
            except requests.exceptions.HTTPError as e:
                print con.Err(str(e))
                print con.Err('failed !\n')
                sys.exit(1)
            except requests.exceptions.Timeout as e:
                print con.Err(str(e))
                print con.Err('failed !\n')
                sys.exit(1)

    def post_photoWithCaption(self, image, caption, token):
        self.image = str(image)
        self.caption = str(caption)
        self.token = token
        try:
            img = open(self.image, 'rb')
        except Exception as e:
            print con.Err(str(e))
            print con.Err('failed !\n')
            sys.exit(1)
        else:
            if not self.caption:
                print con.Err('please enter caption !n')
                sys.exit(1)
            else:
                try:
                    files = {'source': img}
                    print con.Proc('uploading...')
                    requests.post('https://graph.facebook.com/me/photos?access_token=' + self.token + '&message=' + self.caption, files=files)
                    print con.Succ('success !\n')
                except requests.exceptions.ConnectionError as e:
                    print con.Err(str(e))
                    print con.Err('failed !\n')
                    sys.exit(1)
                except requests.exceptions.HTTPError as e:
                    print con.Err(str(e))
                    print con.Err('failed !\n')
                    sys.exit(1)
                except requests.exceptions.Timeout as e:
                    print con.Err(str(e))
                    print con.Err('failed !\n')
                    sys.exit(1)

    def post_photoNoCaption(self, image, token):
        self.image = str(image)
        self.token = token
        try:
            img = open(self.image, 'rb')
        except Exception as e:
            print con.Err(str(e))
            print con.Err('failed !\n')
            sys.exit(1)
        else:
            try:
                files = {'source': img}
                print con.Proc('uploading...')
                requests.post('https://graph.facebook.com/me/photos?access_token=' + self.token, files=files)
                print con.Succ('success !\n')
            except requests.exceptions.ConnectionError as e:
                print con.Err(str(e))
                print con.Err('failed !\n')
                sys.exit(1)
            except requests.exceptions.HTTPError as e:
                print con.Err(str(e))
                print con.Err('failed !\n')
                sys.exit(1)
            except requests.exceptions.Timeout as e:
                print con.Err(str(e))
                print con.Err('failed !\n')
                sys.exit(1)
