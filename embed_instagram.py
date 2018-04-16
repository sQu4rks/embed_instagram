import re
import requests
import json
from pelican import signals
from pelican import contents

def exec_insta(instance):
    if type(instance) in (contents.Article, contents.Page):
        pattern = re.compile(r"\[INSTA\].*?\[/INSTA\]")
        found_ids = pattern.findall(instance._content)
        insta_ids = []
        if found_ids is not None and len(found_ids) > 0:
            for found in found_ids:
                insta_ids.append(str(found).replace("[INSTA]","").replace("[/INSTA]",""))
            print("Found Instagram Ids " + ",".join(insta_ids) + " in " + str(instance))
        # Request embedding code and replace
        content_str = instance._content
        for e in insta_ids:
            res = requests.get("https://api.instagram.com/oembed?url=http://instagr.am/p/{}".format(e))
            if res.status_code == requests.codes.ok:
                json_out = json.loads(res.content)
                id_block = "[INSTA]{}[/INSTA]".format(e)
                print("Replacing " + str(id_block) + " with " + json_out['html'])
                content_str = content_str.replace(id_block, "<center>" + json_out['html'] + "</center>")
        instance._content = content_str

def register():
    signals.content_object_init.connect(exec_insta)
