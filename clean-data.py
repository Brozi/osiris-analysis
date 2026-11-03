import pandas as pd

# read modis data into seperate dataframes
df_modis_archive = pd.read_csv("data/modis-archive.csv")
df_modis_realtime = pd.read_csv("data/modis-realtime.csv")

# read snpp data into seperate dataframes
df_snpp_archive = pd.read_csv("data/snpp-archive.csv")
df_snpp_realtime = pd.read_csv("data/snpp-realtime.csv")

# concatenate two dataframes into one
df_modis_all = pd.concat([df_modis_archive, df_modis_realtime]).drop_duplicates()

df_snpp_all = pd.concat([df_snpp_archive, df_snpp_realtime]).drop_duplicates()

# write the dataframes into files
df_modis_all.to_csv("data/modis-all.csv")
df_snpp_all.to_csv("data/snpp-all.csv")

# concatenate the different satellite df's
# into a single master df
df_all = pd.concat([df_modis_all, df_snpp_all]).drop_duplicates()

# pad time with leading zeros
padded_time = df_all["acq_time"].astype(str).str.zfill(4)

# create a new datetime column with date and time together
df_all["datetime"] = pd.to_datetime(
    df_all["acq_date"] + " " + padded_time, format="%Y-%m-%d %H%M"
)

print(df_all.info())
print(df_all.head(10))
print(df_all["datetime"])
