#!/bin/bash

CURR=$(pwd) \
	&& echo "Installing pystuff, previous working directory: $CURR" && echo \
	&& cd /tmp \
	&& echo "Cloing pystuff to /tmp" && echo \
	&& git clone https://github.com/CurtisNewbie/pystuff --depth 1 && python3 -m pip install pystuff \
	&& rm -rf pystuff \
	&& echo "/tmp/pystuff removed" \
	&& cd $CURR