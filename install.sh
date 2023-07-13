#!/bin/bash

CURR=$(pwd) \
	&& echo "Installing pystuff, previous working directory: $CURR" && echo \
	&& cd /tmp && git clone https://github.com/CurtisNewbie/pystuff && cd pystuff \
	&& python3 -m pip install . \
	&& rm -rf pystuff \
	&& cd $CURR