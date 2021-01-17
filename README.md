# Vector_Notifications

This script will alert you via a notification to your phone if Vector becomes stuck somewhere and can't free himself.

It uses an app called Pushover which handles the notifications recieved on your phone.
Pushover offer a 7 day free trial and then theres a one-off payment of £4.99 if you want to continue using it.*

If Vector becomes stuck, he will start a countdown. If he does not get free by the end of the countdown, Vector will take a photo using his camera, and send a notification along with the photo to your mobile phone or smartwatch, even if you're away from home!.
The script will keep checking if Vector is stuck and will reset once he is free'd.

If Vector manages to free himslef before the countdown has elapsed, the script will reset and he will carry on his usual activities.

You will need to setup an account on Pushover here:

https://pushover.net

Download the Pushover App which is available on iOS and Android.

Once your account is setup you should get a USER KEY, you will need this to send notifications to the app. Put the USER KEY in the key.py script.

Then create a new app in the Pushover dashboard, name it what you like, I chose 'Vector Alerts' as this is what will by shown on the notification on your device.
Once your app is created, you should receive an API KEY, put this in the key.py script as well.

Enter your Vectors serial number in the serial.py script. (I do this as I have multiple Vectors using the SDK on the same machine, so this is easier than entering the serial number in the script each time).

Make sure the key.py and serial.py scripts are in the same directory as the main script (or change the paths to where they are located).

Run the vector_alert_pic.py script and you should get notifications on your linked device if Vector gets stuck!
