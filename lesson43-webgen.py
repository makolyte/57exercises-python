import os


def createSite(sitename, author, wantJS, wantCSS):
    html = """
    <html>
        <head>
            <title>{0}</title>
            <meta name='author' content='{1}'>
        </head>
        <body/>
    </html>
        """

    pathTemplate = "{0}/{1}"

    os.makedirs(sitename)
    if wantJS:
        os.makedirs(pathTemplate.format(sitename, "js"))
    if wantCSS:
        os.makedirs(pathTemplate.format(sitename, "css"))

    with open(pathTemplate.format(sitename, "index.html"), 'w') as htmlFile:
        htmlFile.write(html.format(sitename, author))

createSite("lesson43website", "Mac", True, False)