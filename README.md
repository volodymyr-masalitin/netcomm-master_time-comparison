# netcomm - time comparison
This repository consists of the following files

 1. utils.py containing some useful functions
 2. experiment_script_original.py containing the original experiment script (and template) without usage of multiprocessing
 3. experiment_script_multiprocessing containing the edited version of the experiment script using multiprocessing features
 4. visualisation_script.py containing a template of plotting procedures
 5. compare_time.py containing the setup for comparing time of execution of the original and the edited versions of experiment scripts. It can be used to edit the number of iterations (sessions).

<b>How to use/mark:</b> to observe the efficiency of running in parallel please run the <b>compare_time.py</b> file. In order different initial preferences please <b>adjust the 10-th</b> line of this file: <i><b>niter = 50</b></i>


