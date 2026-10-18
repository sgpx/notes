#!/bin/bash
pacmd list-sinks
pacmd set-sink-input-mute $SINK_INDEX
pulseaudio -k
