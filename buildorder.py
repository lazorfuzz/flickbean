#!/home/apolysec/dev/Python-2.7.8/python
import flickbean, cgi, cgitb, Cookie, base64

def check_cart():
    if environ.has_key('HTTP_COOKIE'):
        cookie_string=environ.get('HTTP_COOKIE')
        c=Cookie.SimpleCookie()
        c.load(cookie_string)
        try:
            value = c['Cart'].value
            cart = base64.b64decode(value).split('|')
        except: return None
        return cart
    return None

form = cgi.FieldStorage()
formtype = form.getvalue('formtype')
bean = form.getvalue('bean')
roast_type = form.getvalue('roasttype')
amount = form.getvalue('amount')
grinded = form.getvalue('grinded')
packaging = form.getvalue('packaging')
instructions = form.getvalue('instructions')
checkout = form.getvalue('checkout')
bean_list = ['magdalena', 'bourbon', 'vecinos']
phones = ['4083910180@vtext.com', '4087064249@vtext.com', '4087060872@vtext.com']

if roast_type and not checkout:
    c = Cookie.SimpleCookie()
    c['Cart'] = base64.b64encode(bean + '|' + roast_type+ '|' + amount + '|' + grinded + '|' + packaging + '|' + instructions)
    c['Cart']['expires'] = 'Fri, 31 Dec 9999 23:59:59 GMT'
    print c

print 'Content-type: text/html\r\n'

if not formtype and not checkout:
    print '<script>window.location = "coffee.flick";</script>'
    exit()

if formtype == 'order':
    with open('buildorder.leon') as f:
        html = base64.b64decode(f.read())
    html = html.replace('BEANTYPE', bean)
    print html
    exit()

if checkout:
    with open('checkout.leon') as f:
        html = base64.b64decode(f.read())
    if not check_cart() and not roast_type: print html; exit();
    if not check_cart() and roast_type:
        cart_proto = '''<div class='col-md-8 col-md-offset-2' id='shadbox'>
                                <h2 style='text-align: center;'>Finalize Build</h2>
                                <div class='row'>
                                  <div class='col-md-12'>
                                    <p id='finalbeantype'>Bean: BEANTYPE</p>
                                    <p id='finalroasttype'>Roast: ROASTTYPE</p>
                                    <p id='finalamount'>Amount: AMOUNT</p>
                                    <p id='finalgrinded'>Grinded: YES</p>
                                    <p id='finalpackage'>Packaging: PACKAGING</p>
                                    <p id='finalinstructions'>Additional Instructions: INSTRUCTS</p>
                                  </div>
                                </div>
                                </div>'''
        cart_proto = cart_proto.replace('BEANTYPE', bean)
        cart_proto = cart_proto.replace('ROASTTYPE', roast_type)
        cart_proto = cart_proto.replace('AMOUNT', amount)
        cart_proto = cart_proto.replace('YES', grinded)
        cart_proto = cart_proto.replace('PACKAGING', packaging)
        cart_proto = cart_proto.replace('INSTRUCTS', instructions)
        html = html.replace('<!--CARTHTML-->', cart_proto)
        print html