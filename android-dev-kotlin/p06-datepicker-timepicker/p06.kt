package com.example.myapplication

import android.app.DatePickerDialog
import android.app.TimePickerDialog
import android.os.Build
import android.os.Bundle
import android.widget.*
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import java.util.*

class MainActivity : AppCompatActivity() {
    @RequiresApi(Build.VERSION_CODES.N)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val myButton = findViewById<Button>(R.id.my_button)
        val myCalendar = Calendar.getInstance()
        val myTextView = findViewById<TextView>(R.id.txt1)

        myButton.setOnClickListener {
            Toast.makeText(this, "Button was pressed", Toast.LENGTH_LONG).show()
            var displayText : String = "";
            var currentDate = "Current Date: ${myCalendar.get(Calendar.YEAR)}-${myCalendar.get(Calendar.MONTH)}-${
                myCalendar.get(Calendar.DATE)
            } ${myCalendar.get(Calendar.HOUR)}:${myCalendar.get(Calendar.MINUTE)}:${
                myCalendar.get(
                    Calendar.SECOND
                )
            }"
            myTextView.text = displayText

            DatePickerDialog(this, { _: DatePicker, year: Int, month: Int, dayOfMonth: Int ->
                run {
                    TimePickerDialog(this,
                        { _: TimePicker, hourOfDay: Int, minute: Int ->
                            run {
                                displayText = "Selected Date: $year-$month-$dayOfMonth $hourOfDay:$minute\n$currentDate"
                                myTextView.text = displayText
                            }
                        }, 1, 1, false
                    ).show()
                }
            }, 2020, 1, 1).show()
        }
    }
}