# components

building blocks of android apps

coupled by `AndroidManifest.xml`

- activities: UI
- services: background tasks
- broadcast receivers: communication between OS and apps
- content providers: data and database management

## example - activities

```
public class MyActivity extends Activity {
}
```

## example - services 

```
public class MyService extends Service {}
```

## example - broadcast receivers

```
public class MyReceiver extends BroadcastReceivers {
	public void onReceive(context, intent){}
}
```

## example - content providers

```
public class MyContentProvider extends  ContentProvider {
   public void onCreate(){}
}
```

## additional components

- fragments : portion of UI in an activity
- views : elements drawn on screen
- layouts : hierarchies controlling apprearance of views
- intents : messages between components
- resources : external elements like strings text pictures or colors
- manifest : config file for app


