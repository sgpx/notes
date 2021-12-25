# 01 

## linear layout 

`<LinearLayout></LinearLayout>`

A layout that arranges other views either horizontally in a single column or vertically in a single row.

### adjusting alignment

use `android:gravity`

`android:gravity="center"`

`android:gravity="center_horizontal"`

`android:gravity="center_vertical"`

## row vs column arrangement

```
Set android:orientation to specify whether child views are displayed in a row or column.
```

https://developer.android.com/reference/android/widget/LinearLayout

`android:orientation="vertical"`

## adding color values to colors.xml

add

```xml
<color name="myColor">#FF00FF</color>
```

to `app/src/main/res/values/colors.xml`

```bash
#!/bin/bash
a="app/src/main/res/values/colors.xml"
cat $a | sed -r "s/<\/resources>//" > tmp.xml;
#echo '<color name="white">#FFFFFF</color>' >> tmp.xml
printf '\t<color name="white">#FFFFFF</color>' >> tmp.xml
printf '\n</resources>' >> tmp.xml
mv -v tmp.xml $a
```
