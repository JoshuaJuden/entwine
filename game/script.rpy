# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg kitchen = "images/kitchen_bg.jpg"
image bg diningroom = "images/diningroom.png"

#who_style=character name color
#what_Style=spoken text
#window_style = window

# Declare characters used by this game.
define adolf = Character('Adolf', color="#B7E1FF", what_color="000000")
define alex = Character('Alessandra', color="FF5D58", what_color="000000")
define nchar = Character(None, kind=nvl, what_color="#FFFFFF")
define narrator = Character(None, what_color="000000")

#init python:

# The game starts here.
label start:

    scene black with dissolve
    show text "Act 1\nA New School" with Pause(2.5)
    scene black with dissolve

    nchar "With the amount of times I've told him, one would assume my father would get the message."
    nchar "A fucking boarding school?"
    nchar "I'm not that poorly behaved."
    nchar "And yet, here we are."

    scene bg kitchen
    with fade

    adolf "A few hours ago I was lured into the kitchen with the cheap promise of a meal and was subsequently forced into a conversation that I felt I should never be having -- boarding school.
"
    adolf "After more stern assertions than valid arguments from his side, I mentally concluded that arguing further would be a waste of thought."
    adolf "It was clear we would reach no peaceful consensus."
    adolf "With this set in my mind, I would continue to agree with him, less out of hope that he would see how insane he sounds and more out of inability to explain anything to him.
"

    "Adolf, please, the decision is final and you need to respect that."
    "Fighting is only going to make it that much more difficult."
    "There's nothing wrong with this school anyway."
    "It's ranked highly, and some of your friends are transferring this year anyway."
    "Please, understand my decision Adolf. I'm doing this for your own good."
    "You'll still see me, but this job is more important to me than you could ever imagine."

    adolf "My family kills me sometimes."
    adolf "Mother would have had something optimistic to say. She always did."
    adolf "Sometimes I question the relationship between them. I question if Father even misses her."

    adolf "This line of questioning leads to bad emotion, so I repress it and move on to the act of packing my bags."
    adolf "Apparently, I'm leaving tomorrow."

    nvl clear
    scene black with dissolve

    nchar "What would be different if I made the change anyway?"
    nchar "I’ve practically taken care of myself as long as I can remember."
    nchar "A boarding school? This doesn’t make any sense."

    scene bg diningroom
    with fade

    alex "Protest on the tip of my tongue, I swallow it and turn my gaze downward at the table."
    alex "I just don’t understand why this is necessary."
    alex "My grades are as perfect as always and I don’t have any disciplinary marks."
    alex "Clearly I am able to supervise myself."

    "We believe it’s for the best, Alessandra."
    "We acknowledge that you are quite capable of minding yourself, but this absence will not be standard fare."
    "What is usually weeks will be months."
    "Your father was just made vice president of the company and I assume you’re aware of what that entails."

    alex "Yes, it’s time for another vacation."

    "This school ranks just as well as the one you were previously attending."
    "The only difference between them is that you will be boarding now."
    "If you’re concerned about having to cavort with trash you needn’t be."
    "While not as nice as our estate of course, you should find it comfortable enough."



    return
