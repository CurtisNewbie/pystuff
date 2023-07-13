#!/bin/bash

CURR=$(pwd) \
	&& echo "Installing pystuff, previous working directory: $CURR" && echo \
	&& cd /tmp \
	&& echo "Cloing pystuff to /tmp" && echo \
	&& git clone https://github.com/CurtisNewbie/pystuff && cd pystuff \
	&& python3 -m pip install . \
	&& rm -rf pystuff \
	&& cd $CURR