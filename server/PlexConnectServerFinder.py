import time
import urllib2

class Finder():
  ip = '0.0.0.0'
  last_update = 0
  def get_ip(self):
    now = time.time();
    print (now - self.last_update)
    if (now - self.last_update) < 5:
      print 'Using PlexConnect server recently found at ' + self.ip
      return self.ip

    self.last_update = now

    for i in range(50, 100, 1):
        _ip = "192.168.1." + str(i)
        url = "http://" + _ip + "/plexconnect"
        req = urllib2.Request(url)
        try:
          handler = urllib2.urlopen(req, timeout=0.1)
          if not handler.headers.getheader('X-PlexConnect'):
            continue
          else:
            print 'PlexConnect server found at ' + _ip
            self.ip = _ip
            return self.ip
        except urllib2.URLError, e:
          continue
    self.ip = '0.0.0.0'
    return self.ip