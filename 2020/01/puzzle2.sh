#!/bin/bash

# input_file=example_set
input_file=input
count=$(cat $input_file | wc -l)

echo "Numbers in ${input_file}: ${count}"

number_list1=$(cat $input_file)
number_list2=$(cat $input_file)
found="false"
num1=0
num2=0
num3=0
counter=0
for i in $number_list1; do
    counter=$(($counter+1))
    echo $i
    for j in $number_list2; do
        echo "$i $j"
        for k in $(cat $input_file); do
            echo "$counter: $i $j $k"
            sum=$(($i+$j+$k))
            if [ $sum -eq 2020 ]; then
                num1=$i
                num2=$j
                num3=$k
                found="true"
                break
            fi
        done
        if [ $found = "true" ]; then
            break
        fi
    done
    if [ $found = "true" ]; then
        break
    fi
done
if [ $found = "true" ]; then
    echo "The numbers are $num1, $num2 and $num3."
    echo "The sum of the numbers is: $(($num1+$num2+$num3))"
    echo "The multiplication of the number is: $(($num1*$num2*$num3))"
fi
