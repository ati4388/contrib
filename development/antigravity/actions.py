#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."
NoStrip = ["/"]



def install():
     pisitools.insinto("/opt/Antigravity", "Antigravity/*")
    #pisitools.insinto("/opt/", "*")
    #pisitools.dosym("/opt/antigravity/bin/antigravity", "/usr/bin/antigravity")
