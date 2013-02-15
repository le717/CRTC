# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


# Cycles Render Calculator V1.0 Beta 1
# Copyright 2013 le717
# http://triangle717.wordpress.com
# and rioforce
# http://rioforce.wordpress.com

import sys, time

app = "Cycles Render Calculator"
majver = "Version 1.0"
minver = "Beta 1"
creator = "le717 and rioforce"

# ASCII Blender logo. Displayed upon app exit.

logo = '''                                   
                                   
                                   
                 ::                
                ;ii:               
                ;iiii;.            
                 ;iiiii            
                  ;iiii;           
                   iiiiii.         
     .:,;;;;;i;;;;;;;itiii,        
     ;ttiiiiiiiiititiiiiiii;.      
     tiiiiiiiiiii;iiiiiiiiiti.     
     .;,,,,,,iitiiiii,:;ititii:    
          ..,tiiiii.    .:tiiii,   
           .tiiti;.   .   ;ttiti:  
          :iiiii;.  ,tfi.  ,iiit;  
        .tittiti   EDDDDDE  :ttit  
       :iitiiit;  tGDEDDDD. .;iii. 
      ,titiiiit,  GEDDDDDDt  ,tit: 
    .tiitttitit, .DDEDDEDDj  :iti, 
  .:iitti;;iitt,  fDDEDDEE,  ,tti, 
  ,ttitit..tttii  :DDDEDDE  .itti: 
 .jitttt; .ttitt   DEEDEEL  :ttti: 
:ttiti:    ;ttti;.   .:    ;tittt  
,tttt.     :ttttti.       itttttt  
:ttt;       tttittt.    .,tiittti  
            :jtittttttttttitttt;   
             ,jtiititttttttttt;    
              :ttttttttttttitj     
               .tttttttttttji:     
                  .;iiii;,.        
                                   '''

def preload():
    '''Python 3.3 version check'''
    if sys.version_info < (3,3): # You need to have at least Python 3.3 to run this program.
        print("You need to download Python 3.3 or greater to run {0} {1}.".format(app, majver))
        time.sleep(2) # Don't open browser immediately
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # Open in new tab, raise browser window (if possible)
        time.sleep(5) # It automatically closes after this
    else: # If you are running Python 3.3
        main()

def main():
    '''Menu Layout'''
    print() # Blank space helps keep it all nice and neat
    print("{0}\nCopyright 2013 {1}".format(app, creator))
    print('''\nPlease make a selection:\n
[t] Render Using Tiles
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "t":
            tilerender()
        elif menuopt.lower() == "q":
            print(logo)
            raise SystemExit
        else:
            main()

# Unused code. Might be repurposed later.

##def sizerender():
##    try:
##        tilewdt = int(input("Please enter your tile width: "))
##        tilehgt = int(input("Please enter your tile height: "))
##        imagewdt = int(input("Please enter the width of your image: "))
##        imagehgt = int(input("Please enter the height of your image: "))
##        print("You are rendering a {0}x{1} image using {2}x{3} tiles.".format(imagewdt, imagehgt, tilewdt, tilehgt))
##        confirmsizes = input("\nIs this correct?" + r"(y\N)" + "\n> ")
##        if confirmsizes.lower() != "y":
##            sizerender()
##        else:
##            tilerendertime = int(input("Please enter (using seconds) how long it takes a single tile to render using the above values: "))
##            numtiles = (imagewdt / tilewdt) + (imagehgt / tilehgt)
##            print("\nThere will be approximately {0} tiles.".format(round(numtiles, 2)))
##            secrendertime = (tilerendertime * numtiles)
##            minrendertime = (secrendertime / 60)
##            print("It will take approximately {0} minutes to render your image.\n".format(round(minrendertime, 2)))            
##            main()
##    except ValueError:
##        print("That is an invalid input. Please try again.\n")
##        sizerender()

def tilerender():
    '''Calculates Image Render Time (Using Tiles)'''
    try:
        numtiles = int(input("\nHow many tiles are in your render? "))
        tilerendertime = int(input("How long does a single tile take to render (in seconds)? "))
        # Mathamatical functions
        seconds = (numtiles * tilerendertime)
        global minutes
        minutes = (seconds / 60)
        hours = (minutes / 60)
        if seconds >= 60.0: # It will take over a minute
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your image.\n".format(round(minutes, 2)))
        else: #It will take only a few seconds
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your image.\n".format(round(seconds, 2)))
            # TODO: Possibly add an hour slot. Not currently available due to odd bug
    except ValueError: # Catch any non-numeral input
        print("That is an invalid input. Please try again.\n")
        tilerender()
    video = input("Are you rendering an animation? ") # AKA video or "multi-frame" animation
    if video.lower() != "y": # No, I am not
        main()
    else: 
        videorender(minutes) # Yes, I am
            

def videorender(minutes):
    '''Calculates Animation Render Time (Using Tiles)'''
    try:
        time.sleep(0.2) # Sleep for a tiny bit so the text doesn't "jump" at you (and same everywhere else)
        framenumber = int(input("\nHow many frames are in your animation? "))
        # More mathamatical functions 
        videominutes = (minutes * framenumber)
        videohours = (videominutes / 60)
        if videominutes >= 60.0: # It will take over an hour
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your animation.\n".format(round(videohours, 2)))
        else: # It will take only minutes
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your animation.\n".format(round(videominutes, 2)))
        time.sleep(0.6)
        main()
    except ValueError: # Catch any non-numeral input
        print("That is an invalid input. Please try again.\n")
        videorender(minutes)  
    
if __name__ == "__main__":
    preload()
else: # Display app info if imported
    print("{0} {1} {2}\nCopyright 2013 {3}".format(app, majver, minver, creator))
    
