from cProfile import label
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

raw_data = pd.read_csv('europe.csv')
features = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']

x = raw_data.loc[:, features].values
y = raw_data.loc[:,['Country']].values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=0.95, svd_solver='full')

components = pca.fit_transform(x)
df = pd.DataFrame(data = components)
final_df = pd.concat([df, raw_data[['Country']]], axis = 1)
first_component = pd.DataFrame(data=components[:, 0], index=y).T

print(final_df)
print(f'Primer Componente: \n {first_component}')
print(f'Varianza: \n {pca.explained_variance_ratio_}' + "\n")
print(f'Varianza acumulada: \n {pca.explained_variance_ratio_.cumsum()}')
print(f'Autovectores: \n {pca.components_}')