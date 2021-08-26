from twilio.rest import Client
import random
import schedule
import time


TWILIO_PHONE_NUM = "***+12345678901***"
GWYNETHS_PHONE_NUM = "***+10987654321***"
ACCOUNT_SID = "***ACCOUNT_SID***"
AUTH_TOKEN = "***AUTH_TOKEN***"
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
GWYNETH_IS_BEAUTIFUL = [
		"hello my beautiful darling",
		"i love you soooo much, you beautiful thang",
		"theres no one more beautiful than my gwyneth",
		"im so lucky to have such a beautiful girlfriend",
		"oh shit, i just burned myself, cuz my girlfriend's so beautifully hot",
		"damn girl, ur so freakin beautiful",
		"omg there's something in your mirror! oh, its just u, u beautiful thang",
		"theres no words to describe how beautiful you are",
		"oh hey, look, its my beautiful girlfriend!",
		"girls wish they could be as beautiful as you",
		"look, its the most beautiful girl in the world! how do you do it so flawlessly?",
		"i look at u and i think, yum, beautiful",
		"so, whats cookin? good lookin?",
		"what is up with you being so beautiful every frickin day?",
		"some people are subjectively beautiful... youre objectively beautiful",
		"u got somethin on ur face, please rub it off... oh it didn't come off? that's called beauty my dear.",
		"hey u sexy beautiful thang",
		"what has two thumbs and is the most beautiful in the girl? u!",
		"there's no one more beautiful than gwyneth hunger",
		"you're so beautiful im gonna die",
		"my eyes are so lucky every time they see your beautiful face",
		"beautiful beautiful gwyneth!",
		"girl, u so damn fiiiiiiiiiiine, so beautiful!",
		"goddam my girlfriend's so beautiful!",
		"she a hot thang, she a beautiful thang, she my thang",
		"wow how u so freaking hot, goddammmmmmmm",
		"im dating a super model, and her name is gwyneth hunger",
		"girl, u the most beautifullest thang in the whole wide universe",
		"i wish you could see you through my eyes, then you'd see you're the most beautiful girl in the world",
		"im so lucky this beautiful girl is mine",
		"soon, imma marry this beautiful girl",
		"do you smell something burning? Oh, its just u, u beautiful hot thang",
	]

def send_message():
	message = random.choice(GWYNETH_IS_BEAUTIFUL)
	CLIENT.messages.create(to=GWYNETHS_PHONE_NUM,
						from_=TWILIO_PHONE_NUM,
						body=message)

send_message()