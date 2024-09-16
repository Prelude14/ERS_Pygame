# Escape Room Simulator Pygame Project

### A very basic point and click puzzle game, built using Pygame (a set of Python modules designed for creating video games)

ERS is a simple, and custom-made puzzle game where players must figure out how to "escape" each level and move onto the next. It is the first game I have ever made, and I built it for the final project of my CPSC 101 class at Selkirk College in 2019. 
I haven't touched this project or its repository since the end of that class, and it was my first experience with GitHub, so I've decided to update it now that I've completed my education and have more experience. I've tried to keep as much of the original files and code as possible, but I've updated some of the game's sounds and images to ensure no copyright issues, and put all the extra files into the Old Prototypes folder in order to clean up the repository. 

Here are the main components:
* ### Main Game (this includes both levels, and is the only file that needs to be run)
  * **ers.py** (found here: https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/ers.py)

    * Starts at the main menu, where players can view the "bonus" menu that displays credits, or they can start the game. After starting, players will then have to play through each level on order starting with level 1.

* ### Assets (audio and image assets)
  * **audio** (https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/audio):
    
    * All audio files that each level and menu uses, see credits below for specific sounds and their information.
 
  * **imgs** (https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/imgs):
    
    * All image files that each level and menu uses, see credits below for specific images and their information.

  * **leftover** (https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/leftover):
    
    * Extra images for a secret purpose. See credits below for more specific information.

* ### Old Protype Files (the original repository wasn't made with perfect standards in mind, so in and effort to clean it up, I've put the older, extra files into this folder)
  * **Old Prototypes folder** (https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/ers.py):
    * *ers.v1.py* (first version of complete main menu, first level and outro -- NO second level)

      * https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/ers.v1.py
    * *hello.py* (early version of main menu and level one -- NO second level, and NO outro)

      * https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/hello.py
    * *manor.py* (made level 2 seperate of the rest of the game at first, before combining it into the main game)

      * https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/manor.py
    * *Tests.py* (unfortunately not actual unit tests (I didn't know about them at the time), it's just a file used to build the main menu early in the project's life and never updated past that)

      * https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/Tests.py

## Technologies Used

- **Game:** Pygame, Python, Visual Studio
- **Art:** Photoshop, Piskel, Audacity

## Developer Setup Instructions


### Full Game:
* #### Pygame Install & Clone Repository

      1. Visit this link for instructions on how to install pygame (https://www.pygame.org/wiki/GettingStarted)

      2. Clone this repository (https://github.com/Prelude14/ERS_Pygame.git)
  
* #### Run the Game

      1. Once the repository is cloned and pygame is successfully installed, navigate to its location in Command Prompt
         (or whichever program you are using to run python), and run the command:
  
      2. py ers.py
  
      3. This should start the game in its own window that you can quit safely by clicking the x in the top right,
         or by pressing Command + C on Windows while in your Command Prompt's window.

      4. Enjoy playing the game!
  
### Known Issues: 

* Due to how the assets are located and loaded in by pygame, the game might not run if you are NOT using Windows (which is what I built it on most recently, but it was originally built on MAC).
  You might have to change the path of each asset to reflect your OS's requirements, and you can find them in lines 33 to 106 in "ers.py".

* The Main Menu's Buttons are supposed to display differently when the mouse is hovering over them, but instead they flash back and forth the regular and alternate versions of the buttons while
  the mouse is over them.

### What I would do differently now (2024): 

* I would definitely fix the Main menu's button hover issues.

* I never got around to changing the electronic colour pad's buzzer noise (from lvl 2) to change when the code is entered correctly. So it makes the same buzz whether you get it wrong or right
  currently, and I definitely would change that up.

* I ended up drawing level 2's "room" using photoshop and using an image for each wall in the room, and this was so much better (more efficient, more immersive) than how I did level 1 (I used
  pygame's draw feature to outline the walls, door and the bed instead). So I wouldn't use the draw feature again at all most likely, I would continue making the levels using images I make in
  Photoshop.

* Unit tests would be great. I had no idea what they were at the time, and I hard coded or manually tested all of the game's logic, but I would feel more confident if I had some unit tests
  written up. For example I remember writing the electronic colour pad's logic and feeling pretty solid about it, but looking at it now, I'm not sure I can guarantee it is perfect by any means,
  or that I can guarantee I could have manually tested every combination of the four colours being clicked.

* Lastly, I would make more levels (at least 3, but maybe 5). I had just under a full semester (about 3 months) to make this and I had to teach myself pygame's features since everyone else in
  the class were doing their own specific topic for their projects (some did cyber security or app development as examples). Level one took the longest to make since I was learning the most
  during its development, and definitely could have done things in much better ways. I also ran into a couple week roadblock, due to an issue with how the text is displayed in level one when
  certain things are clicked, and my professor also struggled to help with it for a bit. I don't regret the time spent on level one or that roadblock though, since they were valuable learning
  experiences that changed how I approached coding problems in general (For example, I learned how important patience can be, but also that I shouldn't be afraid of trying new ideas and
  changing my approach to a puzzle if needed). It also impacted how I approached making level 2, I ended up ditching the text feature and the level plays a lot different because of it.
  I still put a lot of time into making the images for each part of level 2, but I think I had found my groove by the end of the semester and could have made more if I had another month or two.


## Credits:

* #### Images
     
        1. All the Main Menu and Countdown images (the logo, buttons, lock sprites, and countdown slides)
           were made by me, using Photoshop and Piskel (see https://www.piskelapp.com/terms for Piskel's
           policy regarding copyright).
  
        Find these images here:
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/imgs/mainmenu

        2. Level 1 only uses a few images (the key sprites and the redacted thing), and they were made by
           me, using Photoshop and Piskel (see https://www.piskelapp.com/terms for Piskel's policy
           regarding copyright), everything else is drawn using pygame's "draw" feature.
  
        Find these images here:
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/imgs/lvl1
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/leftover/redacted.png
  
        3. Level 2 has a lot more images, but they were all made by me using Photoshop and Piskel (see
           https://www.piskelapp.com/terms for Piskel's policy regarding copyright), or they have been replaced by
           pictures I created (I had to remove some memes in the books in order to avoid copyright issues).

        Find these images here:
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/imgs/lvl2

* #### Sounds https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/audio
  
        1. Main Menu Sounds: 
           beep1.wav and beep2.wav: "Film Projector Countdown" by Iwan Gabovitch, Copyright 2013, CC-BY3 license:
           (https://creativecommons.org/licenses/by/3.0/). Modified into two shorter files.
           https://freesound.org/people/qubodup/sounds/182109/
  
           but.wav: "Chain Rustling 3 Sound Effect"
           https://www.fesliyanstudios.com/royalty-free-sound-effects-download/chain-44 (Num 3)
  
        Find these sounds here:
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/audio/mainmenu

        2. Level One Sounds:
           keys.wav: "Picking Up Keys From Floor 2 Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=keys  (Num 16)
           doorc.wav: "Closing Squeaky Door B1 Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=close+door  (Num 22)
           secretn.wav: "Slow Hard Breathing Sound Effect"
                     https://www.fesliyanstudios.com/royalty-free-sound-effects-download/breathing-150  (Num 4)
           secretn2.wav: "Screaming Rat Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=scream  (Num 13)
           doorh.wav: "Trying To Open Door Handle 1 Sound Effect"
                     https://www.fesliyanstudios.com/royalty-free-sound-effects-download/door-lock-91  (Num 4)
           unlock.wav: "Heavy Door Lock Locking 1 Sound Effect"
                     https://www.fesliyanstudios.com/royalty-free-sound-effects-download/door-lock-91  (Num 1)
  
        Find these sounds here:
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/audio/lvl1

        3. Level Two Sounds:
           melo.wav: "Last Resort" by Philipp Weigl (https://freemusicarchive.org/music/philipp-weigl/).
                     Available for use under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
                     Modified into a 24 second snippet and slowed down. Source: Free Music Archive
                     (https://freemusicarchive.org/music/philipp-weigl/piano-compositions/last-resort/)
           medgears.wav: "Cranking Gears Medium Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=gears  (Num 3)
           fastgears.wav: "Cranking Gear Faster Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=gears  (Num 1)
           startup.wav: "Computer Beep Beeping 2 Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=beeping  (Num 3)
           click.wav: "Putting Cap Back Onto Marker Sound Effect"
                     https://www.fesliyanstudios.com/royalty-free-sound-effects-download/open-close-marker-cap-105  (Num 1)
           switch.wav: "Light Switch On Off 04 Sound Effect"
                     https://www.fesliyanstudios.com/sound-effects-search.php?q=switch  (Num 5)
           bopen.wav: "Turning Paper Book Page Quick A1 Sound Effect"
                     https://www.fesliyanstudios.com/royalty-free-sound-effects-download/book-238  (Num 22)
           bclose.wav: "Closing Book A1 Sound Effect"
                     https://www.fesliyanstudios.com/royalty-free-sound-effects-download/book-238  (Num 1)
           buzz.wav: "Wrong Buzzer", created by Alexander
                     The sound effect is permitted for commercial use under license Creative Commons License 4.0
                     (https://creativecommons.org/licenses/by/4.0/), and unmodified.
                     Source: https://orangefreesounds.com/wrong-buzzer/
  
        Find these sounds here:
        https://github.com/Prelude14/ERS_Pygame/blob/71d84cfd9245affd767af73c892509f04bd66a1d/audio/lvl2

        4. Additional Sounds:
           qubodup (https://freesound.org/people/qubodup/)

  * #### For free sound effects from https://www.fesliyanstudios.com, view their policy here: https://www.fesliyanstudios.com/sound-effects-policy
        
