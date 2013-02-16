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


# Cycles Render Time Calculator V1.0 Beta 2
# Copyright 2013 le717
# http://triangle717.wordpress.com
# and rioforce
# http://rioforce.wordpress.com

import sys, time, webbrowser

app = "Cycles Render Time Calculator"
majver = "Version 1.0"
minver = "Beta 2"
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
    # You need to have at least Python 3.3 to run this program.
    if sys.version_info < (3,3):
        print("You need to download Python 3.3 or greater to run {0} {1}.".format(app, majver))
         # Don't open browser immediately
        time.sleep(2)
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # Open in new tab, raise browser window (if possible)
        # It automatically closes after this
        time.sleep(5) 
    # If you are running Python 3.3     
    else:
        main()

def main():
    '''Menu Layout'''
    print() # Blank space helps keep it all nice and neat
    print("{0}\nCopyright 2013 {1}".format(app, creator))
    print('''\nPlease make a selection:\n
[t] Render Using Tiles
[p] Render Using Progressive Refine
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "t":
            tilerender()
        elif menuopt.lower() == "p":
            layerrender()   
        elif menuopt.lower() == "q":
            print(logo)
            time.sleep(2)
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
        tilerendertime = float(input("How long does a single tile take to render (in seconds)? "))
        # Mathamatical functions
        global tileseconds
        tileseconds = (numtiles * tilerendertime)
        tileminutes = (tileseconds / 60)
        tilehours = (tileseconds / 3600)
        # It will take over an hour
        if tileseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your image.\n".format(round(tilehours, 2)))
        # It will take over a minute but less than an hour
        elif tileseconds >= 60.0 and tileseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your image.\n".format(round(tileminutes, 2)))
        #It will take only seconds    
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your image.\n".format(round(tileseconds, 2)))
    # Catch any non-numerical input        
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        tilerender()
    print("Are you rendering an animation? " + r"(y\N)") # AKA video or "multi-frame" animation
    tilevideo = input("\n> ")
    if tilevideo.lower() != "y": # No, I am not
        time.sleep(0.2)
        main()
    else: 
        tilevideorender(tileseconds) # Yes, I am
            

def tilevideorender(tileseconds):
    '''Calculates Animation Render Time (Using Tiles)'''
    try:
        time.sleep(0.2) # Sleep for a tiny bit so the text doesn't "jump" at you (and same everywhere else)
        tileframenumber = int(input("\nHow many frames are in your animation? "))
        # More mathamatical functions
        tilevideoseconds = (tileseconds * tileframenumber)
        tilevideominutes = (tilevideoseconds / 60)
        tilevideohours = (tilevideoseconds / 3600)
        # It will take over an hour
        if tilevideoseconds >= 3600.0:
            print("\nIt will take approximately {0} hours to render your animation.\n".format(round(tilevideohours, 2)))
        # It will take over a minute but less than an hour 
        elif tilevideoseconds >= 60.0 and tilevideoseconds < 3599.9:
            print("\nIt will take approximately {0} minutes to render your animation.\n".format(round(tilevideominutes, 2)))
        else:   
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your animation.\n".format(round(tilevideoseconds, 2)))
        time.sleep(0.6)
        main()
    # Catch any non-numerical input     
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        tilevideorender(tileseconds)

def layerrender():
    '''Calculates Image Render Time (Using Progessive Refine)'''
    '''Progressive Refine Image and Animation render is just the Tile render code adapted to
support the Progressive Refine method. Therefore, I've omitted the comments'''
    try:
        layernum = int(input("\nHow many layers are in your render? "))
        layerrendertime = float(input("How long does a single layer take to render (in seconds)? "))
        # Even more Mathamatical functions
        global layerseconds
        layerseconds = (layernum * layerrendertime)
        layerminutes = (layerseconds / 60)
        layerhours = (layerseconds / 3600)
        if layerseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your image.\n".format(round(layerhours, 2)))
        elif layerseconds >= 60.0 and layerseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your image.\n".format(round(layerminutes, 2)))
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your image.\n".format(round(layerseconds, 2)))
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        layerrender()
    print("Are you rendering an animation? " + r"(y\N)")
    layervideo = input("\n> ")
    if layervideo.lower() != "y": 
        main()
    else: 
        layervideorender(layerseconds)
        
def layervideorender(layerseconds):
    '''Calculates Animation Render Time (Using Progessive Refine)'''
    try:
        time.sleep(0.2)
        layerframenumber = int(input("\nHow many frames are in your animation? "))
        # Math is FUN!
        layervideoseconds = (layerseconds * layerframenumber)
        layervideominutes = (layervideoseconds / 60)
        layervideohours = (layervideoseconds / 3600)
        if layervideoseconds >= 3600.0:
            print("\nIt will take approximately {0} hours to render your animation.\n".format(round(layervideohours, 2)))
        elif layervideoseconds >= 60.0 and layervideoseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your animation.\n".format(round(layervideominutes, 2)))
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your animation.\n".format(round(layervideoseconds, 2)))
        time.sleep(0.6)
        main()
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        layervideorender(layerseconds)            
        
        
if __name__ == "__main__":
    preload()
# Display complete app info if imported as a module    
else: 
    print("{0} {1} {2}\nCopyright 2013 {3}".format(app, majver, minver, creator))
    
