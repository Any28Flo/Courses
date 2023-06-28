#!/bin/bash
read -p 'Defina la variable a crear: ' v1
if [[ $v1 == 'carro']];then
	echo "es carro"
elif [[ $v1 == 'casa']];then
	echo 'es casa'
else
	ls
fi
