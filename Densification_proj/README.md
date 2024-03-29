# densificationscalingMLE
This is the README file for the python code that estimates the population size and overall activity in temporal networks based on a numerical maximum-likelihood method.

**Reference**:

"Identifying the temporal dynamics of densification and sparsification in human contact networks," Shaunette Ferguson and Teruyoshi Kobayashi. arXiv 2201.09489, 2022. https://arxiv.org/pdf/2201.09489.pdf


## Sample network data (.csv files)

a) **Hospital**: Contacts among patients, nurses, doctors and staffs in a Hospital in Lyon. Taken from SocioPatterns project <http://www.sociopatterns.org/datasets/hospital-ward-dynamic-contact-network/>.

b) **Workplace**: Contacts between workers in an office building in France in 2015. Taken from SocioPatterns project <http://www.sociopatterns.org/datasets/test/>.

 c) **IC2S2-17**: Contacts between participants of the International Conference on Computational Social Science 2017 at GESIS in Cologne. The original data can be found at: <https://zenodo.org/record/2531537#.X6qTndtUvOQ>

d) **WS-16**: Contacts between participants of the Computational Social Science Winter Symposium 2016 at GESIS in Cologne. Original data can be found at: <https://zenodo.org/record/2531537#.X6qTndtUvOQ>
	
## Data format

The following input is required to implement the maximum-likelihood estimation:
	
**NM**: *L* x 2  array (i.e., sequence of (*N*,*M*) tuples). The length of the sequence is denoted by *L*.
	* _N_: An integer denoting the number of nodes that have at least one edge (or link).
	* _M_: An integer denoting the total edges.
	

## Code **MLestimation.py**
The python script defines the methods used to estimate the overall activity (&kappa;) and population size (N</sub>p) for networks.
 
The following packages are needed: 
* Pandas
* Numpy
* Numba
* configr

The *configr.py* script allows the user to change the directory location for *parameter_combinations* and *likelihoodfns* on which *MLestimation.py* depends.

## To implement the method:
1. Download all folders/files (parameter_combinations, likelihoodfns, configr.py etc.)
2. For *configr.py*, update the file location for *parameter_combinations* and *likelihoodfns* to your working directory. Save.
3. You may now ```import MLestimation as mle``` as use as shown in the demo file. The module takes 1 minute to load.
Note that the MLestimation module takes as input an (N, M) sequence denoting, respectively, total active nodes and total edges.

## Demo   
An example of how to implement our numerical maximum likelihood estimation is shown in Demo.ipynb. The module takes 1 minute to load.

## Additional info:
In generateMLF.ipynb, we demonstrate how joint probability distributions(likelihood functions) are generated. The user may therefore update the probability equation from p<sub>ij</sub> = 1-e<sup>-&kappa;a<sub>i</sub>a<sub>j</sub></sup> as used in our analysis to any other form as desired. 

Likelihoodfs folder has joint probability distributions for given combinations of the model parameters, &kappa; and N</sub>p. Dictionary format with key and values (i.e., ID of parameter combination: joint prob. dist.).
	For Hospital, IC2S2-17 and WS-16 data sets, we use the likelihood fuctions in the **Likelihoodfns** folder and for Workplace data set we use those in **Likelihoodfns_workplace**.
	
Parameter_combinations folder has tuple combinations of the parameters unique along with their respective identifiers. Dictionary format with key and values (i.e., Identifier: unique tuple combination of &kappa; and N</sub>p) e.g., p0: (0,2) denotes combination identifier p0 for &kappa; = 0 and N</sub>p = 2.
	From the **parameter_combinations** folder, we use _paramcombs.csv_ for Hospital, IC2S2-17 and WS-16 data sets and for the Workplace data set we use those in _paramcombs_workplace.csv_.
