package com.hmkcode.android;
 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.apache.http.NameValuePair;

import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import android.app.Activity;
import android.content.Context;
 
public class MainActivity extends Activity {
	String lat,log;
    EditText etResponse;
    TextView tvIsConnected;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	
    	ListView list;
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //LocationManager mylocman=(LocationManager)getSystemService(Context.LOCATION_SERVICE);
		//LocationListener myloclist=new MylocListener();
		//mylocman.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, myloclist);
        // get reference to the views
        etResponse = (EditText) findViewById(R.id.etResponse);
        tvIsConnected = (TextView) findViewById(R.id.tvIsConnected);
 
        // check if you are connected or not
        if(isConnected()){
            tvIsConnected.setBackgroundColor(0xFF00CC00);
            tvIsConnected.setText("You are conncted");
        }
        else{
            tvIsConnected.setText("You are NOT conncted");
        }
 
        
        //http://dashboardlynn.herokuapp.com/
        	new HttpAsyncTask().execute("http://dashboardlynn.herokuapp.com/users/?format=json");
        // call AsynTask to perform network operation on separate thread
        //new HttpAsyncTask().execute("http://10.0.2.2:8000/users/?format=json");
    }
public class MylocListener implements LocationListener{
		
		public void onLocationChanged(Location loc){
		String text="My location is Latitude ="+ loc.getLatitude()+"Longitude="+loc.getLongitude();
		lat=loc.getLatitude()+"";
		log=loc.getLongitude()+"";
		updateDatabase();
		}
		
	   public void onProviderDisabled(String provider){
		
	   }
	   public void onProviderEnabled(String provider){
		
	   }
	   public void onStatusChanged(String  provider,int status ,Bundle extras){
		   
	   }
	 }
  public void updateDatabase(){
	 
  }
    public static void POST(String url2){
   	 // Creating HTTP client
       HttpClient httpClient = new DefaultHttpClient();
       // Creating HTTP Post
       HttpPost httpPost = new HttpPost(
               "http://10.0.2.2:8000/users/");

       // Building post parameters
       // key and value pair
       List<NameValuePair> nameValuePair = new ArrayList<NameValuePair>(2);
       nameValuePair.add(new BasicNameValuePair("username", "the_user"));
       nameValuePair.add(new BasicNameValuePair("email",
               "userzzz@gmail.com"));

       // Url Encoding the POST parameters
       try {
           httpPost.setEntity(new UrlEncodedFormEntity(nameValuePair));
       } catch (UnsupportedEncodingException e) {
           // writing error to Log
           e.printStackTrace();
       }

       // Making HTTP Request
       try {
           HttpResponse response = httpClient.execute(httpPost);

           // writing response to log
           Log.d("Http Response:", response.toString());
       } catch (ClientProtocolException e) {
           // writing exception to log
           e.printStackTrace();
       } catch (IOException e) {
           // writing exception to log
           e.printStackTrace();

       }
   }
   
    
    public static String GET(String url) {
        InputStream inputStream = null;
        String result = "";
        System.out.print("here");
        try {
 
            // create HttpClient
            HttpClient httpclient = new DefaultHttpClient();
 
            // make GET request to the given URL
            HttpResponse httpResponse = httpclient.execute(new HttpGet(url));
 
            // receive response as inputStream
            inputStream = httpResponse.getEntity().getContent();
            JSONObject json=null;
            // convert inputstream to string
            if(inputStream != null)
            	
                result = convertInputStreamToString(inputStream);
            else
                result = "Did not work!";
 
        } catch (Exception e) {
            Log.d("InputStream", e.getLocalizedMessage());
        }
 
        return result;
    }
 
    private static String convertInputStreamToString(InputStream inputStream) throws IOException{
        BufferedReader bufferedReader = new BufferedReader( new InputStreamReader(inputStream));
        String line = "";
        String result = "";
        while((line = bufferedReader.readLine()) != null)
            result += line;
 
        inputStream.close();
        return result;
 
    }
 
    public boolean isConnected(){
        ConnectivityManager connMgr = (ConnectivityManager) getSystemService(Activity.CONNECTIVITY_SERVICE);
            NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
            if (networkInfo != null && networkInfo.isConnected()) 
                return true;
            else
                return false;   
    }
    private class HttpAsyncTask extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... urls) {
             System.out.print(urls[0]);
            // System.out.print(urls[0]);
            //POST("http://10.0.2.2:8000/users");
           // return "it worked";
            return GET(urls[0]);
        }
        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {
            Toast.makeText(getBaseContext(), "Received!", Toast.LENGTH_LONG).show();
            try {
				JSONArray json =  new JSONArray(result);
				etResponse.setText(json.getJSONObject(0).getString("username"));
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				etResponse.setText("Failed2!!");
				
			}
        
            
           
       }
    }
}