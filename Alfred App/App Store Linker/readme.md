# App Store Linker

A simple script to generate App Store Affiliate Links. It's inteded to be used with Alfred (extension available) but can just as easily be used with any other type of launcher that supports launching scripts.

## Usage
The script has only one required parameter, the **App Name**. the remainder of the paramenters are optional and simply aim to facilitate usage.

    usage: as_linker.py [-h] [-m | -i | -s] [-n N] [-l] App Name [App Name ...]

    positional arguments:
      App Name        Type the Apps Name

    optional arguments:
      -h, --help      show this help message and exit
      -m, --mac       Mac App
      -i, --ipad      iPad App
      -s, --software
      -n N, --num N   Number of results to display
      -l, --link      Format markdown links

The parameters can either be passed with the Alfred query or be hard coded into the extension itself.
