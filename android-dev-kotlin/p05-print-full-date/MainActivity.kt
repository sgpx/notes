package com.example.myapplication

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import java.util.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val myButton = findViewById<Button>(R.id.my_button)
        val myCalendar = Calendar.getInstance()
        val myTextView = findViewById<TextView>(R.id.txt1)

        myButton.setOnClickListener {
            Toast.makeText(this, "Button was pressed", Toast.LENGTH_LONG).show()
            val displayText = "${myCalendar.get(Calendar.YEAR)}/${myCalendar.get(Calendar.MONTH)}/${myCalendar.get(Calendar.DATE)} ${myCalendar.get(Calendar.HOUR)}:${myCalendar.get(Calendar.MINUTE)}:${myCalendar.get(Calendar.SECOND)}"
            //val displayText = "The year is ${myCalendar.get(Calendar.YEAR)}"
            myTextView.text = displayText
        }
    }
}
