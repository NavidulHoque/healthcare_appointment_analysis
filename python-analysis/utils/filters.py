def filter_appointments(df, division=None, specialty=None):
    filtered_df = df.copy()

    if division is not None:
        filtered_df = filtered_df[
            filtered_df['division'].str.strip().str.lower()
            == division.strip().lower()
        ]

    if specialty is not None:
        filtered_df = filtered_df[
            filtered_df['doctor_specialty'].str.strip().str.lower()
            == specialty.strip().lower()
        ]

    return filtered_df