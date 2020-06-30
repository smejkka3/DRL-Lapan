#!/usr/bin/env bash
xvfb-run -s "-screen 0 640x480x24 +extension GLX" ./02_play.py -m $1 -r $2
