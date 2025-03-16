# discord-MassMessageDelete-selfbot
Delete every message from your user account within one (or multiple) channels. Includes a filter to only remove specific messages.

# Note:
Automating user accounts is against the Discord ToS. This script is for educational purposes only and I cannot recommend using it. Do so at your own risk.
This script uses the [discord.py-self](https://github.com/dolfies/discord.py-self) library.

# Usage:
This script is meant to delete your messages from one or more channels. Two ways to use it:
## Startup:
- Replace `GUILD_ID` and `CHANNEL_ID` with your own guild and channel id's.
- When the bot starts up, it will start going through those channels and deleting every message from the user.
## Prefix method:
- Start up the script, go into whichever channel you want, and send a message starting with ```$ suicide``` - you can add things after this, like ```hi``` (so the full message would be ```$ suicide hi```), in which case the bot will filter for messages only containing ```hi``` in that channel.

- For both methods, replace `TOKEN` with your own discord user token. If you don't know how to get it, you can find out [here.](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6)

# Known Issues:
- The script won't delete messages from a user app or from bot messages where the user used a command, only the messages from the user directly.
- Inefficiency when going through a channel to find the user's messages - instead of loading the channel's messages (as if the user were scrolling up), we could just search for messages from the user (as if we were using the seach function).
- No way to use filter (eg. filtering only for messages containing "hi") if using the startup method.
- Filtering could be better: add the ability to filter for messages only starting / ending with something specific, messages with images, etc...
- Not really an issue, but I've added a manual 'slow-mode' for when going through dm messages (between every message, the bot will wait a bit) - this was made to make the behaviour appear more human, but if it actually helps i'm not tech-saavy enough to know.
- Code is unreadable
