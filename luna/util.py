import codecs
import sys

import six


def read(filepath):
    with codecs.open(filepath, 'r', 'utf8') as f:
        content = f.read()
    return content

def write(s):
    if six.PY2:
        s = s.encode('utf8')

    s = '%s\n' % s
    sys.stdout.write(s)
