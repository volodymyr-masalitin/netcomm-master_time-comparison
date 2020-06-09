# netcomm - time comparison
This repository consists of the following files

 1. utils.py containing some useful functions
 2. experiment_script_original.py containing the original experiment script (and template) without usage of multiprocessing
 3. experiment_script_multiprocessing.py containing the edited version of the experiment script using multiprocessing features
 4. visualisation_script.py containing a template of plotting procedures
 5. compare_time.py containing the setup for comparing time of execution of the original and the edited versions of experiment scripts. It can be used to edit the number of iterations (sessions).

<b>How to use/mark:</b> to observe the efficiency of running in parallel please run the <b>compare_time.py</b> file. In order different initial preferences please <b>adjust the 10-th</b> line of this file: <i><b>niter = 50</b></i>.

<br /><br />

<b>Description/reasoning of implementation of multiprocessing:</b>

We use Pools in multiprocessing library to run each dialogue in parallel. It is extremely important not to run exactly sessions in parallel.
That's because we do not want to compute [n/4] sessions from the initial conditions 4 times (4 depends on the amount of cores etc),
but we want to compute exactly n sessions. 
At the same time, when doing these computations for each dialogue, we avoid this problem as well as we should avoid overwrite/memory issues. 

We could run in parallel some other functions/cycles as well but there is really no sence to do it. Firstly, they do not take as much time (checked experimentally 
by measuring time of each fragment of the session). Secondly, considering they do not take that much time, we would only lose efficiency since multiprocessing 
has specific advised conditions (and restrictions) and thus is not always relevant.



<b>Worth mentioning: </b>

Not only we run Bernoulli trials + Dialogues in parallel, we compute the Bernoulli trials themselves (if channel is active) only once (before simulating sessions). The reason for that is that in this case of conducting experiment
we do not change parameter 'a' (probability of being active) of each channel in any way. Which means that in a long run there is no need to 

This assumption is however not always true/cannot be made because having a chance of 0.5 is NOT THE SAME as being active all the time after having success in the first trial. 
But since all the activation ratios are the same in this particular example of experiment, this way of computing should be quite accurate in the long run.
In the end of the day these changes can be reverted quite easily (and without too much time losses).
