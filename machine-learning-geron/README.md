# machine learning

1. study problem
2. train model
3. inspect solution
4. better understand problem
5. repeat

# types of ml systems (supervision)

- supervised 
- unsupervised
- semi-supervised
- self-supervised

# types of ml systems (incremental learning)

- online
- batch

# types of ml systems (working)

- data comparison based
- pattern detection + predictive model building

# supervised learning

- training data includes solutions or LABELS
- example: classification

# classification

- classify something as one label or the other

# regression

- predict the numerical value of a quantity

# target vs label

- both 
- target is used for regression tasks
- label is used for classification tasks

# features

- also known as inputs or attributes

# unsupervised learning

- training data is unlabeled
- example: clustering, visualization algorithms, dimensionality reduction, anomaly detection, association rule learning
- feed unlabeled data -> get representation of data

- dimensionality reduction simplifies data by merging multiple features into one
- novelty detection: detecting items that look different from other items in the training set
- association rule learning: discover relations between items

# semi-supervised learning

- label a few inputs, system will label everything else

# self-supervised learning

- generating a fully labeled database from a fully unlabeled one

# reinforcement learning

- agent observes environment
- agent selects and performs actions
- agents gets rewards or penalties in return
- agent defines its own strategy (a.k.a. policy) to get the most rewards overtime

# batch learning

- system is trained using all possible data

# online learning

- system is trained incrementally

# instance based learning

- gets a measure of similarity with the given examples

# model rot

- decay in model's performance because of changes in the data or in the world

# model based learning

- build a model from examples and use the model to get predicted values


# challenges 

1. insufficient quantity of training data
2. nonrepresentative training data
3. poor quality data
4. irrelevant features
5. overfitting

a simple ML algorithm may perform equally as well as a complex ML algorithm without enough data


# regularization

constraining a model to make it simpler and reduce risk of overfitting

linear model has two params a,b : y = ax + b

two parameters gives it two degrees of freedom

if we force the algorithm to keep b small, then the algorithm will product a better result

# hyperparameter

parameter of the learning algorithm

not a parameter of the ML model itself

the amount of regularization applied is controlled by hyperparameters 

# out of core memory

Out-of-core learning refers to a set of algorithms designed to handle data that exceeds the capacity of a machine's primary memory (RAM)

# root mean square error

```
RMSE = sqrt(
		sum(
			[(prediction_function(feature[i]) - label[i])**2 
			for i in range(number_of_instances)]
		)
		/number_of_instances
	)
```

# mean absolute error

```
MAE = sum([ abs(prediction_func(feature[i]) - label[i]) for i in range(number_of_instances)])/number_of_instances
```

