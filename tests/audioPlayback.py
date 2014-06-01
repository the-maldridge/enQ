#!/usr/bin/env python

# Add the entire audio folder to path
import sys
sys.path.insert(0, '../audio')

import audio

bus = QMixer()
bus.play(sys.argv[1])
