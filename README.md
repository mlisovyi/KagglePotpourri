# KagglePotpourri

There are solutions to several small-scale kaggle competitions:
   * [Forest cover prediction (2018 edition)](https://www.kaggle.com/c/forest-cover-type-kernels-only):
      * Modeling relies on ExtraTrees + LightGBM + Ranfom Forest;
      * Voting classifier with evaluation in a nested CV loop is used;
      * EDA + Feature Engineering + training of a model with weights according to class proportion: [featureengineering-training-with-weights.ipynb](ForrestCoverType2018/featureengineering-training-with-weights.ipynb). This code is also availabe as a kaggle kernel: https://www.kaggle.com/mlisovyi/featureengineering-training-with-weights/notebook;
      * Estimation of the target class fractions (for weights used in the main solution above): [class-fractions-in-the-test.ipynb](ForrestCoverType2018/class-fractions-in-the-test.ipynb);
      * Hyperparameter optimisation for various model types: [hyper-parameter-optimisation.ipynb](ForrestCoverType2018/hyper-parameter-optimisation.ipynb).
      
   * 
