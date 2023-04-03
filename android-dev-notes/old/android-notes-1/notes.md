# 1.kt

`ERR_CACHE_MISS` error in webview 1.kt occurs because of missing android.permission.INTERNET in AndroidManifest.xm

# 1.build.gradle

buildscript block: build and configuration information
actually create your project

groovy works on a plugin system

you can write your own plugin that does a task

and plug it into the build pipeline

`classpath "com.android.tools.build:gradle:7.0.2"` -> provides android specific config to build your app
`classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:1.5.31"` -> takes care of compiling kotlin code within project

dependencies follow maven project object model (POM)

groupId:artifactId:versionId

# 2.build.gradle

API level build gradle

specific to project config

`android` block: configures android specific configuration settings

- compileSdkVersion: API level of app
- buildToolsVersion: version of build tools used to build app
- defaultConfig: base configuration of app
- applicationId: unique identifier for google play
- minSdkVersion: minimum API level supported by app
- targetSdkVersion: API level targeted by app
- versionCode: specifies version code of app
- versionName: user friendly name of version
- testInstrumentationRunner: test runned used to run UI tests
- buildTypes: configures app to create a release build. `minifyEnabled` will shrink app size by removing unused code and obfuscate app
- compileOptions: language level of java source code `sourceCompatibility` and bytecode `targetCompatibility`
- kotlinOptions: jvm library used by `kotlin gradle` plugin (jvmTarget = '1.8')

`dependencies` block specifies libraries used by app on top of Android SDK

- `implementation` : internal dependencies not exposed, compilation is faster

# ====
# 1.gradle.properties

sets project wide gradle settings

# ====
# 1.settings.gradle

shows modules used by app

on creating a project there will only be one module "[name-of-applicaton]" but more more modules can be created

`implementation 'com.google.android.material:material:1.4.0'` inside `./app/build.gradle` api level gradle build file specifies the material ui design package


# ====
# 1.themes.xml

located at ./app/src/main/res/values/themes.xml

material dependency in build.gradle is used to apply material design themes

# ====
# 1.kt

`import` statements import libraries

`class MainActivity : AppCompatActivity()` means MainActivity is extending the AppCompatActivity class

`:` in kotlin is used for both extending classes and implementing interfaces

`override` keyword in kotlin `override fun onCreate` specifies you are implementing the required oncreate function

`ic_launcher_background.xml/ic_launcher_foreground.xml` => launcher icon of app in vector format, used by `ic_launcher.xml` in API 26+

`activity_main.xml` => layout file. 

`ConstraintLayout` viewgroup allows precise positioning of views

`TextView` displays text through the android:text attribute

xml namespaces in `ConstraintLayout` tag

xmlns:android refers to android specific namespace

xmlns:app namespace for anything not in the android SDK

ConstraintLayout is not part of the main android SDK

xmlns:tools workspace for adding metadata to XML

most important attributes of android XML layout file are `android:layout_width` and `android:layout_height`

`wrap_content` big enough to enclose content only

`match_parent` sized according to size of parent

`LinearLayout` lays out views vertically or horizontally

`FrameLayout` usually displays single child view

`RelativeLayout` is a simple version of ConstraintLayout

`ic_launcher.png` icons are PNG files having icons for different density of devices

`nodpi` => density independent resources

`ldpi` => 120 dpi screens

`mdpi` => 160 dpi screens

`hdpi` => 240 dpi screens

`xhdpi` => 320 dpi

`xxhdpi` => 480 dpi

`xxxhdpi` => 640dpi

`tvdpi` => TV resources 213 dpi

# ====
# 1.colors.xml

colors can be defined in tags inside colors.xml

`<color name="purple_200">#FFBB86FC</color>`

transparency controlled by two extra hex characters

`<color name="colorBlue">#0000FF</color>`
`<color name="colorBlue50PercentTransparent">#770000FF</color>`

# ====
# strings.xml

`<string name="app_name">myapp</string>`

