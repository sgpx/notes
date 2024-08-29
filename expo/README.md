# expo

## create project with specific expo SDK version

```
npx create-expo-app new-sdk-47-app --template expo-template-blank@sdk-47
```

## eject for specific platform

`npx expo prebuild --platform android`


old : 

`expo eject --platform android`

`expo eject --platform ios`

`expo eject` does not ask for confirmation when something is piped into it

`ls | expo eject --platform android`
`yes | expo eject --platform android`

## define version code for play store builds


use `android.versionCode` in app.json 

```json
{
...
	"android":
	{
		...,
		"versionCode":" 2
	}
}
```

android.versionCode resolves to versionCode in android/app/build.gradle

`versionCode` must be an int

https://docs.expo.dev/versions/latest/config/app/

`versionCode` as a string can cause mess up the definition of the build method and causes an ERROR like this:

```
No signature of method: build_XXX.android() is applicable for argument types: (build_XXX$_run_closure1) values: [build_XXX$_run_closure1@XXX]
```

# dev backend server URL "TypeError: Network Request Failed" workaround

set base URL as `http://10.0.2.2:$PORT`

(ubuntu)
