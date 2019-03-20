import pandas as pd


def main():
    gs_df = pd.read_csv("data/SS_2018 public.csv")
    print(gs_df)


if __name__ == "__main__":
    main()
