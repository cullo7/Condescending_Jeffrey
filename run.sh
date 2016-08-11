#! bin/sh

# Purpose of this script is to make compiling and running faster in the thought that there will be 
# more to do to run the program in the future

make find_city
python main.py -a
rm *.pyc find_city
