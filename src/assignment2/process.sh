#!/bin/bash

PREFIX="$HOME/src/negative-selection/syscalls"

ALPHABET="$PREFIX/snd-cert/snd-cert.alpha"
TRAIN="$PREFIX/snd-cert/snd-cert.train"
TEST="$PREFIX/snd-cert/snd-cert.2.test"
LABELS="$PREFIX/snd-cert/snd-cert.2.labels"
NEGSEL2="$PREFIX/../negsel2.jar"
TEMP_FILE="$PWD/.natcom_assignment2_ex2_$RANDOM.dat"

negsel2 ()
{
	java -jar $NEGSEL2 -alphabet file://"$ALPHABET" -self "$TRAIN" $@
}

roc_auc()
{
	python3 - <<-___HERE
		from numpy import loadtxt
		from sklearn.metrics import roc_auc_score

		data = loadtxt('$1')
		print(roc_auc_score(data[:, 0], data[:, 1]))
	___HERE
}

average()
{
	local _N=$1
	local _R=$2
	sed -E 's/(.{'$_N'})/\1\n/g' <<< "$3" \
		| negsel2 -n $_N -r $_R -c -l 2>/dev/null \
		| awk 'BEGIN{x=0} {x+=$1} END{print x/NR}'
}


test_one()
{
	local _N=$1
	local _R=$2
	paste "$LABELS" \
		<(while IFS='' read -r line || [[ -n "$line" ]]; do
			average $_N $_R "$line"
			done < "$TEST") > "$TEMP_FILE"
	roc_auc "$TEMP_FILE"
	rm -f "$TEMP_FILE"
}

test_one 10 4
