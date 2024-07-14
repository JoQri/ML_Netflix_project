from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 모델과 파라미터 정의
models = {
    'DecisionTreeRegressor': (DecisionTreeRegressor(random_state=13),
                              {'max_depth': [3, 5, 7, 10],
                               'min_samples_split': [10, 20, 25, 30]}),
    
    'RandomForestRegressor': (RandomForestRegressor(random_state=13),
                              {'n_estimators': [100, 200, 300, 350],
                               'max_depth': [3, 5, 7, 10],
                               'min_samples_split': [10, 15, 20, 30]}),
    
    'XGBRegressor': (XGBRegressor(random_state=13),
                     {'n_estimators': [50, 100, 200],
                      'max_depth': [3, 5, 7],
                      'learning_rate': [0.05, 0.1, 0.2]}),
    
    'LGBMRegressor': (LGBMRegressor(random_state=13),
                      {'n_estimators': [50, 100, 200, 250],
                       'max_depth': [3, 5, 7],
                       'learning_rate': [0.05, 0.1, 0.2, 0.3]}),
    
    'GradientBoostingRegressor': (GradientBoostingRegressor(random_state=13),
                                  {'n_estimators': [50, 75, 100, 200, 250],
                                   'max_depth': [3, 5, 7, 10],
                                   'learning_rate': [0.05, 0.1, 0.2, 0.3]}),
    
    'AdaBoostRegressor': (AdaBoostRegressor(random_state=13),
                          {'n_estimators': [30, 50, 100, 200],
                           'learning_rate': [0.03, 0.05, 0.1, 0.2]}),
    
    'KNeighborsRegressor': (KNeighborsRegressor(),
                            {'n_neighbors': [5, 10, 15, 20, 30],
                             'weights': ['uniform', 'distance']})
}

# 그리드 서치 함수
def grid_search(X, y, model, param_grid):
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_absolute_error')
    grid_search.fit(X, y)
    return grid_search.best_estimator_, grid_search.best_params_

# 모델 평가 함수
def evaluate(model, X, y):
    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    print("MAE:", mae)
    print("MSE:", mse)
    print("R^2:", r2)
    return mae, mse, r2