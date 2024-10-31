#!/bin/bash

ng () {
	echo ${1}行目が違うよ
	res=1
}
res=0

###普通入力###
out=$(seq 5 | ./plus.py)
[ "${out}" = "15.0" ] || ng "$LINENO"

###変入力###
out=$(echo あ | ./plus.py)
[ "$?" = 1 ] 	  || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(echo | ./plus.py)
[ "$?" = 1 ] 	  || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit "$res"


