from .imgwillkommen import ImgWillkommen

def setup(bot):
	n = ImgWillkommen(bot)
	bot.add_cog(n)
