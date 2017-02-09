# Piclodio3
[![Gitter](https://badges.gitter.im/gitterHQ/gitter.svg)](https://gitter.im/piclodio/Lobby)

Piclodio is a web radio player and a also an alarm clock that can be installed on Raspberry Pi.
You can add url stream to complete the collection. Scheduling alarm clock is easy and can be periodic.
A local backup MP3 file is used in case of losing internet connection or if the web radio is not anymore available to be sure you'll be awaken.

![piclodio_home](https://github.com/Sispheor/piclodio3/blob/dev/images/picliodio_presentation.png)

## Installation

### Pre-compiled image disk (Raspberry Pi)
If you want to install it on a Raspberry Pi, you can download a [pre-compiled image disk](https://github.com/Sispheor/piclodio3/releases) and deploy it on your SD card as usual.

### Manual install
The project is split in two parts:
- [Backend](back/README.md)
- [Frontend](front/README.md)

Installation procedures have been tested on a Raspberry Pi and on Ubuntu 16.04 but the project should works on any Linux system that can handle Django and Angular 2.

## Web Radio URLs

There is a lot of web radio online. In most of case, websites provide a `pls` or `m3u` file that contain the URL you need to give to Piclodio.
You can also get the URL from the console of your web browser. Look for the URL that consume the most brandwith in the network console.

Take a look to [internet-radio.com](https://www.internet-radio.com/) for a large selection of web radio sorted by genre.

## Contribute

If you need help you can come on the [Gitter chat room](https://gitter.im/piclodio/Lobby).
Fell free to open an issue to ask a new feature or raise a bug.

## License

Copyright (c) 2016. All rights reserved.

Piclodio is covered by the MIT license, a permissive free software license that lets you do anything you want with the source code, as long as you provide back attribution and "don't hold you liable". For the full license text see the [LICENSE.md](LICENSE.md) file.
