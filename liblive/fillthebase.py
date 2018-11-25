from liv.models import Author
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append('liblive')



list = ['Антон', 'Ваня', 'Петя']


print('succes!')
'''
for name in list:
    author = Author()
    author.name = name
    author.save()
'''