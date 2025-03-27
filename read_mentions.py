import marimo

__generated_with = "0.11.28"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    import polars as pl
    path_to_public = mo.notebook_location() / "public"
    csv_files = path_to_public.glob("*.csv")
    dataframes = {}

    for csv_file in csv_files:
        df = pl.read_csv(str(csv_file))
        # Extract the year from the file name
        year = csv_file.name.split()[-1].split(".")[0]
        # Add the year as a new column
        df = df.with_columns(pl.lit(year).alias("year"))
        # Filter the dataframe
        filtered_df = df.filter(df["NarrativeText"].str.contains("innovation|Innovation"))
        dataframes[csv_file.name] = filtered_df
        print(filtered_df)

    return (
        csv_file,
        csv_files,
        dataframes,
        df,
        filtered_df,
        path_to_public,
        pl,
        year,
    )


@app.cell
def _(dataframes):
    import matplotlib.pyplot as plt
    country_counts = {}
    for file_name, df_ in dataframes.items():
        if "BUSINESS_AREA_NAME" in df_.columns:
            country_counts[file_name] = df_["BUSINESS_AREA_NAME"].n_unique()

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    bars = plt.bar(country_counts.keys(), country_counts.values(), color='skyblue')
    plt.xlabel('CSV Files')
    plt.ylabel('Distinct Count of Countries')
    plt.title('Distinct Count of Countries per CSV File')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Adding labels on top of bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
                 ha='center', va='bottom', fontsize=10)

    plt.show()
    return country_counts, df_, file_name, plt


if __name__ == "__main__":
    app.run()
