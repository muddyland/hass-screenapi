from django.http import JsonResponse
import json
import subprocess
from .decorators import * 

@key_check
def index(request):
    return JsonResponse({"message":"Hello, world. This is just a dumb api"})

# Command to turn off the monitor
off_command = ["xset", "-display", ":0", "dpms", "force", "off"]
# Comamnd to turn on the monitor
on_command = ["xset", "-display", ":0", "dpms", "force", "on"]
# This will print out all the info about the screen, which we can parse to see if the monitor is on
status = ["xset", "-display", ":0", "q"]

# Get Status of monitor
def is_on():
  run = subprocess.run(status, stdout=subprocess.PIPE)
  if "Monitor is On" in str(run.stdout):
    return True
  else:
    return False

# If post, check for action and apply if needed
# If Get, return the status of the moitor. this allows Home Assistant to poll for the status
@key_check
def monitor(request):
  if request.method == "POST":
    body = request.body
    do_action = json.loads(body)
    if do_action.get("on") and is_on() == False:
      run = subprocess.run(on_command)
      return JsonResponse({'success': "True", "exit_code" : run.returncode })
    elif do_action.get("off") and is_on():
      run = subprocess.run(off_command)
      return JsonResponse({'success': "True", "exit_code" : run.returncode })
    else:
      return JsonResponse({"no_action": True})

  elif request.method == "GET":
    return JsonResponse({"status" : is_on()})
  else:
    return JsonResponse({'err':'Wrong method'}, status=400)
