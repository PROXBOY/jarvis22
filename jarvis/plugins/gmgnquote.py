# Edited by @Smart_S54
# thanks for helping @jisan7509
"""
Good Morning and Good Night Plugin
by @Smart_S54
command .gdm and .gdn
"""


import asyncio
import random

##from jarvis.utils import **j_cmd, edit_or_reply, sudo_cmd


@jarvis.on(j_cmd(pattern=f"gdm", outgoing=True))
@jarvis.on(sudo_cmd(pattern=f"gdm", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    await edit_or_reply(event, "Typing...")

    await asyncio.sleep(2)

    x = random.randrange(1, 35)

    if x == 1:
        await event.edit(
            '`"π₯° Life is full of uncertainties. But there will always be a sunrise after every sunset. Good morning! π"`'
        )

    if x == 2:
        await event.edit(
            '`"π₯° It doesnΓ’ΒΒt matter how bad was your yesterday. Today, you are going to make it a good one. Wishing you a good morning! π"`'
        )

    if x == 3:
        await event.edit(
            '`"π₯° If you want to gain health and beauty, you should wake up early. Good morning! π"`'
        )

    if x == 4:
        await event.edit(
            '`"π₯° May this morning offer you new hope for life! May you be happy and enjoy every moment of it. Good morning! π"`'
        )

    if x == 5:
        await event.edit(
            '`"π₯° May the sun shower you with blessings and prosperity in the days ahead. Good morning. π"`'
        )

    if x == 6:
        await event.edit(
            '`"π₯° Every sunrise marks the rise of life over death, hope over despair and happiness over suffering. Wishing you a very enjoyable morning today! π"`'
        )

    if x == 7:
        await event.edit(
            '`"π₯° Wake up and make yourself a part of this beautiful morning. A beautiful world is waiting outside your door. Have an enjoyable time! π"`'
        )

    if x == 8:
        await event.edit(
            '`"π₯° Welcome this beautiful morning with a smile on your face. I hope youΓ’ΒΒll have a great day today. Wishing you a very good morning! π"`'
        )

    if x == 9:
        await event.edit(
            '`"π₯° You have been blessed with yet another day. What a wonderful way of welcoming the blessing with such a beautiful morning! Good morning to you! π"`'
        )

    if x == 10:
        await event.edit(
            '`"π₯° Waking up in such a beautiful morning is a guaranty for a day thatΓ’ΒΒs beyond amazing. I hope youΓ’ΒΒll make the best of it. Good morning! π"`'
        )

    if x == 11:
        await event.edit(
            '`"π₯° Nothing is more refreshing than a beautiful morning that calms your mind and gives you reasons to smile. Good morning! Wishing you a great day. π"`'
        )

    if x == 12:
        await event.edit(
            '`"π₯° Another day has just started. Welcome the blessings of this beautiful morning. Rise and shine like you always do. Wishing you a wonderful morning! π"`'
        )

    if x == 13:
        await event.edit(
            '`"π₯° Wake up like the sun every morning and light up the world your awesomeness. You have so many great things to achieve today. Good morning! π"`'
        )

    if x == 14:
        await event.edit(
            '`"π₯° A new day has come with so many new opportunities for you. Grab them all and make the best out of your day. HereΓ’ΒΒs me wishing you a good morning! π"`'
        )

    if x == 15:
        await event.edit(
            '`"π₯° The darkness of night has ended. A new sun is up there to guide you towards a life so bright and blissful. Good morning dear! π"`'
        )

    if x == 16:
        await event.edit(
            '`"π₯° Wake up, have your cup of morning tea and let the morning wind freshen you up like a happiness pill. Wishing you a good morning and a good day ahead! π"`'
        )

    if x == 17:
        await event.edit(
            '`"π₯° Sunrises are the best; enjoy a cup of coffee or tea with yourself because this day is yours, good morning! Have a wonderful day ahead. π"`'
        )

    if x == 18:
        await event.edit(
            '`"π₯° A bad day will always have a good morning, hope all your worries are gone and everything you wish could find a place. Good morning! π"`'
        )

    if x == 19:
        await event.edit(
            '`"π₯° A great end may not be decided but a good creative beginning can be planned and achieved. Good morning, have a productive day! π"`'
        )

    if x == 20:
        await event.edit(
            '`"π₯° Having a sweet morning, a cup of coffee, a day with your loved ones is what sets your Γ’ΒΒGood MorningΓ’ΒΒ have a nice day! π"`'
        )

    if x == 21:
        await event.edit(
            '`"π₯° Anything can go wrong in the day but the morning has to be beautiful, so I am making sure your morning starts beautiful. Good morning! π"`'
        )

    if x == 22:
        await event.edit(
            '`"π₯° Open your eyes with a smile, pray and thank god that you are waking up to a new beginning. Good morning! π"`'
        )

    if x == 23:
        await event.edit(
            '`"π₯° Morning is not only sunrise but A Beautiful Miracle of God that defeats the darkness and spread light. Good Morning. π"`'
        )

    if x == 24:
        await event.edit(
            '`"π₯° Life never gives you a second chance. So, enjoy every bit of it. Why not start with this beautiful morning. Good Morning! π"`'
        )

    if x == 25:
        await event.edit(
            '`"π₯° If you want to gain health and beauty, you should wake up early. Good Morning! π"`'
        )

    if x == 26:
        await event.edit(
            '`"π₯° Birds are singing sweet melodies and a gentle breeze is blowing through the trees, what a perfect morning to wake you up. Good morning! π"`'
        )

    if x == 27:
        await event.edit(
            '`"π₯° This morning is so relaxing and beautiful that I really donΓ’ΒΒt want you to miss it in any way. So, wake up dear friend. A hearty good morning to you! π"`'
        )

    if x == 28:
        await event.edit(
            '`"π₯° Mornings come with a blank canvas. Paint it as you like and call it a day. Wake up now and start creating your perfect day. Good morning! π"`'
        )

    if x == 29:
        await event.edit(
            '`"π₯° Every morning brings you new hopes and new opportunities. DonΓ’ΒΒt miss any one of them while youΓ’ΒΒre sleeping. Good morning! π"`'
        )

    if x == 30:
        await event.edit(
            '`"π₯° Start your day with solid determination and great attitude. YouΓ’ΒΒre going to have a good day today. Good morning my friend! π"`'
        )

    if x == 31:
        await event.edit(
            '`"π₯° Friendship is what makes life worth living. I want to thank you for being such a special friend of mine. Good morning to you! π"`'
        )

    if x == 32:
        await event.edit(
            '`"π₯° A friend like you is pretty hard to come by in life. I must consider myself lucky enough to have you. Good morning. Wish you an amazing day ahead! π"`'
        )

    if x == 33:
        await event.edit(
            '`"π₯° The more you count yourself as blessed, the more blessed you will be. Thank God for this beautiful morning and let friendship and love prevail this morning. π"`'
        )

    if x == 34:
        await event.edit(
            '`"π₯° Wake up and sip a cup of loving friendship. Eat your heart out from a plate of hope. To top it up, a fork full of kindness and love. Enough for a happy good morning! π"`'
        )

    if x == 35:
        await event.edit(
            '`"π₯° It is easy to imagine the world coming to an end. But it is difficult to imagine spending a day without my friends. Good morning. π"`'
        )


# GDNIGHT messages starts from here.....


@jarvis.on(j_cmd(pattern=f"gdn", outgoing=True))
@jarvis.on(sudo_cmd(pattern=f"gdn", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    await edit_or_reply(event, "Typing...")

    await asyncio.sleep(2)

    x = random.randrange(36, 67)

    if x == 36:
        await event.edit('`"π₯° Good night keep your dreams alive. π"`')

    if x == 37:
        await event.edit('`"π₯° Night, night, to a dear friend! May you sleep well! π"`')

    if x == 38:
        await event.edit(
            '`"π₯° May the night fill with stars for you. May counting every one, give you contentment! π"`'
        )

    if x == 39:
        await event.edit(
            '`"π₯° ishing you comfort, happiness, and a good nightβs sleep π"`'
        )

    if x == 40:
        await event.edit(
            '`"π₯° Now relax. The day is over. You did your best. And tomorrow youβll do better. Good Night! π"`'
        )

    if x == 41:
        await event.edit(
            '`"π₯° Good night to a friend who is the best! Get your forty winks! π"`'
        )

    if x == 42:
        await event.edit('`"π₯° Rest soundly tonight, friend! π"`')

    if x == 43:
        await event.edit('`"π₯° Have the best nightβs sleep, friend! Sleep well!. π"`')

    if x == 44:
        await event.edit('`"π₯° Have a very, good night, friend! You are wonderful!. π"`')

    if x == 45:
        await event.edit('`"π₯° YRelaxation is in order for you! Good night, friend! π"`')

    if x == 46:
        await event.edit('`"π₯° Good night. May you have sweet dreams tonight. π"`')

    if x == 47:
        await event.edit(
            '`"π₯° As we wait for a brand new day, good night and have beautiful dreams. π"`'
        )

    if x == 48:
        await event.edit(
            '`"π₯° Dear friend, I wish you a night of peace and bliss. Good night. π"`'
        )

    if x == 49:
        await event.edit(
            '`"π₯° Darkness cannot last forever. Keep the hope alive. Good night. π"`'
        )

    if x == 50:
        await event.edit(
            '`"π₯° By hook or crook you shall have sweet dreams tonight. Have a good night, buddy! π"`'
        )

    if x == 51:
        await event.edit(
            '`"π₯° Good night, my friend. I pray that the good Lord watches over you as you sleep. Sweet dreams. π"`'
        )

    if x == 52:
        await event.edit(
            '`"π₯° Good night, friend! May you be filled with tranquility! π"`'
        )

    if x == 53:
        await event.edit('`"π₯° Wishing you a calm night, friend! I hope it is good! π"`')

    if x == 54:
        await event.edit(
            '`"π₯° Wishing you a night where you can recharge for tomorrow! π"`'
        )

    if x == 55:
        await event.edit(
            '`"π₯° Slumber tonight, good friend, and feel well rested, tomorrow! π"`'
        )

    if x == 56:
        await event.edit(
            '`"π₯° Wishing my good friend relief from a hard dayβs work! Good Night!Good π"`'
        )

    if x == 57:
        await event.edit('`"π₯° Good night, friend! May you have silence for sleep! π"`')

    if x == 58:
        await event.edit(
            '`"π₯° Sleep tonight, friend and be well! Know that you have done your very best today, and that you will do your very best, tomorrow! π"`'
        )

    if x == 59:
        await event.edit(
            '`"π₯° Friend, you do not hesitate to get things done! Take tonight to relax and do more, tomorrow π"`'
        )

    if x == 60:
        await event.edit(
            '`"π₯° Friend, I want to remind you that your strong mind has brought you peace, before. May it do that again, tonight! May you hold acknowledgment of this with you! π"`'
        )

    if x == 61:
        await event.edit(
            '`"π₯° Wishing you a calm, night, friend! Hoping everything winds down to your liking and that the following day meets your standards! π"`'
        )

    if x == 62:
        await event.edit(
            '`"π₯° May the darkness of the night cloak you in a sleep that is sound and good! Dear friend, may this feeling carry you through the next day! π"`'
        )

    if x == 63:
        await event.edit(
            '`"π₯° Friend, may the quietude you experience tonight move you to have many more nights like it! May you find your peace and hold on to it! π"`'
        )

    if x == 64:
        await event.edit(
            '`"π₯° May there be no activity for you tonight, friend! May the rest that you have coming to you arrive swiftly! May the activity that you do tomorrow match your pace and be all of your own making! π"`'
        )

    if x == 65:
        await event.edit(
            '`"π₯° When the day is done, friend, may you know that you have done well! When you sleep tonight, friend, may you view all the you hope for, tomorrow! π"`'
        )

    if x == 66:
        await event.edit(
            '`"π₯° When everything is brought to a standstill, friend, I hope that your thoughts are good, as you drift to sleep! May those thoughts remain with you, during all of your days! π"`'
        )

    if x == 67:
        await event.edit(
            '`"π₯° Every day, you encourage me to do new things, friend! May tonightβs rest bring a new day that overflows with courage and exciting events! π"`'
        )
