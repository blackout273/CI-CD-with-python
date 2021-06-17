from .index_injetavel import html

def app(environ, start_response):
    data = html
    status = "200 ok"
    headers=[('Content-type', 'text/html')]
    start_response(status,headers)
    return [data]
def somar(x,y):
    return (x+y)