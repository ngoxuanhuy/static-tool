# MY TOOL - study firmware in a statical way

## Setup

To run this project, we firstly need to install `binwalk` locally
```
$ sudo apt install binwalk
```

## Useage

```
+ Clone the project
+ Navigate to the newly cloned folder: $ cd static-tool
+ Copy the firmware image to the same folder *static-tool*
+ Run the command: *$ python3 scan.py [firmware_name]*
```

## Example

In this repository, there are two firmware samples: **c7v5.bin** and **R6220.img**
The image below illustrates how to start the tool with a sample
![alt text](https://github.com/ngoxuanhuy/static-tool/blob/master/images/file_system_finding.png "My Tool - starting point")

The tool extracts a file system, finds all files with specific extensions, possible system's accounts and keys
![alt text](https://github.com/ngoxuanhuy/static-tool/blob/master/images/patterns_finding.png "Info extraction")




