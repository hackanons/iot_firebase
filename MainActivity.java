package com.example.root.led_control;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity {

    Button on;
    Button off;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        on = (Button) findViewById(R.id.on);
        off = (Button) findViewById(R.id.off);

        on.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                FirebaseDatabase database = FirebaseDatabase.getInstance();
                DatabaseReference myRef = database.getReference("LED_STATUS");

                myRef.setValue(1);

            }
        });

        off.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                FirebaseDatabase database = FirebaseDatabase.getInstance();
                DatabaseReference myRef = database.getReference("LED_STATUS");

                myRef.setValue(0);

            }
        });

    }
}
