def app(environ, start_response):
    data = b"<h1>Ola Muno</h1>"
    status = "200 ok"
    headers=[('Content-type', 'text/html')]
    start_response(status,headers)
    return [data]
def test_logico(x,y):
    return (x+y)