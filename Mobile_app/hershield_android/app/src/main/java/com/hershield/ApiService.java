package com.hershield;

import retrofit2.Call;
import retrofit2.http.POST;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Field;

public interface ApiService {

    @FormUrlEncoded
    @POST("sos")
    Call<String> sendSOS(
            @Field("name") String name,
            @Field("location") String location
    );
}