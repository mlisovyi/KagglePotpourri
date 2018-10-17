# KagglePotpourri

There are solutions to several small-scale kaggle competitions:
   * [Forest cover prediction (2018 edition)](https://www.kaggle.com/c/forest-cover-type-kernels-only):
      * Modeling relies on ExtraTrees + LightGBM + Ranfom Forest;
      * Voting classifier with evaluation in a nested CV loop is used;
      * EDA + Feature Engineering + training of a model with weights according to class proportion: [featureengineering-training-with-weights.ipynb](ForrestCoverType2018/featureengineering-training-with-weights.ipynb). This code is also availabe as a kaggle kernel: https://www.kaggle.com/mlisovyi/featureengineering-training-with-weights/notebook;
      * Estimation of the target class fractions (for weights used in the main solution above): [class-fractions-in-the-test.ipynb](ForrestCoverType2018/class-fractions-in-the-test.ipynb);
      * Hyperparameter optimisation for various model types: [hyper-parameter-optimisation.ipynb](ForrestCoverType2018/hyper-parameter-optimisation.ipynb).
      
   * [Costa Rican Household Poverty Level Prediction](https://www.kaggle.com/c/costa-rican-household-poverty-prediction/overview):
      * Preprocessing:
         * [Study of missing values](CostaRicanPovertyLevel/missing-values-in-the-data.ipynb). Also available as https://www.kaggle.com/mlisovyi/missing-values-in-the-data.
         * [Cleaning of categorical features](CostaRicanPovertyLevel/cluster-analysis-tsne-mds-isomap.ipynb). Also available in https://www.kaggle.com/mlisovyi/categorical-variables-encoding-function.
      * [Visualisation of various dimentionality-reduction techniques](CostaRicanPovertyLevel/cluster-analysis-tsne-mds-isomap.ipynb). Aslo available in https://www.kaggle.com/mlisovyi/cluster-analysis-tsne-mds-isomap.
      * [Hyperparameter optimisation of LightGBM with F_1 score for parameter choosing](CostaRicanPovertyLevel/lighgbm-hyperoptimisation-with-f1-macro.ipynb). Aslo in https://www.kaggle.com/mlisovyi/lighgbm-hyperoptimisation-with-f1-macro.
      * [Feature engineering and LightGBM model training with F_1 score](CostaRicanPovertyLevel/feature-engineering-lighgbm-with-f1-macro.ipynb). Aslo in https://www.kaggle.com/mlisovyi/feature-engineering-lighgbm-with-f1-macro.
      * [A little study of why scores are small](CostaRicanPovertyLevel/why-are-scores-low.ipynb). Also in https://www.kaggle.com/mlisovyi/why-are-scores-low.
      
   * [PUBG Finish Placement Prediction](https://www.kaggle.com/c/pubg-finish-placement-prediction):
      * LightGBM is used for modelling
      * [pubg-survivor-kit.ipynb](PUBG/pubg-survivor-kit.ipynb): user-level model with no feature engineering at all.. Aslo available in https://www.kaggle.com/mlisovyi/pubg-survivor-kit/notebook.
      * [eda-team-strategy-guide.ipynb](PUBG/eda-team-strategy-guide.ipynb): model interpretation using [SHAP](https://github.com/slundberg/shap) and [LIME](https://github.com/marcotcr/lime) packages. Also available in https://www.kaggle.com/mlisovyi/eda-team-strategy-guide
      * [relativerank-of-predictions.ipynb](PUBG/relativerank-of-predictions.ipynb): demonstration that relative rank of tem placement within each game outperforms plain predction. Aslo available in https://www.kaggle.com/mlisovyi/relativerank-of-predictions.
      * [pubg-team-guide.ipynb](PUBG/pubg-team-guide.ipynb): Team-level model training. Some Feature engineering. This implementation exploits the leak in the data and leads too good results. Private kernel :)

   * [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques):
      * [EDA_feature_extraction.ipynb](HousePricing/EDA_feature_extraction.ipynb): extensive EDA, feature engineering and a comparison of various models with different feature-selection methods. 
      * [Prepare_Submission.ipynb](HousePricing/Prepare_Submission.ipynb): Prepare submission based on the output of the script above.
