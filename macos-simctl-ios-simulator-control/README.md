# simctl

control ios simulators from command line

## list running simulators and their IDs

`xcrun simctl list | grep -i booted`

## installing simulator apps

`xcrun simctl install XXXXXXXX-XXXX-XXXX-XXXX-XXXXYYYYZZZZ myProj.app`

## launching apps

`xcrun simctl launch XXXXXXXX-XXXX-XXXX-XXXX-XXXXYYYYZZZZ com.myProj.identifier`

returns a PID

## enabling verbose logs

`xcrun simctl logverbose $SIMULATOR_ID enable`

## getting logs for a process

`xcrun simctl spawn booted log stream  --level="debug" --process 36562`
