from .parser import Lark_StandAlone
from sys import argv

parser = Lark_StandAlone()

with open(argv[1]) as f:
  print(parser.parse(f.read()).pretty())
