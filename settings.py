import os

# ---------------------- Filepaths ---------------------
# Using environment variables to avoid hardcoding the data path
PROJECT_PATH = os.environ.get("SUPERVISED_LEARNING_PROJECT_PATH")
TRANSACTIONS_FILE_PATH = os.path.join(PROJECT_PATH, "transactions.npz")
TAX_HOUSEHOLDS_FILE_PATH = os.path.join(PROJECT_PATH, "foyers_fiscaux.csv")
DEBT_RATIO_FILE_PATH = os.path.join(PROJECT_PATH, "taux_endettement.csv")
FINANCIAL_ASSETS_FILE_PATH = os.path.join(PROJECT_PATH, "actifs_financiers.csv")
INTEREST_RATE_FILE_PATH = os.path.join(PROJECT_PATH, "taux_interet.csv")
NEW_LOANS_FILE_PATH = os.path.join(PROJECT_PATH, "flux_nouveaux_emprunts.csv")
REGIONS_FILE_PATH = os.path.join(PROJECT_PATH, "departements-france.csv")
RENT_REFERENCE_INDEX_FILE_PATH = os.path.join(PROJECT_PATH, "indice_reference_loyers.csv")


# ---------------------- Raw Column names ------------------
TRANSACTION_DATE = "date_transaction"
TRANSACTION_MONTH = "mois_transaction"
TRANSACTION_YEAR = "annee_transaction"
DEPARTEMENT = "departement"
REGION = "region"
CITY_UNIQUE_ID = ["departement", "ville", "id_ville"]
SURFACE = "surface_habitable"
PRICE_PER_SQUARE_METER = "prix_m2"

# ---------------------- Feature & Target Column names ------------------
AVERAGE_PRICE_PER_SQUARE_METER = "prix_m2_moyen"
NB_TRANSACTIONS_PER_MONTH = "nb_transactions_mois"
VEFA = "vefa"

REGRESSION_TARGET = "prix"
CLASSIFICATION_TARGET = "en_dessous_du_marche"

random_state = 42
