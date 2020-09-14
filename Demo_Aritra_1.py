#   python code
#		script_name:dem0
#   RD_UK_HOUSE__5THCHORD_2
#		author:Aritra Bose
#		description:Composition Practice
#   Set Up

from earsketch import *

init()
setTempo(120)
# Music 
chord=RD_UK_HOUSE__5THCHORD_2
secondaryBeat=HIPHOP_BASSSUB_001
mainBeat=HOUSE_MAIN_BEAT_003
fitMedia(chord, 1, 1, 16)
# Add Effect between measures 1 and 16 from -60db to 5db
setEffect(1, VOLUME, GAIN,  -60 , 1, 5, 12)
setEffect(1, VOLUME, GAIN,  5, 12 ,-60 ,16)

fitMedia(secondaryBeat, 2, 1, 12)
# Add Effect
setEffect( 2, DELAY, DELAY_TIME, 500 )
fitMedia(mainBeat, 3 , 1 , 8)
# Add Effect
setEffect( 3, REVERB, REVERB_TIME, 200)
# Finish
finish()
