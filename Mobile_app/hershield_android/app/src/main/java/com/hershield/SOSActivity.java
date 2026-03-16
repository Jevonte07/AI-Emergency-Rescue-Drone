package com.hershield;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SOSActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sos);

        sendSOS();
    }

    private void sendSOS(){

        ApiService apiService = ApiClient.getClient().create(ApiService.class);

        Call<String> call = apiService.sendSOS("Jevonte","13.0827,80.2707");

        call.enqueue(new Callback<String>() {

            @Override
            public void onResponse(Call<String> call, Response<String> response) {

                Toast.makeText(SOSActivity.this,
                        "Drone dispatched",
                        Toast.LENGTH_LONG).show();
            }

            @Override
            public void onFailure(Call<String> call, Throwable t) {

                Toast.makeText(SOSActivity.this,
                        "Server error",
                        Toast.LENGTH_LONG).show();
            }
        });

    }

    private double calculateETA(double distanceKm){

        double droneSpeed = 40.0;

        return distanceKm / droneSpeed;
    }

    private void callEmergency(){

        Intent intent = new Intent(Intent.ACTION_CALL);
        intent.setData(Uri.parse("tel:100"));

        startActivity(intent);
    }
}