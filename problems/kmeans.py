
import numpy as np

class KMeans:

    def __init__(self, k) -> None:
        pass

    def run(self, X, k, func2cal_distance, max_iter=1000):
        """
        
        :X: numpy.ndarray. 要聚类的样本. 2维数组，如：np.array([[1, 2], [2, 3]])
        :k: int. 聚类数；
        :func2cal_distance: 距离计算方法
        :max_iter: int. 最大迭代次数
        :return: labels: array([1, ... 0, 0]); centers: np.array([[1, 2], [2, 3]])
        """
        if len(X.shape) == 1: # np.array([1, 2, 3, 4])
            X = X[:, np.newaxis] # np.array([[1], [2], [3], [4]])
        # 1. 初始化：选择 k 个随机点作为初始聚类中心
        centers = X[np.random.choice(range(X.shape[0]), size=k, replace=False)]

        for _ in range(max_iter):
            # 2. 分配：对于数据集中的每个点，计算它到每个聚类中心的距离，并将其分配给距离最近的聚类
            labels = np.argmin(((X[:, np.newaxis] - centers) ** 2).sum(axis=2), axis=1)
            # 3. 更新：重新计算每个聚类的中心，方法是取属于该聚类的所有点的平均值
            new_centers = np.array([X[labels==i].mean(axis=0) for i in range(k)])

            # 判断是否收敛
            if np.all(centers == new_centers):
                break

            centers = new_centers

        return labels, centers

