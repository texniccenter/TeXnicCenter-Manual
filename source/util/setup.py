# Copyright (c) 2011 Sergiu Dotenco
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import gettext, locale, os, sys, re, docutils.nodes
from sphinx import addnodes
from docutils.parsers import rst
from docutils.parsers.rst import roles

current_locale, encoding = locale.getdefaultlocale()

translation = gettext.translation('util', os.path.dirname(__file__) +
  '/locale', [current_locale])
translation.install()

html_keys = {
  'enter': u'\u21B5 ' + _('Enter'),
  'backspace': u'\u2190 ' + _('Backspace'),
  'tab': u'\u21B9 ' + _('Tab'),
  'shift': u'\u21E7 ' + _('Shift'),
  'capslock': u'\u21E9 ' + _('Caps Lock'),
  'cmd': u'\u2318'
}

plain_keys = {
  'enter': _('Enter'),
  'backspace': _('Backspace'),
  'tab': _('Tab'),
  'shift': _('Shift'),
  'capslock': _('Caps Lock'),
  'cmd': _('Command')
}

html_shortcut_sep = ' + '
latex_shortcut_sep = '+'
escape = '|'
latex_keystroke = open(os.path.dirname(__file__)+'/keystroke.tex', 'r').read()
latex_preamble = latex_keystroke

def extract_nodes(text, keys):
  tokens = filter(None, re.split('\+(\+|[^\+]*\+$|[^\+]+)', text))
  result = []

  for value in tokens:
    try:
      value = keys[value]
    except KeyError:
      pass

    result.append(value)

  nodes = []

  for value in result:
    nodes.append(value)

  return nodes


class shortcut(docutils.nodes.Element): pass

def visit_shortcut_latex(self, node):
  nodes = extract_nodes(node['text'], plain_keys)

  for text in nodes:
    if is_escaped(text):
      self.body.append(unescape(text))
    else:
      self.body.append(r'\keystroke{' + text + '}')

    self.body.append(latex_shortcut_sep)

  self.body.pop()

  raise docutils.nodes.SkipNode


def visit_shortcut_html(self, node):
  nodes = extract_nodes(node['text'], html_keys)

  for text in nodes:
    if is_escaped(text):
      self.body.append(unescape(text))
    else:
      self.body.append('<kbd>' + text + '</kbd>')

    self.body.append(html_shortcut_sep)

  self.body.pop()

  raise docutils.nodes.SkipNode


def parse_cmakevar(env, sig, signode):
  c = '='
  v = sig.split(c)

  node = addnodes.desc_name

  if len(v) != 2:
    signode += node(sig, sig)
  else:
    param = v[0]
    value = v[1]

    signode += node(param, param)
    signode += docutils.nodes.generated(c, c)
    signode += docutils.nodes.emphasis(value, value)

    sig = param

  return sig


def is_escaped(t):
  return t.startswith(escape) and t.endswith(escape)


def unescape(t):
  return t[1:-1]


def shortcut_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
  return ([shortcut(text=text)], [])


def setup(app):
  app.add_stylesheet('keypress.css')
  app.add_object_type('cmakevar', 'cmakevar', _('%s (CMake variable)'),
      parse_cmakevar)
  
  app.add_node(shortcut, latex=(visit_shortcut_latex, None),
      html=(visit_shortcut_html, None))
  app.add_role('shortcut', shortcut_role)
