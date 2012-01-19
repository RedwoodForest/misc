#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2012 Lawrence Johnston
# Licensed under the MIT license. See http://opensource.org/licenses/MIT
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# Attribution appreciated.

# Dumps a TextMate bundle's tab trigger and key equivalent shortcuts to the console.
# The name of the bundle to dump can be set via the bundleName variable.
# Can be run by opening this file in TextMate and running it via ⌘-R or via the console.

import os
import plistlib

bundleName = "OpenSCAD"
snippetsDir = os.path.expanduser("~/Library/Application Support/TextMate/Bundles/%s.tmbundle/Snippets" % bundleName)

snippetFiles = os.listdir(snippetsDir)

plists = []
for snippetFile in snippetFiles:
    filePath = os.path.join(snippetsDir, snippetFile)
    plists.append(plistlib.readPlist(filePath))

for plist in plists:
    plist.setdefault("")
    name = plist["name"];
    
    keyEquivalentKey = "keyEquivalent"
    plist.setdefault(keyEquivalentKey);
    
    tabTriggerKey = "tabTrigger"
    plist.setdefault(tabTriggerKey);
        
    shortcut = plist[keyEquivalentKey] or (
                plist[tabTriggerKey] and plist[tabTriggerKey] + u"⇥");
    
    if shortcut:
        print("%s: %s" % (shortcut, name))