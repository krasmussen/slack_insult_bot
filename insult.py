# -*- coding: utf-8 -*-

from .base import MessageHandler
import requests
import HTMLParser
import re

class InsultHandler(MessageHandler):

  TRIGGER_ANCHOR = ''
  TRIGGER_PREFIX = ''
  TRIGGERS = ['!insult']
  HELP = 'sends an insult optionally insults a user with !insult @[username]'

  def handle_message(self, event, triggers, query):
    print query
    try:
        response = requests.get('http://www.insultgenerator.org/')
        return_message = response.text[431:response.text.find('</div>\n<center>')]
        # Don't bother checking for insult @ user if the remaining message is blank
        if query.strip() != '':
            # Check for @ to send an insult @ a user or something
            user_check = re.search('(?<=@)\w+', query)
            if user_check:
                # Apparently slack replaces user strings with user ids on the backend lets try to convert that back
                user_string = user_check.group()
                user_lookup = self.client.api_call('users.info', user=user_string)
                if user_lookup.get('ok',False):
                    user_name = user_lookup.get('user', {}).get('name','')
                else:
                    user_name = user_string
                return_message = '@%s: %s' %(user_name, return_message)
        # handle html unescaping
        h = HTMLParser.HTMLParser()
        return_message = h.unescape(return_message)
        return return_message
    except Exception as E:
        return E
