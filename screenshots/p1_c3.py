import polars as pl
import os
from settings import PROJECT_PATH
import matplotlib.pyplot as plt
import seaborn as sns

transactions = pl.read_parquet(
    os.path.join(PROJECT_PATH, "transactions_post_feature_engineering.parquet")
)

feature_names = [col for col in transactions.columns if col != "id_transaction"]

# %%
categorical_features = [col for col in feature_names if "type_batiment" in col]
categorical_features.append("vefa")
categorical_features.extend([col for col in feature_names if "nom_region" in col])

# %%
numerical_features = [col for col in feature_names if col not in categorical_features]
numerical_features.remove("nom_departement")
# %%
correlation_matrix = transactions.to_pandas()[numerical_features].corr()
plt.figure(figsize=(15, 12))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


highly_correlated_features = [
    "type_batiment_Maison",     # Keep one or the other
    "n_pieces",                 # Keep living area instead
    # "annee_transaction",      # Keep debt ratio instead
    "euros_par_habitant",       # Highly correlated with debt ratio
    "montant_impot_moyen",      # Highly correlated with average taxable income
    "fraction_assurance_vie",
    "fraction_fonds_communs",
    "fraction_titres_non_action",
    "fraction_actions",
    "taux",
    "IRL",
]
