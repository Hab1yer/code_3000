import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    identifiers = ["age", "gender", "zip3"]
    # Missing values should not count as exact matches.
    candidates = anon_df.dropna(subset=identifiers).merge(
        aux_df.dropna(subset=identifiers + ["name"]),
        on=identifiers,
        how="inner",
    )
    match_counts = candidates.groupby("anon_id")["name"].transform("size")
    matches = candidates.loc[match_counts == 1, ["anon_id", "name"]]
    return matches.rename(columns={"name": "matched_name"}).reset_index(drop=True)


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    if len(anon_df) == 0:
        return 0.0
    return matches_df["anon_id"].nunique() / len(anon_df)
