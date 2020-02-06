from sys import exit
import random
from textwrap import dedent


class Engine(object):
    def __init__(self, chapter):
        self.chapter = chapter

    def go(self):
        chapter_now = self.chapter.beginning()
        chapter_end = self.chapter.chapter_now('concert')

        while chapter_now != chapter_end:
            next_chapter = chapter_now.play()
            chapter_now = self.chapter.chapter_now(next_chapter)


class Chapter(object):

    def play(self):
        print("Lets just try and get to the show, dude")

    def line(self):
        print('*' * 30)


class WinTickets(Chapter):

    tickets = ["""
               You put an add on craigslist.... withing minutes someone responds.
               Excitedly, you rush to meet them.... only to get knocked out and robbed.
               Don't be such a dumbass.""",
               "Well you're absolutely no fun...... why did you even bother playing at all??",
               "There is no point to this game if you value money over expieriences, pal"]

    def play(self):
        print(dedent("""
            'Caller 2,465 ......... the tickets are yours!!!!!!!'
            Finally, having no life is defnately paying off.

            But the rent is due.......

            Should you sell, or should you go????"""))

        choice = input('what do you do? go or sell?')
        if choice == 'sell':
            print('*' * 30)
            print(WinTickets.tickets[random.randint(0, 2)])
            print('*' * 30)
            print('*' * 30)
            exit(1)
        else:
            print('*' * 30)
            print(dedent("""
                         HELL YEAH WERE GOING TO ROCK OUT

                         not even a question.
                         better get to the bar, friend, and find someone to drive your ass there!!"""))
            return 'bar'


class Bar(Chapter):

    oof = ["""Why am I so cold?... you ask yourself as you slowly come too....
           floating in a tub of ice... Why does my side hurt? Where are my clothes????
           You look down, and see the sutures accross your abdomin.....MY MOTHER F_ING KIDNEY!!!""",
           """What time is it?? Your head is pounding, its pitch black, and something smells awful.
           Fumbling, you feel around, and realize youre in some sort of padded cell.
           The hall lights ouside the door come on, illumnating the room.
           You wish it would not have. UnSaNiTaRy. Looking through the porthole sized window in the door,
           you can read a small sign....
           ARKHAM INSANE ASYLUM.....................well fuck.""",
           """'JUST VAT DO YOU TINK YOU'RE DOINGK?!?!?!?'
           You look over your shoulder...... the rest of the bar has been completely blocked by some giant mass.....
           like a wall. You trace the outline and realize..... That's no wall. THATS A MAN!!!
           Katia snickers.... 'Oh, Ivan, this guy was givingk me such a hardt time!'
           ......Right before you feel your spirit leave your body.....
           you regret every life decision up until this point"""]

    def play(self):
        print('*' * 30)
        print(dedent("""
                      You head over to the local watering hole.

                      This place is crowded...... yuck.
                      Thank GOD Kate's working behind the bar. She's totally awesome and would
                      LOVE to go rock the f out.... and she drives. The perfect person to ask. She'll be getting
                      done soon, too, so tha-

                      WOAH. Wait a minute. There's a really hot chick at the back corner table.
                      And DUDE.... im pretty sure she's making eye contact.

                      (you look around just to make sure)

                      Yup. Definately looking at you.

                      Now what's the play, man?? Ask Kate to go to the concert... or take your
                      chances with 'Katia'?"""))
        choice = input('Who are you going to ask? Katia or Kate?')
        if choice == 'kate' or choice == 'Kate':
            print(dedent("""
                        Walking towards the bar, you obviously shrug off Katia's stare.

                        You've heard stories about these women.......

                        Waking up in a bathtub of ice with a kidney missing doesn't sound like a good time.

                        """))
            return 'havedrink'
        else:
            print('*' * 30)
            print(dedent("""
                         COULD ANYONE BLAME YOU?!?!?!

                         I mean, just look at this woman.

                         You sit down beside Katia, and happily accept the drink(s) she starts putting
                         in front of you.......
                         """))
            print(Bar.oof[random.randint(0, 2)])
            print('*' * 30)
            print('*' * 30)
            exit(1)


class HaveDrink(Chapter):

    def play(self):
        print('*' * 30)
        print(dedent("""
                     Kate's definately the wiser choice.....
                     Messing with girls like Katia will have you regretting all yur life decisions.

                     You slide up and lay the tickes on the bar, waving Kate over.
                     DUDE!!!!!!! F**K YEAH IM DOWN!!!!

                     I'll be outta here in no time.... you wanna chill and have a drink before we go?
                     Or do you just wanna get going right away??
                     """))
        choice = input('have a drink? yes or no?')
        if choice == 'yes':
            print('*' * 30)
            print(dedent("""
                     You pull up a barstool and wait for Kate to come around.
                     The bartender comes over with a drink...."Someone bought this for you."

                     WELL SHIT, TODAY IS MY LUCKY DAY!!!!Without even hesitating... you take a huge sip.

                     Crap.The room starts to spin.
                     As the lights begin to fade.... you see a figure approach. KATIA.
                     Goodnight, friend..... she whisperes.

                     ....................................................

                     You come too in the front seat of Katie's car. YET AGAIN, she's done you a solid.SAVED YOUR LIFE.
                     She kicked Katia's ass and got you on the road to the concert.

                     NEVER UNDERESTIMATE A GOOD BARTENDER!"""))
            return 'inline'
        else:
            print('*' * 30)
            print(dedent("""
                    Kate grabs her keys and heads for the door, dragging you along.

                    LATER, FREAKS!!!!

                    and you're off"""))
            return 'inline'


class InLine(Chapter):

    trip = ["Have you ever heard colors??? Well, you're about too...",
            "Ummm..... Kate, why is your face melting?",
            "I AM A GOLDEN GOD!!!!!"]

    def play(self):
        print('*' * 30)
        print(dedent("""

                     You pull up outside the venue, where the line to get in has wrapped around the block.
                     Making yur way to the VIP line, you and Kate cant help but notice all the FREAKS on parade.

                     One dodgy looking dude is making his way up the line.... he looks like Dr. Seuss and Ursula the Sea Witch had a baby.
                     He finally makes it to you... as he stands infront of you, he pulls a small bag from his pocket.

                     LOOKING TO EXPAND YOUR MIND, MAN?????
                     He asks as he waves the baggie.....

                     Well, do you??"""))
        choice = input('feel like tripping the light fantastic? yes, or no?')
        if choice == 'yes':
            print('*' * 30)
            print(InLine.trip[random.randint(0, 2)])
            print(dedent("""

                         You wake up two days later, covered in blue paint, and 3 states over.

                         DON'T DO THE MYSTERY WEEDS, KIDS"""))
            print('*' * 30)
            print('*' * 30)
            exit(1)
        else:
            print('*' * 30)
            print("JUST SAY NO TO THE MYSTERY WEEDS, MAN!!!!!!!!")
            return 'concert'


class Concert(Chapter):

    def play(self):
        print('*' * 30)
        print('*' * 30)
        print('*' * 30)
        print(dedent("""

                     HELLS TO THE FRICKING YEAH!!!!!!!

                     You made it in.... Kate pushed you through to the front....
                     And you totally got your ass kicked in the pit.



                     ABSOLUTELY RIGHTEOUS"""))


class Contents(object):

    chapters = {'wintickets': WinTickets(), 'bar': Bar(
    ), 'havedrink': HaveDrink(), 'inline': InLine(), 'concert': Concert()}

    def __init__(self, chapter_1):
        self.chapter_1 = chapter_1

    def chapter_now(self, chapt):
        place = Contents.chapters.get(chapt)
        return place

    def beginning(self):
        return self.chapter_now(self.chapter_1)
