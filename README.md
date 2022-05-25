# Business Objective

The primary goal of this project is to forecast sales in all Rossmann Pharmaceuticals stores across multiple cities six weeks in advance.

# project overview

The goal of this project is to use Machine and Deep Learning to predict sales six weeks in advance across all Rossman Pharmaceutical stores. Promotions, competitions, school-state holidays, seasonality, and locality are all factors that influence sales.

# installation 

```
git clone
```
```
jupyter notebook`
```
# ML Pipeline design
![image](https://user-images.githubusercontent.com/49780811/169189105-b9e10399-fb16-4651-87f9-7126535435f4.png)


# Skills implemented in this project 

* Building dashboards
* Model management
* MLOps with DVC, CML, and MLFlow
* ML Model building and fine-tuning
* CI/CD deployment of ML models
* Python logging
* Unit testing
* Advanced use of scikit-learn
* Feature Engineering

# Data 

The data used in the project is generated automatically by Rossman Pharmaceutical company and are avalaible [here](https://drive.google.com/file/d/1EgqYG4gN3GKtMhmPala81dEsFpFVm97j/view)

# Dataset column description

* Id - an Id that represents a (Store, Date) duple within the test set
* Store - a unique Id for each store
* Sales - the turnover for any given day (this is what you are predicting)
* Customers - the number of customers on a given day
* Open - an indicator for whether the store was open: 0 = closed, 1 = open
* StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
* SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
* StoreType - differentiates between 4 different store models: a, b, c, d
* Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
* CompetitionDistance - distance in meters to the nearest competitor store
* CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
* Promo - indicates whether a store is running a promo on that day
* Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
* Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
* PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store
