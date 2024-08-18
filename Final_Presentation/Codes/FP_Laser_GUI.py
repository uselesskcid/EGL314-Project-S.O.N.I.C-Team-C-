# THIS FILE IS INTENDED TO EXTRACT FUNCTIONS FROM FUNCTION.PY AND PLAY THEM.

import tkinter as tk
import FP_Laser_Functions as r
import FP_Laser_Sequence as l

main = tk.Tk()
main.title("Laser GUI")
laserLabel=tk.Label(main,text="Laser Control", font="20")
teamLaserThree_On_Btn = tk.Button(main, text="Laser 3 On", bg="GREEN", width=20, height=4, command=l.teamLaserThree_On)
teamLaserFour_On_Btn = tk.Button(main, text="Laser 4 On", bg="GREEN", width=20, height=4, command=l.teamLaserFour_On)
teamAllLasers_On_Btn = tk.Button(main, text="Team Lasers On", bg="GREEN", width=20, height=4, command=l.teamAllLasers_On)
teamLaserThree_Off_Btn = tk.Button(main, text="Laser 3 Off", bg="RED", width=20, height=4, command=l.teamLaserThree_Off)
teamLaserFour_Off_Btn = tk.Button(main, text="Laser 4 Off", bg="RED", width=20, height=4, command=l.teamLaserFour_Off)
teamAllLasers_Off_Btn = tk.Button(main, text="Team Lasers Off", bg="RED", width=20, height=4, command=l.teamAllLasers_Off)
EveryLaserOn_Btn = tk.Button(main, text="All Lasers On", bg="GREEN", width=20, height=4, command=l.EveryLaserOn)
EveryLaserOff_Btn = tk.Button(main, text="All Lasers Off", bg="RED", width=20, height=4, command=l.EveryLaserOff)

sequenceLabel=tk.Label(main,text="Sequence Control", font="20" )
reaper_play_btn = tk.Button(main, text="Play Reaper", bg="GREEN",command=r.REA_JumpLaserMarker,width=20,height=4)
reaper_stop_btn = tk.Button(main, text="Stop Reaper", bg="RED",command=r.REA_Stop,width=20,height=4)
ma3_play_btn = tk.Button(main, text="Play MA3 Seq 104", bg="GREEN",command=r.MA3_Seq104,width=20,height=4)
ma3_clear_btn = tk.Button(main, text="Clear MA3 Seq 104", bg="RED",command=r.MA3_Clear,width=20,height=4)
laser_btn = tk.Button(main, text="Laser Sequence Only", bg="BLUE",command=r.LaserSeq,width=20,height=4)
neopixel_btn = tk.Button(main, text="NeoPixel Sequence Only", bg="BLUE",command=r.NeoPixelSeq,width=20,height=4)
full_btn = tk.Button(main, text="Full Sequence", bg="CYAN",command=r.FullSeq,width=20,height=4)



laserLabel.grid(row=0, column=0, columnspan=2)
teamLaserThree_On_Btn.grid(row=1, column=0)
teamLaserFour_On_Btn.grid(row=2, column=0)
teamAllLasers_On_Btn.grid(row=3, column=0)

teamLaserThree_Off_Btn.grid(row=1, column=1)
teamLaserFour_Off_Btn.grid(row=2, column=1)
teamAllLasers_Off_Btn.grid(row=3, column=1)

EveryLaserOn_Btn.grid(row=4, column=0)
EveryLaserOff_Btn.grid(row=4, column=1)

sequenceLabel.grid(row=5, column=0, columnspan=2)
reaper_play_btn.grid(row=6,column=0)
reaper_stop_btn.grid(row=6,column=1)
ma3_play_btn.grid(row=7,column=0)
ma3_clear_btn.grid(row=7,column=1)
laser_btn.grid(row=8,column=0)
neopixel_btn.grid(row=8,column=1)
full_btn.grid(row=9,column=1)

main.mainloop()