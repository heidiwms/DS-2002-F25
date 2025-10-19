import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    if not os.path.exists(portfolio_file):
        print(f"Error: Portfolio file '{portfolio_file}' not found.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    if df.empty:
        print("The portfolio file is empty — no data to summarize.")
        return

    total_portfolio_value = df["card_market_value"].sum()
    most_valuable_card = df.loc[df["card_market_value"].idxmax()]

    print("\n=== Pokémon TCG Portfolio Summary ===")
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print("\nMost Valuable Card:")
    print(f"  Name:  {most_valuable_card['card_name']}")
    print(f"  ID:    {most_valuable_card['set_id']}-{most_valuable_card['card_number']}")
    print(f"  Value: ${most_valuable_card['card_market_value']:,.2f}")
    print("=====================================\n")


def main():
    generate_summary("card_portfolio.csv")


def test():
    generate_summary("test_card_portfolio.csv")


if __name__ == "__main__":
    test()
