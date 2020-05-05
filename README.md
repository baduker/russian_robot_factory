# russian_robot_factory
Just an ordinary Russian robot factory. `d[ o_0 ]b`

~~~~
                                         |
    Russian Robot Factory                |
            version 0.1.2                |
                                         |
   _______                   ________    |
  |ooooooo|      ____       | __  __ |   |
  |[]+++[]|     [____]      |/  \/  \|   |
  |+ ___ +|     ]()()[      |\__/\__/|   |
  |:|   |:|   ___\__/___    |[][][][]|   |
  |:|___|:|  |__|    |__|   |++++++++|   |
  |[]===[]|   |_|_/\_|_|    | ______ |   |
_ ||||||||| _ | | __ | | __ ||______|| __|
  |_______|   |_|[::]|_|    |________|   \
              \_|_||_|_/               jro\
                |_||_|                     \
               _|_||_|_                     \
      ____    |___||___|                     \
     /  __\          ____                     \
     \( oo          (___ \                     \
     _\_o/           oo~)/
    / \|/ \         _\-_/_
   / / __\ \___    / \|/  \
   \ \|   |__/_)  / / .- \ \
    \/_)  |       \ \ .  /_/
     ||___|        \/___(_/
     | | |          | |  |
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___]
~~~~
### What is Russian Robot Factory?

This is my Python port of a cool, little Go module 
[go-asciibot](https://github.com/mattes/go-asciibot), which in itself is a port
of a JavaScript [asciibot](https://github.com/walsh9/asciibots) generator.

So, in an essence, this is a port of a port... `¯\_(ツ)_/¯`

Anyhow, `russian_robot_factory` is an ASCII bot generator with, well,
a Russian twist. It produces an ASCII robot and labels the robot with a random
Russian name and an ID.

Here's a handful of examples:
```
     _._._     
    -)o o(-    
     \_=_/     
 .-._/___\_.-. 
 ;   \___/   ; 
     // \\     
    _\\ //_    
Magomedov GYU181
```
```
     .---.     
    } - - {    
     \_0_/     
   .=(+++)=.   
o="  (___)  "=o
     [] []     
    /:] [:\    
Pankrat PQF621
```

```
     ___T_     
    | o o |    
    |__-__|    
   .=[::+]=.   
 ]=' [___] '=[ 
     (_|_)     
     (o|o)     
Koshelev CHF068
```

## Usage:

Copy the code or clone the repo.

```
>>> import russian_robot_factory
>>> print(russian_robot_factory.build_robot())
    .=._,=.    
   ' (q q) `   
     _)-(_     
}-. /\--o/\ .-{
   " |___| "   
     ]| |[     
    [_| |_]    
Vasilev NUH172
```

If you don't want the label, set the `no_label` argument to `True`. By default,
it's set to `False`:
```
>>> import russian_robot_factory
>>> print(russian_robot_factory.build_robot(no_label=True))
     _._._     
    -)o o(-    
     \_=_/     
    /|(\)|\    
   d |___| b   
     ]| |[     
    [_| |_]    
```
## Requirements:

- `Python3+`

## License

Russian Robot Factory is licensed under MIT.