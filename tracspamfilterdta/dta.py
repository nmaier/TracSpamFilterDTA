# -*- coding: utf-8 -*-
# License: public domain
# Author: Nils Maier <testnutzer123 at googlemail>

import re

from trac.config import IntOption
from trac.core import *
from tracspamfilter.api import IFilterStrategy

PATTERNS = ('dta', 'downthemall', 'pref reload', 'chrome://dta')

class DtaFilterStrategy(Component):
    implements(IFilterStrategy)

    karma_points = IntOption(
            'spam-filter',
            'dta_karma',
            '7',
            "By how many points will a match improve the Karma for dTa related Submissions"
            )

    def __init__(self):
        self.patterns = []
        for p in PATTERNS:
            self.patterns += re.compile(re.escape(p.strip()), re.I),

    # IFilterStrategy implementation

    def test(self, req, author, content):
        points = 0
        for pattern in self.patterns:
            match = pattern.search(content)
            if match:
                self.log.debug('Pattern %r found in submission',
                               pattern.pattern)
                points += abs(self.karma_points)
        if points != 0:
            return points, 'Content contained dta whitelisted patterns'

    def train(self, req, author, content, spam=True):
        pass
