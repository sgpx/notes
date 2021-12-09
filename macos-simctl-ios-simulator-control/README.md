# simctl

control ios simulators from command line

## list running simulators and their IDs

`xcrun simctl list | grep -i booted`

## installing simulator apps

`xcrun simctl install XXXXXXXX-XXXX-XXXX-XXXX-XXXXYYYYZZZZ myProj.app`

## installing 

`xcrun simctl launch install XXXXXXXX-XXXX-XXXX-XXXX-XXXXYYYYZZZZ com.myProj.ext`
