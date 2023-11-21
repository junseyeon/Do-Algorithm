# -*- coding: utf-8 -*-
import sys
le = list(sys.stdin.readline().split())
if le == ['R','G','B'] or le == ['G','B','R'] or le == ['B','R','G']: print('possible')
else: print('impossible')