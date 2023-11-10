import dataclasses
import re

from src.shared.helpers.errors.domain_errors import EntityParameterError

@dataclasses.dataclass
class Schedule:
  _url: str
  
  def __init__(self, url):
    if (type(url) != str):
      raise EntityParameterError("url")
    if not re.search(r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&=\/]*)", url):
      
      raise EntityParameterError("url")
    self._url = url
  
  @property
  def url(self):
    return self._url
  
  @url.setter
  def url(self, value):
    if (type(value) != str):
      raise EntityParameterError("url")
    if not re.search(r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&=\/]*)", value):
      raise EntityParameterError("url")
    
    self._url = value