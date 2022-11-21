package com.example.myapplication

import android.os.Bundle
import android.util.TypedValue
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val x = findViewById<LinearLayout>(R.id.row1)

        val tv = TextView(this)
        tv.text = "blah"
        tv.layoutParams = LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT)
        tv.setTextSize(TypedValue.COMPLEX_UNIT_SP, 50.0F)
        x.addView(tv)
    }
}