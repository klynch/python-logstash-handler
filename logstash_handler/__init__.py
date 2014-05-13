from logging.handlers import SocketHandler
import ssl

class LogstashHandler(SocketHandler):
  """
  Sends output to an optionally encrypted streaming logstash TCP listener.
  """

  def __init__(self, host, port, keyfile=None, certfile=None, ssl=True):
    SocketHandler.__init__(self, host, port)
    self.keyfile = keyfile
    self.certfile = certfile
    self.ssl = ssl


  def makeSocket(self, timeout=1):
    s = SocketHandler.makeSocket(self, timeout)
    if self.ssl:
      return ssl.wrap_socket(s, keyfile=self.keyfile, certfile=self.certfile)
    return s


  def makePickle(self, record):
    """
    Just format the record according to the formatter. A new line is appended to
    support streaming listeners.
    """
    return self.format(record) + "\n"
