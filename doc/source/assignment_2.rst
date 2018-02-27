Assignment 2
==========================================================================

1. Here's the code for computing ROC AUC scores for different test sets
   and parameters:

   .. literalinclude:: ../../src/assignment2/language.sh
      :language: bash
      :linenos:
      :lines: 29-67

   And here's the output:

   .. code::

     English vs. Tagalog, r = 1: 0.543534718425
     English vs. Tagalog, r = 2: 0.739645981411
     English vs. Tagalog, r = 3: 0.83112356479
     English vs. Tagalog, r = 4: 0.791609713869
     English vs. Tagalog, r = 5: 0.728244031347
     English vs. Tagalog, r = 6: 0.668084791325
     English vs. Tagalog, r = 7: 0.590725806452
     English vs. Tagalog, r = 8: 0.520161290323
     English vs. Tagalog, r = 9: 0.512096774194
     English vs. Hiligaynon, r = 4: 0.797467741935
     English vs. Plautdietsch, r = 4: 0.753403225806
     English vs. Middle English, r = 4: 0.533887096774
     English vs. Xhosa, r = 4: 0.832274193548


   We notice that the best results are obtained for :math:`r` of about 3.
   :math:`r = 1` is basically a single letter and hence not enough
   information to make a reasonable conclusion. Too high an :math:`r` is
   again meaningless as there are almost no such long words.

   And about other languages, one notices that it's basically impossible
   to distinguish similar languages (e.g. English vs. Middle English)
   while the ones that are drastically different from English (e.g. Xhosa)
   are very well recognised.

#. Aside from the chunking, the algorithm is the same:

   .. literalinclude:: ../../src/assignment2/process.sh
      :language: bash
      :linenos:
      :lines: 28-50

   Surprisingly, it produces amazing results, i.e. ROC AUC is higher than
   90%.
