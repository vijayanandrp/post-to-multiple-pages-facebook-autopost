#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from facepy import GraphAPI
import configparser

_company_ = 'AWP DIGITAL SOLUTIONS'
_about_ = 'Automation software to post media in social media sites.'
_developer_ = 'Vijay Anand Pandian (https://www.github.com/vijayanandrp)'
_date_ = '26 Jan 2018'

config_file = 'fb_config.ini'


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
        """
            :param _page_id:
            :return: page_specific_token
        """
        for data in self.accounts:
            if _page_id == data['id']:
                _page_access_token = data['access_token']
                # print('access_token: ', _page_access_token)
                print('')
                print('Page id: ', data['id'])
                print('Page Name: ', data['name'])
                return _page_access_token
        else:
            return None

    @staticmethod
    def post_in_page(page_access_token, page_id, image_file=None, message=None):
        """
             Method to post the media and text message to your page you manage.
             :param page_access_token: valid api token
             :param page_id: Your page id
             :param image_file: Image File along with path
             :param message: Text
             :return: None
         """
        try:
            page_graph = GraphAPI(page_access_token)
            print('Posting .....')
            if image_file:
                image_file = open(image_file, 'rb')
                if message:
                    page_graph.post(path=page_id + '/photos', source=image_file, message=message)
                else:
                    page_graph.post(path=page_id + '/photos', source=image_file)
            else:
                if not message:
                    message = 'Hello everyone!!'
                page_graph.post(path=page_id + '/feed', message=message)
            print('Posted Successfully !! ..')
        except Exception as error:
            print('Posting failed .. ', str(error))


if __name__ == '__main__':
    config = configparser.ConfigParser()

    config.read(config_file)
    # get sections
    sections = config.sections()
    print('Config sections - ', sections)

    def config_section_map(_section):
        dict1 = {}
        options = config.options(_section)
        for option in options:
            try:
                dict1[option] = config.get(_section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    access_token = config_section_map('ACCESS_TOKEN')['access_token']
    if not access_token:
        print('Access token cannot be none. visit: https://developers.facebook.com/tools/explorer/')
        exit()

    # this token is users (don't use the global token)
    fb = FbPageAPI(access_token)
    sections.remove('ACCESS_TOKEN')

    for index, section in enumerate(sections):
        page_info = config_section_map(section)
        print(index+1, page_info)
        # get page token
        page_access_token = fb.get_page_access_token(_page_id=page_info['page_id'])
        # publish
        fb.post_in_page(page_access_token=page_access_token,
                        page_id=page_info['page_id'],
                        image_file=page_info['image_file'],
                        message=page_info['message'])
