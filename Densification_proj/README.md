# densificationscalingMLE
This is the readme file for the python code for that estimates the population size and overall activity in temporal networks based on a numerical maximum-likelihood method.

**Reference**:

"Estimating the temporal dynamics of densification and sparsification in human contact networks," Shaunette Ferguson and Teruyoshi Kobayashi. 


## Sample network data (.csv files)

a) **Hospital**: Contacts among patients, nurses, doctors and staffs in a Hospital in Lyon. Taken from SocioPatterns project <http://www.sociopatterns.org/datasets/hospital-ward-dynamic-contact-network/>.

b) **Workplace**: Contacts between workers in an office building in France in 2015. Taken from SocioPatterns project <http://www.sociopatterns.org/datasets/test/>.

 c) **IC2S2-17**: Contacts between participants of the International Conference on Computational Social Science 2017 at GESIS in Cologne. The original data can be found at: <https://zenodo.org/record/2531537#.X6qTndtUvOQ>

d) **WS-16**: Contacts between participants of the Computational Social Science Winter Symposium 2016 at GESIS in Cologne. Original data can be found at: <https://zenodo.org/record/2531537#.X6qTndtUvOQ>
	
A sequence of snapshot networks is created, for each dataset, every 5 minutes for each day. The length of each a single snapshot (i.e., a time window) is 10 minutes. 


## Data format

The following inputs are required to implement the maximum-likelihood estimation:
	A T x 3  array (i.e., a sequence of triplets), each triplet consists of the time (*t*), number of active nodes (*N*) and the number of edges (*M*). *N* and *M* are integers. Each sequence of (*t*, *N*, *M*) belongs to a single day.
  t: Identifies the time interval *[t,t+\Delta t]* in datetime.datetime format.
* *N*: An integer denoting the number of nodes that have at least one edge (or link) at *t* on a given day *d*.

* *M*: An integer denoting the total edges at time interval *t* on a given day *d*.

## Code **Maximum-likelihood-estimation.ipynb**
In the Jupyter notebook file Maximum-likelihood-estimation.ipynb, we define the method use to estimate the overall activity (\kappa) and population size (N_p) for networks.

To run the code, you need to import the following:
*Pandas
*Numpy
*Numba

To implement the method, the sequence of (total active nodes, total edges) i.e., (N,M) is required as an input. 

## Demo   
An example of how to implement the method is shown in Demo.ipynb.

    	
