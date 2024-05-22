import scratchattach as sa3
from random import choice

session = sa3.login("username", "password")
banbot2 = session.get_linked_user()
followers = banbot2.followers(limit = banbot2.follower_count())

if len(followers) > 0:
    featured_follower = choice(followers)
    follower_phrase = "Follower of the day is @" + str(featured_follower) + ", "
    projects = featured_follower.projects()
    if len(projects) > 0:
        project_phrase = "who made this: " + choice(projects).url + "."
    else:
        project_phrase = "for being an active and meaningful part of the community."
else:
    follower_phrase = "I have no followers. How did this happen?\n"
    project_phrase = "So much for highlighting someone's project..."

working_phrase = "Creating neural networks to solve hard problems and studying in preparation for higher education.\n\n"
banbot2.set_wiwo(working_phrase + follower_phrase + project_phrase)



