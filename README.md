# Epic Onslaught - BombSquad Plugin

Enables Epic Mode (slow-motion), boxing gloves, and triple infinite bombs for Onslaught co-op in [BombSquad](https://www.froemling.net/apps/bombsquad).

## Features

- **Epic Mode** - Slow-motion gameplay
- **Boxing Gloves** - Start every life with gloves
- **Triple Bombs** - Always have 3 bombs, no powerup needed

## Install

1. Download `epic_onslaught.py`
2. Place it in your BombSquad mods folder (`~/.bombsquad/mods/`)
3. Restart BombSquad
4. Go to **Settings > Advanced > Plugins** and enable **EpicOnslaughtPlugin**
5. Play any **Co-op Campaign > Onslaught** mode

## Console fallback

Press ` (tilde) in-game and paste:

```
import bascenev1lib.game.onslaught as o; orig=o.OnslaughtGame.__init__; o.OnslaughtGame.__init__=lambda s,settings:(orig(s,settings), setattr(s,'slow_motion',True))
```

Then start an Onslaught game.

## Requirements

- BombSquad 1.7.62+ (API 9)
