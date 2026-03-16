package com.hershield;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    Button sosButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        sosButton = findViewById(R.id.sosButton);

        sosButton.setOnClickListener(v -> {

            Intent intent = new Intent(MainActivity.this, SOSActivity.class);
            startActivity(intent);

        });
    }
}