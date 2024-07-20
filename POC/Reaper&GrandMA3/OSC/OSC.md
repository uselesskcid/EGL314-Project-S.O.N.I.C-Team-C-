<h1 align="center">
  OSC
</h1>

<p align="center">

 <i align="center">OSC for Station 5 - Memory Sequence </i>
</p>

## Overview

We are using OSC (Open Source Control) to control Reaper and grandMA3 from Raspberry Pi, with the Master Laptop acting as a middle ground.

In our [file](https://github.com/uselesskcid/EGL314-Project-S.O.N.I.C-Team-C-POC/blob/main/Reaper%26GrandMA3/OSC/POC_FunctionStorage.py), we combined the grandMA3 and Reaper IP settings into one file.

```
# GRANDMA3 SETTINGS RIGHT HERE
MA3_IP = "192.168.254.229"		# NEW laptop IP
MA3_PORT = 8888 # GRANDMA3 Local listen port
MA3_ADDR = "/gma3/cmd" # Trigger TRUE Value
# msg = "Go Sequence wtv"


# REAPER SETTINGS RIGHT HERE
REA_IP = "192.168.254.30"		# laptop IP
REA_PORT = 6800 # REAPER Local listen port
REA_MSG = float(1) # Trigger TRUE Value
# addr = "/action"
```

We then added all necessary commands from grandMA3 and Reaper to the file.

For our sequence, we added a mixture of both grandMA3 and Reaper functions into one single sequence.
```
# SEQUENCE CODE SEQUENCE (These are functions stacked to make 1 bigger function)

def SEQ_Intro():
	MA3_Seq92()
	REA_JumpBGM()
	REA_PlayPause()
	time.sleep(60)
	REA_PlayPause()

def SEQ_OrangeBtn():
	MA3_Seq91()
	REA_JumpSuspense()
	REA_PlayPause()
	time.sleep(10)
	REA_PlayPause()

def SEQ_Win():
	MA3_Seq97()
	REA_JumpWin()
	REA_PlayPause()
	time.sleep(6)
	REA_PlayPause()
	
def SEQ_Lose():
	MA3_Seq96()
	REA_JumpLose()
	REA_PlayPause()
	time.sleep(6)
	REA_PlayPause()
```

