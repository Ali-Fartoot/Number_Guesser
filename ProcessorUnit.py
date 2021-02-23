from SplitDataSet import x_train_augmented, y_train_augmented
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def find_best_param():
    knn_clf = KNeighborsClassifier()
    # the parameters for finding best parameters between them
    param_grid = [{'weights': ["uniform", "distance"], 'n_neighbors': [3, 4, 5, 6]}]
    # cv=5 means test 5 times for each param.
    grid_search = GridSearchCV(knn_clf, param_grid, cv=5, verbose=3)
    # finally train our data
    grid_search.fit(x_train_augmented,y_train_augmented)
    # returning best param.
    final_param = grid_search.best_params_

    print(final_param)

    return final_param
