#! bin/sh

# Purpose of this script is to make compiling and running faster in the thought that there will be 
# more to do to run the program in the future

g++ find_city.cpp
python main.py -a
rm *.pyc

