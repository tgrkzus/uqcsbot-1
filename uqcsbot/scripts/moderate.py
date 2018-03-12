from uqcsbot import bot, Command

@bot.on_command("add_mod")
def add_mod(command: Command):
	if not command.has_arg():
		bot.post_message(command.channel, "Invalid usage")
    args = command.args

@bot.on_command("remove_mod")
def remove_mod(command: Command):
	if not command.has_arg():
		bot.post_message(command.channel, "Invalid usage")
    args = command.args

@bot.on_command("get_mods")
def get_mods(command: Command):
	pass

# On archive clean up moderated channel from persistent state
def archive_channel():
	pass

class ModeratedChannel(object):
	def __init__(channel_id, delete_emoji):
		self.channel_id = channel_id
		self.moderators = []
		self.delete_emoji = delete_emoji; # Probably store this as :delete_emoji:

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

	def try_delete(asker, target):
		'''
		When the appropriate reaction is detected on a moderated channel.
		Try delete the target message. Fails if the reactor isn't a moderator
		'''
		if asker in self.moderators:
			# Delete message
