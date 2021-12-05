# 01 

## linear layout 

`<LinearLayout></LinearLayout>`

A layout that arranges other views either horizontally in a single column or vertically in a single row.

### adjusting alignment

use `android:gravity`

`android:gravity="center"`
`android:gravity="center_horizontal"`
`android:gravity="center_vertical"`

## adding color values to colors.xml

add

```xml
<color name="myColor">#FF00FF</color>
```

to `app/src/main/res/values/colors.xml`


```bash
a=$(app/src/main/res/values/colors.xml)
cat $a | sed -r "s/<\/resources>//" > tmp.txt;
echo '<color name="white">#FFFFFF</color>' >> tmp.xml
echo '</resources>' > $a
```
