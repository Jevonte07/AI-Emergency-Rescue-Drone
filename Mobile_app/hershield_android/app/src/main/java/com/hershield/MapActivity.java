package com.hershield;

import android.os.Bundle;
import androidx.fragment.app.FragmentActivity;
import com.google.android.gms.maps.*;
import com.google.android.gms.maps.model.*;

public class MapActivity extends FragmentActivity implements OnMapReadyCallback {

    GoogleMap map;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map);

        SupportMapFragment mapFragment =
                (SupportMapFragment) getSupportFragmentManager()
                        .findFragmentById(R.id.map);

        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {

        map = googleMap;

        LatLng victim = new LatLng(13.0827, 80.2707);
        LatLng drone = new LatLng(13.0837, 80.2717);

        map.addMarker(new MarkerOptions().position(victim).title("Victim"));
        map.addMarker(new MarkerOptions().position(drone).title("Drone"));

        map.moveCamera(CameraUpdateFactory.newLatLngZoom(victim, 15));
    }
}