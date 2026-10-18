package com.example.a1

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.textfield.TextInputEditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        findViewById<Button>(R.id.enter_button)?.setOnClickListener {
            val greetingDisplay = findViewById<TextView>(R.id.greeting_display)
            val firstName = findViewById<TextInputEditText>(R.id.first_name)?.text.toString().trim()
            val lastName = findViewById<TextInputEditText>(R.id.last_name)?.text.toString().trim()

            val qstr = "$firstName $lastName"
            greetingDisplay.setText("Hello $qstr")
        }
    }
}
