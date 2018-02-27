#!/bin/bash

# English vs. Tagalog, r = 1: 0.543534718425
# English vs. Tagalog, r = 2: 0.739645981411
# English vs. Tagalog, r = 3: 0.83112356479
# English vs. Tagalog, r = 4: 0.791609713869
# English vs. Tagalog, r = 5: 0.728244031347
# English vs. Tagalog, r = 6: 0.668084791325
# English vs. Tagalog, r = 7: 0.590725806452
# English vs. Tagalog, r = 8: 0.520161290323
# English vs. Tagalog, r = 9: 0.512096774194
# English vs. Hiligaynon, r = 4: 0.797467741935
# English vs. Plautdietsch, r = 4: 0.753403225806
# English vs. Middle English, r = 4: 0.533887096774
# English vs. Xhosa, r = 4: 0.832274193548

PREFIX="$HOME/src/negative-selection"

ENGLISH_TRAIN="$PREFIX/english.train"
ENGLISH_TEST="$PREFIX/english.test"
TAGALOG_TEST="$PREFIX/tagalog.test"
HILIGAYNON_TEST="$PREFIX/lang/hiligaynon.txt"
MIDDLE_ENDLISH_TEST="$PREFIX/lang/middle-english.txt"
PLAUTDIETSCH_TEST="$PREFIX/lang/plautdietsch.txt"
XHOSA_TEST="$PREFIX/lang/xhosa.txt"
NEGSEL2="$PREFIX/negsel2.jar"
TEMP_FILE="$PWD/.natcom_assignment2_ex1_$RANDOM.dat"

negsel2 ()
{
	java -jar $NEGSEL2 -alphabet file://"$ENGLISH_TRAIN" -self "$ENGLISH_TRAIN" $@
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

test_tagalog()
{
	for _r in {1..9}; do
		cat <(cat "$ENGLISH_TEST" | negsel2 -n 10 -r $_r -c -l | sed 's/^/0\t/') \
			<(cat "$TAGALOG_TEST" | negsel2 -n 10 -r $_r -c -l | sed 's/^/1\t/') > "$TEMP_FILE"
		echo "English vs. Tagalog, r = $_r:" $(roc_auc "$TEMP_FILE")
		rm -f "$TEMP_FILE"
	done
}

test_generic()
{
	cat <(cat "$ENGLISH_TEST" | negsel2 -n 10 -r 4 -c -l | sed 's/^/0\t/') \
		<(cat "$2"            | negsel2 -n 10 -r 4 -c -l | sed 's/^/1\t/') > "$TEMP_FILE"
	echo "English vs. $1, r = 4:" $(roc_auc "$TEMP_FILE")
	rm -f "$TEMP_FILE"
}

test_tagalog
test_generic "Hiligaynon" "$HILIGAYNON_TEST"
test_generic "Middle English" "$MIDDLE_ENDLISH_TEST"
test_generic "Plautdietsch" "$PLAUTDIETSCH_TEST"
test_generic "Xhosa" "$XHOSA_TEST"
