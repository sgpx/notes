# expo

## eject for specific platform

`expo eject --platform android`

`expo eject --platform ios`

`expo eject` does not ask for confirmation when something is piped into it

`ls | expo eject --platform android`
`yes | expo eject --platform android`

~~## define version code for play store builds~~ (can cause errors)

use `android.versionCode` in app.json 
```json
{
...
	"android":
	{
		...,
		"versionCode":"2.0"
	}
}
```
https://docs.expo.dev/versions/latest/config/app/

android.versionCode resolves to versionCode in android/app/build.gradle

which interferes with the definition of the method and causes an ERROR like this:

```
No signature of method: build_XXX.android() is applicable for argument types: (build_XXX$_run_closure1) values: [build_XXX$_run_closure1@XXX]
```
