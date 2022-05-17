

### A powerful bot that can play music on telegram group's voice chat with some useful features !!

<p align="center">
  <img src="https://telegra.ph/file/00a389a0c21a632ee29aa.jpg">
</p>

<h3>Requirements 📝</h3>

- FFmpeg
- Python 3.10.0
- [NodeJS](https://nodesource.com/)
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

### Commands 🛠
#### For all in group
- `/play <reply/url>` - Youtube url
- `/play <reply audio>`- Song file to play song
- `/play <song name>` - Play song you requested
- `/song <song name>` - Download songs you want
- `/search <query>` - Search videos on youtube with details
- `@botusername <query>` - Get youtube url by inline

#### Admins only
- `/pause` - Pause song play
- `/resume` - Resume song play
- `/skip` - Play next song
- `/end` - Stop music play
- `/cleandb` - Clear all files
- `/userbotjoin` - Add assistant
- `/userbotleave` - Remove assistant

#### Sudo & Owner only
- `/restart` - Restart bot
- `/gcast <text/reply>` - Broadcast to groups (auto pinned)
- `/broadcast <text>` - Broadcast to groups (without pinned)
- `/exec <code>` - Excute a code
- `/userbotleaveall` - remove assistant of all groups
