#!/bin/bash
a="app/src/main/res/values/colors.xml"
cat $a | sed -r "s/<\/resources>//" > tmp.xml;
#echo '<color name="white">#FFFFFF</color>' >> tmp.xml
printf '\t<color name="white">#FFFFFF</color>' >> tmp.xml
printf '\n</resources>' >> tmp.xml
mv -v tmp.xml $a
