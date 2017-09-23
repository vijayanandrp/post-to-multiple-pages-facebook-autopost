# -*- coding: utf-8 -*-
import os

from facepy import GraphAPI


class FbPageAPI:
    def __init__(self, _access_token, limit=250):
        self.access_token = _access_token
        self.graph = GraphAPI(self.access_token)
        self.accounts = self._get_accounts(limit)

    def _get_accounts(self, limit=250):
        self.accounts = self.graph.get('me/accounts?limit=' + str(limit))
        return self.accounts['data']

    def get_accounts(self):
        return self.accounts['data']

    def get_page_access_token(self, _page_id):
        for data in self.accounts:
            if _page_id == data['id']:
                page_access_token = data['access_token']
                print('access_token: ', page_access_token)
                print('id: ', data['id'])
                print('name: ', data['name'])
                return page_access_token
        else:
            return None

    @staticmethod
    def post_in_page(page_access_token, page_id, image_file=None, message=None):
        page_graph = GraphAPI(page_access_token)
        print('Posting .....')

        if not message:
            message = '.'

        if image_file:
            image_file = open(image_file, 'rb')
            page_graph.post(path=page_id+'/photos', source=image_file, message=message)
        else:
            page_graph.post(path=page_id+'/feed', message=message)


    def create_new_page_directories(self, media_path):
        count = 1
        # check for new directories
        for data in self.accounts:
            print(count, ' - ', 'id: ', data['id'])
            print(count, ' - ', 'name: ', data['name'])
            count += 1
            page_id = data['id']
            page_name = data['name'].replace(' ', '_')
            page_path = os.path.join(media_path, page_name)
            page_file = os.path.join(page_path, '__' + page_id + '__')
            if not os.path.exists(page_path):
                os.makedirs(page_path)
                if not os.path.isfile(page_file):
                    with open(page_file, 'w') as fp:
                        fp.write(page_id + '\n')


if __name__ == '__main__':

    # ENTER YOUR ACCESS TOKEN + PAGE ID 
    access_token = ''
    page_id = ''
    image_file = 'test.jpeg'
    media_path = os.path.join(os.getcwd(), 'media')

    fb = FbPageAPI(_access_token=access_token)

    fb.create_new_page_directories(image_file)

    fb.post_in_page(fb.get_page_access_token(page_id), page_id, message='GOOD MORNING <3 <3')
