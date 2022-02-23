#!/bin/bash
usermod --append --groups mygroup myuser
usermod -a -G mygroup myuser
