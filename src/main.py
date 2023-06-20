import os
import discord
from bardapi import Bard
from dotenv import load_dotenv
from keep_alive import keep_alive
from discord import app_commands, Intents, Interaction

load_dotenv()

bard_api = os.environ.get('BARD_API_KEY')
discord_token = os.environ.get('DISCORD_TOKEN')

class BardBot(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.tree = app_commands.CommandTree(self)

	async def setup_hook(self) -> None:
		await self.tree.sync()

	async def on_ready(self):
		print(f'Currently logged in as {self.user}. (ID: {self.user.id})')

client = BardBot(intents = Intents.default())
bard_client = Bard(token = bard_api)

@client.tree.command(name='bard', description='your personal bard ai using bardapi')
async def bard(interaction: Interaction, prompt: str):
	# defer response to avoid api processing exceeds 3s interaction reply requirement
	await interaction.response.defer()
	print(f'{interaction.user} used the bard command with the parameter \'{prompt}\'.')
	# keep response under 1500 characters for discord message character limit
	response = bard_client.get_answer(prompt + ', limit response to under 1500 characters')['content']
	print(response)
	await interaction.followup.send(response)

if __name__ == '__main__':
	# keep_alive()  # create and deploy a flask webserver to keep bot alive for replit hosting, uncomment if needed
	client.run(discord_token)