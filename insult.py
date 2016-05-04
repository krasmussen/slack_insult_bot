# -*- coding: utf-8 -*-

from .base import MessageHandler
import requests

class InsultHandler(MessageHandler):

  TRIGGER_ANCHOR = ''
  TRIGGER_PREFIX = ''
  TRIGGERS = ['!insult']
  HELP = 'sends an insult optionally insults a user with !insult [username]'

  def handle_message(self, event, triggers, query):
    try:
        response = requests.get('http://www.insultgenerator.org/')
        return_message = response.text[431:response.text.find('</div>\n<center>')]
        if query.strip() != '':
            return_message = '@%s: ' %(query) + return_message
        return return_message
    except Exception as E:
        return E

