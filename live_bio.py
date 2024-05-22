import scratchattach as sa3

session = sa3.login("username", "password")
banbot2 = session.get_linked_user()
stats = banbot2.stats()
ranks = banbot2.ranks()
messages = banbot2.message_count()

if messages > 1:
    message_phrase = "My mailbox has " + str(messages) + " new notifications. This means I'm offline, so leave a message at the beep.\n\n"
elif messages < 1:
    message_phrase = "According to my Raspberry Pi, I have 0 new messages. Maybe you could help change that?\n\n"
else:
    message_phrase = "My mailbox has 1 new notification. This means I'm offline, so leave a message at the beep.\n\n"

numbers_phrase = "#" + str(ranks["followers"]) + " most followed scratcher, with a total of " + str(stats["loves"] + stats["favorites"] + stats["views"]) + " loves, favorites, and views."

banbot2.set_bio(message_phrase + numbers_phrase)



