# Fake News Detection through Ego Network Analysis

![Twitter Ego Network for Verified Users with Over 1 Million Followers](https://github.com/briansrebrenik/Final_Project/blob/master/network_screenshots/new2/screenshot_074045.png)
![title](https://github.com/briansrebrenik/Final_Project/blob/master/network_screenshots/new2/final.png)
Data Sources:

* "Fake News" data from [Credbank](http://compsocial.github.io/CREDBANK-data/)

* Twitter Network Edges from [Luca Hammer](https://github.com/lucahammer)

Tools Used:
* [Neo4j Graph Database](https://neo4j.com/)

* [Gephi](https://gephi.org/) for graph visualizations

* [Node2Vec](https://snap.stanford.edu/node2vec/) from Stanford Network Analysis Project

* [Node2Vec Algorithm Implementation](https://github.com/eliorc/node2vec)

* [NetworkX](https://networkx.github.io/)

* [Keras](https://keras.io/)



![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project1.jpg)
![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project2.jpg)
![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project3.jpg)
![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project4.jpg)

Eigenvector centrality is a measure of the influence of a node in a network. Relative scores are assigned to all nodes in the network based on the concept that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes. A high eigenvector score means that a node is connected to many nodes who themselves have high scores.

PageRank is widely recognized as a way of detecting influential nodes in a graph. It is different to other centrality algorithms because the influence of a node depends on the influence of its neighbours.

![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project5.jpg)

The Louvain method of community detection is an algorithm for detecting communities in networks. It maximizes a modularity score for each community, where the modularity quantifies the quality of an assignment of nodes to communities by evaluating how much more densely connected the nodes within a community are compared to how connected they would be in a random network.

![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project6.jpg)

The node2vec framework learns low-dimensional representations for nodes in a graph by optimizing a neighborhood preserving objective. The objective is flexible, and the algorithm accomodates for various definitions of network neighborhoods by simulating biased random walks. Specifically, it provides a way of balancing the exploration-exploitation tradeoff that in turn leads to representations obeying a spectrum of equivalences from homophily to structural equivalence.

Using profile descriptions for classification in a recurrent neural network. The Embedding Layer inside the network computes word embedding vectors. Word Embeddings are a type of vectorization strategy that computes word vectors from a text corpus by training a neural network, which results in a high-dimensional embedding space, where each word is in the corpus is a unique vector in that space. In this embedding space, the position of the vector relative to the other vectors captures semantic meaning.

![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project7.jpg)

Combining features from Node2Vec and probabilities from word embeddings in an XGBoost and SVM Classifier.

![title](https://github.com/briansrebrenik/Final_Project/blob/master/presentation_screenshots/Final%20Project8.jpg)
