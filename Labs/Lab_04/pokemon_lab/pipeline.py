import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("Starting full production Pokémon TCG data pipeline...", file=sys.stderr)

    print("Step 1: Running ETL process (update_portfolio)...", file=sys.stderr)
    update_portfolio.main()

    print("Step 2: Running reporting process (generate_summary)...", file=sys.stderr)
    generate_summary.main()

    print("Production pipeline complete.", file=sys.stderr)


if __name__ == "__main__":
    run_production_pipeline()
