import re
import os

for f in os.listdir("./"):
    fpath = f
    if not f.endswith(r'.md'):
        continue
    if not f.startswith(r'2'):
        continue

    ret = re.findall(r'\d{4}-\d{2}-\d{1,2}', f)
    f = re.sub(r'\d{4}-\d{2}-\d{1,2}', '', f)
    if len(ret) == 0:
        continue
    date = ret[0]
    title = f.strip('-').strip('.md')

    header = """---
layout: post
title:  {}
toc: true 
excerpt: 
date:   {}
---
""".format(title, date)
    lines = [line for line in open(fpath, encoding='utf8')]

    lines.insert(0, header)
    with open(fpath, 'w', encoding='utf8') as fp:
        fp.write(''.join(lines))

