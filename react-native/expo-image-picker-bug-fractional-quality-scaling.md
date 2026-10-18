# this works

```
    await ExpoImagePicker.getMediaLibraryPermissionsAsync();
    const res = await ExpoImagePicker.launchImageLibraryAsync({
      mediaTypes: ExpoImagePicker.MediaTypeOptions.Images,
      base64: true,
    });
```

# this crashes

```
    await ExpoImagePicker.getMediaLibraryPermissionsAsync();
    const res = await ExpoImagePicker.launchImageLibraryAsync({
      mediaTypes: ExpoImagePicker.MediaTypeOptions.Images,
      base64: true,
      quality: 0.5,
    });
```
