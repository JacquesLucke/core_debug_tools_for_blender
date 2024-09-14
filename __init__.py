# SPDX-FileCopyrightText: See AUTHORS file
#
# SPDX-License-Identifier: GPL-2.0-or-later

from . import node_tree

modules = (node_tree,)


def register():
    for m in modules:
        m.register()


def unregister():
    for m in reversed(modules):
        m.unregister()
