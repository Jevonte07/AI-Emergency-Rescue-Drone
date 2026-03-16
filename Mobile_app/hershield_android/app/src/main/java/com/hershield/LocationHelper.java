package com.hershield;

import android.content.Context;
import android.location.Location;
import android.location.LocationManager;

public class LocationHelper {

    public static String getLocation(Context context){

        LocationManager locationManager =
                (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);

        try {

            Location location =
                    locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);

            if(location != null){

                return location.getLatitude() + "," + location.getLongitude();

            }

        } catch (SecurityException e){
            e.printStackTrace();
        }

        return "0,0";
    }
}