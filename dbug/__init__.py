#
# Copyright 2018 Léo Flaventin Hauchecorne
# You can do every damn thing you want with this file and its content, except put it
# in a nuclear bomb, except if it is for starting a fusion reaction for reasearch purpose or
# to produce civil energy.
#
# Disclaimer : However, I won't waranty any thing happend following the use of this file

import inspect
import sys

# Debug stream. On each function, if not provided, it will use this value.
_Dstream = sys.stderr

# Indent string. Used by indented version of the functions to prepend i * indent
_Dindent_str = '  '

# Each function F exists in 2 flaviours : 
# F() : normal
# nF() : adds a newline before

# Each function accepts as keyword-only arguments : 
# i : indent level
# indent_str : indent string
# stream : stream where to write

def getFrameList():
  """Get stack from the caller (outside this module)"""
  stack = inspect.stack()
  return stack[next( i for i, v in enumerate(stack) if v.filename != __file__ ):]

def Dindent(n, indent_str=None, stream=None, **kwargs):
  """Print indentation (without ending new_line)"""
  if stream is None :
    stream = _Dstream
  if indent_str is None :
    indent_str = _Dindent_str
  print(_Dindent_str * n, file=stream, end='')
  
def DNL(stream=None, **kwargs):
  """Print an empty line in debug stream"""
  if stream is None :
    stream = _Dstream
  print(file=stream)
  
def D(*args, i=0, stream=None, **kwargs):
  """Print args indented at ith level in stream stream"""
  if stream is None :
    stream = _Dstream
  Dindent(i, stream)
  print(*args, file=stream, **kwargs)

def nD(*args, **kwargs):
  DNL()
  D(*args, **kwargs)

# *D*ebugging *W*here *A*m *I*
def getDWAI():
  """return "function(args) # file:line
  /!\ The values display are the values of these variables at the moment of the call to the xDWAI().
  If these parameters have been changed, it's their latest value that is printed"""
  stack = getFrameList()
  last = stack[0]
  function = last.function
  frame = last.frame
  module = inspect.getmodulename(last.filename)
  args = inspect.formatargvalues(*inspect.getargvalues(last.frame))
  if module :
    function = f'{module}.{function}'
  return f'{function}{args} # {last.filename}:{last.lineno}'

def DWAI(**kwargs):
  """function(args) # file:line"""
  D(getDWAI(), **kwargs)
  
def nDWAI(**kwargs):
  DNL(**kwargs)
  DWAI(**kwargs)

def getDvar1(v):
  frame = getFrameList()[0].frame
  g = frame.f_globals
  l = frame.f_locals
  return f'{v} = {eval(v, g, l)}'

def Dvar(*args, **kwargs):
  """Dvar(*v, **kwargs)
  Print f'{i*Dindent}{v} = {eval(v)} for each v as argument"""
  for a in args :
    D(getDvar1(a), **kwargs)

def nDvar(*args, **kwargs):
  DNL()
  Dvar(*args, **kwargs)




class Dbug(object):
  """
  Class to memorize indentlevel and stream
  """
  def __init__(self, stream=sys.stderr, indent_str='  '):
    self.stream = stream
    self.indent_str = indent_str
    self.indent_level = 0
  
  def indent(self, i=None, *args, **kwargs):
    Dindent(i=(i if i is not None else self.indent_level), stream=self.stream, *args, **kwargs)

  def NL(self, *args, **kwargs):
    DNL(stream=self.stream, *args, **kwargs)

  def __call__(self, *args, i=None, **kwargs):
    D(*args, i=(i if i is not None else self.indent_level), stream=self.stream, **kwargs)

  def WAI(self, *, i=None, **kwargs):
    DWAI(i=(i if i is not None else self.indent_level), stream=self.stream, **kwargs)

  def var(self, *args, i=None, **kwargs):
    Dvar(*args, i=(i if i is not None else self.indent_level), stream=self.stream, **kwargs)

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self.stream.close()

dbug = __import__(__name__)

__all__ = ['dbug', 'getFrameList', 'Dindent', 'DNL', 'D', 'nD', 'getDWAI', 'DWAI', 'nDWAI', 'getDvar1', 'Dvar', 'nDvar', 'Dbug']
    


