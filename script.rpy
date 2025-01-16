# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Angus", color = "#DF5F00")
define b = Character("Bailey", color = "#00a05d")
define e = Character("Esme", color = "#F0C800")
define p = Character("Pedro", color = "#A838FF")
define ap = Character("April", color = "#002AD6")
define br = Character("Bradley", color = "#5fff67")
define m = Character("Morgan", color = "#ec038b")
define g = Character("Gary", color = "#E30000")
define pl = Character("[name]", color = "#ffffffff")
define mil = Character("Millicent", color = "#69144d")
define mum = Character("Mum", color = "#999494ff")


#define the starting friendship point variables

define a_friend = 0
define b_friend = 0 
define e_friend = 0
define p_friend = 0
define ap_friend = 0
define br_friend = 0
define m_friend = 0
define g_friend = 0


#define variables like who you pick to interact with first on any given day

define d1_eg1 = False
define d2_e1 = False
define d1_u_p1 = False
define p_tell_take = False
define b_know_crush = False
define cppl = False
define m_hang = False
define ap_date = False
define ap_com_tree = False
define ap_com_drag = False

define crush = "no one"
define game = "none"



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Keeping this here for now until I figure out how best to write the game:
   
    scene bg logo with fade
    pause 5.0
    scene bg black with fade
    
    "This game was created on the lands of the Wurundjeri Woi Wurrung and Wadawurrung people, of the Kulin Nations."
    "Generic Beetle acknowledges the contributions of Indigenous Australians to millenia of art, work, and play on these countries."
    "We pay our respects to elders past and present, and extend this respect to the young people representing the future."
    "We acknowledge that sovereignty was never ceded, and that this always was, and always will be, Aboriginal Land."
   
   
   
    "Welcome! Before we begin, we need to get a couple things sorted."

python:
    name = renpy.input("Firstly, what is your name?")
    name = name.strip() or "Beetle"

"Great!"

"And of these three options, what would you most like to study?"

menu subject:
    "Music Production":
        $ subject = "Music Production"
    "Marine Biology":
        $ subject = "Marine Biology"
    "Speech Therapy":
        $ subject = "Speech Therapy"


show angus neutral at left
show bailey neutral at right

"And, of these two fine people, who is your partner, [name]?"

menu partner_choice:
        "Angus (left)":
            $ partner = "Angus"
            jump angus_partner
        "Bailey (right)":
            $ partner = "Bailey"
            jump bailey_partner
        
label angus_partner:
    
    hide bailey neutral
    hide angus neutral
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "Perfect! Now we can begin."

    scene bg bedroom aft with fade

    play music "Theme.mp3" fadein 1.5 loop

    "On a fine spring day, you get home from work, put all your things away, and sit down in your bedroom for a bit. "
    
    "About two months ago, you moved in with your partner of two years, [partner]. The two of you now rent a small house in a suburb a short travel from both your work and the university you attend. It’s very convenient, and very lucky."

    "It's been good, it really has."

    "The only issue is, well..."

    "Angus has been acting a little strange ever since you moved in."

    "It's hard to describe, but he's... less present. Spacing out more. Like he's never really quite... {i}here{/i}."

    "Maybe he's just stressed from work. He does have a big trip coming up, after all."
    
    "Speaking of Angus, you should go find him. You haven't seen him since you got back."

    scene bg garden aft with fade

    "It doesn't take you long to find Angus, as the house is small and you know he likes spending time in the garden."

    show angus neutral

    # These display lines of dialogue.

    stop music fadeout 5.0

    "When you find him, Angus is just staring at the garden hose, which is running. It is not aimed at any plants, but rather just spilling over the ground."

    menu garden_hose:
        "Turn off the garden hose":
            jump a_garden_hose_off
        "Put your thumb over the spout of the garden hose":
            $ a_friend += 5
            jump a_garden_hose_thumb
        "Just keep staring at Angus":
            jump a_garden_hose_on
    
    label a_garden_hose_off:
        
        show angus shocked
        
        a "Oh! I didn't see you there..."
        
        show angus neutral
        
        a "I didn't... hear you come home."
        
        jump a_after_hose
    
    label a_garden_hose_thumb:

        "At first, the water stops. But very soon it begins to push and spill around your thumb."
        
        "Then it starts to spurt everywhere, tiny jet-streams making their way forcefully over your hands, your clothes, your face."

        show angus shocked

        "Angus rushes to turn off the hose."

        a "What are you {b}doing!?{/b}"

        show angus happy

        a "Oh, wow... you look so silly, [name]. Why did you do that?"

        a "Gosh. I didn't even hear you come home."

        show angus neutral

        jump a_after_hose

    label a_garden_hose_on:

        "After a few moments, Angus puts his thumb over the hose, momentarily stopping the water flow."

        "Shortly, though, water finds its way around his blockage, and begins to seep and then spurt out around his thumb."
        
        "His hands drip with water and his clothes begin to soak."
        
        show angus shocked

        "Seeming to come to his senses, Angus lets go of the hose and turns it off at the tap."

        "He turns and sees you, clearly startled."

        a "Wh-? [name]! When did you get ther- I mean, back?"

        show angus neutral

        jump a_after_hose

label a_after_hose:

    a "I mean, welcome home! You must be tired."
    
    if a_friend >= 5:
        "Angus kisses you on the cheek before you tell him about your day."
    else:
        "Angus smiles at you as you tell him about your day."
    
    "The two of you chat for a little while."

    "You notice that, once again, Angus seems to be thinking of something else. He keeps looking to the side and fiddling with his hands."

    "After a lull in conversation, he takes a deep breath."

    show angus embarrassed

    a "So, um... there's something I've been thinking about. I mean, meaning to talk to you about."
    a "And before I say it, I want to make it clear that I don't expect an answer right away. In fact, I'd rather you didn't say anything for a... for a little bit."
    a "In fact... you know how I have that work trip starting tomorrow?"
    a "Maybe don't- {i}yeah{/i}. I'd like to wait to hear your thoughts until after I get back. It'll just be a week, but I think... I think that's long enough."
    a "For you to really think about it and for me to... {i}prepare{/i} myself."
    
    menu a_interrupt:
        "Ask him what it is":
            $ a_friend -= 5
            a "Oh, well it's..."
            jump a_after_interrupt
        "Just wait":
            $ a_friend += 5
            "Angus takes another deep breath."
            jump a_after_interrupt
    
label a_after_interrupt:
    
    show angus neutral

    a "I'm polyamorous. Do you... know what that is?"

    menu a_polyq:
        "Yes":
            a "Okay... good."
            jump a_after_polyq
        "No":
            a "Okay, well it's essentially... it's when a person, like me, feels like they have... well, feelings for more than one person... at a time."
            a "There's kind of more to it than that."
            a "But for me, it means I can't really contain my feelings to just one person."
            a "It's not like cheating. Although some people {i}will{/i} cheat to... deal with it, I guess."
            a "But I just... I want to be open and... and honest. And well, I love you. But I want to love other people, too. Does that make sense?"
            a "But it has to have everyone's consent. To work. To be... {i}real{/i}, I guess?"
            a "And it can even be like a... a loop. Where everyone is dating each other, and it's just one relationship, but with more than two people in it."
            jump a_after_polyq

label a_after_polyq:

    a "I guess the thing for me is, there's this guy Bradley, and I think I'm... developing feelings for him."
    a "But I also still have feelings for you."
    a "What I want is to be able to pursue things with Bradley, but I also still want to be with you."
    a "But I understand if that's not... something you're comfortable with."
    show angus sad
    a "So if you want to break up with me, I... I understand."
    show angus shocked
    a "We can still live together and be friends and everything, of course! But..."
    show angus neutral
    a "Well, I need to be able to explore this part of my identity. That's a decision I've made for me."
    a "It isn't meant to be an ultimatum or anything, either. I just... I know what {i}I{/i} need, but I don't know what you're comfortable with."
    a "So, I want to give you time to really think about it. I don't want to pressure you into anything you're not okay with, but I don't want you to just dismiss it, either."
    a "So don't tell me now. But think about it, and when I get back... tell me then. Okay?"
    a "..."
    show angus embarrassed
    a "Um, anyway. I should get started on dinner."

    hide angus embarrassed

    "You are left in the garden, thinking about what he said."
    
    scene bg bedroom n with fade
    
    "Over dinner, the two of you talk about unrelated things, and then you go to your room to wind down and go to bed."
    
    scene bg black with fade

    scene bg bedroom with fade

label a_day1:

    play music "Theme.mp3" fadein 1.5 loop

    "The next day starts as all Mondays do - with a groan and the insistent sound of your alarm."
    
    "You don't have much time to yourself in the mornings. Before you know it you're up and showered and heading out the door to work. You almost stop to say goodbye to Angus, before remembering that he has already left for his work trip."

    menu a_d1_mtext:
        "Send a good morning text":
            $ a_friend += 5
            pl "{i} hey bb! Heading to work rn, thinking of you <3 miss u already {/i}"
            stop music fadeout 5.0
            "Now you really have to get going. You jump into the car and pull out of the driveway, and away you go."
            jump a_d1_work
        "No time, you gotta get to work!":
            stop music fadeout 5.0
            "You'll text Angus later. You jump into the car and pull out of the driveway, and away you go."
            jump a_d1_work

label a_d1_work:
    scene bg cafe
    play music "Lounge Lizard.mp3" loop
    "You work at the hit cafe 'Sugar in My Coffee', everyone's favourite local haunt." 
    "You barrel through the door and say hi to your manager and coworkers, and then it's a flurry of setting tables and warming pastries and pulling espresso shots until people start trickling in."
    "The morning rush hits you hard, but you get through most of it on auto-pilot. You're still turning last night's conversation over in your head, examining it from every angle, finding yourself rush back to it every time you think you've found a sufficient distraction."
    menu a_d1_feeling:
        "Mostly, you've been feeling..."
        "...excited. You've never thought about being polyamorous before!":
            $ a_friend += 5
            "You can feel it bubble up inside you like soft drink, waiting to be let out." 
            "You guess a part of you thought that because you were with [partner], that would mean the end of any personal exploration." 
            "But that isn't the case, and you're realising that you're much more excited at the prospect of learning something new about yourself than you were anticipating."
            jump a_d1_start
        "...stressed. You have no idea what you're meant to do now.":
            "How are you meant to figure this out by yourself? You feel like a teenager again, young and fresh and woefully inexperienced." 
            "It sounded like Angus had been thinking about being polyamorous for a while now, but it's not something that you've even considered." 
            "You wish [partner] was here with you, even if he doesn't have answers either. Everything's so much easier with him by your side."
            jump a_d1_start
        "...angry. What a dick move from Angus!":
            $ a_friend -= 5
            "It was shitty of [partner] to dump this all on you and then leave without letting you get a word in." 
            "You suppose you understand the desire to wait until after the work trip to talk this through, but still, what the hell?" 
            "You're just supposed to sit in your feelings for a whole week, trying to figure out something you didn't ask to figure out? That sucks!"
            jump a_d1_start
        "...worried. You hope Angus is doing okay right now.":
            $ a_friend += 5
            "Angus doesn't always let on how stressed he can get. Knowing him, he's been sitting on this for a while." 
            "You're sure that Angus is freaking out about this, waiting tensely for your response on top of also being stressed about the work trip." 
            "You ache a little for him."
            jump a_d1_start

label a_d1_start:
    "Eventually, the rush hour dies down. There are only a couple people remaining in the store, all of them regulars."

    show bailey neutral

    "Your coworker Bailey strides up to you."
    
    "She joined a little bit after you, and you became fast friends after you realised you..."

    menu:
        "Both love animals - especially the weird, unpopular ones!":
            $ b_friend += 10
            "You remember on her first shift, how Bailey fearlessly coaxed a spider into a cup and out into the garden." 
            "She had gushed all the while about her favourite kind of spiders, disco spiders, which had sparked a lively conversation between the both of you."
            jump a_d1_afterq
        "Both love gossip - about anyone and anything.":
            $ b_friend += 5
            "Somehow, Bailey ferreted out the affair that your old manager had been having with your old coworker." 
            "You had gasped and tittered with each other after each closing shift, and you continued to do so even after your old manager's ex found out, came into the shop and threw a drink in his face."
            jump a_d1_afterq

label a_d1_afterq:

    pl "Heyyy bitch!"

    b "Heyyyyy bitch!"

    pl "How was your weekend?"

    show bailey disgusted

    b "Ugh. {i}so{/i} boring."

    b "My TV broke down so all I had was my phone and my tablet and my laptop to occupy me."

    menu:
        "\"Have you tried going outside instead?\"":
            $ b_friend -= 5
            show bailey angry
            b "Is that some kind of a joke?"
            b "You told me to take it easy after my last marathon!"
            pl "Er... yeah, just a joke. Haha..."
            b "Well, it wasn't funny. Get a better one next time."
            b "Anyway, my TV's all fixed now."
            jump a_d1_aq2
        "\"Is your TV fixed now?\"":
            show bailey happy
            b "Yup!"
            b "Which is great, I've been in need of some brain-empty garbage."
            b "I'm exhausted after my last marathon. Anyway."
            jump a_d1_aq2
        "\"That sounds a little unhealthy... are you doing okay?\"":
            $ b_friend -= 5
            show bailey neutral
            b "Why would I not be doing okay?"
            b "I'm great. It's my TV that's broken."
            b "Well, actually, it's not broken {i}anymore{/i}..."
            jump a_d1_aq2

label a_d1_aq2:

    show bailey happy
    b "Y'know Gary?"

    "You do know Gary." 
    "He's a regular at Sugar in my Coffee. When he's not here, he's tending to the animals on his farm."
    "Bailey has been obsessed with him ever since he started coming here."
    "He's actually here {i}right now{/i} - you hope Bailey keeps her volume down, but it doesn't seem like he's listening out for her anyway."
    "Just last week, she actually succeeded in getting his number."
    "You told her how excited you were for her, all the while thinking..."

    menu:
        "\"I can't believe Gary got to her before me\"":
            "In the present moment, you nod."
            pl "Of course I know Gary."
            pl "Lucky guy..."
            b "Hah! He's not 'lucky' about anything."
            show bailey flirty
            b "Not yet, at least..."
            show bailey neutral
            jump a_d1_aq3
        "\"I'm happy for her! I hope she and Gary get along\"":
            $ b_friend += 5
            "In the present moment, you nod."
            pl "Of course I know Gary."
            pl "Oooh, did something happen between you two?"
            "Bailey giggles."
            b "Nothing {i}really{/i}... Buuuuut, he {i}did{/i} come over to my house over the weekend."
            pl "Gasp! Scandalous!"
            show bailey neutral
            b "To help with the TV, {i}obviously{/i}."
            b "If anything else had happened, I woulda led with that..."
            jump a_d1_aq3
        "\"I would be way better for her than Gary\"":
            $ b_friend -= 5
            "In the present moment you nod, suppressing an eyeroll."
            pl "How could I not know Gary..."
            show bailey disgusted
            b "Okay, chill out."
            b "Are you jealous or something?"
            b "I never said you didn't have a shot, you know."
            show bailey neutral
            b "Anyway."
            jump a_d1_aq3
        "\"God, she's not gonna shut up about him now\"":
            "In the present moment you nod, suppressing an eyeroll."
            pl "Gary again, huh?"
            b "Yup!"
            show bailey embarrassed
            b "Sorry about bringing him up so much..."
            show bailey happy
            b "... {i}NOT!!{/i}"
            jump a_d1_aq3

label a_d1_aq3:

    show bailey neutral
    b "He came over on the weekend to help me out."

    b "I had {i}no idea{/i} he was so good with tech... what a dreamboat!"

    show bailey happy

    b "So now my TV is all fixed up, {i}and{/i} I got to hang out with my crush."

    b "Teehee!"

    "She says 'teehee' out loud, like it's a word."

    show bailey neutral
    b "What about you? How was your weekend?"

    menu:
        "\"It was okay.\" (tell her about the thing with your partner)":
            b "Huh... I see."
            b "That kinda sounds like something I'd do, to be honest."
            b "Talking about polyam stuff can get really shitty."
            b "Like, I have for {i}sure{/i} had exes who really couldn't deal with me being polyam, even though they said they could, and then that got put on {i}me{/i} as {i}my fault{i}, and it was, like, a whole thing!"
            "Wait... Bailey is polyamorous? You had no idea!"
            "...Although, now that she mentions it, it {i}does{/i} make a lot of sense..."
            b "Angus probably just wants to make sure neither of you are gonna say something you regret."
            b "And also so you don't bother him on his work trip!"
            b "Can you blame him??"
            pl "I suppose I can't."
            b "That was rhetorical, bestie. You can blame him all you want!"
            b "If that's how you feel. I'm not a cop."
            "You have no idea if that was a helpful response or not."
            jump a_d1_aq4
        "\"It was kinda shitty.\" (tell her about the thing with your partner)":
            $ b_friend += 5
            b "Huh... I see."
            b "That kinda sounds like something I'd do, to be honest."
            b "Fair enough to be mad at it!"
            b "I'd probably be mad at it, too..."
            b "But also, like, talking about polyam stuff can get kinda... shitty?"
            b "Like, I have for {i}sure{/i} had exes who really couldn't deal with me being polyam, even though they said they could, and then that got put on {i}me{/i} as {i}my fault{i}, and it was, like, a whole thing!"
            "Wait... Bailey is polyamorous? You had no idea!"
            "...Although, now that she mentions it, it {i}does{/i} make a lot of sense..."
            b "Angus probably wants to make sure neither of you are gonna say something you regret."
            b "And also so you don't bother him on his work trip!"
            b "Can you blame him??"
            "You're... not {i}quite{/i} sure if that was the response you were looking for."
            jump a_d1_aq4
        "\"It was exciting!\" (tell her about the thing with your partner)":
            $ b_friend += 10
            show bailey happy
            b "Ooh fun!"
            b "I didn't know you were polyam!"
            pl "Well, I don't 'know' anything just yet. I'm kinda... trying stuff out."
            b "OOOH!"
            b "I'm so happy for you, [name]!"
            b "When I was figuring out I was polyamorous, it was, like, {i}super{/i} a bummer."
            b "My exes just did not get it..."
            "Wait... Bailey is polyamorous? You had no idea!"
            "...Although, now that she mentions it, it {i}does{/i} make a lot of sense..."
            jump a_d1_aqexciting
        "\"It was nothing special.\" (don't tell her about the thing with your partner)":
            b "Fair enough."
            jump a_d1_aq4

label a_d1_aqexciting:
    b "I wish {i}I{/i} had a hot stud of a boyfriend that was looking for a third!"
    menu:
        "\"He actually has a crush on Bradley\"":
            $ b_friend -= 5
            $ a_friend -= 5
            $ b_know_crush = True
            show bailey disgusted
            b "..."
            b "Oh. Gross."
            b "Never mind."
            jump a_d1_aq4
        "Don't tell her that Angus has a crush on Bradley.":
            $ a_friend += 5
            pl "Haha, yeah..."
            pl "I mean, you don't know Gary's preferences, right?"
            show bailey neutral
            b "Oh, no I definitely know."
            b "It was like the first thing I asked him."
            b "He's as monogamous as a tree! Though he's fine with me doing what I want, which, like, good."
            "You sit in bafflement for a moment. Like a tree?"
            "Then it hits you."
            pl "Are you talkng about... mahogany?"
            jump a_d1_aq4

label a_d1_aq4:

    "Just then, the bell for the drinks dings."
    show bailey neutral
    b "Oop! Maybe we should finally do some work around here."

    "You and Bailey head towards the bar."

    "Bailey picks up one tray of drinks that is for some customers sitting outside, and gestures to the ones she leaves behind."

    b "Hey, [name], can you help me with these drinks?"
    
    pl "Sure! Where'm I headed?"

    b "Mimosa for Esma, soda water for Gary, and the decaf extra hot no foam almond cappuccino with honey for Bradley"

    pl "No foam in a cappuccino?"

    pl "So basically a fancy flat white."

    b "Basically a fancy flat white."

    b "He is such an idiot, I swear to God."

    hide bailey neutral

    "Bailey sweeps away to tend to the customers outside."

    menu:
        "Whose drinks will you deliver first?"
        "Esme and Gary are sitting together, so you may as well bring out the mimosa and soda water first":
            $ d1_eg1 = True
            jump d1_eg
        "You should get the 'cappuccino' out to Bradley before it gets cold":
            $ d1_eg1 = False
            jump a_d1_br

label d1_eg:

    scene bg cafe with fade

    pl "Mimosa and soda water?"
    
    "Esme and Gary have been regulars at Sugar in My Coffee for as long as you've worked there."
    "You have no idea how they met, but they seem to be close friends."
    
    show esme neutral at left
    "Esme is dramatic and verbose..."
    
    show gary neutral at right
    "while Gary is more reserved."
    
    "Gary signs to Esme." 
    "When he's talking to everyone else, he writes in an app on his phone which then voices the text for him." 
    
    e "Oh {i}thaaaaaaank{/i} you, darling!"

    e "You wouldn't {i}believe{/i} the day I've been having. Trust me, I need this."

    g "He's been giving me a headache all morning."

    if partner == "Bailey":
        "You remember from last night: Gary is the person who Bailey mentioned she was interested in."

    menu d1_esme_ask:
        "\"What's wrong, Esme?\"":
            $ e_friend += 5
            e "What {i}isn't{/i} wrong, would be a better question."
            jump d1_eg_aq1
        "\"Day drinking? Are you sure you should be doing that at your age?\"":
            $ e_friend -= 5
            show esme angry
            e "Criticising your elders?"
            e "Are you sure you should be doing that at yours?"
            jump d1_eg_aq1
        "\"Tell me about it. I wish I had a mimosa too right now.\"":
            $ e_friend += 5
            show esme happy
            e "Pull up a chair! I'm sure your manager wouldn't mind."
            g "They definitely would."
            jump d1_eg_aq1
        "\"It's barely 11am. How much of a 'day' could it be?\"":
            $ g_friend += 5
            show gary happy
            show esme angry
            "Gary raises his eyebrows and snorts."
            e "Oh, yes, you two think you're such comedians, don't you!?"
            jump d1_eg_aq1
        "Leave":
            jump d1_eg_aq3


label d1_eg_aq1:
    
    show esme neutral
    show gary neutral
    e "You see, darling, I've been caught in a passionate back-and-forth with a new wrestling companion."
    e "He goes by many names. The Green Giant... The King of the Waves... The Emerald Emperor."
    show esme flirty
    e "Personally, I've been calling him... the Legend."
    show esme neutral
    e "The conditions were perfect today. Slight easterly winds, bright skies... a perfect day to hook the biggest catch of my career!"
    e "I got up bright and early and set off. Armed to the teeth, wasn't I, Gary?"
    
    "Gary shrugs."

    g "I wasn't there."

    e "I set off at 5:45. Arrived at my favourite spot at 6." 
    e "I lean back with all my might, cast my rod with a strength that would have sent the gods themselves into a fit of envy, and...!"
    
    show esme sad
    "Esme sniffs and covers his eyes with a sob."

    e "I threw my rod into the sea."

    g "Talk about 'overboard'."

    menu:
        "Laugh":
            $ g_friend += 5
            show gary happy
            show esme angry
            "Gary smiles."
            e "Don't laugh!!!"
            jump d1_eg_aq2
        "Don't laugh":
            $ e_friend += 5
            pl "That's awful."
            show esme neutral
            e "I haven't felt this way since my last husband died."
            g "Why would you say that...?"
            jump d1_eg_aq2

label d1_eg_aq2:

    show gary neutral
    pl "I know how much you loved that rod, Esme."
    pl "I'm sorry for you, uh... loss..."

    show esme neutral
    e "Thank you, sweetheart. I am in mourning. Hence!"
    
    "Esme raises up the mimosa."

    e "I am drowning my sorrows!"

    menu:
        "\"Amen to that.\"":
            $ e_friend += 5
            show esme happy
            e "I knew you would understand, dear."
            jump d1_eg_aq3
        "Pour yourself a glass (of water) and raise it up":
            $ e_friend += 10
            show esme sad
            e "To my rod!"
            show gary embarrassed
            "Gary doesn't write anything, but you can tell he would rather you weren't declaiming loudly about Esme's rod in public."
            jump d1_eg_aq3
        "\"Well, make sure to pace yourself.\"":
            e "Psh! I've spent a whole lifetime pacing myself."
            show esme flirty
            e "Was never any good at it, though."
            jump d1_eg_aq3

label d1_eg_aq3:
    hide esme neutral
    hide gary neutral
    "You leave Esme and Gary's table."
    if d1_eg1 == True:
        "Now, time to get that 'cappuccino' to Bradley."
        if partner == "Angus":
            jump a_d1_br
        else:
            jump b_d1_br
    else:
        jump d1_work_end

label a_d1_br:
    show bradley neutral
    
    "When you arrive at the table, Bradley doesn't even notice you." 
    
    "He is too busy staring out the window, his whole body twisted around in his chair. His eyes are narrowed."
    
    "You remember from last night: Bradley is the person Angus is also interested in dating."

    pl "Cappuccino?"

    br "What? Oh, hello [name]."

    "He reaches out for the cappuccino, except it's already on the table, so he just sort of grasps at thin air."

    br "Yes, yes. Thank you."

    "You can't help but follow his gaze. Outside, Bailey - Bradley's twin sister - is laughing with a few customers."

    menu:
        "\"How are you, Bradley?\"":
            br "Absolutely awful, thanks for asking."
            jump a_d1_br_aq1
        "\"Lovely weather we're having, isn't it?\"":
            show bradley angry
            br "Tch. I suppose. If you're into that sort of thing."
            jump a_d1_br_aq1
        "\"Can I get you anything else?\"":
            $ br_friend += 5
            br "No."
            br "..."
            br "Thanks, though."
            jump a_d1_br_aq1
        "\"What on earth are you looking at?\"":
            br "My sister, unfortunately."
            jump a_d1_br_aq1
        "\"Did you know that Angus is into you?\"":
            $ a_friend -= 5
            $ br_friend -= 5
            show bradley shocked
            br "I... I'm sorry?"
            "For a second it looks like Bradley wants to say something in response, but then a bout of laughter from Bailey makes his head snap back around and scowl."
            show bradley neutral
            jump a_d1_br_aq1
        "Leave":
            jump a_d1_br_end

label a_d1_br_aq1:
    show bradley neutral
    br "When does Bailey get off work?"
    
    br "Wasn't she meant to leave like an hour ago??"

    pl "Uh, nope, she's scheduled for the full day today."

    br "Oh."

    br "Christ. Isn't that my luck."

    menu:
        "\"Sorry.\"":
            br "Oh, no, it's not {i}your{/i} fault."
            jump a_d1_br_aq1_sorry
        "\"You should probably pay more attention to your sister\"":
            $ br_friend -= 5
            show bradley disgusted
            br "Ew. Don't tell me what to do."
            br "It's not like she needs more attention anyways."
            jump a_d1_br_aq2
        "\"Can't you just call or text her afterwards?\"":
            br "As genius of a suggestion as that is, I've already done that."
            br "This is an in-person matter."
            br "An in-person, {i}family{/i} matter, okay?"
            jump a_d1_br_aq2
        "\"Do you want me to leave a message?\"":
            $ br_friend += 5
            br "Hmmm."
            br "..."
            br "......"
            br "No."
            br "I appreciate the offer, though."
            jump a_d1_br_aq2


label a_d1_br_aq1_sorry:

    br "It's hers. As always!"

    menu:
        "\"Hey! Don't talk bad about Bailey!\"":
            $ br_friend += 5
            $ b_friend += 5
            show bradley angry
            br "I can talk about her however much I want!"
            show bradley neutral
            br "It's older sibling privilege. You probably wouldn't understand."
            jump a_d1_br_aq2
        "\"Yeah, that sounds abour right. Classic Bailey.\"":
            $ br_friend -= 5
            $ b_friend -= 5
            show bradley angry
            br "I'm sorry, are you her brother?"
            br "No? How interesting."
            br "Then watch yourself."
            jump a_d1_br_aq2

label a_d1_br_aq2:
    show bradley neutral
    br "I've got a tremendous amount of volunteer work I need to be doing right now, so I'll have to come by another day."

    if br_friend >= 10:
        show bradley happy
        br "Thanks anyway, [name]."
    else:
        "Bradley finishes his ridiculous coffee order in one gulp and gets up."
        "Without another word, he heads out of the door."

label a_d1_br_end:
    hide bradley neutral
    if d1_eg1 == True:
        jump d1_work_end
    else:
        "Now, on to Esme and Gary's table."
        jump d1_eg



label d1_work_end:
    
    "Your shift is just about finished for the day."

    "You say goodbye to your coworkers and manager, and get your things."

    stop music fadeout 3.0

    "You have a class starting in half an hour, so you head to the university."

label d1_uni:
    
    show bg uni with fade
    play music "Thinking Ahead.mp3" loop

    "You make it to campus just in time for your class, Applications of [subject]."
    "You're technically a third year student, but this isn't your first attempt at tertiary education." 
    "You tried an arts course at some fancy establishment years ago, but it just... didn't stick. Life just seemed more important at the time."
    "In some ways, 'life' still {i}is{/i} more important than studying." 
    "But you've come to see life as a collection of whatever you decide to be doing at the time. Which, you suppose, includes studying."
    "Currently, you're not doing a full load of classes. Just taking it slow and steady, one step at a time."
    "As you head into your only tutorial, you notice pretty much everyone is already there."
    "It's still pretty early on in the semester, so you haven't made many... what you might call {i}close{/i} friends. But you know a couple people's names, which is always a good start."
    "There happen to be a couple spaces free next to some of those people you know."
    "Who do you want to sit with?"

    show morgan neutral at right
    show pedro neutral at left

    menu:
        "Pedro (left)":
            $ d1_u_p1 = True
            jump d1_u_p
        "Morgan (right)":
            $ d1_u_p1 = False
            jump d1_u_m


label d1_u_p:
    
    hide morgan neutral

    show pedro neutral at center

    "You sit next to Pedro, a young and studious man with sharp nails and an even sharper attitude."
    "You've been paired a few times in discussions, and he seems really bright."
    
    pl "Hi, Pedro."

    p "Oh, hi, [name]."

    p "Did you have work this morning?"

    pl "Yeah, how could you tell?"

    show pedro disgusted
    p "The smell."

    p "Someone must have had almond milk in their order."

    p "Makes me sick."

    menu:
        "\"Oh, are you allergic?\"":
            p "No, just disgusted."
            jump d1_up_aq1
        "\"Oh, sorry...\"":
            $ p_friend -= 5
            p "Don't apologise, that's weird."
            jump d1_up_aq1

label d1_up_aq1:
    pl "Right..."

    p "I've always hated almond milk."
    show pedro neutral
    p "I mean, I'm lactose intolerant, so I can't drink normal milk."

    p "I do anyway, but that's hardly the point."

    p "I just don't see why you have to make it out of {i}almonds{/i}."

    p "There's plenty of other options, like soy, or rice, or... or oat!"

    p "I just don't see the need to resort to nuts."
    show pedro disgusted
    p "It's {i}milk{/i}. Why would you {i}milk{/i} a {i}nut!?{/i}"

    menu:
        "\"I agree!\"":
            $ p_friend += 5
            pl "I mean, it tastes bad, sounds pretentious, and is for some reason like the most popular requested alternative!?"
            pl "Make it make sense."
            show pedro happy
            p "Exactly!"
            jump d1_up_aq2
        "\"I don't know... I don't really have an opinion.\"":
            $ p_friend -= 5
            show pedro neutral
            p "Hm."
            p "No, I don't suppose you would."
            jump d1_up_aq2
        "\"I think almond milk is fine.\"":
            $ p_friend += 5
            show pedro neutral
            pl "Some people like it, I see no reason to stop them from enjoying it."
            p "Right. Everyone's entitled to their opinions."
            p "Their very, very {i}wrong{/i} opinions."
            jump d1_up_aq2

label d1_up_aq2:
    show pedro neutral
    pl "Anyway, have you been up to much today?"

    p "Not really. I called my mum. Painted my nails. See?"

    "His nails are a very nice shade of purple."

    menu:
        "\"Ooh, pretty!\"":
            p "Thanks."
            jump d1_up_aq3
        "\"Oh nice! Did you do that yourself?\"":
            $ p_friend += 5
            show pedro happy
            p "I did. Impressive, I know."
            p "I could do yours sometime, if you'd like."
            jump d1_up_q3_2
        "\"Don't you feel a bit... emasculated? Or like, nervous to wear that?\"":
            $ p_friend -= 10
            p "..."
            p "Why should I?"
            show pedro disgusted
            p "Only creeps like you are thinking that."
            jump d1_up_aq3

label d1_up_q3_2:
    menu:
        "\"Oh, I could never pull that off\"":
            "Pedro looks you up and down."
            show pedro neutral
            p "No, you're probably right."
            jump d1_up_aq3
        "\"That would be awesome!\"":
            $ p_friend += 5
            show pedro happy
            p "Great."
            jump d1_up_aq3
        "\"Hm. I appreciate the offer, but I don't think it's for me.\"":
            $ p_friend += 5
            show pedro neutral
            p "Fair enough. It's not for everyone."
            p "Some of us just shine brighter."
            jump d1_up_aq3

label d1_up_aq3:
    show pedro neutral
    p "Anyway, I think the tute's about to start properly. I want to pay attention."

    "During the class, Pedro has a lot of cool and insightful things to say." 
    "You're not sure you're always on the same wavelength, but he definitely knows what he's talking about."
    "Throughout the class, you..."

    menu:
        "Throughout the class, you..."
        "Agree with everything he has to say":
            $ p_friend -= 5
            jump d1_up_aq4
        "Disagree with everything he has to say":
            $ p_friend -= 5
            jump d1_up_aq4
        "Chime in here and there, neither agreeing nor disagreeing with Pedro":
            jump d1_up_aq4
        "It doesn't matter what he has to say! You have your own opinions, and they deserve to be shared!":
            $ p_friend += 10
            jump d1_up_aq4

label d1_up_aq4:

    "The class comes to an end."

    "You didn't catch quite everything your tutor was talking about, but you think you learnt a decent amount."

    "The practical side of things is always tricky, but rewarding when you get it right."

    "As you're packing up your things, Morgan comes up to you."

    show morgan neutral at left

    p "Bye, [name]."

    hide pedro neutral

    pl "Bye, Pedro."

    show morgan neutral at center

    m "Hey, [name], how are you?"

    pl "Alright... how about you?"

    m "I'm pretty good. Wiped, but good."

    pl "..."

    show morgan embarrassed
    m "Um. A-Anyway. I thought you had some really cool things to say today."

    show morgan neutral
    m "That source you mentioned, Rediscovered History of [subject], do you remember the name of the author?"

    menu:
        "\"I don't, sorry... But you should be able to find it on the uni library site pretty easily.\"":
            m "Okay, cool. Thanks."
            jump d1_up_aq5
        "\"I don't... maybe look it up yourself?\"":
            $ m_friend -= 5
            show morgan embarrassed
            m "Ah, okay... No, you're probably right."
            m "Sorry to... bother you."
            jump d1_up_aq5
        "\"I don't... but I have the source bookmarked. Is it okay if I DM you the link?\"":
            $ m_friend += 5
            show morgan happy
            m "Oh! Sure. Thanks, [name]. I appreciate it."
            jump d1_up_aq5

label d1_up_aq5:
    show morgan neutral
    m "I was just thinking it could be a good source for what I want to write for the assignment."

    menu:
        "\"Oh, shit, the assignment...\"":
            $ m_friend += 5
            m "I'm guessing you haven't started yet...?"
            m "Well, hey, that makes me feel better haha!"
            jump d1_up_aq6
        "\"I'm already finished with my essay.\"":
            m "Jeez, way to show me up, [name]."
            m "I'm kidding. Good job! Very impressive."
            m "Wild to me, but impressive."
            jump d1_up_aq6
        "\"Good idea, I'm planning to use it, too.\"":
            show morgan happy
            m "Uh oh! Competition..."
            show morgan neutral
            jump d1_up_aq6

label d1_up_aq6:
    show morgan happy
    m "Anyway, good luck with your essay."

    m "With how much of a grump Mr Holt is, I'm guessing it'll be hard to do well."

    menu:
        "\"Thanks. Good luck to you, too.\"":
            jump d1_up_end
        "\"God, yeah, he's such a ... what's the word I'm looking for here?\"":
            $ m_friend += 5
            jump d1_up_holtq
        "\"Really? I thought he was pretty nice.\"":
            $ m_friend -= 10
            jump d1_up_holtq2

label d1_up_holtq:

    m "A sexist asshole?"

    menu:
        "\"Yeah, that's it!\"":
            jump d1_up_holtq1
        "\"I was thinking 'insufferable fuckwit', but that works, too.\"":
            $ m_friend += 5
            show morgan happy
            m "Yeah, that definitely works."
            m "Honestly, it'd be almost funny, if it wasn't so disgusting."
            jump d1_up_end

label d1_up_holtq1:
    show morgan angry
    m "Yeah... he really rubs me the wrong way."

    menu:
        "\"And fair enough, too!\"":
            $ m_friend += 5
            pl "He's been really rude to a lot of students, particularly women."
            pl "Which is to say nothing of how he's treated trans students..."
            m "Yeah..."
            m "It'd almost be funny, if it wasn't so disgusting."
            jump d1_up_end
        "\"I don't know, maybe we're misjudging him.\"":
            m "I don't really think so."
            m "But maybe... maybe he's got something really dark going on."
            show morgan neutral
            m "I still don't think that's any excuse for his behaviour, though."
            jump d1_up_end

label d1_up_holtq2:
    show morgan angry
    m "No, he's sexist."

    menu:
        "\"Really? I'm sorry, I hadn't noticed... I guess I was wrong.\"":
            $ m_friend += 5
            pl "I've been pretty checked out of these lessons, to be honest."
            show morgan neutral
            m "Hmm... I guess that's fair enough."
            m "Still, you should probably pay more attention when someone's being such an asshole."
            jump d1_up_end
        "\"Not that I've noticed? Maybe you're reading into things too much.\"":
            $ m_friend -= 5
            show morgan angry
            m "I'm not."
            m "But whatever."
            jump d1_up_end

label d1_up_end:
    show morgan neutral
    m "Anyway, I've got to head off now."
    
    m "See you later."

    pl "See you later!"

    jump d1_uni_end


label d1_u_m:
    
    hide pedro neutral

    show morgan neutral at center

    "You sit next to Morgan, who is a shy and sweet young woman, from what you can gather."

    "She doesn't say very much during classes, but when she does contribute, you always find it interesting."

    m "Oh, hi, [name]."

    pl "Hi Morgan."

    m "How are you going today?"

    menu:
        "\"Not bad.\"":
            m "Cool."
            jump d1_um_cstart
        "\"Alright, but I had a bit of a weird day yesterday.\"":
            jump d1_um_aqweird
        "\"Kind bad to be honest - I had a bad day yesterday.\"":
            jump d1_um_aqbad

label d1_um_aqweird:

    m "Oh? What happened? If you don't mind me asking."

    menu:
        "Tell her about [partner] bringing up polyamory and then leaving for a week":
            pl "Well, my partner told me they're polyamorous, and told me not to say anything until next week, after a work trip."
            jump d1_um_weird1
        "Don't tell her":
            pl "It's sorta... private."
            m "Oh, no worries!"
            jump d1_um_cstart

label d1_um_weird1:

    m "Oh, that's kind of rough."

    menu:
        "\"Yeah. To be honest, I'm a bit angry with them\"":
            jump d1_um_weird2
        "\"It's ok - I get it. I'm just a bit lost.\"":
            $ m_friend += 5
            m "Well that's very... sensible?"
            m "I mean... like, you're in a very difficult situation, but you're still being really respectful of your partner."
            jump d1_um_cstart
        "\"I don't really know what to think\"":
            m "That's fair enough."
            jump d1_um_cstart

label d1_um_weird2:
   
    m "For leaving? Or for being polyam?"
    
    menu:
        "\"For leaving without giving me a chance to respond\"":
            m "That's fair enough. It's a bit of a dick move."
            m "But I have to admit - I see where they're coming from."
            m "I mean, I'd be nervous, too."
            jump d1_um_cstart
        "\"I don't know what for, really. I just am\"":
            $ m_friend += 5
            m "I get that."
            m "It sounds really confusing."
            jump d1_um_cstart
        "\"For wanting to be... unfaithful.\"":
            $ m_friend -= 5
            show morgan angry
            m "That's not really what polyamory is."
            m "Like, at all..."
            m "I get you're confused, but that's a pretty shitty thing to think about your partner, to be frank."
            jump d1_um_cstart

label d1_um_aqbad:
    show morgan sad
    m "I'm sorry to hear that. Do you want to talk about it at all?"

    menu:
        "\"Yes\" (Tell her about your partner)":
            jump d1_um_bad1
        "\"Not really\" (Don't tell her)":
            $ m_friend += 5
            show morgan neutral
            m "Well, that's fair."
            m "I hope today is better for you."
            jump d1_um_cstart

label d1_um_bad1:
    show morgan neutral
    pl "It's just that... my partner dropped something kind of huge, and then went off to a trip."

    menu:
        "\"I don't really know how to feel about it\"":
            m "That's fair. It sounds pretty... intense."
            jump d1_um_cstart
        "\"And it feels pretty shitty\"":
            $ m_friend += 5
            m "Aw man, I'm sorry. That sucks."
            jump d1_um_cstart
        "\"And it's okay, but now I just feel kind of down.\"":
            m "Well, that's fair enough. It sounds pretty difficult."
            jump d1_um_cstart

label d1_um_cstart:

    "Class starts before the two of you can talk much more."

    "Throughout the tutorial, Morgan speaks to you, asking you questions and making little comments here and there."

    menu:
        "Focus on the class":
            "Even though you're paying attention, it feels like your tutor is eyeing you with suspicion."
            jump d1_um_aqclass
        "Chat normally with Morgan":
            $ m_friend += 5
            "Your tutor tells you to be quiet once or twice."
            "Morgan rolls her eyes at him."
            jump d1_um_aqclass
        "Try to joke a bit with Morgan":
            $ m_friend += 10
            show morgan happy
            "Morgan laughs at some of your jokes, and scoffs playfully at others."
            "Your tutor tells Morgan off for laughing, and for 'distracting the class'."
            "Morgan rolls her eyes at him."
            jump d1_um_aqclass
        "Flirt with Morgan":
            $ m_friend -= 5
            show morgan sad
            "She smiles a little, but for only less than a second."
            "She does not flirt back."
            jump d1_um_aqclass

label d1_um_aqclass:
    show morgan neutral
    "The class comes to an end."

    m "Bye, [name]! See you later."

    pl "See you, Morgan."

    hide morgan neutral

    show pedro neutral

    "Pedro is walking towards you."

    p "Hello, [name]."

    pl "Hi, Pedro."

    pl "What can I do for you?"

    "Pedro is a young and studious man with sharp nails and an even sharper attitude."
    
    "You've been paired a few times in discussions, and he seems really bright, if a little abrasive."

    p "Well... that thing you said in class. About the potential negatives of [subject] in a tertiary institution..."
    show pedro angry
    p "I disagree."

    p "I didn't have a chance to respond during the tute, but I think you're wrong."

    menu:
        "\"Okay...?\"":
            jump d1_um_ok
        "\"Well, maybe I was wrong. I sort of just said it.":
            $ p_friend -= 5
            p "Gross."
            jump d1_um_aqp1
        "\"Well, that's not going to change my opinion, but okay.\"":
            $ p_friend += 5
            show pedro shocked
            p "Nor should it!"
            jump d1_um_opinion

label d1_um_ok:

    p "Okay? You don't have any sort of follow up defense for your point?"

    menu:
        "\"Not really?\"":
            $ p_friend -= 5
            p "Psh. Typical."
            p "I bet you don't even really believe your own point!"
            jump d1_um_aqp1
        "\"Do I need to defend my point to you?\"":
            $ p_friend += 5
            show pedro neutral
            p "I guess not..."
            p "Maybe later, like tomorrow, you could explain your point to me more."
            p "See if I can see your side."
            jump d1_um_aqp1
        "\"Of course I do! I'm just not in the mood to share it\"":
            show pedro neutral
            p "Ohhhhhh sure. Of course."
            "Pedro rolls his eyes."
            jump d1_um_aqp1

label d1_um_opinion:

    p "I just thought you should know that not everyone agrees with you, even though it seemed like a lot of people did."

    menu:
        "\"Good. It wouldn't be interesting if everyone agreed.\"":
            $ p_friend += 5
            show pedro happy
            p "That's true."
            p "Fighting about it is better."
            jump d1_um_aqp1
        "\"Well, that's a shame\"":
            $ p_friend -=5
            show pedro neutral
            p "Really?"
            p "I think it's more interesting if there's more diversity of opinions."
            p "Maybe I'm just more mature about it than... others."
            jump d1_um_aqp1
        "\"Maybe it's just you that disagrees\"":
            show pedro angry
            p "And what? I'm not enough?"
            p "It wouldn't just be me, anyway. Not in the real world."
            jump d1_um_aqp1

label d1_um_aqp1:
    show pedro neutral
    pl "Okay, sure."
    
    pl "Thanks for that, Pedro..."

    menu:
        "\"Anyway, see you later.\"":
            $ p_friend -= 5
            p "Oh, sure... Bye, I guess."
            jump d1_um_aqp2
        "\"Was there anything else?\"":
            p "No. I just wanted you to know that."
            jump d1_um_aqp2
        "\"What is your take on it, anyway?\"":
            $ p_friend += 10
            p "It's far too complicated to be condensed to a passing conversation."
            if p_friend >= 15:
                $ p_tell_take == True
                p "Sit with me next class, and I'll tell you then."
                jump d1_um_aqp2
            else:
                p "Maybe you'll hear it in class, sometime."
                jump d1_um_aqp2

label d1_um_aqp2:
    
    p "I've got to run, anyway."

    p "See you later."

    hide pedro neutral



label d1_uni_end:

    stop music fadeout 5.0
    "You're all finished with uni for the day."

    "But, you can't quite head home yet."

label d1_po:

    scene bg black with fade

    "Now it's time to head to the post office."
    "You've been waiting for a package from your parents." 
    "It's nothing special, just some old clothes and things that you weren't able to take with you when you first moved out."
    "The package definitely should have arrived by now, but it's nowhere to be seen. You figure that the local post office might have it."
    
    scene bg post office with fade
    play music "Welcome.mp3" loop
    "When you enter, nobody is manning the desk."
    "However, you can hear muffled voices coming from the mailroom." 
    "One person gasps, then laughs in a bewildered sort of way."

    menu:
        "Ring the bell":
            "Someone calls out from the depths of the mailroom."
            ap "One second!!"
            jump d1_po_aq1
        "Wait for someone to arrive":
            "You can hear people shuffling around in the mailroom."
            "It's probably best just to wait."
            jump d1_po_aq1

label d1_po_aq1:
    
    show april neutral

    "April the postie emerges from the back." 
    "She looks a bit frazzled, but they perk up when she sees that it's you."

    ap "Hi there, [name]! What a pleasant surprise!"

    "April is about the same age as you." 
    "You're both new to the area, and while you've always been friendly with each other, you've never gotten the chance to talk much because of your incompatible work hours."

    pl "Hey there, April. How're things?"
    show april sad 
    ap "Oh, absolutely wretched!"
    show april neutral
    ap "Just kidding. Busy as always!"

    ap "Though, you've walked in during the afternoon lull, so you'll have to take my word for it."

    ap "What can I do ya for?"

    menu:
        "\"I'm here to check on a parcel\"":
            pl "It's from my parents. They mailed it about a week ago?"
            pl "I just wanted to check if it's arrived."
            "April sucks in a bt of ar through their teeth."
            jump d1_po_aq2
        "\"Everything good back there?\"":
            $ ap_friend += 5
            show april embarrassed
            ap "Aha... I guess you could hear some of that, huh?"
            jump d1_po_aq2

label d1_po_aq2:
    show april sad
    ap "I hate to be the bearer of bad news, but our warehouse manager called in sick out of nowhere."

    ap "There's a blanket delay on all mail items until he comes back."
    show april neutral
    ap "Though if your package was sent out last week, it shouldn't be too far off. Maybe give it another day?"

    menu:
        "\"It's not urgent, I can wait another day\"":
            show april happy
            ap "That's good! I'm glad for that."
            ap "I've had a bunch of people come in today, and some of them really do need their deliveries to be made on time."
            ap "So, like... glad you're not one of them!"
            jump d1_po_aq3
        "\"That kinda sucks, but I know it's not your fault\"":
            $ ap_friend += 5
            ap "Aw, thanks for understanding, [name]."
            ap "It's fair enough to be annoyed - I know I would be!"
            jump d1_po_aq3
        "\"That's really not good enough, April\"":
            $ ap_friend -= 5
            show april embarrassed
            ap "Yeah... I understand."
            show april neutral
            ap "I'm really sorry about the inconvenience. We're working as hard as we can to ensure that packages get sent out to the community ASAP."
            "They used her customer service voice there. You get the impression April's been giving a {i}lot{/i} of people that little spiel today."
        "Thank April and leave":
            jump d1_po_end

label d1_po_aq3:
    show april neutral
    ap "It's just totally out of character for our warehouse manager... Not even Millicent can remember the last time he took a day off."
    
    pl "I guess everybody's got to take a sick day some time."

    ap "That's true!"

    ap "And there's not many {i}good{/i} days to be sick when you work with mail, lemme tell you!"

    ap "Oh!"
    show april happy
    "April lights up a little bit."

    ap "That reminds me of a fun fact I learned recently - did you know calling in sick is statistically the third-likeliest reason people make phone calls?"

    menu:
        "\"Really?? That's wild!\"":
            ap "Yup! Wild {i}and{/i} true!"
            ap "What a world we live in, eh?"
            jump d1_po_aq4
        "\"There's no way that's true\"":
            $ ap_friend += 5
            show april embarrassed
            ap "What, are you calling me a liar, [name] Lastname?"
            ap "I'd never lie. I've never told a lie in my entire life."
            jump d1_po_aq4
        "\"Ha ha ha, you're funny, April\"":
            $ ap_friend -= 5
            show april angry
            ap "Who says I'm joking?"
            jump d1_po_aq4
        "\"What are the second - and most - likely reasons?\"":
            $ ap_friend += 10
            ap "Hmm, let me see..."
            ap "We could come up with them together! Haha!"
            jump d1_po_aq4

label d1_po_aq4:

    "Another voice issues from the mailroom. It's a much older, female voice."
    
    mil "April? Are you telling lies again?"
    show april neutral
    ap "Whoops! I've been rumbled."

    ap "I'll have to make my dastardly getaway."

    ap "Though I {i}am{/i} stuck behind this desk, so somebody's gonna have to do one for me..."

    menu:
        "\"Should I do that?\"":
            ap "Mmmmmm..."
            ap "...Nah. The moment's passed."
            pl "Oh. My bad..."
            ap "Nothin' bad about it! Did you need anything else today?"
            pl "I was just checking on the package, really. Thanks for your help, April."
            pl "And for the fun fact."
            ap "Anytime!"
            ap "See you tomorrow, [name]."
            jump d1_po_end
        "\"You could run and I could take your place!\"":
            ap "Ooh, that's a fun idea!"
            ap "But nah, I'm super duper absolutely still on the clock."
            ap "Was there anything else you needed today?"
            pl "I was just checking on the package, really. Thanks for your help, April."
            pl "And for the fun fact."
            ap "Anytime!"
            ap "See you tomorrow, [name]."
            jump d1_po_end
        "Immediately turn tail and bolt outta there.":
            $ ap_friend += 10
            show april happy
            "You hear April's gleeful shouts receed into the distance."
            ap "They're getting away, Millicent!"
            hide april happy
            ap "{i}They're getting awaaaayyyy... {/i}"
            "You're like 90 percent sure she made their own voice fade away on purpose there."
            "Post office visits are kind of a pain, but at least April makes them fun."
            jump d1_po_end

label d1_po_end:
    "You leave the post office and finally head home for the day."
    stop music fadeout 5.0
    scene bg black with fade

label d1_home:
    "When you get home for the evening, you feel completely wiped." 
    scene bg bedroom aft with fade
    "You shuck off your shoes, put the kettle on, get changed into something cosy and sit down with your feet up for a moment."
    "You need to get started on dinner, but before that, you want to see how [partner] is doing." 
    "You fish out your phone."
    play music "Slipstream.mp3" loop
    if partner == "Angus":
        jump d1_a_home
    else:
        jump d1_b_home

label d1_a_home:
    "Angus has already texted you at some point during the day, but you didn't see the notification."
    a "{i} Hi, [name]! I hope your day has gone well. My first day here was pretty hectic, but there have been some fascinating talks already and I've met some cool people. Been thinking of you <3{/i}"

    menu:
        "Give a generic response":
            pl "{i}Thanks Angus! My day was alright, but long. Glad ur day was ok by the sounds of it! Thinking of you too <3{/i}"
            "Angus replies almost instantly."
            a "{i} Fair enough. Make sure to rest tonight!{/i}"
            jump d1_a_home_aq1
        "Give a flirty response":
            $ a_friend += 5
            pl "{i}You're pretty cool yourself ;) Thinking of you too <3 {/i}"
            "Angus replies almost instantly."
            a "{i}Hmmm... and I guess ur not so bad either ;){/i}"
            jump d1_a_home_aq1
        "Give a tired response":
            pl "{i}My day was sooooo long :( Really tired now{/i}"
            "Angus replied almost instantly."
            a "{i}Aw bby I'm sorry :( Make sure to rest up tonight and take things easy!{/i}"
            jump d1_a_home_aq1
        "Ignore the message and ask if you can talk about being polyamorous.":
            $ a_friend -= 10
            pl "{i}Hey can we talk about yesterday? The whole polyamory thing?{/i}"
            "Angus responds after a few minutes."
            a "{i}Sorry, [name]. I really want to wait until I get back, and talk in person.{/i}"
            jump d1_a_home_aq1

label d1_a_home_aq1:

    a "{i}Anyway. Anything interesting happen today?{/i}"
    menu:
        "\"Yeah! I had some really fun talks with some people!\"":
            $ a_friend += 5
            a "{i}Oh, that's awesome!{/i}"
            jump d1_a_home_newf
        "\"Yeah actually... I think I'm maybe interested in someone...\"":
            a "{i}Oh? Who is it? Do I know them?{/i}"
            jump d1_a_home_psn
        "\"Not really\"":
            a "{i}Damn{/i}"
            jump d1_a_home_end
        "\"I really think we should talk about yesterday\"":
            $ a_friend -= 10
            jump d1_a_home_yesterday

label d1_a_home_newf:
    a "{i}New friends, or...?{/i}"
    menu:
        "\"Too soon to say for sure\"":
            a "{i}Well, that's fair. Good luck!{/i}"
            jump d1_a_home_end
        "\"I think so!\"":
            a "{i}Hey, that's awesome!{/i}"
            jump d1_a_home_end
        "\"Maybe more than friends...\"":
            a "{i}Oho?? Who? Do I know them?{/i}"
            jump d1_a_home_psn

label d1_a_home_psn:
    menu:
        "\"I don't really wanna say who...\"":
            $ crush = "That person"
            a "{i}Oh boo!{/i}"
            a "{i}But fr that's fair enough. Good luck!{/i}"
            jump d1_a_home_end
        "\"Well, it's a few people...\"":
            $ a_friend += 5
            $ crush = "Everyone"
            a "{i}Oh! Good for you!{/i}"
            a "{i}Do you think any of them might be into you, too?{/i}"
            jump d1_a_home_aq2
        "Bailey":
            $ crush = "Bailey"
            a "{i}Oh! She works with you, right?{/i}"
            a "{i}She seems nice{/i}"
            a "{i}If a little... intense{/i}"
            a "{i}Do you think she might be interested in you, too?{/i}"
            jump d1_a_home_aq2
        "Bradley":
            $ crush = "Bradley"
            a "{i}So now you're my partner and my competition, huh?{/i}"
            a "{i}Like, fr, I'm pretty sure Bradley is monogamous{/i}"
            a "{i}So may the best person win, I guess!{/i}"
            a "{i}Do you think he might be interested in you, too?{/i}"
            jump d1_a_home_aq2
        "Esme":
            $ crush = "Esme"
            a "{i}I don't think I know of Esme...{/i}"
            a "{i}Well, good luck!{/i}"
            a "{i}Do you think she might be interested in you, too?{/i}"
            jump d1_a_home_aq2
        "Gary":
            $ crush = "Gary"
            a "{i}Oh, Gary!{/i}"
            a "{i}I think Bradley may have mentioned him before{/i}"
            a "{i}He's close with your coworker Bailey, right?{/i}"
            a "{i}Anyway, do you think he might be interested in you, too?{/i}"
            jump d1_a_home_aq2
        "Morgan":
            $ crush = "Morgan"
            a "{i}From your class?{/i}"
            a "{i}Cool. Do you think she might be interested in you, too?{/i}"
            jump d1_a_home_aq2
        "Pedro":
            $ crush = "Pedro"
            a "{i}From your class?{/i}"
            a "{i}Cool. Do you think he might be interested in you, too?{/i}"
            jump d1_a_home_aq2
        "April":
            $ crush = "April"
            a "{i}Oh April! From the post office, right?{i}"
            a "{i}They're a lot of fun{/i}"
            a "{i}Do you think she might be interested in you, too?{/i}"
            jump d1_a_home_aq2

label d1_a_home_aq2:
    menu:
        "\"No idea!\"":
            a "{i}Well, good luck anyway!{/i}"
            jump d1_a_home_end
        "\"Maybe... there have been some hints\"":
            a "{i}Oooh spicy! Good luck!{/i}"
            jump d1_a_home_end
        "\"Oh, definitely!\"":
            a "{i}Someone's confident...{/i}"
            a "{i}Good luck, anyway!{/i}"
            jump d1_a_home_end
        "\"Definitely not\"":
            a "{i}Damn, that's a shame :/{/i}"
            a "{i}Good luck, anyway!{/i}"
            jump d1_a_home_end

label d1_a_home_yesterday:

    if a_friend >= 15:
        a "{i}I really don't want to. Can we please just talk about your day?{/i}"
        menu:
            "\"Okay, I'm sorry\"":
                $ a_friend += 5
                jump d1_a_home_reset
            "\"Fine.\"":
                jump d1_a_home_reset
            "\"No. We have to talk about it.\"":
                $ a_friend -= 5
                "It's a few minutes before Angus responds."
                a "{i}I think I'm actually just gonna go to bed{/i}"
                a "{i}Talk tomorrow.{/i}"
                a "{i}Goodnight.{/i}"
                jump d1_a_home_end2
    else:
        "It's a few minutes before Angus responds."
        a "{i}Hey, I'm actually pretty tired.{/i}"
        a "{i}Think I'll go to bed. Talk to you tomorrow{/i}"
        a "{i}Goodnight.{/i}"
        jump d1_a_home_end2

label d1_a_home_reset:
    menu:
        "\"Anyway, I had some really fun talks with some people today\"":
            $ a_friend += 5
            a "{i}Oh, that's awesome!{/i}"
            jump d1_a_home_newf
        "\"Anyway... I actually... I think I'm maybe interested in someone...\"":
            a "{i}Oh? Who is it? Do I know them?{/i}"
            jump d1_a_home_psn
        "\"Nothing really interesting happened today\"":
            a "{i}Damn{/i}"
            jump d1_a_home_end

label d1_a_home_end:
    
    a "{i}Anyway, I'm kinda beat...{/i}"
    a "{i}I might head to bed now{/i}"
    
    if a_friend >= 20:
        a "{i}Love you, goodnight xx {/i}"
    else:
        a "{i}Goodnight x{/i}"
    
    pl "{i}Goodnight!{/i}"

    jump d1_a_home_end2

label d1_a_home_end2:

    scene bg bedroom n with fade
    stop music fadeout 5.0
    "Your day finally comes to an end."
    "You hop into bed, watch some videos on your phone, and eventually fall asleep."
    "You wonder what tomorrow will hold."

    jump d2_start

label d2_start:

    show bg black with fade

    "That night, you have very vivid, involved dreams"

    "...that you can't remember even a little bit."

    play music "Theme.mp3" fadein 1.5 loop

    scene bg bedroom with fade

    "Today is a bit less full-on than yesterday, as you only have to go to work. And then the post office afterwards, but that shouldn't be too difficult."

    "After scrolling on your phone for a bit, you finally get up, get showered, and get dressed for the day."   
    
    "You woke up with a fair amount of time, so you're not in any rush." 
    
    "Still, it's a good idea to head to work now."

    stop music fadeout 3.0

    if partner == "Angus":
        jump d2_a_work
    else:
        jump d2_b_work

label d2_a_work:

    scene bg cafe with fade
    play music "Lounge Lizard.mp3" loop
    "Work is busy for the first hour or so, but it flattens out pretty quickly." 
    "Tuesdays are never as bad as Mondays, which gives you ample time to chill out and chat with Bailey and your other coworkers."

    show bailey neutral at center

    pl "Hey, girlie!"

    b "Heyyy!"

    b "Okay, I've got some really important shit to tell you."

    pl "Oh? Intriguing."

    pl "Is this about Gary, by any chance?"

    b "Wowww, you're sharp!"

    show bailey happy

    b "Haha, just kidding. It's, like, {i}so{/i} obvious."

    b "I've come to a really significant crossroads, [name]."

    show bailey neutral

    b "I need to know... if I should ask Gary out or not."

    b "This is a really big deal for me! So you better answer with nothing but my best interests in mind, 'kay?"

    menu:
        "\"I think you should go for it - Gary seems into you!\"":
            $ b_friend += 5
            b "Yeah??"
            b "You think so??!!"
            show bailey happy
            b "YAY!! I {i}knew{/i} you'd get it."
            "You're pretty sure Bailey would have asked him out regardless of what you said. Either way, it's nice to see her happy."
            show bailey neutral
            jump d2a_work_aq1
        "\"I think you shouldn't go for it - Gary doesn't seem into you\"":
            $ b_friend -= 5
            b "Oh yeah?"
            show bailey sad
            b "Weird... that's totally not been my experience."
            b "I probably shouldn't have asked you tee bee haitch."
            b "I know Gary way better!"
            show bailey neutral
            b "I'm doing it anyway - with or without your blessing."
            "In hindsight, you probably should have known this would happen."
            jump d2a_work_aq1
        "\"You should date me instead\"":
            $ b_friend += 5
            b "Hah! How bold."
            if b_friend >= 25:
                show bailey flirty
                b "After I ask Gary out, maybe I'll consider it..."
                b "Don't get me wrong, he's still totally my number one!"
                b "But I've still got some open spots, if you catch my drift? Haha!"
                show bailey neutral
                jump d2a_work_aq1
            else:
                b "Not interested, though."
                b "You're gonna have to work a lot harder than that."
                b "Gary's still totally my number one!"
                jump d2a_work_aq1
        "\"You should date someone else\"":
            $ b_friend -= 10
            show bailey disgusted
            b "Did you forget that I'm polyamorous or something?"
            b "I don't want to date someone else right now. I can do that later if I want."
            b "I want to date {i}Gary{/i}."
            b "Which I think I will after all."
            b "No thanks to {i}you{/i}."
            show bailey neutral
            jump d2a_work_aq1
        
label d2a_work_aq1:
    b "Speaking of dating, how's things with you and Angus?"
    
    pl "Oh - like the polyam stuff?"

    b "No, dummy!"

    b "Well... technically, yes."

    if b_know_crush == True:
        jump d2_bno
    else:
        jump d2_bnno

label d2_bno:
    b "I was doing some thinking about yesterday."
    show bailey disgusted
    b "Y'know, when you said Angus is interested in - {i}eugh{/i}- Bradley."

    pl "Yeah, he-"

    "Bailey cuts you off."

    b "Of course, there's no actual way that's the name I heard."
    show bailey neutral
    b "I must've fully not heard you correctly!"

    b "So I wanted to check to make sure I knew who Angus' {i}actual{/i} crush is."

    b "Gimme the hot goss!"

    menu:
        "\"No, you heard right\"":
            $ b_friend -= 5
            $ a_friend -= 5
            show bailey disgusted
            b "..."
            show bailey happy
            b "Ahahahahahahaha!"
            b "You're hilarious, [name!]"
            show bailey neutral
            b "Wow, you really almost got me there. Haha. {i}Bradley{/i}."
            b "It's cool if you don't want to our your boyf."
            pl "Boyf...?"
            b "I'm just sayin', if you ever want to talk crushes, I'm here."
            jump d2a_work_aq2
        "Make up someone Angus is into":
            $ b_friend += 5
            pl "Well, he's, uh, kind of short."
            b "Mhmmmm?"
            pl "He's a bit of a homebody."
            pl "Apparently he's pretty scary when he's angry, but I've never seen it."
            b "Is that so?"
            pl "He likes making jokes. Lives in a colder climate than I'm used to."
            pl "Low sort of voice? Uh... sexy. To some. I don't really see the appeal, personally."
            b "Uh-huh."
            b "And this guy's name?"
            pl "Uhm. Sss. Sss-uh..."
            "Bailey stares impassively at you, then bursts into laughter."
            show bailey happy
            b "If you don't wannna tell me, you don't have to!"
            show bailey neutral
            b "Although it was really funny seeing you try to come up with someone."
            jump d2a_work_aq2
        "\"...You don't know them.\"":
            $ a_friend += 5
            b "Fair enough then!"
            jump d2a_work_aq2

label d2_bnno:
    b "I want to know if Angus has a crush on anyone I know!"
    
    b "We've met a few times. I like him!"

    b "You hit the jackpot, I think."

    b "Soooo, dish! Does he have his eyes on anyone??"

    menu:
        "\"He's got a crush on Bradley\"":
            $ b_friend -= 5
            $ a_friend -= 5
            show bailey disgusted
            b "..."
            show bailey happy
            b "Ahahahaha!"
            b "You're hilarious, [name]!"
            show bailey neutral
            b "Wow, you really almost got me there. Haha. {i}Bradley{/i}."
            b "It's cool if you don't want to out your boyf."
            pl "Boyf...?"
            b "I'm just sayin', if you ever want to talk crushes, I'm here!"
            jump d2a_work_aq2
        "Make up someone Angus is into":
            $ b_friend += 5
            pl "Well, he's, uh, kind of short."
            b "Mhmmmm?"
            pl "He's a bit of a homebody."
            pl "Apparently he's pretty scary when he's angry, but I've never seen it."
            b "Is that so?"
            pl "He likes making jokes. Lives in a colder climate than I'm used to."
            pl "Low sort of voice? Uh... sexy. To some. I don't really see the appeal, personally."
            b "Uh-huh."
            b "And this guy's name?"
            pl "Uhm. Sss. Sss-uh..."
            "Bailey stares impassively at you, then bursts into laughter."
            show bailey happy
            b "If you don't wannna tell me, you don't have to!"
            show bailey neutral
            b "Although it was really funny seeing you try to come up with someone."
            jump d2a_work_aq2
        "\"...You don't know them.\"":
            $ a_friend += 5
            b "Fair enough then!"
            jump d2a_work_aq2

label d2a_work_aq2:
    pl "Crushes aside, is there anything new with you?"
    show bailey sad
    b "Not really. It's my mum's birthday soon, so I've been agonising over what gift to get her."

    b "I'm freaking out about it a little, but mostly it'll be fine."

    pl "I'm sure she'll love whatever you get her!"

    pl "Though, I get it, gift-giving can be stressful."
    
    pl "Angus still makes fun of my for the gift I gave him for our first anniversary."
    show bailey neutral
    b "Oh? Which was??"

    pl "A single orange."
    show bailey happy
    b "HAH!"
    show bailey neutral
    b "I would've appreciated the simplicity."

    "This is absolutely not true, but you let it slide."
    show bailey sad
    b "Mum always says she likes my gifts, but it always feels kinda fake, y'know?"

    b "Like she's trying too hard to reassure me that I did I good job."

    pl "Yeah, I definitely get that."

    pl "Sounds uncomfortable... but I'm sure she really does appreciate it."

    pl "And if she doesn't, it's on her to say so, right?"
    show bailey neutral
    b "So true! You're so smart, you know that?"

    "You and Bailey chat for a little more."

    "At some point Bailey is called away to deal with a couple of tables outside, leaving you to bring out some drinks."
    hide bailey neutral

    "There is a flat white, for Esme, and the same awful coffee order from yesterday, for Bradley. Gary isn't here today."
    

    menu:
        "Who will you serve first?"
        "Esme":
            $ d2_e1 = True
            jump d2_work_e
        "Bradley":
            jump d2a_work_br
    


label d2_work_e:
    "You approach Esme's table. Gary isn't here today."
    show esme neutral at center
    menu:
        "Give a cheeky greeting":
            $ e_friend += 5
            pl "Not day drinking today, Esme?"
            show esme flirty
            e "You rascal, you!"
            show esme neutral
            e "My life is on the up and up, I'll have you know."
            e "I'm meeting with a friend later today. It wouldn't do if I were sloshed before eleven."
            jump d2_work_e_aq1
        "Give a pleasant greeting":
            pl "G'morning, Esme. How are you?"
            show esme flirty
            e "Gladder for having laid eyes on you, my dear."
            show esme neutral
            e "And yourself?"
            pl "Can't complain. Here's your drink."
            e "Thank you very much."
            pl "What's on the docket for today?"
            e "So glad you asked! I'm meeting with a friend later today. It wouldn't do if I were sloshed before eleven."
            jump d2_work_e_aq1

label d2_work_e_aq1:
    "This friend is probably not Gary, otherwise Esme would have mentioned his name."

    pl "That's exciting! Do you see them much?"

    e "Not so much nowadays."

    e "Which is part of why it's all so exciting!"

    e "We're doing such different things now. It will be lovely to catch up."

    e "When we were younger, everything we did we did together - jobs, boys, heartbreaks..."

    e "Then she decided she wanted to settle down and have kids!"

    e "Not at all the life I thought we'd share with each other - I told her as much at the time, and we butted heads quite ferociously over it."

    e "It felt like a betrayal... but I understand now that we simply wanted different things."

    e "Can't build a world without stubborn hearts, I always say."

    e "And it's a stroke of luck to have friends by your side for as long as I have."
    show esme happy
    e "Longer even than you've been alive!"

    menu:
        "\"That's so impressive!\"":
            e "I do associate with impressive individuals, it's true."
            jump d2_work_e_aq2
        "\"There's no way that's true\"":
            $ e_friend += 5
            e "Heehee! Well, aren't you sharp?"
            jump d2_work_e_aq2

label d2_work_e_aq2:
    show esme neutral
    e "Regardless of our past difficulties, it will be lovely to meet up with her again."

    pl "I'm excited for you, Esme!"

    pl "I hope that I'll keep friends for as long as you."

    pl "It's hard enough to keep relationships up now as it is, even with the internet and everything making things easier."

    e "Easier on paper, perhaps."

    e "Although we stuck together largely out of necessity."

    e "Which isn't to say our connections weren't beautiful. But..."
    show esme sad
    e "... Well. I'm sure you can imagine. It was harder back then."

    menu:
        "\"I could never have lived through what you've lived through\"":
            $ e_friend -= 10
            jump d2_work_e_lived
        "\"I'm glad it's easier now\"":
            jump d2_work_e_easy
        "\"I'm sorry - it must have been really difficult\"":
            $ e_friend += 5
            jump d2_work_e_diff
        "\"Thank you for all the work you did to make it safer for us now\"":
            $ e_friend += 5
            jump d2_work_e_safer

label d2_work_e_lived:
    show esme angry
    e "I didn't think I could either, you know."

    e "In fact, many people didn't."
    show esme sad
    e "I wonder... is my life so unthinkable? It wasn't too long ago that I was young."

    e "It wasn't too long ago that things were much worse for queer and trans people."

    e "And they can get worse again."
    show esme angry

    "He makes hard eye contact with you. You feel as if all the air in the room has been sucked out."

    show esme happy
    "Then she smiles and the feeling dissipates like morning fog."

    e "But they are not worse just yet, hm?"

    e "And so we celebrate!"
    jump d2_work_e_aq3

label d2_work_e_easy:
    e "Me too."

    e "You younger people... so many of you have no idea what it was like."

    e "On one hand, I'm bitter - and on the other, relieved."
    show esme sad
    e "The death and tragedy of my early days feels like a fairy story."
    show esme neutral
    e "Surely this is a sign we have made things better, yes?"

    "You don't quite know what to say."

    e "Maybe. Maybe not."

    e "I would never wish tragedy upon anyone young. But sometimes..."
    show esme sad
    e "Sometimes I wish for other people's memories to be longer."

    "Esme falls silent, staring into the middle distance with his hands cupped around her drink."
    show esme neutral
    "You can't read her expression. You get the feeling that it's not really an expression for you."

    show esme happy
    "Then she smiles and the feeling dissipates like morning fog."

    jump d2_work_e_aq3

label d2_work_e_diff:
    e "Thank you. It was."

    e "Deeply, immensely, unconscionably difficult... and so very fun!"
    
    e "I worry sometimes that people do not have {i}fun{/i} anymore."

    e "Stupid of me. I imagine that they are just having fun where I can't see it."

    pl "That's usually how it goes!"

    pl "I'm glad it wasn't all doom and gloom, though."
    show esme happy
    e "Of course! How could it have been???"

    e "We had each other, and there was so much {i}love{/i} to go around, enough to fill you up for years and years."

    e "Oh, and hate, too. Don't get me wrong."

    jump d2_work_e_aq3

label d2_work_e_safer:
    e "It was hardly work, dear."

    e "Deeply difficult, don't get me wrong!"

    e "And I would have given anything to not have had to do it."

    e "But work is... how can I say this? Coercive. Mandatory. Pointless, in many ways."

    e "It's why I don't do it anymore!"

    e "But I've always been happy to dedicate my life to making the world safer and kinder and stranger."

    e "To wear what you want, to call yourself how you truly are, to love freely and to do whatever you please with your body..."
    show esme happy
    e "What else would I be living for, if not for that?"

    e "Dedication, not work... that's how I've always seen it."

    jump d2_work_e_aq3

label d2_work_e_aq3:
    show esme happy
    "Esme lights up a little, then laughs to herself."

    e "This puts me in mind of an old lover, actually."

    e "One glinting star in a sprawling web of glory and devotion!"

    "Sprawling web..? The phrasing reminds you of [partner] out of nowhere. Not a single partner, but many, simultaneously?"

    e "His name was Errol."
    show esme flirty
    e "We used to {i}play petanque{/i} whenever we could manage it."
    
    "You don't understand the euphemism, but you can fill in the gaps."

    show esme neutral

    e "I was working at the movie theatre at the time, and he was a delivery driver."

    e "We barely talked, but for two or three days out of the week, it was magical."

    pl "And on every other day of the week?"
    show esme happy
    e "Oh, he was {i}miserable!{/i}"

    "Esme throws back his head and crows with laughter."

    e "We called him 'the Snitch'! Loved the cops - we always teased him about loving the wrong kind of man in uniform."

    e "It was awful!!"

    pl "Hah! Well, there's one thing you know never to do again."
    show esme neutral
    "Esme nods sagely."

    e "Don't be with a man named Errol. Exactly."
    hide esme neutral

    if d2_e1 == True:
        "You laugh and chat for a little more before moving away to serve Bradley."
        if partner == "Angus":
            jump d2a_work_br
        else:
            jump d2b_work_br
    else:
        "You laugh and chat for a little more before moving away to serve other customers."
        jump d2_work_end



label d2a_work_br:
    show bradley neutral

    "You swing by Bradley's table."

    "As opposed to yesterday, Bradley is focused solely on his phone, no leaning around or gawking to be had."

    pl "Hey, Bradley!"

    "You put down his drink, but he doesn't respond."

    menu:
        "Leave":
            "You guess Bradley isn't in a social mood today."
            hide bradley neutral
            if d2_e1 == True:
                jump d2_work_end
            else:
                jump d2_work_e
        "Ask if he has games on his phone":
            $ br_friend += 5
            pl "Got any games on that thing?"
            br "Hm? What?"
            br "Oh... games. No, I don't have any games."
            show bradley sad
            br "I tried to download them once, but I broke my phone doing it."
            show bradley neutral
            br "How are you, [name]?"
            pl "I'm fine..."
            jump d2a_work_br_aq1
        "Snap your fingers at him":
            $ br_friend += 5
            "You snap your fingers like you're a customer trying to get a waiter's attention."
            pl "Hey! Bradley! I'm talking to you here."
            br "Hm?"
            br "Oh! Hello there, [name]."
            br "I didn't notice you there."
            jump d2a_work_br_aq1
        "Ask if he wants anything else":
            pl "Anything else I can get you?"
            "Still nothing. Bradley remains fixated on his phone."
            "You're about to leave when he blinks out of his reverie and focuses on you."
            br "Hm?"
            br "Oh, hello, [name]."
            br "Thank you for the drink."
            jump d2a_work_br_aq1

label d2a_work_br_aq1:
    pl "You seem a bit distracted today. Everything okay?"

    br "Well... if you really must know, this may be the most important day of my life."

    "He pauses for a moment, as if debating whether or not to tell you."

    menu:
        "\"Is it about Bailey?\"":
            $ br_friend += 5
            br "Hmph. I was getting to that."
            br "And aren't you insightful?"
            jump d2a_work_br_aq2
        "\"Is it about Angus?\"":
            show bradley angry
            br "Hmph. It's rude to interrupt, you know!"
            show bradley embarrassed
            br "And it's not like everything is about your wonderful, amazing, handsome boyfriend..."
            show bradley shocked
            br "...w-who is VERY much taken, incidentally, as you know!"
            show bradley neutral
            br "(Way to rub that in, by the way...)"
            jump d2a_work_br_aq2
        "Wait for him to tell you":
            $ br_friend += 10
            "After a bit of internal debate, it seems like Bradley comes to a conclusion."
            jump d2a_work_br_aq2

label d2a_work_br_aq2:
    br "It's a family matter. About my parents, specifically."
    br "About my mother, even more specifically."

    br "My mother's birthday is coming up, as Bailey may have already let you know."

    br "I want to get her a good gift."

    br "More than a good gift. A good-er gift."

    pl "... Do you mean a {i}better{/i} gift?"
    show bradley happy
    br "Yes! Yes I do!"
    show bradley neutral
    br "Better than anything {i}Bailey{/i} could get her."

    br "She always gives the {i}best{/i} gifts. Mother gushes over them for hours and hours."
    show bradley sad
    br "And yet she says nothing about mine!!"

    "You think back to your conversation with Bailey. The shape of the situation is becoming clear to you."

    "Bradley gestures with his phone at you."
    show bradley neutral
    br "I've been texting Bailey, trying to get an idea of what she's getting Mother this year."
    show bradley angry
    br "But for {i}some{/i} reason, she's not responded!"

    "There is not a single trace of irony in Bradley's voice."

    pl "If I had to guess, I'd say it's probably because she's on the clock right now."
    show bradley neutral
    br "Oh, psh. She does a tremendous amount of things on the clock that aren't work."
    
    "You have to hand it to Bradley. He's not wrong."

    menu:
        "Reassure Bradley about his gift-giving skills":
            pl "I'm sure you're not as bad at giving gifts as you think!"
            pl "It's the thought that counts, anyway, not the gift itself."
            show bradley disgusted
            "Bradley turns upon you a look so withering that you swear you can feel some nearby plants die."
            br "Sometimes I think you're smart, [name], and then you turn around and say something like that."
            br "It doesn't matter if I'm good! Bailey is always better!"
            br "Always and always and {i}always{/i}!"
            show bradley sad
            br "It's tiring."
            br "A lifetime of Bailey is {i}tiring{/i}."
            show bradley neutral
            jump d2a_work_br_aq4
        "Downplay Bailey's gift-giving success":
            $ br_friend -= 5
            pl "No way Bailey is that good at giving gifts."
            pl "Sounds to me like everyone tells her she's hot stuff even when she's not!"
            show bradley angry
            br "Are you insulting my sister right now?"
            br "Watch yourself!"
            br "If people are saying she's good at something then they're saying it for a reason."
            br "If that's all you've got to say about her, then shut up and don't say anything!!"
            "Yeesh. {i}That{/i} was clearly a misstep."
            show bradley neutral
            jump d2a_work_br_aq4
        "Point out Bailey's insecurities around gift-giving":
            $ br_friend += 5
            pl "Bailey's been freaking out a bit about getting your mum a gift, too."
            pl "Maybe she's not as worried about it as you, but it's not like she isn't stressing."
            br "Hm. Is that so?"
            br "That's news to me..."
            br "She always seemed so confident about gifts."
            pl "Well, Bailey's got feelings, too."
            br "This is true."
            br "Hm. Thanks, [name]."
            jump d2a_work_br_aq4
        "Give Bradley some practical gift ideas":
            pl "Well, what does your mum like?"
            br "Hm..."
            pl "Is she into more practical stuff?"
            pl "Or would she appreciate a decorative kind of gift?"
            br "Well, she likes practical things. But she also has a lot of decoration around her house..."
            pl "What about interests? Hobbies? Books?"
            pl "Maybe you could get her a membership somewhere. Or tickets to an event!"
            show bradley sad
            br "Maybe... but I don't know what she has and doesn't have."
            br "Or what she wants and doesn't want."
            pl "Are you particularly crafty? You could handmake her something!"
            pl "Like a card or a piece of art. Pottery, or crochet, or knitting?"
            pl "You could even write her something, if you want."
            pl "Do any of those options stand out?"
            show bradley disgusted
            "Bradley is making a face. He looks positively green."
            br "Eugh... Too many choices!"
            "Oh dear."
            br "I've thought about all of those ideas already!"
            br "But I can't decide! I can't ever decide!"
            br "Augh!!! Giving gifts is awful!!! How are you meant to know which one you should get!!!!!"
            show bradley neutral
            jump d2a_work_br_aq4

label d2a_work_br_aq4:
    "Bradley groans and buries his face in his palms."
    show bradley sad
    br "Every year, suffering."

    br "How will I ever survive?"

    pl "At the very least, Bailey is going through a similar thing."

    pl "So I guess you're not alone in freaking out?"

    br "Misery does love company..."
    show bradley neutral
    "He stares out at nothing for a moment, then suddenly his eyes light up."
    show bradley happy
    br "Wait. Hmm. Wait, wait, wait."

    br "Company..."

    br "Ooh. Oh, that may be a very good idea."

    br "The best I've maybe ever had!"

    "You have no idea what he's talking about."

    "Bradley scoops up his phone and starts texting with vigour."

    pl "Erm. That's good."

    "Bradley is unresponsive. He nods enthusiastically once or twice, but he is clearly no longer listening to you."

    "Well. You guess that went okay...?"

    "With nothing else to do, you leave Bradley's table and return to work."

    hide bradley happy

    if d2_e1 == True:
        jump d2_work_end
    else:
        jump d2_work_e

label d2_work_end:

    "The rest of your work day is busy, but relatively uneventful."

    "It wraps up pretty quickly. Or, at least, it feels like it does."
    stop music fadeout 5.0

label d2_po:
    scene bg black with fade
    "After work, it's back to the post office for you. Hopefully April was right and your parcel has arrived today."

    scene bg post office with fade
    play music "Welcome.mp3" loop
    show april shocked
    "Upon walking in, you spot April already waiting at the desk. They look... pretty freaked out."

    menu:
        "Give a calm greeting":
            pl "Hey, April. Is everything okay? You look a bit worried."
            ap "Oh, hey there, [name]."
            show april embarrassed
            ap "I guess I am a bit worried. If by 'bit' you mean 'like, a lot'."
            ap "Just like so freaking much."
            jump d2_po_aq1
        "Give a joking greeting":
            pl "Damn, who died?"
            show april happy
            ap "Hah! Nobody yet, but check in after five minutes."
            show april neutral
            ap "I may very well be dead in the ground by then."
            jump d2_po_aq1

label d2_po_aq1:
    pl "What's going on? Has there been any progress on my parcel?"
    show april embarrassed
    "April's eye twitches when you say 'parcel'."

    ap "Well...!"

    ap "..."
    show april neutral
    ap "Ahh, what the hell. It's only you."

    ap "There is some pretty bad news I gotta give you."

    ap "And I swear to God, it's not a joke, either..."

    ap "The parcels."

    ap "They've been stolen."

    menu:
        "\"Good one, April\"":
            show april angry
            ap "Trust me, this isn't a joke."
            ap "If this was a joke, you would be laughing."
            show april neutral
            jump d2_po_aq2
        "\"What do you mean, {i}stolen?{/i}\"":
            $ ap_friend -= 5
            show april angry
            ap "I mean they are no longer in the warehouse and no records were made of them leaving."
            show april neutral
            jump d2_po_aq2
        "\"How the hell did that happen, April?\"":
            $ ap_friend -= 5
            show april angry
            ap "I'm getting to that."
            show april neutral
            jump d2_po_aq2

label d2_po_aq2:
    ap "Remember yesterday, when I told you the warehouse manager was sick?"

    ap "Turns out he {i}wasn't{/i} sick."

    ap "Also, turns out he made off with the company van and took as many parcels as he could with him."

    ap "{i}Also{/i} also, turns out he was doing, just, {i}so{/i} much embezzlement."

    menu:
        "\"That's completely unacceptable!\"":
            show april angry
            ap "Yeah. Yeah!"
            ap "That's sort of our office's official take on it, too."
            jump d2_po_aq3
        "\"That's kind of hilarious\"":
            $ ap_friend += 5
            ap "... God I'm glad you said so."
            show april happy
            pl "It's completely absurd!"
            ap "ISN'T it?!!"
            ap "Millicent was so pissed off about it this morning when she was telling me."
            ap "I didn't want to laugh, but I was {i}this{/i} close to losing it, like, all this morning."
            jump d2_po_aq3
        "\"...How much embezzlement, exactly?\"":
            $ ap_friend += 10
            ap "At least ten."
            show april happy
            pl "Maybe even twenty?"
            ap "Whoof! I wouldn't go {i}that{/i} far."
            pl "To be fair, he did steal a vehicle and a bunch of private correspondence."
            pl "He probably would've gone all the way."
            ap "That's true."
            ap "With crimes like that under his belt, who knows what else he's capable of!"
            jump d2_po_aq3

label d2_po_aq3:
    show april neutral
    ap "Either way, he was apprehended by police early this morning."

    ap "Did you know that it's meant to be impossible to track company vehicles with modern technology?"

    ap "Guess he must've found a workaround."

    ap "Anyway, hopefully the packages will be returned in a timely fashion."
    show april angry
    ap "(Though knowing the cops, that's probably not happening any time soon...)"

    menu:
        "Say nothing":
            jump d2_po_aq4
        "\"Hey, don't disrespect the police! They work really hard!\"":
            $ ap_friend -= 15
            ap "... Oh yeah?"
            ap "I do, too, and yet I've been shouted at fifty times today."
            ap "Weird how that works!"
            jump d2_po_aq4
        "\"I get that. Cops are useless\"":
            $ ap_friend += 5
            show april disgusted
            ap "Ugh, right?"
            ap "And assholes."
            show april angry
            ap "Useless, violent assholes."
            pl "A lot of asshole traits wrapped up into one."
            ap "Like a little asshole bouquet."
            jump d2_po_aq4
        "\"I get that. It's a frustrating situation\"":
            ap "Indubitably, dear Watson."
            jump d2_po_aq4

label d2_po_aq4:
    show april neutral
    ap "So yeah. That's the situation."
    show april embarrassed
    ap "Sorry about the inconvenience, [name] - I know you were really wanting to get your parcel."

    ap "This whole thing will probably take a little longer to resolve."

    ap "Maybe come back in a couple days?"

    pl "I can do that. Couple of days."

    pl "I'll see you then?"
    show april neutral
    ap "Yeah! If I haven't burned down the freakin' building by that point!"

    pl "Alright. Thanks for your help, April."

    pl "See you then!"

    ap "Byeeeeee!!"

    hide april neutral
    stop music fadeout 5.0
    scene bg black with fade

label d2_home:

    scene bg bedroom aft with fade
    play music "Slipstream.mp3" loop

    "When you get home, you're happy to spend the rest of the evening to yourself."

    "You might call or text [partner] a bit later, but for now you decide to spend some time in the garden."
    stop music fadeout 3.0
    scene bg garden aft with fade
    play music "Tranquilize.mp3" loop

    "You're very lucky to have this garden, you and [partner]. Most people around your age that you know have balconies."

    "Your house is small, and so is your garden. Sometimes you miss the larger yard your parents have, and the river you used to live by." 
    
    "Taking a walk by the water always helped calm you down."

    "You would speak to the river, just like you would a close friend."

    "With all that's on your brain right now, you could use that watery confidant again."

    "But you're very grateful for your house and garden! It doesn't have to be the river for nature to still feel like a friend to you."

    "Even if [partner] is the one who's actually better at keeping the plants alive most of the time..."

    "You sit down and take a deep breath, letting the crisp air fill your lungs with the scent of jasmine and jacaranda."

    "You sigh."

    "Already you feel better, your head feels clearer, and your heart feels lighter."

    "But not everything is solved. You still aren't quite sure how to feel about everything, or every{i}one.{/i}"

    scene bg garden n with fade

    "You sit outside until it gets dark, and you feel a buzz in your pocket."

    "[partner] is calling."

    if partner == "Bailey":
        jump d2b_home
    else:
        jump d2a_home

label d2a_home:
    menu:
        "Answer":
            jump d2a_home_ans
        "Don't answer":
            jump d2a_home_noans
    
label d2a_home_ans:
    a "Hey [name]! All my meetings are done for the day, so I thought I'd call!"
    
    menu:
        "\"I'm glad you did!\"":
            $ a_friend += 5
            "You can practically hear Angus smile on the other side of the phone."
            jump d2a_home_ans_aq1
        "\"I would have preferred some warning\"":
            a "Oh, you're right, I should have texted first... sorry."
            jump d2a_home_ans_aq1

label d2a_home_ans_aq1:
    a "Anway, how was your day?"
    
    menu:
        "\"It was okay\"":
            menu:
                "\"I miss you\"":
                    $ a_friend += 5
                    a "Aw, I miss you too!"
                    jump d2a_home_ans_aq2
                "\"Not much really happened\"":
                    a "Fair enough. Same here, really."
                    jump d2a_home_ans_aq2
                "\"How was your day?\"":
                    $ a_friend += 10
                    a "Aw, thanks for asking! You're sweet... My day was alright." 
                    a "Not much really happened though - just a bunch of team activities and stuff."
                    jump d2a_home_ans_aq2
        "\"It was good!\"":
            a "That's great! What happened?"
            menu:
                "\"Not much really\"":
                    a "Fair enough. Same here."
                    jump d2a_home_ans_aq2
                "\"A lot!\" (Tell Angus about your day)":
                    $ a_friend += 10
                    a "Wow! Sounds like a big day. I'm glad you enjoyed it."
                    jump d2a_home_ans_aq2
                "\"First, I want to know about your day\"":
                    $ a_friend += 5
                    a "Oh, well not much really happened! It was just a lot of various team activities and stuff like that."
                    jump d2a_home_ans_aq2
        "\"Pretty bad, to be honest\"":
            a "Oh I'm sorry to hear that. Anything I can do to help?"
            menu:
                "\"Don't think so\"":
                    a "Well, I'm sorry anyway."
                    jump d2a_home_ans_aq2
                "\"We could talk about the polyamory thing?\"":
                    $ a_friend -= 10
                    a "..."
                    a "Other than that, I mean."
                    jump d2a_home_ans_aq2
                "\"Talking to you is already helping\"":
                    $ a_friend += 10
                    a "Oh you smooth talker you... But I'm glad!"
                    jump d2a_home_ans_aq2

label d2a_home_ans_aq2:
    if crush == "no one":
        a "Anyway, you've been talking to a lot of people. Has anyone... caught your eye?"
        jump d2a_home_ans_pique
    else:
        a "Anyway, how is it going with [crush]?"
        if crush == "Morgan" or "Pedro" or "Gary":
            pl "Well, we didn't talk today, so nothing really to report there."
            a "I see... well, is anyone else piquing your interest?"
            jump d2a_home_ans_pique
        else:
            menu:
                "\"Good!\"":
                    a "Glad to hear it!"
                    a "Are you thinking of asking them out at all?"
                    jump d2a_home_ans_ask
                "\"Idk... I think maybe I'm losing interest?\"":
                    a "Ah, I see... that can be tricky."
                    a "Well, is anyone else piquing your interest?"
                    jump d2a_home_ans_pique
                "\"Terribly!":
                    a "Oh, I'm so sorry to hear that!"
                    a "Are you thinking of asking them out, anyway?"
                    jump d2a_home_ans_ask
                "\"Okay I guess? Hard to tell\"":
                    a "That's fair enough."
                    a "Are you thinking of asking them out at all?"
                    jump d2a_home_ans_ask

label d2a_home_ans_pique:
    menu:
        "\"No\"":
            $ crush = "no one"
            a "Fair enough!"
            jump d2a_home_ans_ppl
        "\"Yes\"":
            a "Oh, who?"
            menu:
                "Bailey":
                    if crush == "Bailey":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking her out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "Bailey"
                        a "Your coworker? Nice!"
                        a "Are you thinking of asking her out?"
                        jump d2a_home_ans_ask
                "Bradley":
                    if crush == "Bradley":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "Bradley"
                        a "So you're my competition now?"
                        a "I'm just kidding, but for real Bradley is definitely monogamous, so only one of us would be, er... getting their way, haha"
                        a "Are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                "Gary":
                    if crush == "Gary":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "Gary"
                        a "Gary?"
                        a "I am not familiar... but, hey, good luck!"
                        a "Are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                "Esme":
                    if crush == "Esme":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking her out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "Esme"
                        a "I am not familiar... but, hey, good luck!"
                        a "Are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                "Morgan":
                    if crush == "Morgan":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking her out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "Morgan"
                        a "Your classmate, right? Good luck!"
                        a "Are you thinking of asking her out?"
                        jump d2a_home_ans_ask
                "Pedro":
                    if crush == "Pedro":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "Pedro"
                        a "Your classmate, right? Good luck!"
                        a "Are you thinking of asking him out?"
                        jump d2a_home_ans_ask
                "April":
                    if crush == "April":
                        a "Isn't that who you just said you're losing interest in?"
                        a "You're so fickle, haha."
                        a "Anyway, are you thinking of asking them out?"
                        jump d2a_home_ans_ask
                    else:
                        $ crush = "April"
                        a "Oh! From the post office? Good luck!"
                        a "Are you thinking of asking them out?"
                        jump d2a_home_ans_ask
                "Multiple people":
                    $ crush = "Everyone"
                    a "Aw hell yeah! Good luck!"
                    a "Are you thinking of asking them out?"
                    jump d2a_home_ans_ask

label d2a_home_ans_ask:
    menu:
        "\"No\"":
            a "Fair enough. Can I ask why?"
            menu:
                "\"Not brave enough\"":
                    a "Haha, okay then, coward."
                    a "I'm just kidding."
                    jump d2a_home_ans_ppl
                "\"[crush] will say no!\"":
                    a "Why? You're a perfectly fine person!"
                    a "And I'm not biased at all..."
                    jump d2a_home_ans_ppl
                "\"They should ask me\"":
                    a "Pfft. Okay, then, Your Highness..."
                    jump d2a_home_ans_ppl
                "\"I'm with you - that would be cheating!\"":
                    $ a_friend -= 5
                    a "..."
                    a "No, it wouldn't?"
                    jump d2a_home_ans_ppl
        "\"I don't know yet\"":
            a "That's fair enough - take your time!"
            jump d2a_home_ans_ppl
        "\"Yes!\"":
            a "Oh, so exciting!"
            a "Good luck!"
            jump d2a_home_ans_ppl

label d2a_home_ans_ppl:
    stop music fadeout 3.0
   
    a "..."
    pl "..."

    menu:
        "\"Hey... So, I was wondering, would it be okay for me to see other people?\"":
            $ a_friend += 5
            $ cppl = True
            a "Oh!"
            a "Well, yeah. I mean, if you want to, of course."
            a "I don't want you to feel pressured to - "
            a "Thanks."
            a "For... asking."
            jump d2a_home_ans_end
        "Don't mention it":
            jump d2a_home_ans_end

label d2a_home_ans_end:
    play music "Tranquilize.mp3" loop
    "You and Angus talk for a little bit longer, but you start to get tired."

    menu:
        "Say goodnight now":
            "The two of you say goodnight, and you head to bed."
            scene bg bedroom n with fade
            "You wonder what tomorrow will hold."
            jump d3_start
        "Keep chatting just a bit longer":
            $ a_friend += 5
            "You keep chatting for around 10 minutes before you say goodnight."
            scene bg bedroom n with fade
            "You head to bed, sleepily brushing your teeth and getting changed first."
            "When your head hits the pillow, you're out like a light."
            "You wonder what tomorrow will hold."
            jump d3_start
        "I'm not tired! Keep talking for HOURS!!!":
            $ a_friend += 10
            scene bg bedroom n with fade
            "The two of you chat for hours and hours, at some point heading to your bedroom. When you talk to Angus, it's like time ceases to exist."
            "You don't know when it happens, exactly, but at some point you fall asleep to the sound of his voice."
            jump d3_start


label d2a_home_noans:
    "You ignore the phone call. You're not in the mood, or you're too tired, or too angry."
    "Either way, you start mindlessly scrolling on your phone."
    if a_friend >= 20:
        "Eventually, you receive a text."
        a "{i}Going to bed now. Thinking of you xx Goodnight{/i}"
        "You get ready for bed."
        scene bg bedroom n with fade
        jump d2a_home_noans_aq1
    else:
        "You do not receive any follow up texts."
        scene bg bedroom n with fade
        "Eventually, you get ready for bed. Something sits in your gut, a little uncomfortable, but you can't quite put your finger on what."
        jump d2a_home_noans_aq1

label d2a_home_noans_aq1:
    "You lie in bed, sleepless, for what feels like hours. You check your phone, and find it's only been half an hour."
    "In your head, you start to complain about how hard you're finding it to sleep."
    "But before you know it, you're deep in the thralls of some shapeless dream."
    jump d3_start


label d3_start:
    stop music fadeout 5.0
    scene bg black with fade
    
    "Slowly, your dreams take shape." 
    "The shape - or, rather, shapes - of faces." 
    "Bailey, Angus, Esme, Pedro, April... In your dream, they're all trying to tell you something, but none of them get to say it."
    "They keep getting interrupted, or you can't hear, or you're inexplicably running away..."
    "You wake without knowing what any of them wanted to tell you."

    scene bg bedroom with fade
    play music "Theme.mp3" fadein 1.5 loop

    "You feel a little groggy today, but you're sure you'll pick up energy once the day gets going."
    "Plus, you have the morning entirely to yourself, since you don't have work today."
    "You have a few hours before you need to head to uni."

    menu:
        "What do you want to do?"
        "Spend some time working on your assignment":
            jump d3_ass
        "Spend some time in the garden":
            jump d3_gar
        "Get a few more hours sleep":
            jump d3_sleep

label d3_ass:
    "You want to get a decent mark on this assignment - or at least hand it in with a passable amount of words on the page."

    "It's a bit hard to get stuck into the studying at first. You still feel pretty groggy, after all."

    "But after about an hour of... well, honestly, mostly looking at your phone, you finally start to feel the groove of research and writing."

    "You have a pretty good idea of what you want to write about, but you need at least two more sources for this essay in order to meet the minimum reference count."

    "You spend most of the next few hours just skimming through articles, seeing if they align closely enough with what you want to say."

    "In fact, you get no writing done at all."

    "But!!! Not to worry!!!"

    "Your research does pay off, and you end up finding some really strong sources to add to your argument."

    "By the time you've properly read through and highlighted the important parts, it's about time to head to class."

    jump d3_uni

label d3_gar:
    show bg garden with fade
    "The garden always makes you feel better. It worked yesterday - why not today too?"
    "You make yourself a hot drink (or a cold one if you want, I'm not the boss of you) and head outside."
    "There's not really any proper seating, but you sit on the steps leading up to the gate."
    "The air is a bit warmer than yesterday, but not uncomfortably so." 
    "There is a slight, pleasant breeze which softly fades over your skin, and carries with it that same smell of jacaranda."
    "Today, the birds are loud. They're arguing or showing off or gossipping, or whatever it is that birds actually do when they twitter and squawk at each other."
    "At first, the sound sort of annoys you. But after a while, for some reason, you start to find yourself smiling."
    "Perhaps it's the idea of the pretty little birds squabbling, or the way the trees rustle conspicuously, or maybe it's how tired you are, but something about the birds' nonstop noise-making starts to make you laugh."
    "It's almost like you're joining in."
    "Eventually, the birds settle down back to arrhythmical tweeting here and there, and your laughter too subsides."
    "But something in you feels a little bit brighter, a little bit lifted."
    "You stay out there for a while before heading back inside, cautious of sunburn."
    scene bg bedroom with fade
    "Taking this morning to relax, you put on some music and dance a little to yourself while you decide what to do."
    "A book you haven't picked up in years catches your eye, and for a little while you read it. It's not the most gripping tale, but the author was clearly very passionate about writing it."
    "So, you potter about the house for a while, doing odd hobbies and chores here and there, but never really committing to one activity or another."
    scene bg bedroom aft with fade
    "It's the afternoon before you know it, and time to head to class."
    jump d3_uni

label d3_sleep:
    "You go back to bed, determined to rest and recuperate."
    "Part of you is vaguely hopeful that your dream will pick up again, and you'll finally know what everyone was trying to tell you..."
    scene bg black with fade
    "You get to sleep with surprisingly no problem, but you dream of utter nonsense related to... well, as far as you can tell, nothing."
    "There's something to do with a rabbit and a silicone tube, but you're pretty sure the two never touched. They were just separate, stand out elements for some reason."
    "Also an old friend from primary school was there, but, on waking, you can't for the life of you remember which one."
    "But you do wake after a few hours, and you do feel better."
    scene bg bedroom aft with fade
    "Sleeping in more was a good choice, after all."
    "Now, though, it's time to head to class."
    jump d3_uni

label d3_uni:
    stop music fadeout 5.0
    play music "Thinking Ahead.mp3" loop
    scene bg uni with fade

    "You arrive at class with plenty of time to spare. In fact, only a few people are there yet." 
    "You don't really know any of them that well, so you pick a seat a respectable distance from the front, where you will hopefully be able to see and hear well without necessarily drawing attention to yourself from the tutor."

    "As students slowly trickle in, you wonder who might sit next to you."

    menu:
        "You hope it's..."
        "Morgan":
            $ m_friend +=5
            if crush == "Morgan":
                "Of course you do. You have a bit of a crush on her, after all."
            else:
                "You'd like to get to know her a bit better. She seems nice, but that can't be all there is to her."
            jump d3_u_aq1
        "Pedro":
            $ p_friend += 5
            if crush == "Pedro":
                "Of course you do. You have a bit of a crush on him, after all."
            else:
                "You'd like to get to know him a bit better. Maybe there's something sweet under that prickly exterior." 
                "Then again, maybe there isn't."
            jump d3_u_aq1
        "Both":
            $ p_friend += 5
            $ m_friend += 5
            "You like both of the classmates you've spoken to so far, and want to get to know them both a bit better."
            jump d3_u_aq1
        "Neither":
            "You don't care to get to know those particular classmates any better."
            jump d3_u_aq1
        "I don't really care one way or the other":
            "As long as you can focus on the class and maybe chat to someone interesting, you're about set." 
            "It doesn't have to be Pedro or Morgan."
            jump d3_u_aq1

label d3_u_aq1:
    "Well, for better or for worse, Pedro and Morgan arrive at around the same time, and both head towards you. They each pick a seat next to you."

    show morgan neutral at right
    show pedro neutral at left

    m "Hi, [name]. Hi, Pedro!"

    p "Oh, hello Morgan. And [name]."

    menu:
        "Greet them":
            jump d3_u_greet
        "Ask them how they've been":
            jump d3_u_ask
        "Ignore them":
            jump d3_u_ignore

label d3_u_greet:
    pl "Hey, guys."

    m "So, how have you two been?"
    show pedro happy
    p "I've been excellent! Yesterday, my friend and I went shopping and got a whole facial spa thing. I feel so refreshed and glowing. Aren't I glowing?"

    menu:
        "\"Absolutely glowing\"":
            $ p_friend += 5
            p "I {i}know.{/i} Thank you."
            jump d3_u_greet_aq1
        "\"Can't really tell the difference, to be honest\"":
            m "Well {i}I {/i} think you look amazing."
            show pedro disgusted
            p "Thank you, Morgan. I guess some people just can't tell quality when it smacks them in the face."
            jump d3_u_greet_aq1
        "\"Don't you have a job?\"":
            $ p_friend -= 5
            show pedro angry
            "Of course I have a job. That's how I can afford to go shopping??"
            jump d3_u_greet_aq1

label d3_u_greet_aq1:
    show pedro neutral
    show morgan embarrassed
    m "A-anyway. How about you, [name]?"
    show morgan neutral
    menu:
        "\"I've been a bit swamped with this assignment\"":
            $ m_friend += 5
            show morgan happy
            m "Oh, that's so fair. Me too! I pulled a bit of an all-nighter last night to finish up a couple essays."
            jump d3_u_class
        "\"I've been good! Thinking about some new identity stuff, and it's all very exciting\"":
            $ m_friend += 5
            $ p_friend += 5
            show pedro shocked
            m "Ooh that does sound exciting! Anything you want to share?"
            menu:
                "\"Not really - not right now at least\"":
                    m "Fair enough! Good luck, either way."
                    show pedro neutral
                    jump d3_u_class
                "\"Sure! I've been thinking about possibly being polyamorous\"":
                    $ m_friend += 5
                    $ p_friend += 5
                    m "Oh, cool!"
                    show pedro neutral
                    p "My ex was polyamorous..."
                    p "It didn't go very well."
                    p "..."
                    show pedro shocked
                    p "Oh! But that was just because he wasn't very open about it with me. Ended up cheating on me rather than just telling me the truth."
                    show pedro happy
                    p "So, what I mean to say is, it's great that you're being so open about it. Good on you."
                    jump d3_u_class
        "\"Not so great, to be honest\"":
            m "Oh, I'm sorry to hear that."
            show morgan sad
            jump d3_u_class

label d3_u_ask:
    $ m_friend += 5
    $ p_friend += 5
    pl "So, how have you both been?"
    show pedro happy
    p "I've been excellent! Yesterday, my friend and I went shopping and got a whole facial spa thing. I feel so refreshed and glowing. Aren't I glowing?"

    menu:
        "\"Absolutely glowing\"":
            $ p_friend += 5
            p "I {i}know.{/i} Thank you."
            jump d3_u_ask_aq1
        "\"Can't really tell the difference, to be honest\"":
            m "Well {i}I {/i} think you look amazing."
            show pedro disgusted
            p "Thank you, Morgan. I guess some people just can't tell quality when it smacks them in the face."
            jump d3_u_ask_aq1
        "\"Don't you have a job?\"":
            $ p_friend -= 5
            show pedro angry
            "Of course I have a job. That's how I can afford to go shopping??"
            jump d3_u_ask_aq1

label d3_u_ask_aq1:
    show pedro neutral
    pl "How about you, Morgan?"
    show morgan sad
    m "Ah, it's been ok. I've mostly been swamped with working on this essay, plus an assignment for another class. Haven't had much time for fun."
    show morgan shocked
    m "Oh! But I finished both assignments last night, so I'm much more free now."

    menu:
        "\"Congrats!\"":
            show morgan happy
            m "Thanks!"
            jump d3_u_class
        "\"Fair enough - I've been kinda swamped, too\"":
            $ m_friend += 5
            show morgan happy
            m "Oh, good luck!"
            jump d3_u_class
        "\"About time\"":
            $ m_friend -= 5
            show morgan angry
            m "What's that supposed to mean? I've been trying my best."
            jump d3_u_class


label d3_u_ignore:
    $ m_friend -= 10
    $ p_friend -= 10
    show morgan disgusted
    show pedro disgusted
    "Pedro and Morgan sort of look at each other and shrug. The three of you sit in silence for a few minutes before the class starts."
    show morgan neutral
    show pedro neutral
    jump d3_u_class2

label d3_u_class:
    show morgan neutral
    show morgan neutral
    "Before you have a chance to say anything more, your tutor hushes you all."

label d3_u_class2:
    "Today's lesson is a bit dull, and you find yourself zoning out more and more often." 
    "Looking to your left and right, you see that Morgan seems to be having trouble staying awake, and that even Pedro is lacking his usual sharp attentiveness."

    menu:
        "Try harder to pay attention":
            jump d3_u_att
        "Get just Morgan's attention":
            jump d3_u_matt
        "Get just Pedro's attention":
            jump d3_u_patt
        "Talk to both Morgan and Pedro":
            jump d3_u_batt

label d3_u_att:
    "Despite the heavy feeling in your eyes, you try very, very hard to focus." 
    "So hard, in fact, that you're not sure if you focused more on the class, or on the act of trying to pay attention itself." 
    "Certainly, more information goes in, but you find yourself struggling to retain it, even seconds after it passes through your ears."
    show morgan disgusted
    "At one point, you notice that Morgan has fallen asleep next to you."
    jump d3_u_end

label d3_u_matt:
    $ m_friend += 5
    show morgan neutral
    "You make a few comments about how dull the class is, which she seems to appreciate." 
    "She doesn't respond much, but that might be because she is spending a fair amount of time yawning and rubbing her eyes."
    "At one point, she thanks you for keeping her awake."
    jump d3_u_end

label d3_u_patt:
    $ p_friend += 5
    "Pedro doesn't seem to appreciate any criticism of the class itself, but agrees that the content today is quite dull." 
    "He admits that he had some trouble getting through the reading for today."
    show pedro embarrassed
    "At one point, he tries to tell a joke, but it either goes over your head, or isn't very funny."
    if p_tell_take == True:
        show pedro neutral
        "Finally remembering your conversation from last class, Pedro tells you what his take on Monday's topic was."
        "It's a little confusing, but you think he might have a firmer grasp of the concept than you did last week."
        "Not that that changes your mind very much."
    jump d3_u_end

label d3_u_batt:
    $ p_friend += 5
    $ m_friend += 5
    show morgan happy
    show pedro happy
    "The three of you convene in hushed tones about more or less nothing throughout the class." 
    "Pedro admits he had trouble with today's reading, and Morgan thanks you both for keeping her awake."
    if p_tell_take == True:
        show pedro neutral
        "Finally remembering your conversation from last class, Pedro tells you both what his take on Monday's topic was."
        "It's a little confusing, but you think he might have a firmer grasp of the concept than you did last week."
        "Not that that changes your mind very much."
        "Morgan doesn't seem to understand him at all."
        show pedro happy
    "The three of you pass jokes between you like notes, and chuckle quietly so as to avoid the wrath of Professor Holt. He doesn't seem to notice you, or if he does, he doesn't seem to care."
    "The class passes much more quickly than expected."
    jump d3_u_end

label d3_u_end:
    show morgan neutral
    show pedro neutral
    "Once the tutorial is over, you begin to pack up your things."

    p "I'm in a bit of a rush, got to get to work."

    if p_friend >= 25:
        p "... thanks. For today. It was fun talking to you both."
    else:
        p "Bye."

    m "Bye, Pedro!"

    pl "See you."

    hide pedro neutral
    show morgan neutral at center

    if m_friend >= 30:
        m "Hey, [name], you got some time?"
        pl "Sure."
        m "Great! I was wondering if you wanted to hang out for a bit, then?"
        menu:
            "\"Like a date?\"":
                $ m_friend -= 5
                show morgan embarrassed
                m "Uh... not really... I more meant, like, a hang out... sorry..."
                menu:
                    "\"Oh, no worries! I just wanted to clarify. Did you want to go to my house?\"":
                        $ m_friend += 5
                        show morgan happy
                        m "Sounds great!"
                        jump d3_m_hang
                    "\"Oh... in that case, maybe not\"":
                        $ m_friend -= 5
                        show morgan sad
                        m "Right..."
                        m "Well, see you in class, then."
                        jump d3_nohang
            "\"Sure. We could go to my house?\"":
                show morgan happy
                m "Sounds good!"
                jump d3_m_hang
            "\"Sorry, got to head off, actually\"":
                m "Oh, no worries. See you in class, then."
                jump d3_nohang
    else:
        m "Well, I'm gonna head off, too. Bye!"
        menu:
            "\"Wait!\" (Ask her on a date)":
                if m_friend >= 25:
                    m "Hmm... well. I don't really date..."
                    m "But, I've got some time right now, if you want to hang out?"
                    menu:
                        "\"Sure. We could go to my house?\"":
                            show morgan happy
                            m "Sounds good!"
                            jump d3_m_hang
                        "\"Sorry, got to head off, actually\"":
                            m "Oh, no worries. See you in class, then."
                            jump d3_nohang
                else:
                    show morgan embarrassed
                    m "Oh... I'm sorry, [name]. I like having you as a friend and all, but... well, I don't really... date." 
                    m "It's nothing personal, I'm just not really interested in people that way."
                    show morgan sad
                    m "I hope you can understand."
                    show morgan neutral
                    m "See you in class."
                    jump d3_nohang

label d3_m_hang:
    $ m_hang = True
    hide morgan neutral
    scene bg black with fade
    stop music fadeout 5.0
    "You drive Morgan to your house, chatting about various insignificant things on the way. Like the weather, and Professor Holt, and the music on the radio."

    "When you get home, you head to your room. The kitchen is quite small, and the living room is currently cramped with laundry."

    scene bg bedroom aft with fade
    play music "Coffee Lounge.mp3" loop
    show morgan neutral
    "You sort of half-apologise for the mess."

    m "Nice house!"

    menu:
        "\"Thanks! Make yourself at home\"":
            m "Sure."
            "Morgan starts looking at the photos on your dresser."
            jump m_hang_aq1
        "\"Thanks! Can I get you something to drink?\"":
            $ m_friend += 5
            m "Oh, yes, please. Just water would be great."
            "You fetch Morgan a glass of water from the kitchen."
            "When you return, she is looking at the photos on your dresser."
            jump m_hang_aq1

label m_hang_aq1:
    m "Is this your partner?"
    
    pl "Oh, yeah, that's [partner]."

    if partner == "Bailey":
        m "She's pretty."
    else:
        m "He's pretty."
    
    menu:
        "\"I know, I'm very lucky\"":
            $ m_friend +=5
            if partner == "Bailey":
                $ b_friend += 5
            else:
                $ a_friend += 5
            show morgan happy
            m "I'll say! Got a house, a hot partner..."
            m "Very impressive, [name]."
            pl "Haha, thanks."
            jump m_hang_aq2
        "\"You're quite pretty, yourself\"":
            if m_friend >= 25:
                $ m_friend += 5
                show morgan flirty
                "Morgan shoots you a quick grin."
                m "Why, thank you."
                jump m_hang_aq2
            else:
                m "Haha, thanks."
                jump m_hang_aq2
        "\"Pretty? I guess so...\"":
            $ m_friend -= 5
            show morgan angry
            m "You {i}guess{/i} so?"
            m "Your partner is hot as hell, what are you talking about?"
            show morgan disgusted
            m "Whatever, I guess."
            jump m_hang_aq2

label m_hang_aq2:
    show morgan neutral
    m "Anyway, you've got me in your room, all alone, what do you want to do?"

    menu:
        "\"I was thinking, watch a movie?\"":
            $ m_friend += 5
            show morgan happy
            m "Sounds good to me!"
            jump m_hang_mov
        "\"We could just talk\"":
            m "Hmm... I was hoping for something with a little less... social pressure?"
            m "I'm a bit 'casual conversation'-ed out, from class and all."
            m "Could we maybe watch a movie or something instead?"
            pl "Sure."
            jump m_hang_mov
        "Smile mischievously and get a bit closer to her":
            if m_friend >= 40:
                $ m_friend += 5
                show morgan flirty
                "Morgan smiles back and bites her lip slightly."
                "Then she looks away and coughs quietly."
                show morgan neutral
                m "Maybe we could watch a movie."
                m "... first."
                pl "... Sure."
                jump m_hang_mov
            else:
                $ m_friend -= 5
                show morgan embarrassed
                "Morgan looks away, coughs quietly, and sort of leans back a bit."
                m "H-How about we watch a movie or something?"
                pl "...sure."
                jump m_hang_mov

label m_hang_mov:
    show morgan neutral
    pl "What type of movie are you in the mood for?"

    m "Hmm, well I like horror and action movies most, though I don't mind a comedy." 
    m "I'm not big on romance or fantasy, really... Although I do like thinking about the sets and props of fantasy stuff..."
    show morgan embarrassed
    m "Oh, sorry, that really didn't answer your question."
    show morgan neutral
    m "Um... how about a horror movie? Does that sound okay?"

    menu:
        "\"Sure\"":
            m "Great!"
            "After a bit of searching online to find a movie neither of you have seen yet, you find a supernatural horror film from the eighties, and get it up on your computer." 
            "The effects are really, really bad, but it is surprisingly engaging, and you even find yourself a little wigged out about halfway through."
            jump m_hang_mov_end
        "\"I'd prefer a comedy\"":
            m "Alright. Why not?"
            "After a bit of searching online to find a movie neither of you have seen yet, you get up a spy-comedy on your computer." 
            "As soon as it starts playing, it's clear that the film itself is not very good."
            jump m_hang_mov_end
        "\"I'd prefer an action\"":
            m "Okay, sure. Sounds good!"
            "After a bit of searching online to find a movie neither of you have seen yet, you get up a niche superhero movie from the nineties on your computer." 
            "It's... not very good. But it's a lot of fun, even just to see the effects,"
            jump m_hang_mov_end
        "\"I'd prefer a romance\"":
            show morgan disgusted
            m "Uh... Okay... sure. Maybe we could compromise with, like, a romcom?"
            pl "Alright."
            show morgan neutral
            "After a bit of searching online to find a movie neither of you have seen yet, you get up a generic romcom on your computer." 
            "It's actually pretty good, and quite funny."
            "Morgan doesn't seem to mind it, though she cringes a bit at some of the more cliche romance parts."
            jump m_hang_mov_end

label m_hang_mov_end:
    "Near the end of the movie, during a particularly tense scene, Morgan starts to move a bit closer to you."
    "Your shoulders touch."

    if m_friend >= 50:
        "She places a hand on your leg."
        show morgan flirty
        "She whispers:"
        m "Is this okay?"
        
        menu:
            "Yes":
                $ m_friend += 5
                "She starts to trail her hand up your leg a bit, and moves her face to be right next to yours."
                menu:
                    "Turn off the movie":
                        $ m_friend += 5
                        m "Did you want to... do something else, maybe?"
                        menu:
                            "\"Like what?\"":
                                m "Well..."
                                "She trails her fingers across your leg."
                                m "Can I kiss you?"
                                menu:
                                    "Yes":
                                        $ m_friend += 5
                                        "Morgan kisses you."
                                        "At first it is soft and tentative, but rapidly she deepens it, opening your mouth with hers and-"
                                        "She pulls back."
                                        show morgan neutral
                                        m "Wait."
                                        m "You have a partner, right?"
                                        show morgan embarrassed
                                        m "Sorry, I just got caught up in the moment and I..."
                                        show morgan neutral
                                        m "Well, I'm okay to continue, but only if it's okay with you... {i}and{/i} your partner."
                                        m "So, like, have you spoken to them about... doing stuff with other people?"
                                        menu:
                                            "Yes":
                                                if cppl == True:
                                                    $ m_friend += 5
                                                    "Morgan studies your face for a while before breathing out a sigh."
                                                    show morgan happy
                                                    m "Whew! Almost thought I was becoming a homewrecker!"
                                                    m "But, great!"
                                                    show morgan flirty
                                                    m "Then did you want to, you know... have sex?"
                                                    menu:
                                                        "Yes":
                                                            $ m_friend += 5
                                                            m "Awesome!"
                                                            show morgan neutral
                                                            m "Oh, but, to be clear, I don't want to date you."
                                                            m "This would just be sex. Friends with benefits type situation."
                                                            m "Is that... cool?"
                                                            menu:
                                                                "\"What?\"":
                                                                    m "I get it, for some people sex and romance are really related, but for me that's just not it. I just wanted to make that clear before we do anything."
                                                                    menu:
                                                                        "\"That's fine\"":
                                                                            show morgan happy
                                                                            m "Awesome!"
                                                                            m "Then..."
                                                                            show morgan flirty
                                                                            m "Get on the bed."
                                                                            scene bg black with fade
                                                                            "The two of you have sex, with her leading." 
                                                                            "It's pretty good. Quite good, actually..." 
                                                                            "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                                            "The whole experience feels very... safe." 
                                                                            "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                                            "She doesn't stay the night, but the two of you do hang out a little before she leaves. As she goes, she winks at you."
                                                                            scene bg bedroom n with fade
                                                                            show morgan happy
                                                                            m "Look forward to next time!"
                                                                            hide morgan neutral
                                                                            jump d3_end
                                                                        "\"That's not okay!\"":
                                                                            $ m_friend -= 10
                                                                            show morgan disgusted
                                                                            m "Oh..."
                                                                            m "You mean, you don't think it's, like, {i}appropriate{/i}, or whatever?"
                                                                            show morgan angry
                                                                            m "You think I'm, like, a slut, right? For not being in love first?"
                                                                            menu:
                                                                                "\"It's just wrong\"":
                                                                                    $ m_friend -= 20
                                                                                    $ m_shame = True
                                                                                    m "No, actually, it's very normal."
                                                                                    m "This is {i}my{/i} preference. And if it's not your preference, that's fine. I don't care." 
                                                                                    m "Just don't shame me for it, you {i}asshole{/i}."
                                                                                    m "I'm leaving."
                                                                                    jump m_hang_mleave
                                                                                "\"It's just not my thing\"":
                                                                                    show morgan disgusted
                                                                                    m "Okay, that's fine."
                                                                                    m "Next time, don't say it like an asshole."
                                                                                    m "..."
                                                                                    m "I think I wanna leave."
                                                                                    jump m_hang_mleave
                                                                "\"Totally cool\"":
                                                                    show morgan happy
                                                                    m "Awesome!"
                                                                    m "Then..."
                                                                    show morgan flirty
                                                                    m "Get on the bed."
                                                                    scene bg black with fade
                                                                    "The two of you have sex, with her leading. It's pretty good. Quite good, actually..." 
                                                                    "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                                    "The whole experience feels very... safe." 
                                                                    "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                                    "She doesn't stay the night, but the two of you do hang out a little before she leaves. As she goes, she winks at you."
                                                                    scene bg bedroom n with fade
                                                                    show morgan happy
                                                                    m "Look forward to next time!"
                                                                    hide morgan neutral
                                                                    jump d3_end
                                                        "No":
                                                            show morgan neutral
                                                            m "Alright. No worries."
                                                            m "But, to be clear, I don't want to date you."
                                                            m "I kissed you for, like, sexual reasons. Not romantic ones. So, like, we're not... going out."
                                                            menu:
                                                                "\"What?\"":
                                                                    m "I get it, for some people sex and romance are really related, but for me that's just not it. I just wanted to make that clear."
                                                                    menu:
                                                                        "\"That's fine\"":
                                                                            show morgan happy
                                                                            m "Awesome!"
                                                                            m "Then..."
                                                                            m "Do you want to watch the rest of the movie?"
                                                                            scene bg bedroom n with fade
                                                                            show morgan neutral
                                                                            "The two of you finish the movie. It's alright, overall, but you have a good (if ever so slightly awkward) time hanging out with Morgan." 
                                                                            "After the movie, she thanks you for a nice night, and heads off."
                                                                            hide morgan neutral
                                                                            jump d3_end
                                                                        "\"That's not okay!\"":
                                                                            $ m_friend -= 10
                                                                            show morgan disgusted
                                                                            m "Oh..."
                                                                            m "You mean, you don't think it's like, {i}appropriate{/i}, or whatever?"
                                                                            show morgan angry
                                                                            m "You think I'm, like, a slut, right? For not being in love first?"
                                                                            menu:
                                                                                "\"It's just wrong!\"":
                                                                                    $ m_friend -= 20
                                                                                    $ m_shame = True
                                                                                    m "No, actually, it's very normal."
                                                                                    m "This is {i}my{/i} preference. And if it's not your preference, that's fine. I don't care." 
                                                                                    m "Just don't shame me for it, you {i}asshole.{/i}"
                                                                                    m "I'm leaving."
                                                                                    jump m_hang_mleave
                                                                                "\"It's just not my thing\"":
                                                                                    show morgan disgusted
                                                                                    m "Okay, that's fine."
                                                                                    m "Next time, don't say it like an asshole."
                                                                                    m "..."
                                                                                    m "I think I wanna leave."
                                                                                    jump m_hang_mleave
                                                                "\"Understood\"":
                                                                    show morgan happy
                                                                    m "Awesome!"
                                                                    m "Then..."
                                                                    m "Do you wanna watch the rest of the movie?"
                                                                    scene bg bedroom n with fade
                                                                    show morgan neutral
                                                                    "The two of you finish the movie. It's alright, overall, but you have a good (if ever so slightly awkward) time hanging out with Morgan." 
                                                                    "After the movie, she thanks you for a nice night, and heads off."
                                                                    hide morgan neutral
                                                                    jump d3_end
                                                else:
                                                    "Morgan studies your face for a while before letting out a slow sigh."
                                                    show morgan sad
                                                    m "No, you haven't, have you?"
                                                    m "Like, not if {i}you{/i} can make out with other people."
                                                    m "Fuck! This keeps happening to me..."
                                                    m "Listen, [name], I've made a giant fool of myself and need to go."
                                                    jump m_hang_mleave
                                            "No":
                                                show morgan disgusted
                                                m "Okay... so. We're not going to go any further."
                                                show morgan neutral
                                                m "Wanna just... watch the rest of the movie?"
                                                scene bg bedroom n with fade
                                                show morgan neutral
                                                "You watch the rest of the movie. It's alright. You can tell Morgan feels a little disappointed, though she doesn't say anything." 
                                                "At the end of the movie she thanks you and heads off."
                                                hide morgan neutral
                                                jump d3_end
                                    "No":
                                        show morgan neutral
                                        m "Okay."
                                        m "Maybe we just watch the rest of the movie, then?"
                                        "The two of you finish the movie. It's alright, overall, but you have a good (if ever so slightly awkward) time hanging out with Morgan." 
                                        "After the movie, she thanks you for a nice night, and heads off."
                                        hide morgan neutral
                                        jump d3_end
                            "Just kiss her":
                                show morgan flirty
                                "At first it is soft and tentative, but rapidly you deepen it, opening her mouth with yours and-"
                                "She pulls back."
                                show morgan neutral
                                m "Wait."
                                m "You have a partner, right?"
                                show morgan embarrassed
                                m "Sorry, I just got caught up in the moment, and I..."
                                show morgan neutral
                                m "Well, I'm okay to continue, but only if it's alright with you... {i}and{/i} your partner."
                                m "So, like, have you spoken to them about... doing stuff with other people?"
                                menu:
                                    "Yes":
                                        if cppl == True:
                                            $ m_friend += 5
                                            "Morgan studies your face for a while before breathing out a sigh."
                                            show morgan happy
                                            m "Whew! Almost thought I was becoming a homewrecker!"
                                            m "But, great!"
                                            show morgan flirty
                                            m "Then did you want to, you know... have sex?"
                                            menu:
                                                "Yes":
                                                    $ m_friend += 5
                                                    show morgan happy
                                                    m "Awesome!"
                                                    show morgan neutral
                                                    m "Oh, but, to be clear, I don't want to date you."
                                                    m "This would just be sex. Friends with benefits type situation."
                                                    m "Is that... cool?"
                                                    menu:
                                                        "\"What?\"":
                                                            m "I get it, for some people sex and romance are really related, but for me that's just not it. I just wanted to make that clear before we do anything."
                                                            menu:
                                                                "\"That's fine\"":
                                                                    show morgan happy
                                                                    m "Awesome!"
                                                                    m "Then..."
                                                                    show morgan flirty
                                                                    m "Get on the bed."
                                                                    scene bg black with fade
                                                                    "The two of you have sex, with you leading." 
                                                                    "It's pretty good. Quite good, actually..." 
                                                                    "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                                    "The whole experience feels very... safe." 
                                                                    "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                                    "She doesn't stay the night, but the two of you do hang out a little before she leaves. As she goes, she winks at you."
                                                                    scene bg bedroom n with fade
                                                                    show morgan happy
                                                                    m "Look forward to next time!"
                                                                    hide morgan neutral
                                                                    jump d3_end
                                                                "\"That's not okay!\"":
                                                                    $ m_friend -= 10
                                                                    show morgan disgusted
                                                                    m "Oh..."
                                                                    m "You mean, you don't think it's, like, {i}appropriate{/i}, or whatever?"
                                                                    show morgan angry
                                                                    m "You think I'm, like, a slut, right? For not being in love first?"
                                                                    menu:
                                                                        "\"It's just wrong\"":
                                                                            $ m_friend -= 20
                                                                            $ m_shame = True
                                                                            m "No, actually, it's very normal."
                                                                            m "This is {i}my{/i} preference. And if it's not your preference, that's fine. I don't care." 
                                                                            m "Just don't shame me for it, you {i}asshole{/i}."
                                                                            m "I'm leaving."
                                                                            jump m_hang_mleave
                                                                        "\"It's just not my thing\"":
                                                                            show morgan disgusted
                                                                            m "Okay, that's fine."
                                                                            m "Next time, don't say it like an asshole."
                                                                            m "..."
                                                                            m "I think I wanna leave."
                                                                            jump m_hang_mleave
                                                        "\"Totally cool\"":
                                                            show morgan happy
                                                            m "Awesome!"
                                                            m "Then..."
                                                            show morgan flirty
                                                            m "Get on the bed."
                                                            scene bg black with fade
                                                            "The two of you have sex, with you leading. It's pretty good. Quite good, actually..." 
                                                            "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                            "The whole experience feels very... safe." 
                                                            "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                            "She doesn't stay the night, but the two of you do hang out a little before she leaves. As she goes, she winks at you."
                                                            scene bg bedroom n with fade
                                                            show morgan happy
                                                            m "Look forward to next time!"
                                                            hide morgan neutral
                                                            jump d3_end
                                                "No":
                                                    show morgan neutral
                                                    m "Alright. No worries."
                                                    m "But, to be clear, I don't want to date you."
                                                    m "I kissed you for, like, sexual reasons. Not romantic ones. So, like, we're not... going out."
                                                    menu:
                                                        "\"What?\"":
                                                            m "I get it, for some people sex and romance are really related, but for me that's just not it. I just wanted to make that clear."
                                                            menu:
                                                                "\"That's fine\"":
                                                                    show morgan happy
                                                                    m "Awesome!"
                                                                    m "Then..."
                                                                    show morgan neutral
                                                                    m "Do you want to watch the rest of the movie?"
                                                                    scene bg bedroom n with fade
                                                                    show morgan neutral
                                                                    "The two of you finish the movie. It's alright, overall, but you have a good (if ever so slightly awkward) time hanging out with Morgan." 
                                                                    "After the movie, she thanks you for a nice night, and heads off."
                                                                    hide morgan neutral
                                                                    jump d3_end
                                                                "\"That's not okay!\"":
                                                                    $ m_friend -= 10
                                                                    show morgan disgusted
                                                                    m "Oh..."
                                                                    m "You mean, you don't think it's like, {i}appropriate{/i}, or whatever?"
                                                                    show morgan angry
                                                                    m "You think I'm, like, a slut, right? For not being in love first?"
                                                                    menu:
                                                                        "\"It's just wrong!\"":
                                                                            $ m_friend -= 20
                                                                            $ m_shame = True
                                                                            m "No, actually, it's very normal."
                                                                            m "This is {i}my{/i} preference. And if it's not your preference, that's fine. I don't care." 
                                                                            m "Just don't shame me for it, you {i}asshole.{/i}"
                                                                            m "I'm leaving."
                                                                            jump m_hang_mleave
                                                                        "\"It's just not my thing\"":
                                                                            show morgan disgusted
                                                                            m "Okay, that's fine."
                                                                            m "Next time, don't say it like an asshole."
                                                                            m "..."
                                                                            m "I think I wanna leave."
                                                                            jump m_hang_mleave
                                                        "\"Understood\"":
                                                            show morgan happy
                                                            m "Awesome!"
                                                            m "Then..."
                                                            show morgan neutral
                                                            m "Do you wanna watch the rest of the movie?"
                                                            scene bg bedroom n with fade
                                                            show morgan neutral
                                                            "The two of you finish the movie. It's alright, overall, but you have a good (if ever so slightly awkward) time hanging out with Morgan." 
                                                            "After the movie, she thanks you for a nice night, and heads off."
                                                            hide morgan neutral
                                                            jump d3_end
                                        else:
                                            "Morgan studies your face for a while before letting out a slow sigh."
                                            show morgan sad
                                            m "No, you haven't, have you?"
                                            m "Like, not if {i}you{/i} can make out with other people."
                                            m "Fuck! This keeps happening to me..."
                                            m "Listen, [name], I've made a giant fool of myself and need to go."
                                            jump m_hang_mleave
                                    "No":
                                        show morgan disgusted
                                        m "Okay... so. We're not going to go any further."
                                        show morgan neutral
                                        m "Wanna just... watch the rest of the movie?"
                                        scene bg bedroom n with fade
                                        show morgan neutral
                                        "You watch the rest of the movie. It's alright. You can tell Morgan feels a little disappointed, though she doesn't say anything." 
                                        "At the end of the movie she thanks you and heads off."
                                        hide morgan neutral
                                        jump d3_end
                            "No":
                                show morgan neutral
                                m "Okay."
                                m "Maybe we just watch the rest of the movie, then?"
                                "The two of you finish the movie. It's alright, overall, but you have a good (if ever so slightly awkward) time hanging out with Morgan." 
                                "After the movie, she thanks you for a nice night, and heads off."
                                hide morgan neutral
                                jump d3_end
                    "Keep the movie playing":
                        show morgan neutral
                        "Morgan moves her face away, and eventually her hand, too."
                        "The two of you keep watching the movie."
                        "It's alright, but you have fun watching it with Morgan. She has a lot of funny critiques to make."
                        "After the movie, she thanks you for a fun time and heads home."
                        hide morgan neutral
                        jump d3_end
            "No":
                show morgan embarrassed
                m "Ah, sorry."
                show morgan neutral
                m "She retracts her hand."
                jump m_hang_mov_cont
    else:
        show morgan neutral
        "You look over at her and see she's fully engrossed in the film. You're not even sure if she noticed that your shoulders are touching."
        menu:
            "Put a hand on her leg":
                pl "Is this okay?"
                if m_friend >= 40:
                    show morgan flirty
                    m "Yeah."
                    m "..."
                    "Morgan looks at you for a moment."
                    show morgan neutral
                    m "Hey..."
                    m "Have you spoken to your partner about, like... {i}doing stuff{/i}... with other people?"
                    menu:
                        "Yes":
                            if cppl == True:
                                $ m_friend += 5
                                "Morgan looks at you for a while before letting out a sigh."
                                show morgan happy
                                m "Phew!"
                                m "Then..."
                                show morgan flirty
                                m "Would it be alright if I kissed you?"
                                menu:
                                    "Yes":
                                        $ m_friend += 5
                                        show morgan flirty
                                        "Morgan smiles, then cups your face in her hands, leans in, and kisses you."
                                        "At first, it is light and gentle. But soon, she deepens the kiss, opening your lips with hers and sliding her tongue into your mouth."
                                        menu:
                                            "Grope her":
                                                $ m_friend += 5
                                                "Morgan moans slightly. She presses in to you closer for a moment, grabbing at your shirt."
                                                "Then she pulls away."
                                                show morgan neutral
                                                m "Wait, before we go any further, I just want to clarify..."
                                                m "I'm not into romance."
                                                m "Not at the moment, at least."
                                                m "So, like, I want to keep going, but I've got to be clear, this isn't like... dating, or anything."
                                                m "It'd be more like a... what's it called? Friends with benefits, thing."
                                                m "Is that... cool?"
                                                menu:
                                                    "\"Sure. Totally cool\"":
                                                        $ m_friend += 5
                                                        show morgan happy
                                                        m "Awesome!"
                                                        m "Then..."
                                                        show morgan flirty
                                                        m "Get on the bed."
                                                        scene bg black with fade
                                                        "The two of you have sex, with you leading. It's pretty good. Quite good, actually..." 
                                                        "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                        "The whole experience feels very... safe." 
                                                        "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                        "She doesn't stay the night, but the two of you do hang out a little before she leaves." 
                                                        scene bg bedroom n with fade
                                                        show morgan flirty
                                                        "As she goes, she winks at you."
                                                        m "Look forward to next time!"
                                                        hide morgan neutral
                                                        jump d3_end
                                                    "\"What?\"":
                                                        m "I get it, for some people sex and romance are really related, but for me that's just not it. I just wanted to make that clear before we do anything."
                                                        menu:
                                                            "\"Understood\"":
                                                                $ m_friend += 5
                                                                show morgan happy
                                                                m "Awesome!"
                                                                m "Then..."
                                                                show morgan flirty
                                                                m "Get on the bed."
                                                                scene bg black with fade
                                                                "The two of you have sex, with you leading. It's pretty good. Quite good, actually..." 
                                                                "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                                "The whole experience feels very... safe." 
                                                                "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                                "She doesn't stay the night, but the two of you do hang out a little before she leaves." 
                                                                scene bg bedroom n with fade
                                                                show morgan flirty
                                                                "As she goes, she winks at you."
                                                                m "Look forward to next time!"
                                                                hide morgan neutral
                                                                jump d3_end
                                                            "\"That's so wrong\"":
                                                                $ m_friend -= 20
                                                                $ m_shame = True
                                                                show morgan angry
                                                                m "... No, it's not."
                                                                m "Fuck you, actually. I'm leaving."
                                                                jump m_hang_mleave
                                            "Wait for her to make another move":
                                                show morgan flirty
                                                "Morgan presses in closer to you for a moment, but then pulls away."
                                                show morgan neutral
                                                m "Wait, before we go any further, I just want to clarify..."
                                                m "I'm not into romance."
                                                m "Not at the moment, at least. So like..."
                                                m "I want to keep going, but I've got to be clear, this isn't like... dating, or anything."
                                                m "It'd be more like a... what's it called? Friends with benefits, thing."
                                                m "Is that... cool?"
                                                menu:
                                                    "\"Sure. Totally cool\"":
                                                        $ m_friend += 5
                                                        show morgan happy
                                                        m "Awesome!"
                                                        m "Then..."
                                                        show morgan flirty
                                                        m "Get on the bed."
                                                        scene bg black with fade
                                                        "The two of you have sex, with her leading. It's pretty good. Quite good, actually..." 
                                                        "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                        "The whole experience feels very... safe." 
                                                        "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                        "She doesn't stay the night, but the two of you do hang out a little before she leaves." 
                                                        scene bg bedroom n with fade
                                                        show morgan flirty
                                                        "As she goes, she winks at you."
                                                        m "Look forward to next time!"
                                                        hide morgan neutral
                                                        jump d3_end
                                                    "\"What?\"":
                                                        m "I get it, for some people sex and romance are really related, but for me that's just not it. I just wanted to make that clear before we do anything."
                                                        menu:
                                                            "\"Understood\"":
                                                                $ m_friend += 5
                                                                show morgan happy
                                                                m "Awesome!"
                                                                m "Then..."
                                                                show morgan flirty
                                                                m "Get on the bed."
                                                                scene bg black with fade
                                                                "The two of you have sex, with her leading. It's pretty good. Quite good, actually..." 
                                                                "She seems very experienced. Throughout, she keeps asking if certain actions are okay, and if you're feeling comfortable and good." 
                                                                "The whole experience feels very... safe." 
                                                                "When you're done, she stresses the importance of you both going to the bathroom after, and asks if you like cuddling after." 
                                                                "She doesn't stay the night, but the two of you do hang out a little before she leaves." 
                                                                scene bg bedroom n with fade
                                                                show morgan flirty
                                                                "As she goes, she winks at you."
                                                                m "Look forward to next time!"
                                                                hide morgan neutral
                                                                jump d3_end
                                                            "\"That's so wrong\"":
                                                                $ m_friend -= 20
                                                                $ m_shame = True
                                                                show morgan angry
                                                                m "... No, it's not."
                                                                m "Fuck you, actually. I'm leaving."
                                                                jump m_hang_mleave
                                            "Pull away":
                                                "You pull away, and Morgan smiles."
                                                show morgan happy
                                                m "That was nice."
                                                show morgan shocked
                                                m "Oh! But to be clear, that wasn't, um, romantic."
                                                show morgan neutral
                                                m "Like, I like you and all, but not {i}like that{/i}."
                                                m "I just want to be friends, cool?"
                                                menu:
                                                    "\"Cool\"":
                                                        m "Awesome."
                                                        m "Want to keep watching the movie, then?"
                                                        jump m_hang_mov_cont
                                                    "\"What? No\"":
                                                        $ m_friend -= 10
                                                        show morgan disgusted
                                                        m "What do you mean?"
                                                        m "I'm sorry if I gave you the wrong impression. I got a bit carried away."
                                                        m "But, like, either we're friends, and maybe we could make out or even have sex sometimes, if you want. Or we're not friends, and we don't hang out. What will it be?"
                                                        menu:
                                                            "\"That makes no sense\"":
                                                                $ m_friend -= 10
                                                                show morgan angry
                                                                m "I mean, it {i}does{/i} if you think about it, like, at all."
                                                                m "But, fine, whatever. I guess we're not going to be friends."
                                                                m "So..."
                                                                m "I guess I'll be heading off, then."
                                                                m "... Bye."
                                                                hide morgan neutral
                                                                jump m_hang_mleave
                                                            "\"Sure, we can be friends\"":
                                                                show morgan neutral
                                                                m "Cool."
                                                                m "Then let's just... finish the movie."
                                                                jump m_hang_mov_cont
                                    "No":
                                        show morgan neutral
                                        m "Okay then."
                                        m "Let's just watch the movie, then."
                                        "She gently removes your hand from her leg."
                                        jump m_hang_mov_cont
                            else:
                                "For a while, Morgan just stares at you. Then she lets out a long sigh."
                                show morgan sad
                                m "No, you haven't."
                                m "Not about if {i}you{/i} can, you know?"
                                m "It's fine."
                                show morgan neutral
                                "Morgan brushes your hand off her leg."
                                m "Let's just watch the movie."
                                jump m_hang_mov_cont
                        "No":
                            show morgan disgusted
                            m "Okay..."
                            show morgan neutral
                            m "Maybe we just watch the movie, then."
                            "She gently removes your hand from her leg."
                            jump m_hang_mov_cont
                else:
                    show morgan sad
                    m "Not really."
                    show morgan neutral
                    "You remove your hand and continue watching the movie."
                    jump m_hang_mov_cont
            "Just finish the movie":
                jump m_hang_mov_cont

label m_hang_mov_cont:
    "Overall, the movie was better than you expected. Morgan seemed to have a nice time with it."
    show morgan happy
    m "That wasn't half bad!"

    m "Thanks, [name]. That was fun."

    menu:
        "\"Do you want to stay a bit longer?\"":
            show morgan neutral
            m "Thanks, but I should really be heading off."
            jump m_hang_cont_aq1
        "\"It was fun! Thanks for coming over\"":
            $ m_friend += 5
            show morgan neutral
            m "Thanks for having me! Anyway, I should really be heading off, now."
            jump m_hang_cont_aq1

label m_hang_cont_aq1:
    "Morgan grabs her things and leaves. You feel like you've grown a bit closer to her today."
    jump d3_end

label m_hang_mleave:
    hide morgan neutral
    "Morgan grabs her things and leaves."
    "You're left with a slight hollow feeling in your chest as you bid her goodbye."
    "Unsure exactly what happened, you decide to put it out of your mind for the rest of the night."
    jump d3_end

label d3_nohang:
    "You head home."
    scene bg bedroom aft with fade
    "You can't help feeling like you missed some kind of opportunity today, but you shrug it off."
    "Sometimes days just feel like that, and there's nothing you can really do."
    "Anyway, you take off your shoes, put your things away, and grab a drink of some kind."
    jump d3_end

label d3_end:
    stop music fadeout 3.0
    hide morgan neutral
    "You decide to relax on your bed for a little while."
    scene bg bedroom n with fade
    play music "Tranquilize.mp3" loop
    "After quite a while of watching videos (some with earnest interest, others with barely contained disdain, and others somewhere in the middle), you receive a text from [partner]."

    if partner == "Bailey":
        jump d3_home_b
    else:
        jump d3_home_a

label d3_home_a:    
    a "{i}Hey [name], I'm done with work for the day. Feeling a bit beat, so I might go to bed soon, but I wanted to check in with you first.{/i}"

    a "{i}How was your day?{/i}"

    menu:
        "Great!":
            a "{i}Oh, awesome! Do you want to tell me about it?{/i}"
            menu:
                "Yeah (tell him about your day)":
                    if m_hang == True:
                        $ a_friend += 5
                        a "{i}Oh, that sounds fun! Especially cool about Morgan. I'm glad to see you branching out a bit more... trying new things{/i}"
                        jump d3_home_a_aq1
                    else:
                        a "{i}Oh that sounds fun! Glad you had a good day{/i}"
                        jump d3_home_a_aq1
                "Nah (don't tell him)":
                    a "{i}Fair enough! Glad it was good, though{/i}"
                    jump d3_home_a_aq1
        "It was okay":
            a "{i}Anything you wanna talk about?{/i}"
            menu:
                "Yeah (tell him about your day)":
                    if m_hang == True:
                        $ a_friend += 5
                        a "{i}Oh, that sounds interesting. Especially cool about Morgan. Even if it didn't work out exactly how you wanted, I'm glad to see you branching out a bit more... trying new things{/i}"
                        jump d3_home_a_aq1
                    else:
                        a "{i}Oh that's interesting. Glad ur day was ok, but sorry it wasn't better{/i}"
                        jump d3_home_a_aq1
                "Nah (don't tell him)":
                    a "{i}Fair enough! Glad it wasn't a bad day, at least{/i}"
                    jump d3_home_a_aq1
        "Kinda bad":
            a "{i}Oh, I'm sorry to hear that :( Anything you wanna talk about?{/i}"
            menu:
                "Yeah (tell him about your day)":
                    if m_hang == True:
                        $ a_friend += 5
                        a "{i}Oh, that's a shame. But about Morgan... even if it didn't work out how you wanted, I'm glad to see you branching out a bit more... trying new things{/i}"
                        jump d3_home_a_aq1
                    else:
                        a "{i}Oh that's a shame... Sorry your day was so bad{/i}"
                        jump d3_home_a_aq1
                "Nah (don't tell him)":
                    a "{i}Fair enough! Sorry your day was so bad though{/i}"
                    jump d3_home_a_aq1
label d3_home_a_aq1:
    a "{i}Anyway, I kinda really need to get some sleep... tomorrow's another long day and I've got an early start{/i}"

    a "{i}I'll text you in the morning!{/i}"

    a "{i}Goodnight!{/i}"

    pl "{i}Goodnight!{/i}"

    "You should probably head to bed now, too."

    "You don't have anything on in particular, other than wanting to check for your parcel at the post office..."

    "But still, who knows what the day could hold?"

    jump d3_end_sleep

label d3_end_sleep:
    stop music fadeout 5.0

    "It is not easy to get to sleep."

    "You toss and turn, in excitement or rumination or some secret third thing you can't quite put your finger on."

    "Maybe it would be easier if [partner] were here, or your mother, or just anyone comforting or familiar."

    "Maybe just anyone at all, so you didn't have to deal with whatever this feeling is all alone."

    scene bg black with fade

    "Eventually, you do make it to sleep, though."

    "You dream in black, inky depths not unlike liquid, but not quite {i}like{/i} it, either."

    "You dresm of something deathly important, losing itself to that inkiness."

    "As soon as it's gone, though, you can't remember what it was."

label d4_start:

    scene bg bedroom with fade
    play music "Theme.mp3" fadein 1.5

    "You are woken up a bit earlier than you would have liked, roused by the buzzing of your phone."

    "It's the promised good morning text from [partner]."

    if partner == "Bailey":
        b "{i}good morning babe! I hope you slept well and that this text message didnt wake u {/i}"
        b "{i}theres been some annoying scheduling errors so ive been running around like a headless chook all morning... and probably will for the rest of the day smh{/i}"
        b "{i}good luck for the day! Whatever u have planned, im sure ur gonna smash it <3{/i}"
    else:
        a "{i}good morning babe! I hope you slept well and that this text message didnt wake u {/i}"
        a "{i}theres been some annoying scheduling errors so ive been running around like a headless chook all morning... and probably will for the rest of the day smh{/i}"
        a "{i}good luck for the day! Whatever u have planned, im sure ur gonna smash it <3{/i}"
    
    menu:
        "Respond to your partner":
            if partner == "Bailey":
                $ b_friend += 5
            else:
                $ a_friend += 5
            pl "{i}morning gorgeous! The text did wake me actually... i forgot to put my phone on silent i think siiiighh{/i}"
            pl "{i}im sorry abt the scheduling changes! That sounds super annoying... they should pay u a million dollars for having to deal w their bullshit{/i}"
            "Your partner's reply is instantaneous."
            if partner == "Bailey":
                b "{i}I agree!!! With interest{/i}"
            else:
                a "{i}I agree!!! With interest{/i}"
            pl "{i}Lolll{/i}"
            pl "{i}im gonna try and get up now ill ttyl?{/i}"
            if partner == "Bailey":
                b "{i}sounds good :)) ttyl!{/i}"
            else:
                a "{i}sounds good :)) ttyl!{/i}"
            "Right as you receive that text, your phone buzzes again. You swipe away from the conversation with your partner to check it."
            "It's from your mum."
            jump d4_start_aq1
        "Roll over and try to get back to sleep":
            "You roll over and try to get some more sleep."
            "You're about ready to fall back asleep when your phone buzzes again."
            "Annoyed, you snatch for your phone and fumble for it to be turned to silent, before realising that it's actually a text from your mum."
            jump d4_start_aq1

label d4_start_aq1:
    mum "{i}Hello sweetie good morning! I was just asking about your package, has it arrived yet? I sent it off a long time ago but I haven't gotten a text from you about it?{/i}"

    "Better respond to this ASAP. Your mum likes to call you if she hasn't received a response to a text within five minutes of it being sent, and you're not in the mood to talk out loud right now."

    pl "{i}mornin mum, no sorry i havent received it yet. Theres a lot of inconvenience happening at the post office, i think a lot of ppl havent received their parcels?{/i}"

    mum "{i}Well that's irritating!! You tell them that you have to get your package A.S.A.P. it is very important... for me! Lol{/i}"

    mum "{i}How are you how is [partner] are you liking the new house ok ??{/i}"

    pl "{i}we're all good over here! The new house is lovely{/i}"

    pl "{i}[partner] is at that conference remember?{/i}"

    mum "{i}Oh yes i do remember sweetie of course. Are they doing alright? You know I worry, [partner] makes you so happy but I do worry. Are you sure they're not seeing anyone else at all of these conferences? That they're not cheating or anything?{/i}"
    
    "You immediately are put in a worse mood." 
    
    "Your mum always asks this, but knowing what you know now about [partner] being polyamorous, the word 'cheating' puts you on edge."

    menu:
        "Stand up for your partner, firmly":
            if partner == "Bailey":
                $ b_friend += 5
            else:
                $ a_friend += 5
            pl "{i}mum ive told you not to bring up cheating anymore{/i}"
            pl "{i}not unless you have a really good reason to suspect it{/i}"
            pl "{i}it upsets [partner] and it upsets me{/i}"
            mum "{i}Oh honey you are right, i am sorry. I remember you have said this many times and here i am still worrying!! Well i am okay to worry it is what a mother does after all, but you are right I should be nicer to [partner], they have been nothing but lovely to you.{/i}"
            mum "{i}Im sorry sweetie, ill try not to do it again. I love you very much, good on you for standing up for your partner even if it is to your mum!{/i}"
            "You let a breath out. Your mum is ultimately receptive to criticisms like these, even if it takes her ages for her to remember to be respectful."
            pl "{i}Thanks mum{/i}"
            jump d4_start_aq2
        "Stand up for your partner, but be gentle with your mum":
            if partner == "Bailey":
                $ b_friend += 5
            else:
                $ a_friend += 5
            pl "{i}i know youre just looking out for me mum, and i really appreciate it{/i}"
            pl "{i}but i trust [partner]! We've been together for a while now, i would tell you first thing if i really did think he/she was cheating on me{/i}"
            pl "{i}thank u for trying to protect me but i promise i can take care of myself{/i}"
            mum "{i}Oh honey you are right, i am sorry. I remember you have said this many times and here i am still worrying!! Well i am okay to worry it is what a mother does after all, but you are right I should be nicer to (partner), he/she has been nothing but lovely to you.{/i}"
            mum "{i}Im sorry sweetie, ill try not to do it again. I love you very much, good on you for standing up for your partner even if it is to your mum!{/i}"
            "You let a breath out. Your mum is ultimately receptive to criticisms like these, even if it takes her ages for her to {i}remember{/i} to be respectful."
            pl "{i}thanks mum{/i}"
            jump d4_start_aq2
        "Let it slide for now":
            if partner == "Bailey":
                $ b_friend -= 10
            else:
                $ a_friend -= 10
            "You really, {i}really{/i} are not in the mood to have any sort of difficult conversation right now."
            pl "{i}not sure mum i think its ok{/i}"
            pl "{i}thanks for texting :) ill let you know when I get the parcel{/i}"
            jump d4_start_aq2

label d4_start_aq2:
    pl "{i}I love you very much ok?{/i}"

    mum "{i}of course!! I love you too sweetie mwah mwah mwah. Let me know when youve got the package alright? You have a lovely day, lovely like the flowers!  You like that? Ha ha :) {/i}"

    pl "{i}hehe very cute mum! I will talk to you later :){/i}"

    "You realise as you minimise the conversation that you could have brought polyamory up to your mother."

    "Your next thought is a realisation that you are too tired and too groggy to have done that conversation much justice."
    
    "You really do want to... it's important for your parents to know, you think."

    "But it's also important that [partner] would be comfortable with that."

    "Maybe once [partner] is back you can have a conversation about who you tell."

    "For now, though, you're awake enough to start getting ready to go out."

    jump d4_po

label d4_po:
    stop music fadeout 3.0
    "Now it's time to head to the post office... again."
    
    scene bg post office with fade
    play music "Welcome.mp3" loop

    "When you arrive, something seems amiss. The door is closed, the curtains are drawn, and there is no light emanating from inside."

    "You go up to the door. Sure enough, there is a 'CLOSED' sign hanging against the glass."

    "Underneath, there is a piece of paper with a handwritten explanation, which has been taped to the door."

    "The paper reads:"

    "{i}'Due to unforeseen issues with our warehouse team, we have made the unfortunate decision to close the post office today. We apologise for the inconvenience, and hope to be back in order soon.'{/i}"

    "Well, that sucks. You're filled with dread, confusion, and bafflement. Have things really progressed so far as to make closing the shop a necessity?"

    "You're about to turn around and go home when you hear some movement from inside, muffled by the door."

    "Suddenly, April's face pops up from around the 'CLOSED' sign."

    show april shocked

    "She looks shocked, but then excited to see you. They pull at the doorknob, which miraculously swings open."

    show april happy

    pl "Oh - hey, April."

    pl "I thought you guys were closed today?"

    ap "Howdy, [name]!"
    show april neutral

    ap "We are, I'm just shutting up shop now."
    
    ap "But if it's you then I'm happy to help out - come on in!"

    menu:
        "Decline the offer":
            pl "Ah, it's okay, April. I don't want to intrude."
            pl "If you're closed, you're closed."
            pl "Maybe I can come back some other time, once everything is sorted out?"
            show april sad
            ap "Aw... you sure?"
            ap "I'd be happy to just hang out for a bit. We don't even have to talk shop!"
            pl "Thanks, but maybe some other time."
            show april neutral
            ap "Man... alright! Whatever floats your boat."
            ap "Come by in a couple days. We should have everything sorted out for you then."
            pl "Sounds good! See you round, April."
            ap "Byyyeee!"
            "You get the feeling that April definitely wanted to hang out. You feel a little bad, but then again, your time is your time. You can do with it what you want!"
            jump d4_home
        "Accept the offer":
            $ ap_friend += 5
            pl "Sure, lead the way."
            "You both head into the store."
            jump d4_po_in

label d4_po_in:
    "The afternoon light is casting the store in a pensive glow. It feels like very few people have been in today."
    show april happy
    "April turns to you with a grin, and tosses their arms up dramatically."

    ap "No points for guessing what's not arrived yet!"

    pl "Damn, still no parcel news?"

    ap "Well I didn't say that, exactly!"

    ap "There {i}is{/i} parcel news, but it's not good, and it's also really, really stupid."

    ap "Do you want to play a game? If you can guess correctly what's happened to your parcel, I'll give you a prize."

    menu:
        "\"I don't want to play some stupid game\"":
            $ ap_friend -= 5
            show april shocked
            ap "Whoa, jeez, alright."
            show april embarrassed
            ap "I'll hold off, then. Dang."
            ap "Guess I'll just tell you what happened the boring way."
            show april neutral
            jump d4_po_expl
        "\"Sure, I love games!\"":
            $ ap_friend += 5
            ap "Wonderful!"
            jump d4_po_game
        "\"Sure, but what's the prize?\"":
            show april happy
            ap "Having a grand old time with your best bud, of course!"
            show april neutral
            jump d4_po_game

label d4_po_game:
    show april neutral
    ap "So. I'm going to give you three options. You need to guess which is the real reason your parcel is delayed."

    ap "You only get one shot, so you better be sure about it!"

    ap "Make sense?"

    "That doesn't sound too difficult."

    pl "Indeed it does."

    ap "Alrighty - option one! Your parcel was further delayed because the police thought it was a weapon and confiscated it."

    ap "Option two! Your parcel was further delayed because of a gas leak that turned into a full-blown fire."

    ap "Option three! Your parcel was further delayed because someone, at a critical time, gave birth, and everyone forgot all about the parcels."

    show april happy

    ap "Sooo? Whaddaya think is the truth?"

    menu:
        "\"Option one: confiscation\"":
            $ ap_friend += 5
            ap "Ding ding ding! We have a winner!"
            jump d4_po_expl
        "\"Option two: fire\"":
            ap "Whomp whomp! Incorrect. Unlucky!"
            ap "The {i}actual{/i} answer was... option one!"
            jump d4_po_expl
        "\"Option three: surprise birth\"":
            ap "Whomp whomp! Incorrect. Unlucky!"
            ap "The {i}actual{/i} answer was... option one!"
            jump d4_po_expl

label d4_po_expl:
    show april angry
    ap "Your package, along with a bunch of others, were seized by the police as evidence."

    ap "Earlier, Millicent called them to see if she could get them released... which {i}did{/i} work, for once."
    show april neutral
    ap "That's a dig on the cops, not on Millicent, to be clear. We all love Millicent."
    show april embarrassed
    ap "THEN it turned out that the parcels actually HAVE been released..."

    ap "... eeeeexcept for yours."
    show april neutral
    ap "It was seized specifically because, I dunno, some random cop was getting bad vibes and thought it was some kind of weapon?"
    show april angry
    ap "Which it's {i}not{/i}, obviously, but they went through all the rigamarole of opening it and investigating it and everything."

    ap "So it's been unwrapped."
    show april shocked
    ap "Which is fine! All they need to do is wrap it up again and send it off."
    show april angry
    ap "Except! And here's the kicker!! They {i}can't{/i} wrap it because they don't have any {i}wrapping paper{/i} at the precinct!!!"

    ap "And they were GOING to go get some, but all the stores are CLOSED!"

    "April looks about ready to tear their hair out."

    ap "Here's a fun fact of the day: the police are utterly {i}useless!{/i}"

    pl "That's..."

    menu:
        "\"...hilarious\"":
            show april embarrassed
            "April laughs, high and shrill."
            ap "Is it? I'm glad you're having fun."
            show april angry
            ap "It's been a real pain today, let me tell you."
            pl "I mean, it's a {i}little{/i} funny."
            pl "Like, astonishingly absurd, but funny!"
            show april neutral
            ap "Hm. Yeah, I guess."
            ap "It's been pretty hellish on my end."
            show april angry
            ap "Even without your delayed package, it's been nothing but HATE and VIOLENCE and SHOUTING AT ME all week."
            jump d4_po_aq1
        "\"...ridiculous\"":
            $ ap_friend += 5
            show april embarrassed
            "April wilts."
            ap "Ughhhh, I {i}know, right??{/i}"
            ap "I love jokes! I love absurdism!"
            ap "But there's a point where it gets to be truly untenable, y'know???"
            show april angry
            ap "What the hell were they thinkinggg augugughhhh...!"
            "She smears both hands down her face, groaning all the while."
            ap "It's so stupid. This is so, so stupid."
            jump d4_po_aq1
        "\"...impossible\"":
            show april neutral
            "April snorts."
            ap "Stranger things have happened, is all I'll say."
            ap "Is it surprising? Yes. Baffling? Yes."
            show april angry
            ap "Completely and utterly shameful conduct from our so-called 'boys in blue'? Yes!"
            ap "But it's definitely not impossible."
            ap "I mean, we're living it!"
            jump d4_po_aq1
        "\"...awful\"":
            $ ap_friend += 10
            pl "For me, yes, but also for you. And for Millicent."
            pl "I don't even know how you can begin to deal with that. That really sucks, April."
            show april angry
            ap "I KNOW, RIGHT!"
            ap "I mean, I'm {i}not{/i} dealing with it. That's why the shop's closed."
            ap "Depending on what ends up happening, Millicent and I were talking about one of us going all the way out to the precinct to get the parcel ourselves."
            ap "You've been waiting for sooooooo loooooooong. The least we can do is to get it to you directly."
            show april embarrassed
            ap "But yeah. Auauauguaguh. I've been stressed out of my mind for this whole week."
            ap "Which is partly why I wanted to chat with you! It's nice to have a customer I know isn't going to throw something at me."
            pl "Whoa - has someone actually done that?"
            ap "He did indeed. The prick."
            pl "What an asshole!"
            jump d4_po_aq1

label d4_po_aq1:
    show april angry
    "April laughs hollowly."

    "You work customer service too, so you can understand what April and Millicent have been through the past week."

    "The shouting, the swearing, the dogged refusal to extend even the slightest understanding to a worker who can't help the situation they've been forced into... yeah. You get that."

    "When you first started customer service, there were many shifts where shitty customers would make you want to scream or to cry. You're several years on from those sensitive early days, but even if you can laugh away the crappier days with your coworkers, it still stings."

    "You wish there was something you could do to help April out - to take their mind off this terrible work week."

    "Then it hits you."

    "It's not like you have anything to do this afternoon. And you're pretty sure April's shift is about to finish."

    "Maybe you could invite them round your place? It's not a guarantee, obviously, but it might be a good bit of fun for the both of you."

    "And maybe it'd be a good way to get closer to her..."

    pl "Hey, April."

    ap "Huh?"

    menu:
        "\"I hope things get resolved soon\"":
            show april embarrassed
            ap "Hah. So do I!"
            ap "Thanks for listening to me bitch, [name]."
            ap "Sorry I couldn't help any more."
            pl "That's okay."
            pl "I'll see you in a couple days?"
            ap "Sounds about right."
            show april neutral
            ap "Later, [name]!"
            pl "Bye, April!"
            jump d4_home
        "\"Do you want to hang out at my place after this?\"":
            pl "It could be a nice way to destress."
            pl "We could play some video games, maybe chat for a bit."
            pl "Only if you want, of course!"
            if ap_friend < 40:
                show april neutral
                ap "Hm... I appreciate the offer, [name], but I think I just want to go home and take a nap."
                ap "I'm sure you understand."
                "Oh... well, that's disappointing."
                pl "...Yeah, I get it."
                pl "No worries. Maybe another time?"
                ap "Maybe!"
                ap "Actually, I have to start closing up for real, so..."
                "You get the message."
                pl "Oh. Sure. I'll head out."
                pl "I'll see you in a couple days?"
                ap "Sounds about right."
                ap "Later, [name]!"
                pl "Bye, April!"
                jump d4_home
            else:
                ap "..."
                ap "......"
                ap "............."
                show april neutral
                ap "You know what? Sure!"
                pl "Really?"
                ap "Hell yeah! Why the hell not!"
                ap "Playing video games and dicking around sounds like an awesome time."
                ap "Let me close up and we can get going."
                pl "Awesome!"
                show april happy
                "April grins at you, a certain lightness to their countenance, then they duck behind the desk to finish closing up."
                "You tell them you'll be waiting out at the car park. You don't have to wait long before April appears, keys swinging around her finger and whistling jauntily."
                ap "Thanks for not running away on me!"
                ap "I'll follow you in my car. Lead the way!"
                jump d4_ap_date

label d4_ap_date:
    $ ap_date = True
    stop music fadeout 5.0
    scene bg black with fade
    "And lead the way you do. You get to your house with no incident, April trailing behind you in their beat-up sedan."

    "As you both get out of your cars, you hear April give a low whistle."

    scene bg bedroom aft with fade
    play music "Coffee Lounge.mp3" loop

    show april shocked

    ap "You didn't tell me you were a homeowner, [name]!"

    pl "Hah! That's because I'm not. We're just renting."
    show april neutral
    ap "Ohhh. That makes way more sense."

    ap "Well it's still a lovely spot. Thanks for inviting me over!"

    "You and April head inside. You've cleaned up a bit since yesterday, so you don't feel too self-conscious letting April into your house."
    show april shocked
    "When you're in, April gawks unashamedly at the decor."

    ap "It's so nice in here!"

    pl "Aw, thanks!"

    menu:
        "\"It's mostly my partner's decor\"":
            if partner == "Bailey":
                $ b_friend += 5
            else:
                $ a_friend += 5
            ap "Oh yeah?"
            if ap_friend >= 50:
                show april embarrassed
                "They look a little put out by the mention of your partner."
                ap "Well, they did a really awesome job."
                jump d4_ap_date_aq1
            else:
                show april neutral
                ap "They did a good job! My home looks like garbage in comparison, haha."
                jump d4_ap_date_aq1
        "\"I worked really hard on the decor\"":
            ap "I can tell!"
            ap "Good decorations, a good house..."
            if ap_friend >= 50:
                show april flirty
                ap "... you got anyone to share it with? Hahaha."
                "Oh, right. You haven't told April about [partner] yet."
                pl "Yeah, I have a partner. Here!"
                "You point out a picture of [partner] and you with your arms around each other, laughing."
                pl "[partner] isn't here right now. Away at a work conference."
                show april embarrassed
                ap "Oh wow... a {i}conference{/i}, huh?"
                "April shifts their weight, suddenly looking a bit self-conscious."
                ap "That's really fancy! Haha. You must be so proud."
                jump d4_ap_date_aq1
            else:
                show april neutral
                ap "All you need is a little white dog and a picket fence and you'd be the height of modern sophistication!"
                jump d4_ap_date_aq1
        "\"Me and my partner worked really hard on the decor\"":
            if partner == "Bailey":
                $ b_friend += 5
            else:
                $ a_friend += 5
            show april neutral
            ap "Oh yeah? I didn't know you had a partner."
            if ap_friend >= 50:
                show april embarrassed
                "Does she seem a little put out after learning that?"
            ap "You both did an awesome job with the place! You should be proud."
            jump d4_ap_date_aq1

label d4_ap_date_aq1:
    show april neutral
    "You realise suddenly that you haven't talked at all with April about the whole polyamorous thing going on with you and [partner]."

    "You guess it doesn't {i}really{/i} matter, if you're intending to hang out with April as a friend."

    "But if you were interested in a different kind of way... it would be best to bring it up right now."

    "But then again, what if it's weird?? April is cool, but you have no idea how she'll react to polyam stuff."

    "As you debate the topic internally, you realise that this is exactly how [partner] must have felt before they brought it up with you."

    menu:
        "Tell April about the whole polyam thing":
            if partner == "Bailey":
                $ b_friend += 10
            else:
                $ a_friend += 10
            $ ap_friend += 5
            stop music fadeout 5.0
            pl "Uh... hey, April, can I talk to you about something kind of important?"
            show april shocked
            ap "Woah, is everything alright?"
            ap "Am I in trouble?"
            pl "Oh no! Not at all."
            pl "It's just that I have to tell you something about, well, me. And my partner."
            show april neutral
            pl "Earlier this week, I learnt that [partner] is polyamorous."
            pl "Do you know what that means...?"
            ap "Er... not really."
            ap "I think I've heard it somewhere online before?"
            "Oof. This makes things a bit more complicated."
            pl "Well, it's basically when someone has the capacity to love more than one person, at the same time."
            pl "If you're polyamorous, you can have relationships where you date and love multiple people."
            pl "It's not cheating, it's just another way to organise and structure relationships."
            pl "And it can be really distressing to hide."
            "Is it distressing for you, right now, explaining this to April?"
            "You're not sure. It's definitely confusing, you know that much."
            pl "My partner is polyamorous, actually. And I'm currently, uh, experimenting to see if I am or not."
            if cppl == True:
                pl "It's totally fine for me to see other people - me and [partner] talked about it a couple of days ago, actually."
            pl "Just for your, uh! Information."
            "What are you saying. Why are you saying this. Is this weird??"
            "April is nodding with a thoughtful look on their face."
            ap "Huh... polyamorous, huh?"
            ap "That... sounds really, really cool, actually."
            "You deflate a little. {i}Phew.{/i}"
            "April is looking into the middle distance, clearly weighing up something in her mind. But before you can ask, they snap back to your present conversation and give you a big grin."
            show april happy
            ap "Well, {i}that's{/i} good to know!"
            ap "Very, very good to know..."
            ap "... for many reasons!"
            "She laughs, which gets you laughing, too."
            ap "Thanks for telling me. Which, hey, maybe I shouldn't bother thanking you because it sort of feels like the bare minimum? But still, I appreciate it."
            ap "And I'm sure [partner] appreciates it, too."
            jump d4_ap_date_aq2
        "Do not tell April about the whole polyam thing":
            if partner == "Bailey":
                $ b_friend -= 20
            else:
                $ a_friend -= 20
            $ ap_friend -= 5
            stop music fadeout 5.0
            "You keep your mouth shut."
            "It's kind of a complicated topic... you really don't want to scare April away."
            "It probably won't even come up!"
            "...Right?"
            jump d4_ap_date_aq2

label d4_ap_date_aq2:
    play music "Coffee Lounge.mp3" loop
    show april neutral
    "April claps her hands suddenly together and rubs them mischievously."

    ap "Alriiiight. What did you have planned?"

    pl "Well, not much, truthfully. We could play some video games?"

    show april happy

    "April lights up instantly."

    ap "I {i}love{/i} video games!"

    ap "Do you have Blast? I was an absolute {i}legend{/i} at Blast back in my hometown."

    ap "I won tournaments and everything!"

    menu:
        "\"That's so cool!\"":
            $ ap_friend += 5
            show april flirty
            ap "Yup. I'm kind of a god gamer, what can I say."
            jump d4_ap_date_aq3
        "\"That's not true at all\"":
            $ ap_friend += 10
            show april embarrassed
            ap "Well.. I {i}joined{/i} tournaments, at least."
            jump d4_ap_date_aq3

label d4_ap_date_aq3:
    show april neutral
    "Luckily, you do indeed have Blast." 
    "You've got a couple other games, though, in case you're not really in the mood for a combat game." 
    "Hopefully April will be receptive to them."

    menu:
        "Suggest a board game-style, like Creature Dance":
            $ game = "Creature Dance"
            ap "Hm. Wouldn't that be a little dull?"
            pl "I wouldn't say so. The humour can get pretty raunchy."
            show april flirty
            ap "Ohohoho! {i}That{/i} sounds like fun!"
            show april neutral
            ap "Let's do that!"
            jump d4_ap_date_aq4
        "Suggest a racing game, Marius Voiture":
            $ game = "Marius Voiture"
            ap "Oh no, you've found my weakness!"
            ap "Racing games!"
            ap "Just kidding, I'm pretty good at those too haha. Let's do that!"
            jump d4_ap_date_aq4
        "Agree to play Blast":
            $ ap_friend += 5
            $ game = "Blast"
            show april happy
            ap "Yessssss! Let's go let's go let's go!!"
            jump d4_ap_date_aq4

label d4_ap_date_aq4:
    show april happy

    "You set up your LX Redux console with April cheering you on. It takes a bit of time to download and boot up [game], but with April chatting alongside you, it goes by quick."

    "Once the game is set up, you and April take positions. April deigns to let you be player one."

    if game == "Creature Dance":
        "You explain a few of the rules of Creature Dance during the first round, but it's ultimately not a very complex game so April picks it up quick."
        "They waste no time in flirting with the demon prince and the fish girl, which surprises you. You say that you would've expected April to like the partygoer ghost the best."
        ap "Nah, she's way too much like me."
        ap "It wouldn't be fun if I was just joking with myself the whole time! I like more of a challenge!"
        jump d4_ap_date_play
    if game == "Marius Voiture":
        "After fiddling with some of the settings (April immediately turns off auto-steer and jokingly complains about your narrow range of vehicles), you're off."
        "You have much stronger opinions on which courses you should play, but you do take note that April enjoys the windy routes with very little guard rails, because she enjoys the challenge."
        jump d4_ap_date_play
    if game == "Blast":
        "You like to think you're pretty good at Blast, but it's clear April thinks the same about herself. Immediately, you are going toe to toe, pushed to a much higher limit than you're used to playing with [partner]."
        if partner == "Bailey":
            "Bless her soul, but she is {i}really{/i} bad at Blast."
        else:
            "Bless his soul, but he is {i}really{/i} bad at Blast."
        jump d4_ap_date_play

label d4_ap_date_play:
    "As you play, it's becoming more and more apparent that you're going to need a strategy to beat April." 
    "They're genuinely quite good, and as they feel out your playstyle, she's getting more confident."

    "How are you going to approach this?"

    menu:
        "Play aggressively":
            $ ap_friend += 5
            "You decide to throw caution to the wind. What's gonna let you beat April isn't quiet plays and thought-through plans, it's recklessness and taking them by surprise."
            if game == "Creature Dance":
                "You're making risky rolls and prepping for unlikely events. April's eyes widen more and more as they realise what you're doing. She tries to adjust, but..."
            if game == "Marius Voiture":
                "You're going for dangerous manoeuvres and aggressive attacks. April's eyes widen more and more as they realise what you're doing. She tries to adjust, but..."
            if game == "Blast":
                "You're letting yourself stay open to attacks while setting yourself up for huge hits. April's eyes widen more and more as they realise what you're doing. She tries to adjust, but..."
            "...you now have too much of a lead for her to keep up with."
            "You close out the game victoriously, grinning when the final scores come in. It wasn't even {i}close{/i}."
            "April leans back in their seat and gives a low whistle."
            show april embarrassed
            ap "Whoa... I really thought I had it in the bag!"
            show april happy
            ap "Good game, [name]. Well played."
            jump d4_ap_date_ag
        "Play conservatively":
            "You decide to slow it down. What's gonna let you beat April isn't rushing carelessly in, it's biding your time and waiting it out."
            "...Which is what you {i}thought{/i} would happen, except that doesn't seem to be working out."
            "April is acting quicker and bolder than you, capitalising on your slow pace to increase their lead."
            "When the game is finally over, it's not even close."
            show april sad
            "April looks over at you and pouts."
            ap "Man! Did you let me win or something??"
            pl "No!! I just had a different strategy."
            show april neutral
            ap "Well you should get a {i}different{/i} different strategy."
            "She slaps you on the shoulder."
            show april happy
            ap "Good effort, though!"
            jump d4_ap_date_ag
        "Let April win":
            $ ap_friend -= 5
            "You don't want April to have a bad time - she's had a bit of a crappy week, after all. And you're meant to be cheering her up!"
            "You start playing sloppier, making mistakes where you're pretty sure April won't question you."
            show april angry
            "You shoot a glance at April, and their brow is furrowed."
            "By the end, April has won, but they turn around immediately and raise an eyebrow at you."
            ap "Were you letting me win???"
            pl "Hey - what? No! Noooo!"
            "April squints at you, then huffs, clearly irritated."
            ap "There's no need to baby me, okay? I'm not your kid sister or a freakin' - crybaby! I won't be upset if you win normally against me."
            ap "But I {i}am{/i} upset if you {i}purposefully throw the game.{/i} Which you just did, obviously. Hence me being upset."
            "Yikes. You probably shouldn't have done that, huh?"
            show april embarrassed
            "April whooshes out a big breath in their chest and forces a smile."
            ap "Whatever. You've done it now. I was having a good time until you chose to go easy on me, for what it's worth."
            jump d4_ap_date_ag

label d4_ap_date_ag:
    scene bg bedroom n with fade
    show april neutral

    "It's now getting to evening. April looks outside and notices the time."

    ap "Oh dang. I really ought to get going."

    "You agree, and you both hustle out of the bedroom, making sure that she's accounted for all of her things."

    pl "I'll walk you out."

    ap "Please do!"

    "She gives one last look at your house as she is brought to the door, then she turns around and holds out their arms."

    ap "Hug?"

    menu:
        "Give her a hug":
            pl "Sure!"
            "You both lean in and give each other a big hug."
            if ap_friend >= 60:
                jump d4_ap_date_hughi
            else:
                jump d4_ap_date_huglo
        "Don't give her a hug":
            pl "No thanks, I don't really do hugs."
            ap "That's all good! I get it."
            if ap_friend >= 60:
                jump d4_ap_date_nohughi
            else:
                jump d4_ap_date_nohuglo

label d4_ap_date_hughi:
    "April is warm and soft in your arms. You're both hugging each other firmly, and you're noticing more and more the hum of her breath, the slight floral note to their shampoo."

    "You realise a beat too late that this hug is probably going on for way longer than necessary."

    "You should probably pull away now... but April feels so nice here with you, and it doesn't seem like they're itching to leave any time soon."

    ap "Man... I wish I could stay longer."

    "Their voice is barely above a whisper."

    pl "I do, too."

    "April gives a mischievous little giggle. It bubbles through your chest."

    show april flirty

    ap "We should do this some other time."

    pl "I'd really like that... maybe at your place this time?"
    show april happy
    "April laughs suddenly, high and bright, and it gets you laughing along with them."

    ap "My place is a dump!"

    "Her voice softens again."

    show april neutral

    ap "But yeah, that'd be fun. I'd clean it up for you."

    "It's a silly sort of thing to say, but it still warms you."

    "April sighs, and she disconnects from the hug. You immediately feel the emptiness, and you can't help but let it show on your face."

    "April takes a look at your expression and bursts out laughing again."

    show april happy

    ap "I'm not dying, silly!"

    ap "We'll {i}definitely{/i} meet up again."

    ap "You've still got a parcel to pick up, remember?"

    show april flirty

    "She sticks her tongue out cutely."

    ap "I'll see you then!"
    show april neutral
    "Before you can respond, she turns around and trots down the street. You are left gaping at her for a second, before coming to your senses."

    pl "{i}April!{/i}"

    "It's half a shout, and it stops them in their tracks. They turn around to face you, and is that the faintest blush you can see dusting their cheeks?"

    "Your mind is hilariously blank for something to say."

    pl "... Let me know when you get home safely, yeah?"

    "Hey expression softens."

    ap "Sure thing, ya big softie!"

    "You wave her off. They wave back, and away they go, and they're gone."
    jump d4_home

label d4_ap_date_huglo:
    "April is the first to pull away."

    ap "I had a good time today. Thanks for inviting me over."

    ap "I think this makes us friends now, don't you agree?"

    pl "I think so."

    pl "Thanks for agreeing! I had an awesome time."

    ap "Same here!"

    ap "I'll see you around, yeah?"

    pl "Sure thing - I still gotta get my parcel!"

    "April laughs. She turns around and gives you a two-fingered salute before sauntering back to their car."

    "You close the door, feeling warm and light in your chest. Even if the evening didn't go exactly as planned, you still had a good time."
    
    jump d4_home

label d4_ap_date_nohughi:
    "You're a bit worried that April's going to find that weird, but it doesn't seem so. In fact, she is staring at you with big, adoring eyes, and a gentle sort of smile that you're not quite used to seeing."

    "It leaves you a bit breathless in the evening light."

    "April looks away for a second, clearly debating saying something, then looks back at you and chuckles a little."

    ap "Man... I wish I could stay longer."

    "Their voice is barely above a whisper."

    pl "I do, too."

    "April gives a mischievous little giggle. It bubbles through your chest."

    show april flirty

    ap "We should do this some other time."

    pl "I'd really like that... maybe at your place this time?"
    show april happy
    "April laughs suddenly, high and bright, and it gets you laughing along with them."

    ap "My place is a dump!"

    "Her voice softens again."

    show april neutral

    ap "But yeah, that'd be fun. I'd clean it up for you."

    "It's a silly sort of thing to say, but it still warms you."

    "You notice suddenly that April is blushing, the rosiness of their cheeks deepening as your farewell drags on. She scratches a bit at the back of her head, and you are overcome with a sudden wave of tenderness so powerful it nearly bowls you over."

    "April takes a look at your expression and bursts out laughing again."

    show april happy

    ap "I'm not dying, silly!"

    ap "We'll {i}definitely{/i} meet up again."

    ap "You've still got a parcel to pick up, remember?"

    show april flirty

    "She sticks her tongue out cutely."

    ap "I'll see you then!"
    show april neutral
    "Before you can respond, she turns around and trots down the street. You are left gaping at her for a second, before coming to your senses."

    pl "{i}April!{/i}"

    "It's half a shout, and it stops them in their tracks. They turn around to face you, and is that the faintest blush you can see dusting their cheeks?"

    "Your mind is hilariously blank for something to say."

    pl "... Let me know when you get home safely, yeah?"

    "Hey expression softens."

    ap "Sure thing, ya big softie!"

    "You wave her off. They wave back, and away they go, and they're gone."
    jump d4_home

label d4_ap_date_nohuglo:
    ap "I had a good time today. Thanks for inviting me over."

    ap "I think this makes us friends now, don't you agree?"

    pl "I think so."

    pl "Thanks for agreeing! I had an awesome time."

    ap "Same here!"

    ap "I'll see you around, yeah?"

    pl "Sure thing - I still gotta get my parcel!"

    "April laughs. She turns around and gives you a two-fingered salute before sauntering back to their car."

    "You close the door, feeling warm and light in your chest. Even if the evening didn't go exactly as planned, you still had a good time."
    jump d4_home


label d4_home:
    hide april neutral
    stop music fadeout 5.0
    play music "SLipstream.mp3" loop
    if ap_date == False:
        scene bg bedroom aft with fade

        "You head home, alone, with a vague feeling that maybe there was something else you were supposed to do."

        "You shrug it off and flop onto your bed."

        "You're feeling extremely tired today, for some reason."

        "You stare at your ceiling and let your eyes unfocus."

        scene bg bedroom n with fade

        "Before you realise it, you're waking up from a sleep you didn't know you were having."

        "It's dark outside."

        "You feel a pang of guilt, like maybe you should have done more with the day."

        "But something else in you reassures you that it's ok to have a day where you just rest, every once in a while."

        "Your phone buzzes"
        jump d4_home_buzz
    else:
        scene bg bedroom n with fade

        "After seeing April off, you go back to your room and flop onto your bed."

        "Hanging out with them is always a lot of fun!"

        "But... now you do feel pretty wiped."

        "You begin to shut your eyes, but hear your phone buzz."

        jump d4_home_buzz

label d4_home_buzz:
    "It's from [partner]."

    if partner == "Bailey":
        b "{i}hey, [name]! Hope ur day was good. I'm going out for drinks with some of my coworkers and won't be able to talk tonight (sorry!) But sleep well and we'll chat tomorrow.{/i}"
        if b_friend >= 60:
            b "{i}love you xx{/i}"
            jump d4_home_aq1
    else:
        a "{i}hey, [name]! Hope ur day was good. I'm going out for drinks with some of my coworkers and won't be able to talk tonight (sorry!) But sleep well and we'll chat tomorrow.{/i}"
        if a_friend >= 60:
            a "{i}love you xx{/i}"
            jump d4_home_aq1
    
label d4_home_aq1:
    "Seems like you have the evening to yourself, then."

    "What to do?"

    "..."

    "Oh, right."

    "Your essay is due tomorrow. You should probably do some work on that."

    "Thankfully, you were prepared enough to have already started your essay. So, mostly it's just editing what you've already got to make it even {i}better.{/i}"

    "Or, depending on what you have, to put dot point ideas into actual sentences."

    "Plus your reference list. Pain in the ass that it is."

    "It's already dark, but you aren't especially tired, and still have a few hours before you typically go to bed, anyway."

    "You spend almost two hours neatening up and rewording your essay before you decide it's good enough."

    "You take a deep breath and turn it in."

    "For some reason, you always get a bit anxious about the actual turning-it-in part. Like it's going to evaporate at the last second and suddenly you'll have to write the whole thing again."

    "But it's fine. You check the submitted page, and it's all ticked off with your attachment and everything."

    "You sigh and stretch your arms."

    "Now what?"

    "Deciding that you weren't quite done with flopping on your bed, you do so again and get out your phone."

    "Your mind starts drifting across thoughts of your day. It felt a little... empty. But not necessarily bad."

    if ap_date == True:
        "That date with April was pretty fun, after all."
    
    "You're glad you got to see April today. Otherwise it might have felt a little... lonely."

    "April..."

    "Suddenly, you seem to be scrolling their social media timeline."

    menu:
        "Close it":
            "You shut off your phone, your face a little red from shame."
            "What were you even doing?"
            "You resolve to watch some videos instead before bedtime."
            jump d4_end
        "Scroll through a few posts":
            "Her last post was of the tree outside the post office in the afternoon glow, captioned 'Golden Hour ;P'. Dated nine days ago."
            "The post before that was of her wearing what appears to be a very bedazzled train conductor outfit, with a drawn on moustache and severe eyebrows. The caption is 'What a drag?'. Dated a month ago."
            jump d4_home_post

label d4_home_post:
    menu:
        "Like the golden hour post":
            "You give the post recent post a like."
            menu:
                "Leave a comment, too":
                    $ ap_friend += 5
                    "You leave a comment: '{i}hey I know that tree...{/i}'"
                    $ ap_com_tree = True
                    "Then you spot the time. Probably best to start getting ready for bed."
                    jump d4_end
                "Do not":
                    "You don't leave a comment."
                    "But you do spot the time. Probably best to start getting ready for bed."
                    jump d4_end
        "Like the drag post":
            $ ap_friend += 5
            "You like the slightly older post."
            menu:
                "Leave a comment, too":
                    $ ap_friend += 5
                    "You leave a comment: '{i}Looking handsome af!{/i}'"
                    $ ap_com_drag = True
                    "Then you spot the time. Probably best to start getting ready for bed."
                    jump d4_end
                "Do not":
                    "You don't leave a comment."
                    "But you do spot the time. Probably best to start getting ready for bed."
                    jump d4_end
        "Don't like either of them, that's weird":
            "You don't like either of the posts."
            "Instead, you look at the time and decide it's probably best to start getting ready for bed."
            jump d4_end

label d4_end:
    "You brush your teeth and get changed."
    if ap_com_drag == True:
        "Before getting into bed, you check your phone once more. April has liked and replied to your comment."
        ap "{i}Why thank you! I was kinda nervous since it was my first time doing a drag face...{/i}"
        "You like the comment."
    if ap_com_tree == True:
        "Before getting into bed, you check your phone once more. April has liked and replied to your comment."
        ap "{i}Tree? What tree? This is clearly a moose!!{/i}"
        "You like the comment."
    "You get into bed and make sure your phone is on silent tonight."
    "Despite all the rest you had today, getting to sleep is easy."
    "Somehow, you feel yourself fall asleep with a slight smile on your face."
    scene bg black with fade
    stop music fadeout 5.0
    jump d5_start

label d5_start:


return  































label bailey_partner:

    hide angus neutral
    hide bailey neutral

    "Perfect! Now we can begin."
   
    play music "Theme.mp3" fadein 1.5 loop

    scene bg bedroom aft with fade

    "On a fine spring day, you get home from work, put all your things away, and sit down in your bedroom for a bit. "
    
    "About two months ago, you moved in with your partner of two years, [partner]. The two of you now rent a small house in a suburb a short travel from both your work and the university you attend. It's very convenient, and very lucky."

    "It's been good, it really has."

    "The only issue is, well..."

    "Bailey has been acting a little strange ever since you moved in."

    "It's hard to describe, but she's... less present. Spacing out more. Like she's never really quite... {i}here{/i}."

    "Maybe she's just stressed from work. She does have a big trip coming up, after all."
    
    "Speaking of Bailey, you should go find her. You haven't seen her since you got back."

    scene bg garden aft with fade

    "It doesn't take you long to find Bailey, as the house is small and you know she likes spending time in the garden."

    show bailey neutral

    stop music fadeout 5.0

    "When you find her, Bailey is staring at a garden hose, which is running. It is not aimed at any plants, but rather just spilling on the ground."
    
    menu b_garden_hose:
        "Turn off the garden hose":
            jump b_garden_hose_off
        "Put your thumb over the spout of the garden hose":
            $ b_friend += 5
            jump b_garden_hose_thumb
        "Just keep staring at Bailey":
            jump b_garden_hose_on
    
    label b_garden_hose_off:
        
        show bailey shocked
        
        b "Huh!?"
        
        show bailey neutral
        
        b "Oh, [name]"
        b "Why did you turn off the hose? I was watching that..."
        
        jump b_after_hose
    
    label b_garden_hose_thumb:

        "At first, the water stops. But very soon it begins to push and spill around your thumb."
        
        "Then it starts to spurt everywhere, tiny jet-streams making their way forcefully over your hands, your clothes, your face."

        show bailey shocked

        b "What are you {b}doing!?{/b}"

        "Bailey turns off the hose."

        show bailey happy

        "Bailey starts laughing."

        b "Oh, wow... you look so silly, [name]. Why did you do that?"

        b "I didn't even notice you get home..."

        show bailey neutral

        jump b_after_hose

    label b_garden_hose_on:

        "After a few moments, Bailey puts her thumb over the hose, momentarily stopping the water flow."

        "Shortly, though, water finds its way around her blockage, and begins to seep and then spurt out around her thumb."
        
        "Her hands drip with water and her clothes begin to soak."
        
        show bailey shocked

        "Seeming to come to her senses, Bailey lets go of the hose and turns it off at the tap."

        "She turns and sees you, clearly startled."

        b "Wh-? [name]! When did you get ther- I mean, back?"

        show bailey neutral

        jump b_after_hose

label b_after_hose:

    b "I mean, welcome home! You must be tired."
    
    if b_friend >= 5:
        "Bailey kisses you on the cheek before you tell her about your day."
    else:
        "Bailey smiles at you as you tell her about your day."
    
    "The two of you chat for a little while."

    "You notice that, once again, Bailey seems to be thinking of something else. She keeps looking to the side and fiddling with her earrings."

    "After a lull in conversation, she takes a deep breath."

    show bailey embarrassed

    b "So, there's something I've been meaning to talk to you about."
    b "And before I say it, I want to make it clear that I don't expect an answer right away. In fact, I'd rather you didn't say anything for a... little while."
    b "You know how I have that work trip starting tomorrow?"
    b "I want to wait until after my work trip is done to hear what you have to say about it. It will just be a week, but that should be long enough."
    b "For you to really think about it and for me to... {i}prepare{/i} myself."

    menu b_interrupt:
        "Ask her what it is":
            $ b_friend -= 5
            show bailey angry
            b "I'm getting there, just {b}wait!{/b}"
            jump b_after_interrupt
        "Just wait":
            $ b_friend += 5
            "Bailey takes another deep breath."
            jump b_after_interrupt

label b_after_interrupt:

    show bailey neutral

    b "I'm polyamorous. Do you... know what that is?"

    menu b_polyq:
        "Yes":
            b "Oh, that's great."
            jump b_after_polyq

        "No":
            b "Okay, well it's... essentially, it's when a person, like me, has feelings for more than one person at a time."
            b "There's kind of more to it than that."
            b "But for me, it means that I can't stop myself from having feelings for multiple people."
            b "And I don't {i}want{/i} to stop myself, either."
            b "It's not like cheating. Although I guess some people {i}will{/i} cheat... to, like, deal with it..."
            show bailey embarrassed
            b "But I just... I want to be open and honest. I want to be honest and real with you, because I love you. But... well, I also want to love other people."
            show bailey neutral
            b "But, it has to have everyone's consent. To, like, make sense, and be okay."
            b "So, if I have more than one partner, {i}all{/i} my partners would have to be okay with that."
            b "And it can even be like one big relationship. Where everyone is dating everyone."
            b "Like a love triangle, but like... an {i}actual{/i} triangle, with all three sides. Or more, depending."
            jump b_after_polyq

label b_after_polyq:

    b "The thing for me is, well, I'm starting to have feelings for this guy, Gary."
    b "But I also still have feelings for you."
    b "What I want is to be able to pursue things with Gary, but I also still want to be with you."
    b "But, I understand if that's not something you're comfortable with."
    show bailey sad
    b "So, if you want to break up with me, I... I understand."
    show bailey shocked
    b "We can still live together and be friends and everything, of course! But..."
    show bailey neutral
    b "Well, I need to be able to explore this part of my identity. That's sort of a non-negotiable, for me."
    b "It's not meant to be an ultimatum or anything, either. I just... I know what {i}I{/i} need, but I don't know what you're comfortable with."
    b "So, I want to give you time to really think about it. I don't want to pressure you into anything you're not okay with, but I don't want you to just dismiss it, either."
    b "It's important to me."
    b "So, don't tell me now. But think about it, and when I get back, you can tell me then. Okay?"
    b "..."
    show bailey embarrassed
    b "Um. Anyway, I should get started on dinner."
    hide bailey embarrassed

    
    "You are left in the garden, thinking about what she said."
    
    scene bg bedroom n with fade
    
    "Over dinner, the two of you talk about unrelated things, and then you go to your room to wind down and go to bed."
    
    scene bg black with fade
    scene bg bedroom with fade

label b_day1:

    play music "Theme.mp3" fadein 1.5 loop

    "The next day starts as all Mondays do - with a groan and the insistent sound of your alarm."
    
    "You don't have much time to yourself in the mornings. Before you know it you're up and showered and heading out the door to work. You almost stop to say goodbye to Bailey, before remembering that she has already left for her work trip."

    menu b_d1_mtext:
        "Send a good morning text":
            $ b_friend += 5
            pl "{i} hey bb! Heading to work rn, thinking of you <3 miss u already {/i}"
            stop music fadeout 5.0
            "Now you really have to get going. You jump into the car and pull out of the driveway, and away you go."
            jump b_d1_work
        "No time, you gotta get to work!":
            stop music fadeout 5.0
            "You'll text Bailey later. You jump into the car and pull out of the driveway, and away you go."
            jump b_d1_work

label b_d1_work:
    
    scene bg cafe
    play music "Lounge Lizard.mp3" loop
    "You work at the hit cafe 'Sugar in My Coffee', everyone's favourite local haunt." 
    "You barrel through the door and say hi to your manager and coworkers, and then it's a flurry of setting tables and warming pastries and pulling espresso shots until people start trickling in."
    "The morning rush hits you hard, but you get through most of it on auto-pilot. You're still turning last night's conversation over in your head, examining it from every angle, finding yourself rush back to it every time you think you've found a sufficient distraction."
    menu b_d1_feeling:
        "Mostly, you've been feeling..."
        "...excited. You've never thought about being polyamorous before!":
            $ b_friend += 5
            "You can feel it bubble up inside you like soft drink, waiting to be let out." 
            "You guess a part of you thought that because you were with [partner], that would mean the end of any personal exploration." 
            "But that isn't the case, and you're realising that you're much more excited at the prospect of learning something new about yourself than you were anticipating."
            jump b_d1_start
        "...stressed. You have no idea what you're meant to do now.":
            "How are you meant to figure this out by yourself? You feel like a teenager again, young and fresh and woefully inexperienced." 
            "It sounded like Bailey had been thinking about being polyamorous for a while now, but it's not something that you've even considered." 
            "You wish [partner] was here with you, even if she doesn't have answers either. Everything's so much easier with her by your side."
            jump b_d1_start
        "...angry. What a dick move from Bailey!":
            $ b_friend -= 5
            "It was shitty of [partner] to dump this all on you and then leave without letting you get a word in." 
            "You suppose you understand the desire to wait until after the work trip to talk this through, but still, what the hell?" 
            "You're just supposed to sit in your feelings for a whole week, trying to figure out something you didn't ask to figure out? That sucks!"
            jump b_d1_start
        "...worried. You hope Bailey is doing okay right now.":
            $ b_friend += 5
            "Bailey doesn't always let on how stressed she can get. Knowing her, she's been sitting on this for a while." 
            "You're sure that Bailey is freaking out about this, waiting tensely for your response on top of also being stressed about the work trip." 
            "You ache a little for her."
            jump b_d1_start

label b_d1_start:
    "Eventually, the rush hour dies down. There are only a couple people remaining in the store, all of them regulars."

    show angus neutral

    "Your coworker Angus strides up to you."
    
    "He joined a little bit after you, and you became fast friends after you realised you..."

    menu:
        "Like the same kinds of movies - artistic, thoughtful, heavily metaphorical":
            $ a_friend += 10
            "You're both kind of snobs, with very strong opinions about writing and cinematography." 
            "You've passed many a slow shift with spirited debates that make the rest of your workmates groan." 
            jump b_d1_afterq
        "DIslike the same kinds of movies - glitzy, mindless, vapid":
            $ a_friend += 5
            "One time, you hung out at his place after work, and you had a grand time tearing the latest release in a superhero multiverse cinematic universe to shreds." 
            "It's not every day you find a bona fide hater, and with opinions you agree with, no less." 
            jump b_d1_afterq

label b_d1_afterq:

    a "Hey there, [name]!"

    pl "Hi Angus, what's up? How was your weekend?"

    show angus sad
    a "Aw man, it was exhausting!"

    a "You remember how I told you about that article I'm working on?" 
    "My editor {i}still{/i} isn't happy with the revisions I've made, and it's like the third or fourth time I've passed my stuff back to him."

    menu:
        "\"That sucks! I'm sorry your editor is being difficult.\"":
            $ a_friend += 5
            a "Thanks, [name]."
            a "I swear, the man's out to get me."
            jump b_d1_aq2
        "\"This sounds like a skill issue\"":
            $ a_friend -= 5
            show angus sad
            a "Ugh, maybe it is..."
            a "Maybe I'm {i}not{/i} good enough to be in this magazine."
            a "Then again, maybe the magazine isn't good enough to give me an effective editor."
            a "The world of literature is fickle like that."
            jump b_d1_aq2

label b_d1_aq2:
    show angus neutral
    pl "Can I ask what kind of feedback he's giving you?"

    a "Well, he keeps saying that my work is 'unclear'."

    a "That it still lacks 'direction' and 'conviction'."

    menu:
        "\"Wow, that's really generic advice\"":
            a "I know, right?"
            a "It'd help more if I were given {i}practical{/i} tips."
            a "I mean, it's probably frustrating on his end as well..."
            a "I looked at his CV beforehand, and it looks like he works with a {i}lot{/i} of different people."
            a "I can't blame him too much if he's too busy to spell out absolutely everything."
            a "If only I could just beam exactly what I want my piece to be into my editor's head. Then he could write it for me, if he hates the original so much."
            pl "That'd be a handy ability. You could use it for ordering food, too."
            a "Or phone calls."
            pl "Or when you're trying to change lanes."
            show angus happy
            a "Or when I'm picking a movie to watch!"
            jump b_d1_aq3
        "\"Obviously you need to put more argument into your piece\"":
            $ a_friend -= 5
            show angus angry
            a "I mean, I know that..."
            a "Like I said, I just don't know how to, or even what that would look like."
            a "I suppose I can rewrite some stuff to be a little more opinionated, but this is meant to be a historical retrospective on the oeuvre of Charles Anathema."
            a "More of a reflection rather than a commendation, you know?"
            jump b_d1_aq3
        "\"Why don't you just ask him to explain what he means\"":
            $ a_friend += 5
            a "Well... that's true."
            pl "You could probably just say 'Could you explain what you mean by that?'"
            a "..."
            show angus happy
            a "Oh I could, couldn't I?"
            a "How did I not think of that before..."
            jump b_d1_aq2_ext

label b_d1_aq2_ext:
    a "[name], I think you might be a genius."
    menu:
        "\"It's nothing\"":
            pl "Let me know how it goes with your editor!"
            a "Haha, will do."
            jump b_d1_aq3
        "\"Tell me something I don't know\"":
            $ a_friend += 5
            "Angus laughs."
            pl "Let me know how it goes with your editor!"
            a "Haha, will do."
            jump b_d1_aq3

label b_d1_aq3:
    show angus neutral
    a "Anyway, enough about me. How was your weekend?"

    menu:
        "\"It was okay.\" (Tell him about the thing with your partner)":
            a "Woah... that's. A lot."
            pl "Yeah, I'm not quite sure how to feel about it."
            a "Yeah... that makes sense. It's sort of a tricky situation you're in."
            a "I'm sure Bailey is freaking out too. She sounds really confident, but it's a... difficult thing to open up to your partner about."
            "Angus fidgets for a bit." 
            show angus sad
            "It looks like he is debating on saying something, but before you can ask him about it, he continues talking."
            show angus neutral
            a "At least I imagine it would be!"
            a "Though, of course it is also difficult for you."
            a "Difficult topic all around..."
            jump b_d1_drinks
        "\"It was kinda shitty.\" (Tell him about the thing with your partner)":
            $ a_friend += 5
            a "Woah... that's. A lot."
            "He looks a bit conflicted before speaking to you again."
            jump b_d1_aq3_shitty
        "\"It was exciting!\" (Tell him about the thing with your partner)":
            $ a_friend += 10
            show angus happy
            a "Whoa... that's awesome!"
            pl "Yeah, I've been thinking about whether I'm polyam myself - I don't know if I am, but Bailey got me thinking."
            a "That's really cool, [name]!"
            a "I don't think most people would have taken so kindly to their partner telling them about polyam stuff."
            show angus neutral
            a "That's... really awesome that you're so open-minded about the whole thing."
            jump b_d1_aq3_exciting
        "\"It was nothing special.\" (Don't tell him about the thing with your partner)":
            a "Glad one of us had a relaxing time, then!"
            jump b_d1_drinks

label b_d1_aq3_shitty:
    show angus neutral
    a "Can I ask - just so I'm understanding - what's upsetting you in particular?"
   
    menu:
        "\"That she left without giving me a chance to respond\"":
            a "That's fair. You probably should have been allowed to respond to her."
            jump b_d1_drinks
        "\"That she wants to cheat on me.\"":
            $ a_friend -= 10
            show angus angry
            a "Being polyamorous isn't cheating."
            a "If she wanted to cheat, she wouldn't have asked your opinion."
            a "She was probably really worried about you responding like that."
            a "I'm glad she left before you replied. It probably would have really sucked for her to hear that from you."
            jump b_d1_drinks
        "\"I'm not really sure what's annoying me\"":
            $ a_friend += 5
            a "Yeah, that's fair."
            a "It's a bit of a tricky one, isn't it?"
            a "I think it's okay to be irritated."
            a "Just as long as you're not angry at her because she's polyam."
            jump b_d1_drinks
        "\"Isn't it obvious!?\"":
            $ a_friend -= 5
            a "Er... no. Not really?"
            jump b_d1_drinks

label b_d1_aq3_exciting:
    show angus neutral
    "Angus hesitates for a second. It looks like he is debating whether or not to say something."

    menu:
        "\"What's up?\"":
            a "Oh... nothing!"
            show angus happy
            a "I guess I'm just happy for you, haha!"
            jump b_d1_drinks
        "Wait for him to say it on his own":
            a "Actually... I've been thinking."
            a "About me, being polyam as well."
            pl "Woah, really?"
            a "Yeah! What're the chances!"
            a "I... I haven't decided anything, just yet."
            a "But I've been thinking about it for a long, {i}long{/i} time, I'm realising."
            show angus happy
            a "So... it's cool. To hear that you're so receptive to Bailey."
            a "That's really great, [name]."
            jump b_d1_drinks

label b_d1_drinks:
    show angus neutral
    "Just then, the bell for the drinks dings."

    a "Guess they remembered we're meant to be doing work here."

    "You and Angus head towards the bar."

    "Angus picks up one tray of drinks that is for some customers sitting outside, and gestures to the ones he leaves behind."

    a "Hey, [name], can you help me with these drinks?"
    
    pl "Sure! Where'm I headed?"

    a "Mimosa for Esma, soda water for Gary, and the decaf extra hot no foam almond cappuccino with honey for Bradley"

    pl "No foam in a cappuccino?"

    pl "So basically a fancy flat white."

    a "Basically a fancy flat white."
    show angus happy
    a "Isn't that hilarious?"

    hide angus happy

    "Angus sweeps away to tend to the customers outside."

    menu:
        "Whose drinks will you deliver first?"
        "Esme and Gary are sitting together, so you may as well bring out the mimosa and soda water first":
            $ d1_eg1 = True
            jump d1_eg
        "You should get the 'cappuccino' out to Bradley before it gets cold":
            $ d1_eg1 = False
            jump b_d1_br

label b_d1_br:
    show bradley neutral

    "When you arrive at the table, Bradley doesn't even notice you." 
    "He is too busy staring out the window, his whole body twisted around in his chair." 
    "His cheeks look a little flushed."

    pl "Cappuccino?"

    br "What? Oh, right..."

    "He reaches out for the cappuccino, except it's already on the table, so he just sort of grasps at thin air."

    br "Yes, yes. Thank you, [name]"

    "You can't help but follow his gaze."

    "Outside, Angus is laughing with a few customers."

    menu:
        "\"Can I get you anything else?\"":
            $ br_friend += 5
            br "No."
            br "..."
            br "Thanks, though."
            jump b_b1_end
        "\"Lovely weather we're having, isn't it?\"":
            show bradley angry
            br "Tch. Yes, I suppose, if you like that kind of thing."
            show bradley sad
            br "Siiiiiiggh... No weather is truly lovely for me."
            br "Being as I am all alone, with nobody to love or hold me."
            "He did, in fact, just say the word 'sigh' out loud."
            "Bradley is your partner Bailey's twin brother." 
            "You've never really hung out with Bradley before, because Bailey thinks Bradley is stupid, and Bradley thinks Bailey is insufferable." 
            "Sometimes you see Bailey's point."
            jump b_b1_aq1
        "\"What on earth are you looking at?\"":
            show bradley embarrassed
            br "Bwh- huh - that's! None of our business!"
            br "There's just somebody. Outside."
            br "Somebody who I'm looking at in a very normal way, for normal reasons."
            menu:
                "\"...Okay.\"":
                    "Bradley looks at you and bites his lip."
                    show bradley neutral
                    br "...Can you keep a secret, [name]?"
                    pl "Are you asking me to keep a secret from B-"
                    br "{i}Yes I'm asking you to keep a secret from Bailey{/i}"
                    "Bradley is your partner Bailey's twin brother." 
                    "You've never really hung out with Bradley before, because Bailey thinks Bradley is stupid, and Bradley thinks Bailey is insufferable." 
                    "Personally, you think that Bradley is a bit of a mess."
                    jump b_b1_aq1
                "\"Are you looking at Angus?\"":
                    $ br_friend += 5
                    br "Ex-CUSE me!?"
                    br "That is - just totally inappropriate! And wrong and... incorrect!"
                    br "I don't even know an Angus. Are you sure that's a real name?"
                    "You and Bradley stare at each other before Bradley huffs a large sigh, slumping in his seat."
                    show bradley neutral
                    br "Please don't tell Bailey."
                    "Bradley is your partner Bailey's twin brother." 
                    "You've never really hung out with Bradley before, because Bailey thinks Bradley is stupid, and Bradley thinks Bailey is insufferable." 
                    "Personally, you think Bradley is kind of funny."
                    jump b_b1_aq1
                "\"Look, if you're going to be weird about my coworker, I'm going to have to ask you to leave.\"":
                    $ br_friend += 5
                    show bradley shocked
                    "For a moment, Bradley looks genuinely shocked and dismayed."
                    br "Oh, of course! I would never... ahem. I'm sorry. That was inappropriate of me."
                    show bradley neutral
                    br "I'll leave if you'd like me to. But I'll stop, I swear."
                    "Bradley is your partner Bailey's twin brother." 
                    "You've never really hung out with Bradley before, because Bailey thinks Bradley is stupid, and Bradley thinks Bailey is insufferable." 
                    "Personally, you don't think he's that bad."
        "Leave":
            jump b_b1_end

label b_b1_aq1:
    
    show bradley sad
    br "You must think I'm pathetic."
    br "Coming in here every day like some sort of... swooning schoolgirl!" 
    br "Drooling over my coffee every day just for a chance to ask that barista out..."

    pl "Er... Angus is a waiter, not a barista."
    
    br "{i}See!?{/i} I don't even know what I'm {i}talking{/i} about!"
    br "I'm hopeless."
    br "Hopeless and weird."
    br "A weird, hopeless, {i}freak{/i}."

    menu:
        "\"Don't be so hard on yourself\"":
            $ br_friend += 5
            show bradley neutral
            br "Eugh... I should probably tone it down, you're right."
            jump b_b1_end
        "\"Yeah, it is pretty weird to ask someone out while they're at work\"":
            $ br_friend += 5
            show bradley neutral
            br "... it is, isn't it?"
            br "I should probably wait until he's off work to ask, then..."
            br "Oh my god, how did I not think of that before???"
            jump b_b1_end
        "\"Aw no, buddy, Angus loves you!\"":
            br "Are you sure about that? He said my coffee order was 'hilarious'."
            br "I can hear you guys making fun of my order, you know."
            show bradley angry
            br "No foam cappuccinos are a {i}real thing{/i}, by the way. Look it up."
            jump b_b1_end
        "\"Lucky for you, I {i}like{/i} hopeless and weird\"":
            show bradley disgusted
            br "Wait, ew, are you {i}coming onto me{/i} right now???"
            br "Absolutely stop that. Gross gross gross. I am so fully not interested."
            br "You're {i}dating{/i} my {i}sister{/i}!"
            jump b_b1_end

label b_b1_end:
    show bradley neutral
    "Bradley heaves a big sigh and takes a sip of his definitely-not-a-flat-white."
    br "That'll be all for now."
    br "Thank you, [name]."
    hide bradley neutral

    if d1_eg1 == True:
        jump d1_work_end
    else:
        "Now, on to Esme and Gary's table."
        jump d1_eg

label d1_b_home:
    "Bailey has already texted you at some point during the day, but you didn't see the notification."
    b "{i} heyyyy [name]!! today was SO busy omg. bunch of cool talks and cool ppl but i am so exhausted now lmao. i hope ur day was good! i miss u soso much <33{/i}"

    menu:
        "Give a generic response":
            pl "{i}Glad ur day was cool, but fair enough to be tired. My day was alright, but long. Miss you too <3{/i}"
            "Bailey replies almost instantly."
            b "{i} I am missable aren't I!{/i}"
            b "{i}Anyway, make sure to rest tonight{/i}"
            jump d1_b_home_aq1
        "Give a flirty response":
            $ b_friend += 5
            pl "{i}Not too exhausted to miss me, though... Guess I must be something special {/i}"
            "Bailey replies almost instantly."
            b "{i}Hmmm... and I guess ur not so bad either ;){/i}"
            jump d1_b_home_aq1
        "Give a tired response":
            pl "{i}My day was sooooo long :( Really tired now{/i}"
            "Bailey replied almost instantly."
            b "{i}Aw bby I'm sorry :( Make sure to rest up tonight and take things easy!{/i}"
            jump d1_b_home_aq1
        "Ignore the message and ask if you can talk about being polyamorous.":
            $ b_friend -= 10
            pl "{i}Hey can we talk about yesterday? The whole polyamory thing?{/i}"
            "Bailey responds after a few minutes."
            b "{i}Sorry, [name]. No. Not until I'm back.{/i}"
            jump d1_b_home_aq1

label d1_b_home_aq1:

    b "{i}Anyway. Anything interesting happen today?{/i}"
    menu:
        "\"Yeah! I had some really fun talks with some people!\"":
            $ b_friend += 5
            b "{i}Oh, sweet!{/i}"
            jump d1_b_home_newf
        "\"Yeah actually... I think I'm maybe interested in someone...\"":
            b "{i}Oh? Who is it? Do I know them? Tell meeeeee{/i}"
            jump d1_b_home_psn
        "\"Not really\"":
            b "{i}RIP{/i}"
            jump d1_b_home_end
        "\"I really think we should talk about yesterday\"":
            $ b_friend -= 10
            jump d1_b_home_yesterday

label d1_b_home_newf:
    b "{i}New friends, or...?{/i}"
    menu:
        "\"Too soon to say for sure\"":
            b "{i}Better make them friends >:){/i}"
            jump d1_b_home_end
        "\"I think so!\"":
            b "{i}Awesome >:) Proud of you!{/i}"
            jump d1_b_home_end
        "\"Maybe more than friends...\"":
            b "{i}OOOOOOHHH!!{/i}"
            b "{i}Who who who!?? Do I know them???{/i}"
            jump d1_b_home_psn

label d1_b_home_psn:
    menu:
        "\"I don't really wanna say who...\"":
            $ crush = "That person"
            b "{i}Oh boo!{/i}"
            b "{i}But sure, fair enough. Good luckkk~{/i}"
            jump d1_b_home_end
        "\"Well, it's a few people...\"":
            $ crush = "Everyone"
            $ b_friend += 5
            b "{i}Ooh nice!{/i}"
            b "{i}Do you think the feeling might be mutual for any of them?{/i}"
            jump d1_b_home_aq2
        "Angus":
            $ crush = "Angus"
            b "{i}Oh! He works with you, right?{/i}"
            b "{i}He seems nice{/i}"
            b "{i}Do you think he might be interested in you, too?{/i}"
            jump d1_b_home_aq2
        "Bradley":
            $ crush = "Bradley"
            $ b_friend -= 5
            b "{i}Disgusting{/i}"
            b "{i}That's my weird little brother{/i}"
            "Actually, he's her weird twin brother..."
            b "{i}Plus, he's into someone else and VERY monogamous{/i}"
            b "{i}Sorry to say it babe but you don't have a chance{/i}"
            jump d1_b_home_end
        "Esme":
            $ crush = "Esme"
            b "{i}I don't think I know of Esme...{/i}"
            b "{i}Well, good luck!{/i}"
            b "{i}Do you think he might be interested in you, too?{/i}"
            jump d1_b_home_aq2
        "Gary":
            $ crush = "Gary"
            $ b_friend += 5
            b "{i}Oh, Gary!{/i}"
            b "{i}My crush...{/i}"
            b "{i}So you're my rival now, then?{/i}"
            b "{i}Sorry to break it to you, but I don't think you have a chance babe!{/i}"
            b "{i}Gary is monogamous as a tree! And I intend to be the one he picks...{/i}"
            "A... tree?"
            "Oh..."
            pl "{i}Bailey... Are you thinking of mahogany?{/i}"
            b "{i}...maybe so{/i}"
            jump d1_b_home_end
        "Morgan":
            $ crush = "Morgan"
            b "{i}From your class?{/i}"
            b "{i}Cool. Do you think she might be interested in you, too?{/i}"
            jump d1_b_home_aq2
        "Pedro":
            $ crush = "Pedro"
            b "{i}From your class?{/i}"
            b "{i}Cool. Do you think he might be interested in you, too?{/i}"
            jump d1_b_home_aq2
        "April":
            $ crush = "April"
            b "{i}Oh April! From the post office, right?{i}"
            b "{i}I like them. She seems like fun!{/i}"
            b "{i}Do you think they might be interested in you, too?{/i}"
            jump d1_b_home_aq2

label d1_b_home_aq2:
    menu:
        "\"No idea!\"":
            b "{i}Well, go get an idea, bestie!{/i}"
            b "{i}And good luck!{/i}"
            jump d1_b_home_end
        "\"Maybe... there have been some hints\"":
            b "{i}Oooh spicy! Good luck ;){/i}"
            jump d1_b_home_end
        "\"Oh, definitely!\"":
            b "{i}Someone's confident...{/i}"
            b "{i}Good luck, anyway!{/i}"
            jump d1_b_home_end
        "\"Definitely not\"":
            b "{i}awww baby no!!{/i}"
            b "{i}Good luck, anyway!{/i}"
            jump d1_b_home_end

label d1_b_home_yesterday:

    if b_friend >= 15:
        b "{i}I really don't want to. Can we please just talk about your day?{/i}"
        menu:
            "\"Okay, I'm sorry\"":
                $ b_friend += 5
                jump d1_b_home_reset
            "\"Fine.\"":
                jump d1_b_home_reset
            "\"No. We have to talk about it.\"":
                $ b_friend -= 5
                "It's a few minutes before Bailey responds."
                b "{i}We actually don't.{/i}"
                b "{i}Goodnight.{/i}"
                jump d1_b_home_end2
    else:
        "It's a few minutes before Bailey responds."
        a "{i}Well I don't{/i}"
        a "{i}And I'm actually pretty tired, so imma go bed{/i}"
        a "{i}Goodnight.{/i}"
        jump d1_b_home_end2

label d1_b_home_reset:
    menu:
        "\"Anyway, I had some really fun talks with some people today\"":
            $ b_friend += 5
            b "{i}Oh, sweet!{/i}"
            jump d1_b_home_newf
        "\"Anyway... I actually... I think I'm maybe interested in someone...\"":
            b "{i}Oh? Who is it? Do I know them? Tell meeeee{/i}"
            jump d1_b_home_psn
        "\"Nothing really interesting happened today\"":
            b "{i}RIP{/i}"
            jump d1_b_home_end

label d1_b_home_end:
    
    b "{i}Anyway, I'm kinda beat...{/i}"
    b "{i}I might head to bed now{/i}"
    
    if a_friend >= 20:
        b "{i}Love you, goodnighttttt xx {/i}"
    else:
        b "{i}Goodnight x{/i}"
    
    pl "{i}Goodnight!{/i}"

    jump d1_b_home_end2

label d1_b_home_end2:

    show bg bedroom n with fade
    stop music fadeout 5.0
    "Your day finally comes to an end."
    "You hop into bed, watch some videos on your phone, and eventually fall asleep."
    "You wonder what tomorrow will hold."

    jump d2_start
                    
label d2_b_work:
   
    scene bg cafe with fade
    play music "Lounge Lizard.mp3" loop
    "Work is busy for the first hour or so, but it flattens out pretty quickly." 
    "Tuesdays are never as bad as Mondays, which gives you ample time to chill out and chat with Angus and your other coworkers."

    show angus neutral at center

    pl "Hey, big guy!"

    a "Forgot my name already?"

    pl "Well, you just don't make much of an impression, Angus. What can I say?"

    show angus sad
    a "Wow, rude!"

    a "Guess I'll keep all these lollies to myself..."

    pl "Whoa whoa whoa. I didn't mean to cause any offence."
    show angus neutral
    a "And yet you did!"

    a "What a fairweather friend you are."

    menu:
        "\"Just a friend, huh?\"":
            jump d2b_work_friend
        "Don't say it":
            a "Anyway..."
            jump d2b_work_aq1

label d2b_work_friend:
    if a_friend >= 30:
        $ a_friend += 5
        show angus embarrassed
        a "W-well!"
        "Angus pauses for a moment, clearly flustered."
        a "I mean... I didn't mean to offend!"
        a "I... uh..."
        "You take pity on him, trying not to laugh too much."
        pl "How about those lollies?"
        a "Huh? Oh! Right! Them!!"
        show angus neutral
        jump d2b_work_aq1
    else:
        show angus embarrassed
        a "Er... haha, yep!"
        a "Just a friend!"
        a "Your good friend Angus...!"
        a "Ahem."
        show angus neutral
        a "Anyway uhhhh lollies!"
        jump d2b_work_aq1

label d2b_work_aq1:
    a "I've got snakes and cookies."

    pl "Cookies? Does that count as a lolly?"

    a "Hmm... technically not, but saying 'snakes and lollies' is a bit of a mouthful."

    a "I figured 'lollies' would communicate sweetness most efficiently."

    a "Also, don't tell anybody, but I'm trying to shift these snakes ASAP."

    pl "Since when are you inundated with snakes?"

    a "My mum came down recently, which is lovely, but..."
    show angus disgusted
    a "... I mean. You know, we don't talk much."
    show angus neutral
    a "She's trying though! Hence, the snakes."

    menu:
        pl "I'm almost afraid to ask, but..."
        "\"...Why do you still talk to your mother?\"":
            $ a_friend -= 10
            jump d2b_work_mother
        "\"...Are you okay?":
            $ a_friend += 10
            jump d2b_work_ok
        "\"...How many snakes?\"":
            $ a_friend += 5
            jump d2b_work_snakes

label d2b_work_mother:
    "Angus' face twitches." 
    show angus angry
    "For a second, he has a complicated, dark expression on, but then the moment passes and he's all bright again."
    show angus neutral

    a "Ah, well, you know. Family is family."
    a "What kind of a son would I be if I {i}didn't{/i} talk to her?"
    pl "I mean...I only ask because... well, you've mentioned in the past. That it's been difficult."
    pl "With her."
    show angus sad
    a "Mm..."
    a "Hey, [name], is it okay if we stop talking about this?"
    "You can tell by his tone of voice that it's not really a request."
    
    menu:
        "\"I just want to make sure you're okay\"":
            $ a_friend -= 5
            a "Then let's drop it."
            show angus neutral
            jump d2b_work_aq2
        "\"Sure.\"":
            a "Thank you."
            show angus neutral
            jump d2b_work_aq2
        "\"Why? I'm just curious.\"":
            $ a_friend -= 10
            show angus angry
            a "With all due respect, [name], my life isn't something for you to get 'curious' about."
            show angus neutral
            jump d2b_work_aq2
        "\"Why? Aren't we friends?\"":
            $ a_friend -= 10
            a "..."
            a "We're not talking about this anymore."
            show angus neutral
            jump d2b_work_aq2

label d2b_work_ok:
    "Angus' stance changes almost imperceptibly." 
    "He lets out a big swooshing breath."
    show angus sad
    a "Am I that obvious?"

    pl "Aw, buddy."

    a "Haha..."

    a "To be honest, I'm kind of freaking out."
    show angus neutral
    a "I love her, and it's great to see her - like, we don't usually see each other at {i}all{/i}, but..."
    a "She's trying so hard to be a mum, y'know?"
    show angus sad
    a "Even though I kind of don't need a mum anymore."
    a "I'm a full adult with my own adult problems."
    show angus angry
    a "And an adult stomach! That can't take a kid's amounts of lollies anymore!"
    show angus neutral
    a "I can tell she's trying to make up for lost time."
    a "But that's not really something you can do over a single weekend."
    
    pl "That makes a lot of sense."
    pl "I'm sorry, Angus. That's really stressful."
    pl "Even if she is trying her best, you shouldn't feel pressured to pretend to be comfortable around her."
    pl "It's okay if you need to take it a bit easier today, okay?"

    a "Thanks, [name]. I really appreciate it."
    jump d2b_work_aq2

label d2b_work_snakes:
    a "Hah- far too many for me to eat by myself."
    a "If I had known how many snakes Mum would be bringing over, I wouldn't have bothered baking cookies last night."
    a "I don't even like snakes that much!"
    
    pl "What's your best number estimate?"

    a "Hmmm..."
    a "Surely over a hundred."

    pl "Christ."

    show angus happy
    a "They've been a big hit with the customers, though!"
    a "Turns out passing out sweets indiscriminately endears a lot of people to you, who would've thought it?"
    
    "Angus points over to Bradley with a bashful grin on his face."
    show angus flirty
    a "Bradley's actually been helping me with a lot of them."

    a "He told me he loves sweet stuff! He took a whole bag off my hands."

    a "{i}And{/i} some of the cookies I brought from home."

    "You happen to know from Bailey that Bradley actually hates sweet things." 
    "You would tell Angus this, but you're realising that you don't have the heart for that."

    a "He's really lovely..."

    pl "He is, isn't he?"
    show angus neutral
    jump d2b_work_aq2

label d2b_work_aq2:
    a "Anyway, did you want anything?"

    menu:
        "\"I'll take some snakes\"":
            $ a_friend += 10
            show angus happy
            a "Oh thank God. Here ya go!"
            "Angus procures a handful of snakes from truly nowhere and hands them to you."
            pl "Hell yes. I'll snack on these through the rest of my shift."
            a "As is your god-given right."
            show angus neutral
            jump d2b_work_aq3
        "\"I'll take a cookie\"":
            $ a_friend += 5
            pl "Your cookies are awesome, there's no way I'm passing one up."
            show angus happy
            a "Aw thank you!"
            a "I hope you like chocolate chip..."
            pl "Of course I like chocolate chip!"
            pl "As far as I'm concerned, that's like, the default state of any cookie."
            show angus neutral
            a "Popular media would have to agree with you."
            jump d2b_work_aq3
        "\"No thanks, I don't like sweet food\"":
            show angus neutral
            a "No worries."
            a "I'll see if our manager wants something."
            jump d2b_work_aq3
        "\"No thanks, I don't like your cooking\"":
            $ a_friend -= 5
            show angus sad
            a "Oh..."
            a "Uh, sorry to hear that..."
            show angus disgusted
            a "(How unnecessarily rude...)"
            show angus neutral
            jump d2b_work_aq3

label d2b_work_aq3:
    "You and Angus chat for a little more."

    "At some point you can tell Angus' energy is starting to flag, so you subtly suggest that he goes to the bathroom for a bit."
    hide angus neutral

    "Gratefully, he agrees, leaving you to bring out some drinks."

    "There is a flat white, for Esme, and the same awful coffee order from yesterday, for Bradley." 
    "Gary isn't here today."

    menu:
        "Who will you serve first?"
        "Esme":
            $ d2_e1 = True
            jump d2_work_e
        "Bradley":
            jump d2b_work_br

label d2b_work_br:
    show bradley neutral
    "You swing by Bradley's table."

    "As opposed to yesterday, Bradley is focused solely on his phone, no leaning around or gawking to be had."

    pl "Hey, Bradley!"

    "You put down his drink, but he doesn't respond."

    menu:
        "Leave":
            "You guess Bradley isn't in a social mood today."
            hide bradley neutral
            if d2_e1 == True:
                jump d2_work_end
            else:
                jump d2_work_e
        "Ask if he has games on his phone":
            $ br_friend += 5
            pl "Got any games on that thing?"
            br "Hm? What?"
            br "Oh... games. No, I don't have any games."
            show bradley sad
            br "I tried to download them once, but I broke my phone doing it."
            show bradley neutral
            br "How are you, [name]?"
            pl "I'm fine..."
            jump d2b_work_br_aq1
        "Snap your fingers at him":
            $ br_friend += 5
            "You snap your fingers like you're a customer trying to get a waiter's attention."
            pl "Hey! Bradley! I'm talking to you here."
            br "Hm?"
            br "Oh! Hello there, [name]."
            br "I didn't notice you there."
            jump d2b_work_br_aq1
        "Ask if he wants anything else":
            pl "Anything else I can get you?"
            "Still nothing. Bradley remains fixated on his phone."
            "You're about to leave when he blinks out of his reverie and focuses on you."
            br "Hm?"
            br "Oh, hello, [name]."
            br "Thank you for the drink."
            jump d2b_work_br_aq1

label d2b_work_br_aq1:
    pl "You seem a bit distracted today. Everything okay?"

    br " Well... if you really must know, this may be the most important day of my life."

    br "So my current personal state is hovering somewhere between 'life-changingly joyous' and 'I want to crawl into a hole and die'."

    br "..."
    show bradley embarrassed
    br "... I'm thinking of asking Angus out today."

    pl "Oh, no way! That {i}is{/i}, um... exciting?"

    br "If you want to be massively reductive about it, yes."

    "Bradley gestures with his phone at you."

    br "I've been reading up on some 'tips' and 'tricks' regarding asking someone out."
    show bradley neutral
    br "Hence the focus. Sorry for not answering you immediately before."

    "You take a glance at his phone." 
    "The title of the page Bradley is currently on reads, 'Top 10 Ways to Ask Out Your Crush (For Girls!!!)'."

    menu:
        "\"This article doesn't look very helpful...\"":
            $ br_friend += 5
            show bradley sad
            br "It's not!"
            show bradley neutral
            jump d2b_work_br_aq2
        "\"This article looks great!\"":
            $ br_friend -= 5
            "Bradley looks back at his phone with a wrinkled nose."
            show bradley disgusted
            br "It's not."
            br "It's really, really not."
            show bradley neutral
            jump d2b_work_br_aq2

label d2b_work_br_aq2:
    "Bradley closes the tab with a sigh."

    br "You know what? Now that you're here, you might actually be able to help me out."

    br "You see, I actually feel quite confident doing the asking out part."

    br "That's easy. Been there, done that. It's child's play, really."

    br "But I just don't know {i}to what event{/i} I should ask Angus out."

    br "Should we go to the beach? The movies?"

    br "Maybe we can have a lunch date, or an evening date, or a breakfast date."
    show bradley shocked
    br "There's too many options! What am I meant to do?"

    pl "Can't you ask Bailey?"
    show bradley disgusted
    br "Haha. Ha. Ha."

    br "Aren't you just a regular comedian?"
    show bradley neutral
    br "In many ways, I am asking Bailey. You're dating her, after all."

    br "{i}And{/i} in many other ways, I'm asking Angus as well! You work together, you probably know all about each other."

    pl "I'll be honest, Bradley, it sounds like you have a bit of a misunderstanding as to what being someone's partner slash coworker means..."

    br "Nonsense!"

    "He leans forward, his eyes bright."

    show bradley happy

    br "How about it, [name]? Where do you think I should take Angus on a date?"

    br "... provided he says yes, of course!"
    show bradley neutral

    menu:
        "The beach":
            $ br_friend -= 5
            br "Hm... don't you think that's a little cliche?"
            show bradley disgusted
            br "(And sandy... eugh... I hate sand.)"
            show bradley neutral
            br "Ooh, but then again maybe Angus would like a classic location."
            pl "Yeah, who doesn't love the beach?"
            pl "It's serene and romantic, especially if you go in the early morning or during sunset."
            "Bradley doesn't seem convinced."
            br "I'll think about it."
            jump d2a_work_br_aq3
        "The movies":
            pl "Angus loves movies. You can't go wrong there."
            pl "Just make sure to go to one he'll really like. Something arthouse."
            pl "Or you can go to one he'll really hate... he likes complaining about movies, too."
            br "I'm not a big fan of movies, personally."
            br "They lack a certain charm, don't you think?"
            br "Still, if Angus likes them, perhaps it'll be worth it..."
            jump d2a_work_br_aq3
        "A restaurant":
            $ br_friend += 5
            pl "A fancy dinner at a fancy restaurant could be fun."
            show bradley happy
            br "Ooh, YES!"
            br "Yes yes yes! That sounds excellent to me."
            br "I've got a list of restaurants I've been meaning to visit - what a good idea!"
            "You get the sense that Bradley is probably going to want to go to a restaurant much more than Angus will."
            "Welp... too late to take it back now."
            show bradley neutral
            jump d2a_work_br_aq3
        "A cafe":
            pl "You can get some light cafe food, then maybe go for a walk afterwards."
            pl "You seem like you'd be big on brunch."
            show bradley happy
            br "I am indeed - how did you know??"
            show bradley neutral
            br " Ah, but won't going to a cafe be a bit too close to work for Angus?"
            "Whoops. You didn't think about that."
            pl "Maybe he won't mind? I enjoy going to cafes even though I work at one."
            "(Though you can't lie, the charm of cafes did die down a bit for you after you got this job...)"
            br "Hmm... maybe so."
            jump d2a_work_br_aq3

label d2a_work_br_aq3:
    br "Thanks for your input, [name]."
    pl "Yeah, no worries. I'm not sure how helpful I was, haha."
    br "Oh, nonsense. You're helpful."
    show bradley happy
    br "You're quite helpful, actually. You bring me my drinks!"
    "You think about pointing out that this is not an ability unique to you, but Bradley is smiling too confidently for you to do so."
    pl "Any time, Bradley."
    pl "You sure you don't want something else?"
    show bradley neutral
    br "Oh, I'm sure."
    br "Maybe just some luck, if you could spare it?"
    br "Just kidding! I think I'll be fine."
    "In that moment, Bradley's smile reminds you suddenly of Bailey. He waves you off, and you return back to work."
    hide bradley neutral

    if d2_e1 == True:
        jump d2_work_end
    else:
        jump d2_work_e

label d2b_home:
    menu:
        "Answer":
            jump d2b_home_ans
        "Don't answer":
            jump d2b_home_noans
    
label d2b_home_ans:
    b "[name]! All my meetings are done for the day, so I thought I'd give you a call!"
    
    menu:
        "\"I'm glad you did!\"":
            $ b_friend += 5
            "You can practically hear Bailey smile on the other side of the phone."
            jump d2b_home_ans_aq1
        "\"I would have preferred some warning\"":
            b "Oh, right... Sorry, I probably should have texted first."
            b "I was just excited."
            jump d2b_home_ans_aq1

label d2b_home_ans_aq1:
    b "Anyway, how was your day?"
    
    menu:
        "\"It was okay\"":
            menu:
                "\"I miss you\"":
                    $ b_friend += 5
                    b "Aw, I miss you too! Can't wait to be home."
                    jump d2b_home_ans_aq2
                "\"Not much really happened\"":
                    b "Fair enough. Same here, really."
                    jump d2b_home_ans_aq2
                "\"How was your day?\"":
                    $ b_friend += 10
                    b "Dodging the question, I see!" 
                    b "But my day was ok- thanks for asking. Not much really happened, just a bunch of team activities and things. Which was sorta fun? But sorta weird too."
                    jump d2b_home_ans_aq2
        "\"It was good!\"":
            b "Aw hell yeah! What happened?"
            menu:
                "\"Not much really\"":
                    b "Fair enough. Same here."
                    jump d2b_home_ans_aq2
                "\"A lot!\" (Tell Bailey about your day)":
                    $ b_friend += 10
                    b "Wow! Sounds like a big day. Lots of fun."
                    jump d2b_home_ans_aq2
                "\"First, I want to know about your day\"":
                    $ b_friend += 5
                    b "Oh, well not much really happened! It was just a lot of various team activities and stuff like that." 
                    b "Which was sorta fun? I do love to talk... but I always find those activities kinda weird, too."
                    jump d2b_home_ans_aq2
        "\"Pretty bad, to be honest\"":
            b "Oh, that sucks! Anything I can do to help?"
            menu:
                "\"Don't think so\"":
                    b "Damn. I'm sorry, anyway."
                    jump d2b_home_ans_aq2
                "\"We could talk about the polyamory thing?\"":
                    $ b_friend -= 10
                    b "..."
                    b "Look, as much as I want to help you..."
                    b "Just, other than that, I mean."
                    jump d2b_home_ans_aq2
                "\"Talking to you is already helping\"":
                    $ b_friend += 10
                    b "Ooh we've got a charmer here... But I'm glad!"
                    jump d2a_home_ans_aq2

label d2b_home_ans_aq2:
    if crush == "no one":
        b "Anyway, you've been talking to a lot of people. Has anyone... caught your eye?"
        jump d2b_home_ans_pique
    else:
        b "Anyway, how is it going with [crush]?"
        if crush == "Morgan" or "Pedro" or "Gary":
            pl "Well, we didn't talk today, so nothing really to report there."
            b "I see... well, is anyone else piquing your interest?"
            jump d2b_home_ans_pique
        else:
            menu:
                "\"Good!\"":
                    b "Glad to hear it!"
                    b "So, you're gonna ask them out then?"
                    jump d2b_home_ans_ask
                "\"Idk... I think maybe I'm losing interest?\"":
                    b "Ah, yeah, fair enough. Love's a fickle mistress..."
                    b "Well, is anyone else piquing your interest?"
                    jump d2b_home_ans_pique
                "\"Terribly!":
                    b "Oh no!!"
                    b "You should ask them out anyway. Will you?"
                    jump d2b_home_ans_ask
                "\"Okay I guess? Hard to tell\"":
                    b "That's fair enough."
                    b "One way of finding out is to ask them out. Will you?"
                    jump d2b_home_ans_ask

label d2b_home_ans_pique:
    menu:
        "\"No\"":
            $ crush = "no one"
            b "Fair enough!"
            jump d2b_home_ans_ppl
        "\"Yes\"":
            b "Oh, who?"
            menu:
                "Angus":
                    if crush == "Angus":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking him out?"
                        jump d2b_home_ans_ask
                    else:
                        $ crush = "Angus"
                        b "Your coworker? Nice!"
                        b "Are you thinking of asking him out?"
                        jump d2b_home_ans_ask
                "Bradley":
                    if crush == "Bradley":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking him out?"
                        jump d2b_home_ans_ask
                    else:
                        $ crush = "Bradley"
                        b "My brother?"
                        b "Gross gross gross!"
                        b "Also, he's just. Not gonna be interested, sorry babe. He's, like, soooo in love with Angus, and is super monogamous."
                        b "Don't ask him out."
                        jump d2b_home_ans_ppl
                "Gary":
                    if crush == "Gary":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking him out?"
                        jump d2b_home_ans_ppl
                    else:
                        $ crush = "Gary"
                        b "My crush Gary?"
                        b "Competition..."
                        b "Like, for real, he's super monogamous, so only one of us has a shot."
                        b "And I intend for that to be me."
                        jump d2b_home_ans_ppl
                "Esme":
                    if crush == "Esme":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking her out?"
                        jump d2b_home_ans_ask
                    else:
                        $ crush = "Esme"
                        b "Esme?"
                        b "Oh, right! Gary's friend..."
                        b "She's super weird. I like him."
                        b "And, hey, good luck!"
                        b "Are you thinking of asking him out?"
                        jump d2b_home_ans_ask
                "Morgan":
                    if crush == "Morgan":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking her out?"
                        jump d2b_home_ans_ask
                    else:
                        $ crush = "Morgan"
                        b "Your classmate, right? Good luck!"
                        b "Are you thinking of asking her out?"
                        jump d2b_home_ans_ask
                "Pedro":
                    if crush == "Pedro":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking him out?"
                        jump d2b_home_ans_ask
                    else:
                        $ crush = "Pedro"
                        b "Your classmate, right? Good luck!"
                        b "Are you thinking of asking him out?"
                        jump d2b_home_ans_ask
                "April":
                    if crush == "April":
                        b "Isn't that who you just said you're losing interest in?"
                        b "A real ping pong ball of a time with you, eh?"
                        b "Anyway, are you thinking of asking them out?"
                        jump d2b_home_ans_ask
                    else:
                        $ crush = "April"
                        b "Oh! From the post office? Good luck!"
                        b "Are you thinking of asking them out?"
                        jump d2b_home_ans_ask
                "Multiple people":
                    $ crush = "Everyone"
                    b "Aw hell yeah! Good luck!"
                    b "Are you thinking of asking them out?"
                    jump d2b_home_ans_ask

label d2b_home_ans_ask:
    menu:
        "\"No\"":
            b "Oh boo. Why not?"
            menu:
                "\"Not brave enough\"":
                    b "Haha, okay then, coward."
                    b "I'm just kidding. You know I'm the same..."
                    jump d2b_home_ans_ppl
                "\"[crush] will say no!\"":
                    b "Why? You're some hot stuff!"
                    b "And I'm not biased at all..."
                    jump d2b_home_ans_ppl
                "\"They should ask me\"":
                    b "Pfft. Okay, then, Your Royal Highness..."
                    jump d2b_home_ans_ppl
                "\"I'm with you - that would be cheating!\"":
                    $ a_friend -= 5
                    b "..."
                    b "No, it wouldn't?"
                    jump d2b_home_ans_ppl
        "\"I don't know yet\"":
            b "That's fair enough - take your time!"
            jump d2b_home_ans_ppl
        "\"Yes!\"":
            b "Oooh, so exciting!"
            b "Good luck!"
            jump d2b_home_ans_ppl

label d2b_home_ans_ppl:
    stop music fadeout 3.0   
    
    b "..."
    pl "..."

    menu:
        "\"Hey... So, I was wondering, would it be okay for me to see other people?\"":
            $ b_friend += 5
            $ cppl = True
            b "Oh!"
            b "Well, yeah. I mean, if you want to, of course."
            b "Like, duh, sorta..."
            b "I mean, thanks."
            b "For bringing it up."
            b "It's exciting that you're thinking of seeing other people!"
            jump d2b_home_ans_end
        "Don't mention it":
            jump d2b_home_ans_end

label d2b_home_ans_end:
    play music "Tranquilize.mp3" loop
    "You and Bailey talk for a little bit longer, but you start to get tired."

    menu:
        "Say goodnight now":
            "The two of you say goodnight, and you head to bed."
            scene bg bedroom n with fade
            "You wonder what tomorrow will hold."
            jump d3_start
        "Keep chatting just a bit longer":
            $ b_friend += 5
            "You keep chatting for around 10 minutes before you say goodnight."
            scene bg bedroom n with fade
            "You head to bed, sleepily brushing your teeth and getting changed first."
            "When your head hits the pillow, you're out like a light."
            "You wonder what tomorrow will hold."
            jump d3_start
        "I'm not tired! Keep talking for HOURS!!!":
            $ b_friend += 10
            scene bg bedroom n with fade
            "The two of you chat for hours and hours, and you eventually head to your bedroom at some point. When you talk to Bailey, it's like time ceases to exist."
            "You don't know when it happens, exactly, but at some point you fall asleep to the sound of her voice."
            jump d3_start


label d2b_home_noans:
    "You ignore the phone call. You're not in the mood, or you're too tired, or too angry."
    "Either way, you start mindlessly scrolling on your phone."
    if b_friend >= 20:
        "Eventually, you receive a text."
        b "{i}Gonna sleep. Thinking of you xx Goodnight{/i}"
        scene bg bedroom n with fade
        "You get ready for bed."
        jump d2b_home_noans_aq1
    else:
        "You do not receive any follow up texts."
        scene bg bedroom n with fade
        "Eventually, you get ready for bed. Something sits in your gut, a little uncomfortable, but you can't quite put your finger on what."
        jump d2b_home_noans_aq1

label d2b_home_noans_aq1:
    "You lie in bed, sleepless, for what feels like hours. You check your phone, and find it's only been half an hour."
    "In your head, you start to complain about how hard you're finding it to sleep."
    "But before you know it, you're deep in the thralls of some shapeless dream."
    jump d3_start


label d3_home_b:    
    b "{i}Hey [name], I'm done with work for the day!! Feeling beat as hell, so I might go to bed soon, but I wanted to text u at least once before I sleep{/i}"

    b "{i}How was ur day?{/i}"

    menu:
        "Great!":
            b "{i}Hell yeah! Do you want to tell me about it?{/i}"
            menu:
                "Yeah (tell her about your day)":
                    if m_hang == True:
                        $ b_friend += 5
                        b "{i}Ooh fun! Especially cool about Morgan- gotta give me more details later{/i}"
                        b "{i} I'm glad to see you're trying new things{/i}"
                        jump d3_home_b_aq1
                    else:
                        a "{i}Oooh fun! Glad you had a good day{/i}"
                        jump d3_home_b_aq1
                "Nah (don't tell her)":
                    b "{i}Fair nuff! Glad it was good, though{/i}"
                    jump d3_home_b_aq1
        "It was okay":
            b "{i}Anything you wanna talk about?{/i}"
            menu:
                "Yeah (tell her about your day)":
                    if m_hang == True:
                        $ b_friend += 5
                        b "{i}Oh, interesting. Especially cool about Morgan. Even if it didn't work out exactly how you wanted, I'm glad to see you trying new things a bit{/i}"
                        jump d3_home_b_aq1
                    else:
                        b "{i}Oh interesting. Glad ur day was ok, but sorry it wasn't better{/i}"
                        jump d3_home_b_aq1
                "Nah (don't tell her)":
                    b "{i}Fair enough! Glad it wasn't a bad day, at least{/i}"
                    jump d3_home_b_aq1
        "Kinda bad":
            b "{i}Oh, I'm sorry to hear that :( Anything you wanna talk about?{/i}"
            menu:
                "Yeah (tell her about your day)":
                    if m_hang == True:
                        $ b_friend += 5
                        b "{i}Oh, that's a shame. But about Morgan... even if it didn't work out how you wanted, I'm glad to see you trying new things a bit{/i}"
                        jump d3_home_b_aq1
                    else:
                        b "{i}Oh that's a shame. Sorry your day was so shit{/i}"
                        jump d3_home_b_aq1
                "Nah (don't tell her)":
                    b "{i}Fair enough! Sorry your day was so bad though{/i}"
                    jump d3_home_b_aq1
label d3_home_b_aq1:
    b "{i}Anyway, I am soooo tired and I gotta get up early tomorrow, so imma go sleep{/i}"

    b "{i}I'll text you in the morning!{/i}"

    b "{i}Goodnight!{/i}"

    pl "{i}Goodnight!{/i}"

    "You should probably head to bed now, too."

    "You don't have anything on in particular, other than wanting to check for your parcel at the post office..."

    "But still, who knows what the day could hold?"

    jump d3_end_sleep



# this ends the game
    return
