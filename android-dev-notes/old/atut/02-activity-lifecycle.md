   activity launch 
\-> onCreate()
\-> onStart()
\-> onResume() [when user returns to activity from onPause() ]
\-> activity running
\-> onPause() [when another activity comes to foreground]
\-> onStop() [no longer visible]
\-> onDestroy() [finished by system]


onStop() -> onRestart() when activity is reopened

if an app with higher priority needs memory, the current activity is stopped with onStop()



