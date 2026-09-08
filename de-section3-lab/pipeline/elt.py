from pipeline.database import get_connection


def run_elt(df):
    print("\nStarting ELT...")

    conn = get_connection()

    # Nettoyage des noms de colonnes
    df.columns = [col.replace('"', '') for col in df.columns]

    # Charger les données brutes
    conn.register("temp_df", df)

    conn.execute("DROP TABLE IF EXISTS air_travel_raw")
    conn.execute("""
        CREATE TABLE air_travel_raw AS
        SELECT *
        FROM temp_df
    """)

    # Supprimer l'ancienne table transformée
    conn.execute("DROP TABLE IF EXISTS air_travel_elt")

    # Transformation directement en SQL
    conn.execute("""
    CREATE TABLE air_travel_elt AS
    SELECT
        month,
        CAST("1958" AS INTEGER) AS passengers_1958
    FROM air_travel_raw
    WHERE CAST("1958" AS INTEGER) > 300
    """)

    conn.close()

    print("ELT completed.")