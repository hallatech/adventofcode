#!/bin/bash

# input_file=example_set
input_file=input
count=$(cat $input_file | wc -l)

echo "Numbers in ${input_file}: ${count}"

numbers=$(cat $input_file)
found="false"
num1=0
num2=0
for i in $numbers; do
    # echo $i
    for j in $(cat $input_file); do
        # echo $j
        sum=$(($i+$j))
        if [ $sum -eq 2020 ]; then
            num1=$i
            num2=$j
            found="true"
            break
        fi
    done
    if [ $found = "true" ]; then
        break
    fi
done
if [ $found = "true" ]; then
    echo "The numbers are $num1 and $num2."
    echo "The sum of the numbers is: $(($num1+$num2))"
    echo "The multiplication of the number is: $(($num1*$num2))"
fi
