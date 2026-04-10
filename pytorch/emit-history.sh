function emit() { for i in $(ls ex*py); do ls -l $i | sed -r "s/.+staff  //" ; echo === ; cat $i ; echo === ; done }

emit > ~/tmp.txt
