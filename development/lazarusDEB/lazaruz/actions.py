#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

Version = get.srcVERSION()
WorkDir = "."
NoStrip = ["/"]

def setup():
    shelltools.system("pwd")
    #lazarus-project_4.6.0-0_amd64.deb
    shelltools.system("ar xf lazarus-project_4.6.0-0_amd64.deb")
    shelltools.system("tar xf data.tar.zst")

def install():
   pisitools.insinto("/etc", "./etc/*")
   pisitools.insinto("/usr", "./usr/*")
   


