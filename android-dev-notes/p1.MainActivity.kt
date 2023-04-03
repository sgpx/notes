package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val fooButton: android.widget.Button = findViewById(R.id.foo_button)
        val barButton: android.widget.Button = findViewById(R.id.bar_button)
        fooButton.setOnClickListener {
            val t: Toast = Toast.makeText(this, "foo toast", Toast.LENGTH_LONG)
            t.show()
        }

        barButton.setOnClickListener {
            val t: Toast = Toast.makeText(this, "bar toast", Toast.LENGTH_LONG)
            t.show()
        }
    }
}
