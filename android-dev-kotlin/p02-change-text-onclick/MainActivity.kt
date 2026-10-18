package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val myButton = findViewById<Button>(R.id.mybutton)
        val myText = findViewById<TextView>(R.id.mytext)
        var x = 0;

        myButton.setOnClickListener {
            Log.d("123", "456")
            x += 1;
            val y = "counter: $x"
            myText.text = y
        }
    }
}
