# recommender.py
from surprise import KNNWithMeans
from load_data import data


# To use item-based cosine similarity
sim_options = {
    "name": "cosine",
    "user_based": False,  # Compute similarities between items
}

reco_KNN = KNNWithMeans(sim_options = sim_options)

# train KNN model
trainSet = data.build_full_trainset()
reco_KNN.fit(trainSet)

# create predictions
testSet = trainSet.build_anti_testset()
predictions = reco_KNN.test(testSet)