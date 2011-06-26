# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: __init__.py 39 2008-02-21 18:04:38Z s0undt3ch $
# =============================================================================
#             $URL: http://devnull.ufsoft.org/svn/BlixTheme/trunk/__init__.py $
# $LastChangedDate: 2008-02-21 18:04:38 +0000 (Thu, 21 Feb 2008) $
#             $Rev: 39 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2007 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

from os.path import join, dirname

TEMPLATE_FILES = join(dirname(__file__), 'templates')
SHARED_FILES = join(dirname(__file__), 'shared')

def setup(app, plugin):
    app.add_theme('blix_theme', TEMPLATE_FILES, plugin.metadata)
    app.add_shared_exports('blix_theme', SHARED_FILES)

