#!/bin/bash

# Current time in milliseconds
now=$(date +%s%N)
metric=load_value_test
value=42
host=10.4.2.80
echo "put $metric $now $value host=A" | nc -w 30 $host 4242
