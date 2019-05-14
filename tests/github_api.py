# -*- coding: utf-8 -*-
# --- author: wtavares


from web_app.functions import *

data = github_get_update_data()

if len(data) == 0:
    print("NO DATA FOUND!")

print("{} ITEMS FOUND".format(len(data)))

for i in data:
    print("Name: {0}, ID {1}, Lang: {2}, Stars {3} ".format(i['name'],
                                                            i['id'],
                                                            i['language'],
                                                            i['stargazers_count']
                                                            ))

