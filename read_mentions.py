import marimo

__generated_with = "0.11.28"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mention = mo.ui.text(value="innovation|Innovation|innovations|ابتكار|innovación", placeholder="innovation|Innovation|innovaitons|ابتكار|innovación")
    mo.md(
      f"""
      Enter words sepearted by | 

      {mention}
      """
    )
    return (mention,)


@app.cell
def _(mention, mo):
    import polars as pl
    from pathlib import Path
    path_to_public = mo.notebook_location() / "public"

    print(path_to_public)

    dataframes = {}
    path_to_public = Path(path_to_public)
    combined_df = pl.DataFrame()
    for csv_file in path_to_public.iterdir():
        print(csv_file)
        df = pl.read_csv(str(csv_file))
        # Extract the year from the file name
        year = csv_file.name.split()[-1].split(".")[0]
        # Add the year as a new column
        df = df.with_columns(pl.lit(year).alias("Year"))
    
        df = df.with_columns((pl.col("NarrativeText").str.contains(mention.value)).alias("mention_found")) 
        df = df.with_columns((pl.col("NarrativeText").str.count_matches(mention.value)).alias("doc_count"))
        df = df.drop_nulls()
        df = df.group_by("BUSINESS_AREA_NAME","REGION_NAME","Year").agg(
            pl.col("mention_found").any(),pl.col("doc_count").sum())
        combined_df = pl.concat([combined_df, df])
        dataframes[csv_file.name] = df

    combined_df = combined_df.rename({ "REGION_NAME": "Region","BUSINESS_AREA_NAME": "country"})
    combined_df = combined_df.with_columns(pl.col("doc_count").cast(pl.Int8))
    combined_df = combined_df.with_columns(pl.col("mention_found").cast(pl.Int8))

    print(combined_df.head())


    # CSV download using pandas
    csv_download = mo.download(
        data=combined_df.write_csv().encode("utf-8"),
        filename="data.csv",
        mimetype="text/csv",
        label="Download CSV",
    )
    csv_download
    return (
        Path,
        combined_df,
        csv_download,
        csv_file,
        dataframes,
        df,
        path_to_public,
        pl,
        year,
    )


@app.cell
def _(dataframes, mo, pl):
    import matplotlib.pyplot as plt

    df_plots = []
    country_counts_distinct_count = {} # count mentions once per country 
    country_counts_n_count = {} # count mentions n times per country
    for file_name, df_ in dataframes.items():
        if "BUSINESS_AREA_NAME" in df_.columns:
            country_counts_distinct_count[file_name] = len(df_.filter(pl.col("mention_found")==True))
            country_counts_n_count[file_name] = df_["doc_count"].sum()

    df_plots = [country_counts_distinct_count, country_counts_n_count]

    print(country_counts_distinct_count)
    print(country_counts_n_count)

    # Plotting the bar graph

    ylabels = ['Distinct Count of Countries with mentions', 'Count of mentions']
    titles = ['Distinct Count of Countries with mentions per EYSN File', 'Count of mentions per EYSN File']
    for df_plot, ylabel, title in zip(df_plots, ylabels, titles):
    
        plt.figure(figsize=(10, 6))
        bars = plt.bar(df_plot.keys(), df_plot.values(), color='skyblue')
        plt.xlabel('CSV Files')
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
    
        # Adding labels on top of bars
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
                     ha='center', va='bottom', fontsize=10)
        axis = plt.gca()

        mo.output.append(mo.md(
            f"""
            {mo.as_html(axis)}
            """
        ))
        
    return (
        axis,
        bar,
        bars,
        country_counts_distinct_count,
        country_counts_n_count,
        df_,
        df_plot,
        df_plots,
        file_name,
        plt,
        title,
        titles,
        ylabel,
        ylabels,
    )


if __name__ == "__main__":
    app.run()
