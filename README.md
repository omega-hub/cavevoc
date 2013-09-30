<h1><font face="Helvetica, Arial, sans-serif">CAVEVOC</font></h1>
<font face="Helvetica, Arial, sans-serif"> (C) 2013 by <a
    href="http://jasonleigh.me">Jason Leigh</a>, <a
    href="http://www.evl.uic.edu">Electronic Visualization
    Laboratory</a>, University of Illinois at Chicago<br>
</font>
<p><font face="Helvetica, Arial, sans-serif">CAVEVOC is a means to
    get speech recognition into the CAVE. CAVEVOC has two
    components, the CAVEVOC client and the CAVEVOC Python Module.
    The CAVEVOC client runs on a PC, records audio samples and sends
    them to Google for translation. The translated text and its
    corresponding confidence level is then transmitted to the CAVE
    for application use. On the CAVE, the CAVEVOC Python module will
    read this data and apply it to a user-defined callback function
    within your program.<br>
  </font></p>
<p><font face="Helvetica, Arial, sans-serif">Trivia: CAVEVOC was the
    name given to the first speech recognition system I developed
    for the old CAVE in the mid-90s for <a
      href="http://dl.acm.org/citation.cfm?id=618360">CALVIN </a><a
      href="http://youtu.be/ZYY8JdFgCAc">[Video]</a>. At the time
    IBM's speech engine was used. Arguably this new CAVEVOC is much
    more accurate using Google's crowd-sourced recognition engine.<br>
  </font></p>
<p><font face="Helvetica, Arial, sans-serif">You will need to
    download the following to use CAVEVOC:<br>
  </font></p>
<ol>
  <li><font face="Helvetica, Arial, sans-serif"><a
        href="http://processing.org">Processing<br>
      </a></font></li>
  <li><font face="Helvetica, Arial, sans-serif">
        CAVEVOC-Processing.zip - The client already bundles together the <a
        href="http://stt.getflourish.com/">STT </a>(Speech To Text)
      translation library and the <a
        href="http://ubaa.net/shared/processing/udp/">UDP </a>(networking)
      library in the zip file. But you can download them separately
      from their original source by clicking the respective links.
      These library folders need to be installed in your Processing
      user library folder.<br>
    </font></li>
  <li><font face="Helvetica, Arial, sans-serif">CAVEVOC Python
      Module - cavevoc.py - This is the python module you will use
      to incorporate speech recognition into your CAVE application.<br>
    </font></li>
  <li><font face="Helvetica, Arial, sans-serif">CAVEVOC CAVE Demo
      Application - demo.py - This is a simple CAVE application to
      show you how to use the <a href="http://febret.github.io/omegalib/cavevoc/html/namespacecavevoc.html">CAVEVOC
        Python API</a>.<br>
    </font></li>
</ol>
    <h2><font face="Helvetica, Arial, sans-serif">Simple Example</font></h2>
    <p><font face="Helvetica, Arial, sans-serif">This demo simply takes
        any recognized speech from CAVEVOC and print on the screen in
        the CAVE including the confidence level reported by Google.</font><br>
    </p>
<ol>
  <li><font face="Helvetica, Arial, sans-serif">You should install
      Items 1-3&nbsp; on the PC that will access the microphone.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">Install Items 4 and
      5&nbsp; in the location where you normally install your CAVE
      applications.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">First launch the
      CAVE Demo application: e.g. <code>orun -s demo.py</code><br>
      The environment should just be gray and blank until recognized
      text is received. The picture below is taken from a desktop
      simulation.<br>
      In the demo, whenever recognized text is received, it will
      display its confidence level (reported by Google) and the
      text, in a random position on the screen in front of you,
      hence the picture below.<br>
      <img alt="" src="http://uic-evl.github.io/omegalib/cavevoc/cavevoc-cave.png" border="1" height="299"
        hspace="1" vspace="1" width="447"><br>
    </font></li>
  <li><font face="Helvetica, Arial, sans-serif">Launch Processing
      and open CAVEVOC-PTT.pde.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">You will first need
      to edit the ip address in the code to reflect the ip address
      of the CAVE (e.g. lyra.evl.uic.edu).</font></li>
  <li><font face="Helvetica, Arial, sans-serif">Now RUN the
      CAVEVOC-PTT.pde application.<br>
      <img alt="" src="http://uic-evl.github.io/omegalib/cavevoc/cavevoc-processing.png" border="1"
        height="166" hspace="1" vspace="1" width="445"><br>
    </font></li>
  <li><font face="Helvetica, Arial, sans-serif">Hold down any key on
      your keyboard (like the SPACEBAR) and start talking.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">Release the key when
      you are done talking.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">The audio will begin
      recording when you hold the key down. When released the audio
      sample will be transmitted to Google for translation.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">Once the translation
      is received you should see feedback on the CAVEVOC-PTT window.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">Furthermore that
      text should also be sent to the CAVE application and it should
      show up in the CAVE.</font></li>
</ol>
<p><font face="Helvetica, Arial, sans-serif">Note: There is also a
    CAVEVOC-Auto.pde file that contains a version of the CAVEVOC
    client that will continually listen for audio without requiring
    you to hold a key down. Also both the CAVEVOC-PTT and
    CAVEVOC-Auto code are kept to a minimum so you can further
    customize them for your needs.<br>
  </font></p>
    <h2><font face="Helvetica, Arial, sans-serif">Second Example<br>
      </font></h2>
    <p><font face="Helvetica, Arial, sans-serif"><font face="Helvetica,
          Arial, sans-serif">The second demo (called Ideation) lets you
          create boxes and spheres, color them and move them, all via
          voice command. To select an object simply turn your head
          towards it.<br>
        </font>Launch the program using: orun -s ideation.py<br>
      </font></p>
    <blockquote><img alt="" src="http://uic-evl.github.io/omegalib/cavevoc/ideation.png" height="327" width="432"></blockquote>
    <p><font face="Helvetica, Arial, sans-serif">Ideation is an example
        that shows how you could use <a
          href="http://pyparsing.wikispaces.com/">Pyparsing </a>to
        parse the incoming voice commands. With Pyparsing you can very
        quickly develop a parser for very complex grammars. In the demo
        I have included the module: pyparsing.py so you don't need to
        bother to download and install Pyparsing.</font></p>
    <p><font face="Helvetica, Arial, sans-serif">The following are
        example voice commands:<br>
      </font></p>
    <ul>
      <li><font face="Helvetica, Arial, sans-serif">MAKE | BUILD |
          CREATE A BOX | CUBE - creates a 1-foot cube</font></li>
      <li><font face="Helvetica, Arial, sans-serif">MAKE | BUILD |
          CREATE&nbsp; A SPHERE | BALL - creates a 1-foot diameter
          sphere</font></li>
      <li><font face="Helvetica, Arial, sans-serif">PAINT | COLOR | MAKE
          IT RED | GREEN | BLUE | ....&nbsp; - color the object that
          your head is pointing at Red. Other colors are green, blue,
          magenta, orange, yellow, black.... you get the idea.</font></li>
      <li><font face="Helvetica, Arial, sans-serif">NAME IT | THIS JASON
          - give a name to the object</font></li>
      <li><font face="Helvetica, Arial, sans-serif">PLACE JASON HERE -
          if you navigate the space and say this it will take the object
          named JASON and bring it to you and place it in front of you.</font></li>
      <li><font face="Helvetica, Arial, sans-serif">AGAIN - if you say
          either AGAIN or REPEAT, it will perform the last command
          again. E.g. if you said MAKE A BOX last, it will make a second
          box if you say AGAIN or REPEAT.</font></li>
      <li><font face="Helvetica, Arial, sans-serif">MAKE A BOX AND PAINT
          IT RED AND PLACE JASON HERE - You can chain commands together
          with the AND operator.</font></li>
    </ul>
    <p><font face="Helvetica, Arial, sans-serif">To see the full extent
        of the grammar and how it is used to activate parts of your code
        you will need to read the ideation.py code.<br>
      </font></p>
<h2><font face="Helvetica, Arial, sans-serif">Some General Tips for
    Effective Use of Speech Recognition<br>
  </font></h2>
<ul>
  <li><font face="Helvetica, Arial, sans-serif">Get a wireless
      microphone that has a push-to-talk button if possible- it will
      help cut out any unnecessary attempts at translation- even
      better if you can find a wireless bluetooth microphone. But
      for testing purposes you could just start with your laptop's
      built-in microphone.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">Use speech
      recognition for interactions that take more time or dexterity
      to perform the physical manipulation than to say the phrase.
      For example, it may be challenging to accurately position a
      CAVE object in space using physical interactions but it is
      easy to say: Move object to 2.5 3 5.5 or Rotate 23.5 degrees
      along X axis or Make a box 1 by 2.5 by 3 meters and put it at
      3 4 5.<br>
    </font></li>
  <li><font face="Helvetica, Arial, sans-serif">After text is
      recognized or not recognized, try to give the user feedback-
      for example with an audible cue. You've seen sci-fi movies
      like Iron Man, use your imagination!</font></li>
  <li><font face="Helvetica, Arial, sans-serif">It is sometimes
      helpful to prefix every command with a name, e.g. "Jarvis,
      move the object". You can use this prefix to know when you are
      talking to the CAVE rather than talking to someone else in the
      audience. Another approach is to create a virtual
      character/avatar and have it so that it will only interpret
      your commands if you are facing it.<br>
      <li><font face="Helvetica, Arial, sans-serif">Consider creating a
          grammar to describe your commands and then use something like
          <a href="http://pyparsing.wikispaces.com/">Pyparsing </a>to
          implement the grammar parser. <br>
        </font></li>
      <li><font face="Helvetica, Arial, sans-serif">If you want to be
          more advanced you can also use the <a href="http://nltk.org/">Natural Language Toolkit</a>. 
          The main advantage of using natural language processing techniques is that 
          you can minimize the need for the user to remember a specific grammar. <br>
        </font></li>
      <li><font face="Helvetica, Arial, sans-serif">But if you don't
          have much experience in NLP, try to keep the number of speech
          utterances low to minimize the need to remember them. In any
          case it may be helpful to provide a "dropdown" cheat sheet in
          the CAVE to help the user remember the commands. Better still
          is to create a cheat sheet that unfolds to show the next word
          in a phrase that can be spoken. A good example of this is used
          in the video game <a
            href="http://www.youtube.com/watch?v=WB7yDq1xgxM">End War</a>.<br>
    </font></li>
  <li><font face="Helvetica, Arial, sans-serif">Lastly you may
      consider implementing a state-machine-based conversation
      engine so that followup commands are possible:</font></li>
  <ul>
    <li><font face="Helvetica, Arial, sans-serif">User: Computer,
        make me a cube</font></li>
    <li><font face="Helvetica, Arial, sans-serif">Computer: Where
        would you like me to put it?</font></li>
    <li><font face="Helvetica, Arial, sans-serif">User: Put it at 5
        5 5</font></li>
    <li><font face="Helvetica, Arial, sans-serif">Computer: How big
        would you like it?</font></li>
    <li><font face="Helvetica, Arial, sans-serif">User: How about 3
        by 5 by 2 meters</font></li>
    <li><font face="Helvetica, Arial, sans-serif">Computer: Coming
        right up. Cube at 5 5 5 of size 3 by 5 by 2 meters.</font></li>
    <li><font face="Helvetica, Arial, sans-serif">User: Take me to
        the other side of the cube.</font></li>
    <li><font face="Helvetica, Arial, sans-serif">etc....<br>
      </font></li>
  </ul>
</ul>
<h2><font face="Helvetica, Arial, sans-serif">Release Notes</font></h2>
<ul>
      <li><font face="Helvetica, Arial, sans-serif">7/26/2013 - Revised
          to include example using Pyparsing as the command parser.</font></li>
  <li><font face="Helvetica, Arial, sans-serif">7/20/13 - First
      version released.</font></li>
</ul>
<p><br>
</p>
