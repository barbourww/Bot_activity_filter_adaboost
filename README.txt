README.txt
Adaboost self-implemented ensemble classifier
Written for CS412: Data Mining
Author: William Barbour
Created: 11/26/2015
Last modified: 11/27/2015

Language: Python 2
External required libraries/packages: numpy, pandas, sklearn
Note: external libraries are only used, per the problem statement, for non-critical algorithm operations and base classifier implementation

Code directory structure:
-------------------------
/final_code
	/random_forest
	/extra_trees
	/data
		**features.csv
	/adaboost
		features_col.py
		plot_submission.py
		bot_human_adaboost.py
		my_adaboost.py
		README.txt
		/results - contains past result files

If the directory structure is altered, then the file paths must be changed accordingly in the .py files. The data file features.csv must be added to /data for code to execute - it is not included due to file size considerations.

Classifier execution:
---------------------
To execute the adaboost classification, change terminal/shell directory to /adaboost and execute "sudo python bot_human_adaboost.py". Alternatively, open the bot_human_adaboost.py file with an IDE and execute. The results file will be saved in the /data directory as mySubmission_final_ab.csv and will be ready for submission to Kaggle.

Note: pandas will throw warning at the end of execution regarding a DataFrame operation, but code executes fully without error.
