# AirBnB clone - The console

![alt text](https://psmag.com/.image/t_share/MTU0MTM1MjIzODMzOTk0NjUx/gettyimages-586113550.jpg)

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

## Main commands

These are some commands needed for work in the console

| Command | Description |
| ---------- | ---------- |
| all | Show all objects in an instance   |
| create | Create a new instance of a class |
| update | Update the information of an object |
| show | Shows the information of an element |
| destroy | Remove an instance |


## Execution

Work like this in interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Work like this in non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Examples commands
create -> creates a new instance of BaseModel class
```
(hbnb) create BaseModel
```
update -> updates an instance with class name, id and attribute
```
(hbnb) update BaseModel b6f2ef1d-9673-4hg5-abe4-44eff3d05t78 user "other"
```
show -> show an string representation of an instance
```
(hbnb) show BaseModel b6f2ef1d-9673-4hg5-abe4-44eff3d05t78
```
destroy -> deletes an instance
```
(hbnb) destroy BaseModel b6f2ef1d-9673-4hg5-abe4-44eff3d05t78
```
all -> show all string representation of all instances
```
(hbnb) all
```
## Contributors
- [Carlos Arias](https://github.com/carlosariasf)
- [Samuel Florez](https://github.com/muxanz)
