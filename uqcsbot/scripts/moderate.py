from uqcsbot import bot, Command

@bot.on_command("add_mod")
def handle_cat(command: Command):
	if not command.has_arg():
		bot.post_message(command.channel, "Invalid usage")
    args = command.args

@bot.on_command("moderate")
def handle_cat(command: Command):
	if not command.has_arg():
		bot.post_message(command.channel, "Invalid usage")
    args = command.args

class ModeratedChannel(object):
	def __init__(channel_id):
		self.channel_id = channel_id
		self.moderators = []

	def add_moderator(user_id):
		if user_id not in self.moderators:
			self.moderators.append(user_id)
		return True

	def remove_moderator(user_id):
		if user_id in self.moderators:
			self.moderators.remove(user_id)
			return True
		else:
			return False

	def set_delete_emoji():
		pass

	def get_delete_emoji():
		pass

	def try_delete(asker, target):
		pass
