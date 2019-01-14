import base64
import markdown
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="default.css" rel="stylesheet">
    <link href="github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret


class MarkdownReport:
    def __init__(self):
        self.str_buffer = []
        self.img_buffer = []

    def write_h1(self, line):
        self.str_buffer.append("# " + line)

    def write_h2(self, line):
        self.str_buffer.append("## " + line)

    def write_h4(self, line):
        self.str_buffer.append("#### " + line)

    def write_line(self, line):
        self.str_buffer.append(line)

    def write_pandas(self, p_data):
        self.str_buffer.append(p_data.to_html())

    def write_img(self, img_name, img_data):
        base64_img = base64.b64encode(img_data)
        self.img_buffer.append("[%s]:data:image/png;base64,%s" % (img_name, base64_img))
        self.str_buffer.append("![avatar][%s]" % img_name)

    def save_html(self, output_path):
        f = open(output_path, "w")
        result = "\n".join(self.str_buffer) + "\n" + "\n".join(self.img_buffer)
        f.write(md2html(result))
        f.close()

    def save_markdown(self, output_path):
        f = open(output_path, "w")
        result = "\n".join(self.str_buffer) + "\n" + "\n".join(self.img_buffer)
        f.write(result)
        f.close()


