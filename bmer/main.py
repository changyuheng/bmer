#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage:
    bmer [-i <exec> <alias>]
    bmer [-r <name>]

    -i, --install   install
    -r, --remove    remove

    manage executable file
"""

import os
import sys
import docopt
import re

config = {
        'dir'       : os.path.join(os.environ['HOME'], '.config', 'bmer'),
        'conf'      : os.path.join(os.environ['HOME'], '.config', 'bmer', 'conf.py'),
        'installed' : os.path.join(os.environ['HOME'], '.config', 'bmer', 'installed.py'),
}

conf = None
installed = None

def parse_conf():
    if not os.path.exists(config['conf']):
        return None

    return eval(open(config['conf']).read())


def parse_installed():
    if not os.path.exists(config['installed']):
        return None

    return eval(open(config['installed']).read())

def install(path, alias):
    global conf, installed
    if not os.path.exists(path):
        raise Exception(path + ' not exists')


    abspath = os.path.abspath(path)
    if alias is None:
        symName = os.path.basename(path)
    else:
        symName = alias

    despath = os.path.expanduser(os.path.join(conf['path'], symName))
    try:
        os.symlink(abspath, despath)

        print('install %s as %s in %s' % (abspath, symName, conf['path']))
        if installed is None:
            installed = dict()
        installed[symName] = abspath

        with open(config['installed'], 'w') as fi:
            fi.write(str(installed))
    except OSError as e:
        print(despath + ' exists')
        raise e

def remove(name):
    despath = os.path.expanduser(os.path.join(conf['path'], name))
    if not os.path.exists(despath):
        raise Exception(despath + ' not exists')

    try:
        os.remove(despath)
        print('remove %s success' % name)

        installed.pop(name)
        with open(config['installed'], 'w') as fi:
            fi.write(str(installed))
    except OSError as e:
        raise e

def display_installed():
    for name, path in installed.iteritems():
        print("%s : %s" % (name, path))

def main():
    global conf, installed
    args = docopt.docopt(__doc__, options_first=True)
    #print(args)
    if not os.path.exists(config['dir']):
        os.mkdir(config['dir'])

    conf = parse_conf()
    installed = parse_installed()

    try:
        if args['--install']:
            install(args['<exec>'], args['<alias>'])
        elif args['--remove']:
            remove(args['<name>'])
        else: #display installed list
            display_installed()
    except Exception as e:
        print(e)
        exit(1)

if __name__ == '__main__':
    main()
