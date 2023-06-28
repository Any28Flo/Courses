#!/bin/bash
read -p 'Ingresa el pedido de hamburguesa: ' noPedido
echo $noPedido
#declaro
pedido=''
if [[ $noPedido == '1' ]]; then
 #reasigno
  pedido='Hamburguesa pollo'
	
elif [[ $noPedido == '2' ]]; then
 pedido='Hamburguesa doble carne'
else
 pedido='No valido'
fi

echo "Su pedido es: $pedido"


