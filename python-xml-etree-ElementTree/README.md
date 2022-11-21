# import 

```python3
from xml.etree import ElementTree as et
```

# read from string


```python3
root = et.fromstring(xml_raw)
```

# export to string

```python3
xml_raw = et.tostring(root)
```

# register namespace

use before parsing


```python3
et.register_namespace("android","http://schemas.android.com/apk/res/")
```

# find list of all elements with specified tags or paths

```python3
list(et.iterfind("xyz"))
```

# get attributes of element

```python3
print(root.attrib)
```

# set attribute of element

```python3
root.attrib["abc"] = "xyz"
```
