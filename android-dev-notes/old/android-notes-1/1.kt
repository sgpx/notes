// app to load google.com in webview
// remember to add internet permission in AndroidManifest.xml
// <uses-permission android:name="android.permission.INTERNET" />
package com.example.a1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val webView = WebView(this)
        webView.loadUrl("https://google.com/")
        webView.settings.javaScriptEnabled = true
        setContentView(webView)
    }
}
