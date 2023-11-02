# ================================ Clustering ================================
import sys
sys.path.append('src')
import conf
import pandas as pd
from sklearn_extra.cluster import KMedoids
from joblib import dump

print("Starting to cluster out the data...")
trainTracksDF = pd.read_csv(conf.pro_train_set_path)
testTracksDF = pd.read_csv(conf.pro_test_set_path)

trainSet = trainTracksDF[conf.features]
testSet = testTracksDF[conf.features]

# Clustering train set (user's preferences playlist)
kmedoids = KMedoids(n_clusters = conf.no_cluster, random_state = conf.rnd_state)

clusters = kmedoids.fit_predict(trainSet)
trainTracksDF['Cluster'] = clusters

# Clustering test set with the trained model (playlist from which songs will be suggested)
test_clusters = kmedoids.predict(testSet)
testTracksDF['Cluster'] = test_clusters

print("Clustering completed!")

print("===================================================")
outputTrainFile = conf.output_dir + 'clustertrainSet.csv'
outputTestFile = conf.output_dir + 'clustertestSet.csv'

print("Storing the processed files in the folder processed_data.")
trainTracksDF.to_csv(outputTrainFile, index=False)
testTracksDF.to_csv(outputTestFile, index=False)
print("The data has been stored!")
print("===================================================")

print("First 5 rows of the train set:")
print(trainTracksDF.head())

print("First 5 rows of the test set:")
print(testTracksDF.head())

# Save the model to the file
dump(kmedoids, conf.model_file_path)