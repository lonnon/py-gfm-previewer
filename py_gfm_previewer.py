import io

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

with io.open('/home/lonnon/.zsh/puree/readme.md', mode='r', encoding="utf-8") as mfile:
    data = mfile.read()
    html = markdown.markdown(data, extensions=[GithubFlavoredMarkdownExtension()])
    with io.open('/tmp/mdtest.html', 'w') as hfile:
        hfile.write(html)
