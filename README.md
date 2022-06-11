# hass-screenapi
This is a simple API for Home Assistant to be able to turn off the monitor attached to a Raspberry Pi

I found myself asking: "Why does my Top monitor (which as a Raspberry Pi Dashboard on it 24/7) have to be on when I am not in the room?"

This app was created to allow me to turn off my top monitor based on the pressence on the room. When I leave, it turns off. Simple as that! 

This has only been tested on a Pi, but I assume it could apply to other Linux OSes as well. If your OS has a command to turn off the monitor, you can change the commands that run for on_command and off_command variables in the screenapi/views.py file. 

# Install
* Make sure you have pip3 installed: sudo apt install python3-pip
* pip3 install django
* Change "SECRET_KEY" in screenapi/settings.py to something strong, prefferably random, this will be the password
* python3 manage.py runserver 0:8000

Head over to Home Assistant and add the following to your configuration.yaml:
<pre>
switch:
  - platform: rest
    resource: http://{IP_OF_MACHINE}:8000/monitor/
    name: PI Monitor
    body_on: '{"on" : "true"}'
    body_off: '{"off" : "true"}'
    headers: 
      AUTH: {VALUE_FROM_SECRET_KEY}
    is_on_template: "{{ value_json.status }}"
</pre>
Restart Home assistant and you should have a shinny new switch, which controls your Raspberry Pi Monitor! 
