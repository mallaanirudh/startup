from gtts import gTTS

script = """
Choosing the right college can be overwhelming... especially with entrance exams like JEE, NEET, and more standing in your way.
With so many choices and so much information, it’s easy to feel lost.

But now, there’s a smarter way to make your college decision easier. Meet Your Personal Guide – your personal guide to finding the best college for you!

Just tell us which entrance exam you’ve taken and share your preferences – whether it’s location, specialization, or course type – and we’ll instantly give you personalized recommendations.

From top-tier institutions to hidden gems, you’ll see the best colleges that match your scores and career goals, all in just a few clicks.

Once you’ve narrowed down your options, you can go beyond the brochures and websites. Connect directly with real students already enrolled in those courses.

Want to know what life is really like at your dream college? Ask about the professors, the campus, the hostel facilities, or student life – you’ll get honest answers from those who know best: the students themselves.

Now, with insights from real students, you can make an informed decision with confidence and find the college that’s the best fit for you.
"""

tts = gTTS(text=script, lang='en', tld='co.in')
tts.save("college_guide_audio.mp3")
