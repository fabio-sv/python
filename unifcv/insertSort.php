<?php

$arr = [80, 70, 60, 50, 95];

insertSort($arr);

print_r($arr);

function insertSort(&$arr) {
    for ($i = 0; $i < count($arr); $i++) {

        $elemento = $arr[$i];
        $posicao = $i;

        for ($j = $posicao - 1; $j >= 0; $j--){

            if($elemento < $arr[$j]) {
                $arr[$j + 1] = $arr[$j];
                $posicao --;
            }
        }

        $arr[$posicao] = $elemento;
    }
} 

function bubbleSort($arr) {

    $len = count($arr);

    for($i = 0; $i < $len; $i++) {

        for($j = 0; $j < $len; $j++) {
            
        }

    }

}
?>
