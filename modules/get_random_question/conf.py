from entities.ent_enabled_module import EnabledModule
from entities.ent_chat_keyword import ChatKeyword

ENABLED_MODULE = EnabledModule(
    class_name="get_random_question",
    custom_json_settings={
        "random_questions": [
            "What's your favorite series?",
            "What do you like to listen to?",
            "How many sisters or brothers do you have?",
            "When you are old, what do you think children will ask you to tell stories about?",
            "If you could switch two movie characters, what switch would lead to the most inappropriate movies?",
            "What animal would be cutest if scaled down to the size of a cat?",
            "What inanimate object would be the most annoying if it played loud upbeat music while being used?",
            "When did something start out badly for you but in the end, it was great?",
            "What weird food combinations do you really enjoy?",
            "How would your country change if everyone, regardless of age, could vote?",
            "What are some red flags to watch out for in daily life?",
            "If your job gave you a surprise three day paid break to rest and recuperate, what would you do with "
            "those three days?",
            "Where do you get your news?","What movie can you watch over and over without ever getting tired of?",
            "What’s wrong but sounds right?",
            "What’s the most epic way you’ve seen someone quit or be fired?",
            "If you couldn’t be convicted of any one type of crime, what criminal charge would you like to be immune "
            "to?",
            "What social stigma does society need to get over?",
            "What’s the most creative use of emojis you’ve ever seen?",
            "What’s something that will always be in fashion, no matter how much time passes?",
            "What actors or actresses play the same character in almost every movie or show they do?",
            "In the past people were buried with the items they would need in the afterlife, what would you want "
            "buried with you so you could use it in the afterlife?",
            "What’s the best / worst practical joke that you’ve played on someone or that was played on you?",
            "Who do you go out of your way to be nice to?",
            "Where do you get most of the decorations for your home?",
            "What food have you never eaten but would really like to try?",
            "What food is delicious but a pain to eat?",
            "Who was your craziest / most interesting teacher?",
            "What 'old person' things do you do?",
            "What was the last photo you took?",
            "What is the most amazing slow motion video you’ve seen?",
            "Where are some unusual places you’ve been?",
            "Which celebrity do you think is the most down to earth?",
            "What would be the worst thing to hear as you are going under anesthesia before heart surgery?",
            "What’s the spiciest thing you’ve ever eaten?",
            "What’s the most expensive thing you’ve broken?",
            "What obstacles would be included in the World’s most amazing obstacle course?",
            "What makes you roll your eyes every time you hear it?",
            "What do you think you are much better at than you actually are?",
            "Should kidneys be able to be bought and sold?",
            "When was the last time you got to tell someone 'I told you so.'?",
            "What would a world populated by clones of you be like?",
            "What riddles do you know?",
            "What’s your cure for hiccups?",
            "What invention doesn’t get a lot of love, but has greatly improved the world?",
            "What’s something you really resent paying for?",
            "Do you think that aliens exist?",
            "What are you currently worried about?",
            "What’s the most interesting building you’ve ever seen or been in?",
            "What mythical creature do you wish actually existed?",
            "What are your most important rules when going on a date?",
            "How do you judge a person?",
            "If someone narrated your life, who would you want to be the narrator?",
            "What was the most unsettling film you’ve seen?",
            "What unethical experiment would have the biggest positive impact on society as a whole?",
            "When was the last time you were snooping, and found something you wish you hadn’t?",
            "Which celebrity or band has the worst fan base?",
            "What are you interested in that most people aren’t?",
            "If you were given a PhD degree, but had no more knowledge of the subject of the degree besides what you "
            "have now, what degree would you want to be given to you?",
            "What smartphone feature would you actually be excited for a company to implement?",
            "What’s something people don’t worry about but really should?",
            "What movie quotes do you use on a regular basis?",
            "Do you think that children born today will have better or worse lives than their parents?",
            "What’s the funniest joke you know by heart?",
            "When was the last time you felt you had a new lease on life?",
            "What’s the funniest actual name you’ve heard of someone having?",
            "Which charity or charitable cause is most deserving of money?",
            "What TV show character would it be the most fun to change places with for a week?",
            "What was cool when you were young but isn’t cool now?",
            "If you were moving to another country, but could only pack one carry-on sized bag, what would you pack?",
            "What’s the most ironic thing you’ve seen happen?",
            "If magic was real, what spell would you try to learn first?",
            "If you were a ghost and could possess people, what would you make them do?",
            "What goal do you think humanity is not focused enough on achieving?",
            "What problem are you currently grappling with?",
            "What character in a movie could have been great, but the actor they cast didn’t fit the role?",
            "What game have you spent the most hours playing?",
            "What’s the most comfortable bed or chair you’ve ever been in?",
            "What’s the craziest conversation you’ve overheard?",
            "What’s the hardest you’ve ever worked?",
            "What movie, picture, or video always makes you laugh no matter how often you watch it?",
            "What artist or band do you always recommend when someone asks for a music recommendation?",
            "If you could have an all-expenses paid trip to see any famous world monument, which monument would you "
            "choose?",
            "If animals could talk, which animal would be the most annoying?",
            "What’s the most addicted to a game you’ve ever been?",
            "What’s the coldest you’ve ever been?",
            "Which protagonist from a book or movie would make the worst roommate?",
            "Do you eat food that’s past its expiration date if it still smells and looks fine?",
            "What’s the most ridiculous thing you have bought?",
            "What’s the funniest comedy skit you’ve seen?",
            "What’s the most depressing meal you’ve eaten?",
            "What tips or tricks have you picked up from your job / jobs?",
            "What outdoor activity haven’t you tried, but would like to?",
            "What songs hit you with a wave of nostalgia every time you hear them?",
            "What’s the worst backhanded compliment you could give someone?",
            "What’s the most interesting documentary you’ve ever watched?",
            "What was the last song you sung along to?",
            "What’s the funniest thing you’ve done or had happen while your mind was wandering?",
            "What app can you not believe someone hasn’t made yet?",
            "When was the last time you face palmed?",
            "If you were given five million dollars to open a small museum, what kind of museum would you create?",
            "Which of your vices or bad habits would be the hardest to give up?",
            "What really needs to be modernized?",
            "When was the last time you slept more than nine hours?",
            "How comfortable are you speaking in front of large groups of people?",
            "What’s your worst example of procrastination?",
            "Who has zero filter between their brain and mouth?",
            "What was your most recent lie?",
            "When was the last time you immediately regretted something you said?",
            "What would be the best thing you could reasonably expect to find in a cave?",
            "What did you think was going to be amazing but turned out to be horrible?",
            "What bit of trivia do you know that is very interesting but also very useless?",
            "What’s the silliest thing you’ve seen someone get upset about?",
            "What animal or plant do you think should be renamed?",
            "What was the best thing that happened to you today?",
            "What languages do you wish you could speak?",
            "What’s the most pleasant sounding accent?",
            "What’s something that everyone, absolutely everyone, in the entire world can agree on?",
            "What country is the strangest?",
            "What’s the funniest word in the English language?",
            "What’s some insider knowledge that only people in your line of work have?",
            "Who do you wish you could get back into contact with?",
            "How do you make yourself sleep when you can’t seem to get to sleep?",
            "If people receive a purple heart for bravery, what would other color hearts represent?",
            "What are some of the best vacations you’ve had?",
            "If there was a book of commandments for the modern world, what would some of the rules be?",
            "What’s the craziest video you’ve ever seen?",
            "What’s your 'Back in my day, we…'?",
            "If you could know the truth behind every conspiracy, but you would instantly die if you hinted that you "
            "knew the truth, would you want to know?",
            "What animal would be the most terrifying if it could speak?",
            "What’s the worst hairstyle you’ve ever had?",
            "What habit do you have now that you wish you started much earlier?",
            "If you were given one thousand acres of land that you didn’t need to pay taxes on but couldn’t sell, "
            "what would you do with it?",
            "What about the opposite sex confuses you the most?",
            "When was the last time you yelled at someone?",
            "What’s the opposite of a koala?",
            "What kinds of things do you like to cook or are good at cooking?",
            "What life skills are rarely taught but extremely useful?",
            "What movie universe would be the worst to live out your life in?",
            "If you could hack into any one computer, which computer would you choose?",
            "Who do you feel like you know even though you’ve never met them?",
            "What’s the most ridiculous animal on the planet?",
            "What’s the worst thing you’ve eaten out of politeness?",
            "What’s the most historic thing that has happened in your lifetime?",
            "What happens in your country regularly that people in most countries would find strange or bizarre?",
            "What has been blown way out of proportion?",
            "When was a time you acted nonchalant but were going crazy inside?",
            "What’s about to get much better?",
            "What are some clever examples of misdirection you’ve seen?",
            "What’s your funniest story involving a car?",
            "What would be the click-bait titles of some popular movies?",
            "If you built a themed hotel, what would the theme be and what would the rooms look like?",
            "What scientific discovery would change the course of humanity overnight if it was discovered?",
            "Do you think that humans will ever be able to live together in harmony?",
            "What would your perfect bar look like?",
            "What’s the scariest nonhorror movie?",
            "What’s the most amazing true story you’ve heard?",
            "What’s the grossest food that you just can’t get enough of?",
            "What brand are you most loyal to?",
            "What’s the most awkward thing that happens to you on a regular basis?",
            "If you had to disappear and start a whole new life, what would you want your new life to look like?",
            "What movie or book do you know the most quotes from?",
            "What was one of the most interesting concerts you’ve been to?",
            "Where are you not welcome anymore?",
            "What do you think could be done to improve the media?",
            "What’s the most recent show you’ve binge watched?",
            "What’s the worst movie trope?",
            "What’s a common experience for many people that you’ve never experienced?",
            "What are some misconceptions about your hobby?",
            "What’s the smartest thing you’ve seen an animal do?",
            "What’s the most annoying noise?",
            "What’s your haunted house story?",
            "What did you Google last?",
            "What’s the dumbest thing someone has argued with you about?",
            "If money and practicality weren’t a problem, what would be the most interesting way to get around town?",
            "What’s the longest rabbit hole you’ve been down?",
            "What’s the saddest scene in a movie or TV series?",
            "What’s the most frustrating product you own?",
            "What inconsequential super power would you like to have?",
            "What qualities do all your friends have in common?",
            "What odd smell do you really enjoy?",
            "What’s the coolest animal you’ve seen in the wild?",
            "What’s the best lesson you’ve learned from a work of fiction?",
            "What food do you crave most often?",
            "Who in your life has the best / worst luck?",
            "What fashion trend makes you cringe or laugh every time you see it?",
            "What’s your best story of you or someone else trying to be sneaky and failing miserably?",
            "Which apocalyptic dystopia do you think is most likely?",
            "If you had a HUD that showed three stats about any person you looked at, what three stats would you want "
            "it to show?",
            "What’s the funniest thing you’ve seen a kid do?",
            "What’s your secret talent?",
            "What’s the best way you or someone you know has gotten out of a ticket / trouble with the law?",
            "Tear gas makes people cry and laughing gas makes people giggle, what other kinds of gases do you wish "
            "existed? "
        ]}
)

CHAT_KEYWORDS = [
    ChatKeyword(chat_keyword="question")
]