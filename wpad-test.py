#!/usr/bin/python
#(c) PES 2013 github-wpad-test.py@vigor.co.za
import pacparser
class colour:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\036[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
pacparser.init()
pacparser.parse_pac("wpad.dat")
def printurlinfo(url):
    proxy = pacparser.find_proxy(url)
    if len(url) < 30:
       url = url + "   " + "-"*(30-len(url)) + ">" + colour.ENDC
    header = ""
    if proxy == "DIRECT":
       header = colour.OKGREEN
    url = url.replace("https://",colour.WARNING + "https://" + colour.ENDC , 1)
    url = url.replace("ftp://",colour.OKBLUE + "ftp://" + colour.ENDC , 1)
    #"%-9s %-20s %-9s %-20s"%("Location:","10-10-10-10", "Revision:", "1")
    print "%-35s %s%-20s%s"%(url, header, proxy , colour.ENDC)

print "Start."
printurlinfo("http://elephant")
printurlinfo("http://elephant.anon.co.za")
printurlinfo("http://anon-internal.sourcing.co.za")
printurlinfo("http://127.0.0.1")
printurlinfo("http://www.anon.co.za")
printurlinfo("http://blog.anon.co.za")
printurlinfo("http://www.google.com")
printurlinfo("http://www.cisco.com")
printurlinfo("http://www.is.co.za")
printurlinfo("http://www.absa.co.za")
printurlinfo("http://www.fnb.co.za")
printurlinfo("https://www.fnb.co.za")
printurlinfo("http://www.shoprite.co.za")
printurlinfo("https://www.shoprite.co.za")
printurlinfo("https://office365.com")
printurlinfo("https://microsoftonline.com")
printurlinfo("https://outlook.com")
printurlinfo("https://services.dimensiondata.com")
printurlinfo("ftp://ftp.is.co.za")
printurlinfo("ftp://ftp.fihrst.com")
print "The End."
pacparser.cleanup()


