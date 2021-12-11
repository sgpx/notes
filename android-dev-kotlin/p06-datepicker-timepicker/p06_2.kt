package com.example.myapplication

import android.app.DatePickerDialog
import android.app.TimePickerDialog
import android.os.Build
import android.os.Bundle
import android.widget.*
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import java.text.SimpleDateFormat
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
            var selectedDate = ""
            val currentDate =
                "${myCalendar.get(Calendar.YEAR)}-${myCalendar.get(Calendar.MONTH) + 1}-${
                    myCalendar.get(Calendar.DATE)
                } ${myCalendar.get(Calendar.HOUR)}:${myCalendar.get(Calendar.MINUTE)}"
            myTextView.text = selectedDate

            DatePickerDialog(this, { _: DatePicker, year: Int, month: Int, dayOfMonth: Int ->
                run {
                    TimePickerDialog(
                        this,
                        { _: TimePicker, hourOfDay: Int, minute: Int ->
                            run {
                                selectedDate =
                                    "$year-${month + 1}-$dayOfMonth $hourOfDay:$minute"


                                val xyz = SimpleDateFormat("yyyy-MM-dd HH:mm")
                                val d1: Date = xyz.parse(currentDate)!!
                                val d2: Date = xyz.parse(selectedDate)!!
                                val diff = (d1.time - d2.time)/(1000*3600*24)
                                //d1.time - d2.time
                                val displayText =
                                    "Selected: $selectedDate\nCurrent Date: $currentDate\ndiff: $diff days"
                                myTextView.text = displayText


                            }
                        }, 1, 1, false
                    ).show()
                }
            }, 2021, 11, 1).show()
        }
    }
}