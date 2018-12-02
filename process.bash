#!/env/bin/bash

for f in *
do 
    name=`basename $f`
    echo "processing file: $name"
    cat $f| awk '{print $NF}' >> stair_down_labels_$name.csv
    awk '{print $2}' $f >> stair_time_$name.csv
    awk '{print $3}' $f >> stair_x_$name.csv
    awk '{print $4}' $f >> stair_y_$name.csv
    awk '{print $5}' $f >> stair_z_$name.csv
done
