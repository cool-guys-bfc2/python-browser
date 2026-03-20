from pyscript import web
out=web.page["output"]
def echo(html):
    out.innerHtml+='<br/>'+html
def run():
    #Add your code here
    echo('Hi from python!')
