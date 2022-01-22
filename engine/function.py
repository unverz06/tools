from engine.head import *

class Helpers():
         
    def get_optimum_clusters(df):
        '''
        Args:
            df(pd.Dataframe): dataframe with one column value and time as index 
        Returns:
            clusters with optimum K centers (support levels)
            
        Cette méthode utilise la méthode de l "elbow" pour trouver le nombre optimal de clusters (K).
        Nous initialisons différents K-means avec 1..10 centres et comparons la distance du coude à la droite
        joignant K(1) à K(10) pour trouver le meilleur K
        '''
        
        if len(df)==0:
            return None
        
        warnings.filterwarnings('ignore') 
        wcss = []
        k_models = []

        # Au cas ou passerait moins de 10 lignes dans le df, la taille max pour K sera définie par 
        # le nombre de lignes dans le df
        size = min(11, len(df.index))
        K = range(1, size)
        for i in K:
            kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
            kmeans.fit(df)
            wcss.append(kmeans.inertia_)
            k_models.append(kmeans)

        # Calcule du meilleur K
        
        # fonction inline pour calculer la distance othogonale entre un point et une ligne
        # ---
        def calc_distance(x1, y1, a, b, c):
            d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
            return d        
        # ---
        
        a = wcss[0] - wcss[size-2]
        b = K[size-2] - K[0]
        c1 = K[0] * wcss[size-2] 
        c2 = K[size-2] * wcss[0] 
        c = c1 - c2
        distFromLine = []
        for k in range(size-1):
            distFromLine.append(calc_distance(K[k],wcss[k],a,b,c))

        optimum_k = distFromLine.index(max(distFromLine))+1
        optimum_clusters = k_models[optimum_k]
        warnings.resetwarnings()

        return optimum_clusters.cluster_centers_.ravel().tolist()