# densificationscalingMLE
This is the readme file for the python code for that estimates the population size and overall activity in temporal networks based on a numerical maximum-likelihood method.

**Reference**:

"Identifying the temporal dynamics of densification and sparsification in human contact networks," Shaunette Ferguson and Teruyoshi Kobayashi. arXiv 2201.09489, 2022. https://arxiv.org/pdf/2201.09489.pdf


## Sample network data (.csv files)

a) **Hospital**: Contacts among patients, nurses, doctors and staffs in a Hospital in Lyon. Taken from SocioPatterns project <http://www.sociopatterns.org/datasets/hospital-ward-dynamic-contact-network/>.

b) **Workplace**: Contacts between workers in an office building in France in 2015. Taken from SocioPatterns project <http://www.sociopatterns.org/datasets/test/>.

 c) **IC2S2-17**: Contacts between participants of the International Conference on Computational Social Science 2017 at GESIS in Cologne. The original data can be found at: <https://zenodo.org/record/2531537#.X6qTndtUvOQ>

d) **WS-16**: Contacts between participants of the Computational Social Science Winter Symposium 2016 at GESIS in Cologne. Original data can be found at: <https://zenodo.org/record/2531537#.X6qTndtUvOQ>
	
A sequence of snapshot networks is created, for each dataset, every 5 minutes for each day. The length of each a single snapshot (i.e., a time window) is 10 minutes. 


## Data format

The following inputs are required to implement the maximum-likelihood estimation:
	
1. **NMseq**: A T x 2  array (i.e., a sequence of (N,M) pairs), each pair consists of the number of active nodes (*N*) and the number of edges (*M*). *N* and *M* are integers. 
	Each sequence of (*N*, *M*) belongs to a single day and each (*N*, *M*) is associated with a snapshot.
	
	* _N_: An integer denoting the number of nodes that have at least one edge (or link).
	* _M_: An integer denoting the total edges in a given snapshot.
	
2. **likelihood_funcs**: Likelihood functions which are joint probability distributions for given combinations of the model parameters, &kappa; and N</sub>p. Dictionary format with key and values (i.e., ID of parameter combination: joint prob. dist.).
	For Hospital, IC2S2-17 and WS-16 data sets, we use the likelihood fuctions in the **Likelihoodfns** folder and for Workplace data set we use those in **Likelihoodfns_workplace**.
	
3. **params**: Parameter combinations matched with unique identifiers. Dictionary format with key and values (i.e., Identifier: unique tuple combination of &kappa; and N</sub>p) e.g., p0: (0,2) denotes combination identifier p0 for &kappa; = 0 and N</sub>p = 2.
	From the **parameter_combinations** folder, we use _paramcombs.csv_ for Hospital, IC2S2-17 and WS-16 data sets and for the Workplace data set we use those in _paramcombs_workplace.csv_.

## Code **MaximumLikelihoodEstimation.ipynb**
In the Jupyter notebook file MaximumLikelihoodEstimation.ipynb, we define the method used to estimate the overall activity (&kappa;) and population size (N</sub>p) for networks.
The inputs to this function 
To run the code, you need to import the following:
* Pandas
* Numpy
* Numba

To implement the method, the sequence of (total active nodes, total edges) i.e., (N,M) is required as an input. 

## Demo   
An example of how to implement our numerical maximum likelihood estimation is shown in Demo.ipynb.

In generateMLF.ipynb, we demonstrate how joint probability distributions(likelihood functions) are generated. The user may therefore update the probability equation from p<sub>ij</sub> = 1-e<sup>-&kappa;a<sub>i</sub>a<sub>j</sub></sup> as used in our analysis to any other form as desired. 

    	
