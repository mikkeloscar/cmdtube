# cmdtube

Simple commandline youtube search and play.

## Dependencies
* gdata

#### Players
* youtube-dl + mplayer
* vlc

You can either use `mplayer` + `youtube-dl` or `vlc` as the player. It is also
possible to use a different player, check `cmdtube.conf` for how to setup the
player.

## Installation

### Archlinux

Install `cmdtube-git` from AUR

## Configuration

### System config

cmdtube honors a system-wide config file. It first looks at

    $XDG_CONFIG_DIRS/cmdtube/cmdtube.conf

and fall back to

    /etc/xdg/cmdtube/cmdtube.conf

### User config

Userconfig override the system config. Cmdtube will look for

    $XDG_CONFIG_HOME/cmdtube/config

and fall back to

    $HOME/.config/cmdtube/config

## Usage

    $ cmdtube [OPTIONS] SEARCH-TERM

## License
Copyright (C) 2012  Mikkel Oscar Lyderik

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
