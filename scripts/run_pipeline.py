# scripts/run_pipeline.py
import os
import sys
import snowflake.connector

def main():
    try:
        # Connexion à Snowflake
        ctx = snowflake.connector.connect(
            user=os.environ["SNOWFLAKE_USER"],
            password=os.environ["SNOWFLAKE_PASSWORD"],
            account=os.environ["SNOWFLAKE_ACCOUNT"],
            database=os.environ["SNOWFLAKE_DATABASE"],
            schema=os.environ["SNOWFLAKE_SCHEMA"]
        )
        cs = ctx.cursor()

        # Exemple : Création d'une table si elle n'existe pas
        cs.execute("""
              create or replace table FINAL.yellow_taxi_trips (
                vendorid int,
                tpep_pickup_datetime timestamp_ntz,
                tpep_dropoff_datetime timestamp_ntz,
                passenger_count int,
                trip_distance float,
                ratecodeid int,
                store_and_fwd_flag string,
                pulocationid int,
                dolocationid int,
                payment_type int,
                fare_amount float,
                extra float,
                mta_tax float,
                tip_amount float,
                tolls_amount float,
                improvement_surcharge float,
                total_amount float,
                congestion_surcharge float,
                airport_fee float
            );
        """)
        print("✅ Ingestion terminée.")

        cs.close()
        ctx.close()
        print("🎉 Pipeline exécuté avec succès !")

    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)  # GitHub Actions considère que le job a échoué

if __name__ == "__main__":
    main()
