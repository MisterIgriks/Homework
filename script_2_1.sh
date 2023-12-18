#!/bin/bash

distribution=$(lsb_release -si 2>/dev/null)

if [ "$distribution" != "Ubuntu" ]; then
    echo "Error: This script is intended for Ubuntu distribution only."
    exit 1
fi

echo "Collecting CPU usage for the last hour..."
sar -u 3600 1 > cpu-usage.log
