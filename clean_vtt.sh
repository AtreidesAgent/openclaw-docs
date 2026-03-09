#!/bin/zsh
awk 'BEGIN{IGNORECASE=1} /WEBVTT/{next} /^[0-9]+/{next} /^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9]{3} --> /{next} /^$/{next} {gsub(/&lt;[^&gt;]*&gt;/, "", $0); gsub(/^[ \\t]+|[ \\t]+$/, "", $0); if (length($0) > 0) print $0}' "$1" > "$2"
