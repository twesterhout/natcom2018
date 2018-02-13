Assignment 1
==========================================================================

1. a)
      .. math::

        \frac{157}{76 \cdot 100} \cdot 100 \approx 2 \;.

   #)
      .. math::

        \left( 1 - \frac{157}{100 \cdot 76} \right)^{100} \approx 12.4\% \;.


#. Assume that the whole population consists of :math:`\{3, 5, 7\}` only.
   Then we have

   .. math::

     \left\{
       \begin{aligned}
         \mathbb{P}[3] &= \frac{f(3)}{f(3) + f(5) + f(7)} \approx 0.11 \;,\\
         \mathbb{P}[5] &= \frac{f(5)}{f(3) + f(5) + f(7)} \approx 0.3 \;,\\
         \mathbb{P}[7] &= \frac{f(7)}{f(3) + f(5) + f(7)} \approx 0.59 \;.\\
       \end{aligned}
     \right.

   Calculating :math:`\mathbb{P}`'s for :math:`f_1` is now a matter of
   replacing :math:`f` with :math:`f_1`. We get

   .. math::

     \left\{
       \begin{aligned}
         \mathbb{P}'[3] &\approx 0.16 \;,\\
         \mathbb{P}'[5] &\approx 0.31 \;,\\
         \mathbb{P}'[7] &\approx 0.53 \;,\\
       \end{aligned}
     \right.

   which obviously yields a lower selection pressure.


#. Here's the code:

   .. literalinclude:: ../../src/assignment1/fake_monte_carlo.py
      :language: python
      :linenos:
      :lines: 39-49

   And the result:

   .. image:: FakeMonteCarlo.png


#. Here's the code:

   .. literalinclude:: ../../src/assignment1/genetic_algorithm.py
      :language: python
      :linenos:
      :lines: 40-54

   And the result:

   .. image:: genetic_algorithm.png


