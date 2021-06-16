def app(environ, start_response):
    data = b"<h1>Ola Mundo</h1>"
    status = "200 ok"
    headers=[('Content-type', 'text/html')]
    start_response(status,headers)
    return [data]
def somar(x,y):
    return (x+y)