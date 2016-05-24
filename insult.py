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
    try:
        response = requests.get('http://www.insultgenerator.org/')
        return_message = response.text[431:response.text.find('</div>\n<center>')]
        # Don't bother checking for insult @ user if the remaining message is blank
        if query.strip() != '':
            # Check for @ to send an insult @ a user or something
            user_check = re.search('(?<=@)\w+', query)
            if user_check:
                return_message = '@%s: %s' %(user_check.group(), return_message)
        # handle html unescaping
        h = HTMLParser.HTMLParser()
        return_message = h.unescape(return_message)
        return return_message
    except Exception as E:
        return E
