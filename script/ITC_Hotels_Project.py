# ITC Hotels: Data Analytics Project
# Python: NumPy, Pandas and Matplotlib

# Importing Libraries
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import sys
    
except ModuleNotFoundError:
    raise ModuleNotFoundError("Libraries for this project are not installed.")

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Python:", sys.version.split()[0])

# Loading the dataset

df = pd.read_csv(r"C:\Users\arjun\OneDrive\Desktop\Python\Project\ITC_Hotels.csv")
print("\nDataset loaded.")
print()

#Basic EDA
print("Basic EDA:")
print()

#Question 1: Show the first 10 rows of the dataset.
print("Show the first 10 rows of the dataset.")
print(df.head(10))
print()

#Question 2: How many rows and columns does the dataset have?
print("How many rows and columns does the dataset have?")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
print()

#Question 3: Display all column names and their data types.
print("Display all column names and their data types.")
print("Column names:", df.columns.tolist())
print()
print("Data types per column:")
print(df.dtypes)
print()

#Question 4: Show the statistical summary of all numeric columns.
print("Show the statistical summary of all numeric columns.")
print(df.describe())
print()

# Info (non-null counts and memory)
print("Info (non-null counts and memory)")
print(df.info())
print()

#Data Cleaning Process
print("Data Cleaning Process:")
print("How many missing values are there in each column?")
print("Missing values per column:")
print(df.isnull().sum())
print("Total missing values:", df.isnull().sum().sum())
print()

# Question 5: How many duplicate rows exist? Remove them and confirm the new shape.
print("How many duplicate rows exist? Remove them and confirm the new shape")
print("Duplicate row count :", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape of dataset after removing duplicates.")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
print()

#Question 6: Clean the data properly and format the data with the proper datatypes.
# Converting the Excel serial integers to proper dates
print("Converting Excel serial integers to proper dates.")
df["Checkin_Date"] = pd.to_datetime(df["Checkin_Date"])
df["Checkout_Date"] = pd.to_datetime(df["Checkout_Date"])
print()

# Strip whitespace from all text columns
print("Striping whitespaces from all text columns.")
df["Hotel_Name"] = df["Hotel_Name"].str.strip()
df["City"] = df["City"].str.strip()
df["Room_Type"] = df["Room_Type"].str.strip()
df["Booking_Channel"] = df["Booking_Channel"].str.strip()
df["Customer_Type"] = df["Customer_Type"].str.strip()
df["Payment_Mode"] = df["Payment_Mode"].str.strip()
df["Feedback_Status"] = df["Feedback_Status"].str.strip()
df["Occupancy_Status"] = df["Occupancy_Status"].str.strip()
df["Hotel_Category"] = df["Hotel_Category"].str.strip()
df["Month"] = df["Month"].str.strip()
df["Quarter"] = df["Quarter"].str.strip()
print()

# Type conversion
print("Getting correct datatypes using type conversion.")
df["Year"] = df["Year"].astype(np.int32)
df["Guests"] = df["Guests"].astype(np.int32)
print()

print("Data cleaning complete.")
print()

# Feature Engineering
print("Feature Engineering")
print()

# Question 1: Create a Revenue_Per_Night column: Net Revenue divided by Nights Stayed.
print("Create a Revenue_Per_Night column: Net Revenue divided by Nights Stayed.")
df["Revenue_Per_Night"] = df["Net_Revenue"] / df["Nights_Stayed"]

print("\nSolution:")
print(df[["Booking_ID", "Net_Revenue", "Nights_Stayed", "Revenue_Per_Night"]].head(6))
print()

# Question 2: Create a Discount_Pct column: Discount as a percentage of Gross Revenue.
print("Create a Discount_Pct column: Discount as a percentage of Gross Revenue.")
df["Discount_Pct"] = (df["Discount"] / df["Gross_Revenue"]) * 100

print("\nSolution:")
print(df[["Booking_ID", "Gross_Revenue", "Discount", "Discount_Pct"]].head(6))
print()

# Question 3: Create a Revenue_Per_Guest column: Net Revenue divided by Guests.
print("Create a Revenue_Per_Guest column: Net Revenue divided by Guests.")
df["Revenue_Per_Guest"] = df["Net_Revenue"] / df["Guests"]

print("\nSolution:")
print(df[["Booking_ID", "Net_Revenue", "Guests", "Revenue_Per_Guest"]].head(6))
print()

# Question 4: Create a High_Rating flag - 1 where Customer Rating >= 4.5, else 0.
print("Create a High_Rating flag — 1 where Customer Rating >= 4.5, else 0.")
df["High_Rating"] = (df["Customer_Rating"] >= 4.5).astype(np.int32)

print("\nSolution:")
print("Distribution (0 = below 4.5, 1 = 4.5 and above):")
print(df.groupby("High_Rating")["Booking_ID"].count())
print()

# Question 5: Rename Covid_Impact_Level to Covid_Impact.
# Reorder so Booking_ID, Hotel_Name, City appear first.
print('''Rename Covid_Impact_Level to Covid_Impact.
Reorder so Booking_ID, Hotel_Name, City appear first.''')
df = df.rename(columns={"Covid_Impact_Level": "Covid_Impact"})
df = df[["Booking_ID", "Hotel_Name", "City", "State", "Country",
         "Hotel_Category", "Checkin_Date", "Checkout_Date",
         "Month", "Quarter", "Year", "Room_Type", "Guests",
         "Nights_Stayed", "Room_Rate", "Extra_Charges", "Discount",
         "Gross_Revenue", "Net_Revenue", "GST_Amount", "Total_With_GST",
         "Booking_Channel", "Customer_Type", "Payment_Mode",
         "Occupancy_Status", "Customer_Rating", "Feedback_Status",
         "Covid_Impact", "Revenue_Per_Night", "Discount_Pct",
         "Revenue_Per_Guest", "High_Rating"]]

print("\nSolution:")
print("First 3 columns :", df.columns.tolist()[:3])
print("Covid_Impact present :", "Covid_Impact" in df.columns.tolist())
print()

# Basic Business Queries
print("Basic Business Queries")
print()

# Question 7: List all bookings where Nights Stayed is greater than 3.
print("List all bookings where Nights Stayed is greater than 3.")
print("\nSolution:")
b7 = df[df["Nights_Stayed"] > 3]
print("Count :", b7.shape[0])
print(b7[["Booking_ID", "Hotel_Name", "City", "Nights_Stayed", "Net_Revenue"]].head(8))
print()

# Question 8: List all bookings made in the city of Goa.
print("List all bookings made in the city of Goa.")
print("\nSolution:")
b8 = df[df["City"] == "Goa"]
print("Count :", b8.shape[0])
print(b8[["Booking_ID", "Hotel_Name", "Room_Type", "Checkin_Date", "Net_Revenue"]].head(8))
print()

# Question 9: Show bookings where Booking Channel is Walk-in AND Nights Stayed > 2.
print("Show bookings where Booking Channel is Walk-in AND Nights Stayed > 2.")
print("\nSolution:")
b9 = df[(df["Booking_Channel"] == "Walk-in") & (df["Nights_Stayed"] > 2)]
print("Count :", b9.shape[0])
print(b9[["Booking_ID", "Hotel_Name", "Nights_Stayed", "Net_Revenue"]].head(8))
print()

# Question 10: Show bookings where Customer Rating is 5.0 OR Net Revenue is above 100000.
print("Show bookings where Customer Rating is 5.0 OR Net Revenue is above 100000.")
print("\nSolution:")
b10 = df[(df["Customer_Rating"] == 5.0) | (df["Net_Revenue"] > 100000)]
print("Count :", b10.shape[0])
print(b10[["Booking_ID", "Hotel_Name", "Customer_Rating", "Net_Revenue"]].head(8))
print()

# Question 11: Use query() to find all Luxury hotel bookings with Customer Rating above 4.0.
print("Use query() to find all Luxury hotel bookings with Customer Rating above 4.0.")
print("\nSolution:")
b11 = df.query("Hotel_Category == 'Luxury' and Customer_Rating > 4.0")
print("Count :", b11.shape[0])
print(b11[["Booking_ID", "Hotel_Name", "City", "Customer_Rating", "Net_Revenue"]].head(8))
print()

# Question 12: Show all Presidential Suite bookings sorted by Net Revenue, highest first.
print("Show all Presidential Suite bookings sorted by Net Revenue, highest first.")
print("\nSolution:")
b12 = df[df["Room_Type"] == "Presidential Suite"]
b12 = b12.sort_values(by="Net_Revenue", ascending=False)
print("Total Presidential Suite bookings :", b12.shape[0])
print(b12[["Booking_ID", "Hotel_Name", "City", "Net_Revenue", "Customer_Rating"]].head(10))
print()

# Question 13: What is the total Net Revenue across all bookings?
print("What is the total Net Revenue across all bookings?")
print("\nSolution:")
print("Total Net Revenue : Rs.", df["Net_Revenue"].sum())
print()

# Question 14: What is the maximum and minimum Customer Rating?
print("What is the maximum and minimum Customer Rating?")
print("\nSolution:")
print("Maximum Customer Rating :", df["Customer_Rating"].max())
print("Minimum Customer Rating :", df["Customer_Rating"].min())
print("Maximum Room Rate:", df["Room_Rate"].max())
print("Minimum Room Rate:", df["Room_Rate"].min())
print()

# Question 15: Show all bookings with zero discount applied.
print("Show all bookings with zero discount applied.")
print("\nSolution:")
b15 = df[df["Discount"] == 0]
print("Count :", b15.shape[0])
print(b15[["Booking_ID", "Hotel_Name", "Room_Type", "Net_Revenue", "Customer_Rating"]].head(8))
print()

# NumPy Analysis
print("NumPy Analysis")
print()
# Extract key columns as NumPy arrays
revenue_arr = np.array(df["Net_Revenue"])
rating_arr = np.array(df["Customer_Rating"])
discount_arr = np.array(df["Discount"])
nights_arr = np.array(df["Nights_Stayed"])
gst_arr = np.array(df["GST_Amount"])
guests_arr = np.array(df["Guests"])

print("\nNumPy Arrays")
print("revenue_arr shape:", revenue_arr.shape, ", dtype:", revenue_arr.dtype)
print("rating_arr shape:", rating_arr.shape,   ", dtype:", rating_arr.dtype)
print("discount_arr shape:", discount_arr.shape, ", dtype:", discount_arr.dtype)
print()

# Array properties
print("Array properties")
print()

data_matrix = np.array(df[["Room_Rate", "Extra_Charges", "Discount", "Net_Revenue"]])
print("\nMatrix Properties")
print("Shape:", data_matrix.shape)
print("Size:", data_matrix.size)
print("ndim:", data_matrix.ndim)
print("itemsize:", data_matrix.itemsize)
print("dtype:", data_matrix.dtype)
print()

# Question 16: Descriptive statistics on Net Revenue using NumPy.
print("Descriptive statistics on Net Revenue using NumPy.")
print("\nSolution:")
print("Mean: Rs.", round(np.mean(revenue_arr), 2))
print("Median: Rs.", round(np.median(revenue_arr), 2))
print("Standard Deviation: Rs.", round(np.std(revenue_arr), 2))
print("Variance: Rs.", round(np.var(revenue_arr), 2))
print("25th Percentile: Rs.", round(np.percentile(revenue_arr, 25), 2))
print("50th Percentile: Rs.", round(np.percentile(revenue_arr, 50), 2))
print("75th Percentile: Rs.", round(np.percentile(revenue_arr, 75), 2))
print("Minimum: Rs.", round(np.min(revenue_arr), 2))
print("Maximum: Rs.", round(np.max(revenue_arr), 2))
print("Sum (total): Rs.", round(np.sum(revenue_arr), 2))
print("Index of Min booking:", np.argmin(revenue_arr))
print("Index of Max booking:", np.argmax(revenue_arr))
print()

# Question 17: Use np.unique() on Nights Stayed, Year, and Quarter.
print("Use np.unique() on Nights Stayed, Year, and Quarter.")
print("\nSolution:")
print("Unique Nights_Stayed:", np.unique(nights_arr))
print("Unique Years :", np.unique(np.array(df["Year"])))
print("Unique Quarters:", np.unique(np.array(df["Quarter"])))
print()

# Question 18: Boolean mask - count bookings where Discount > 3000. Show as percentage.
print("Boolean mask - count bookings where Discount > 3000. Show as percentage.")
print("\nSolution:")
mask_disc = discount_arr > 3000
count_disc = np.sum(mask_disc)
pct_disc = (count_disc / len(revenue_arr)) * 100
print("Count:", count_disc)
print("Total bk:", len(revenue_arr))
print("Percentage:", round(pct_disc, 2), "%")
print("Avg Net Revenue (discount > 3000): Rs.", round(np.mean(revenue_arr[mask_disc]), 2))
print()

# Question 19: 2D matrix from Net Revenue and GST Amount. np.sum on axis=0 and axis=1.
print("2D matrix from Net Revenue and GST Amount. np.sum on axis=0 and axis=1.")
print("\nSolution:")
matrix_2d  = np.array(df[["Net_Revenue", "GST_Amount"]])
col_totals = np.sum(matrix_2d, axis=0)
print("Shape :", matrix_2d.shape)
print("Column-wise total (axis=0):")
print("  Net_Revenue :", round(col_totals[0], 2))
print("  GST_Amount  :", round(col_totals[1], 2))
print("Row-wise total for first 6 bookings (axis=1):")
print(np.sum(matrix_2d[:6], axis=1))
print()

# Question 20: Quarterly Net Revenue - np.diff() and np.cumsum().
print("Quarterly Net Revenue - np.diff() and np.cumsum().")
print("\nSolution:")
quarterly = df.groupby("Quarter")["Net_Revenue"].sum().sort_index()
q_arr = np.array(quarterly)
print("Quarters:", list(quarterly.index))
print("Revenue per Qtr:", q_arr)
print("np.diff():", np.diff(q_arr))
print("np.cumsum():", np.cumsum(q_arr))
print()

# Question 21: Compare np.mean() and np.median(). State if distribution is skewed.
print("Compare np.mean() and np.median(). State if distribution is skewed.")
print("\nSolution:")
mean_r = np.mean(revenue_arr)
median_r = np.median(revenue_arr)
print("Mean: Rs.", round(mean_r, 2))
print("Median: Rs.", round(median_r, 2))
print("Gap (Mean - Median): Rs.", round(mean_r - median_r, 2))
if mean_r > median_r:
    print("Distribution is RIGHT-SKEWED.")
    print("Most bookings are moderate value. A smaller number of high-value")
    print("bookings pull the mean above the median.")
else:
    print("Distribution is LEFT-SKEWED.")
print()

# Advanced Pandas Queries
print("Advanced Pandas Queries")
print()

# Question 22: Total Net Revenue per Hotel Category. Sort highest to lowest.
print("Total Net Revenue per Hotel Category. Sort highest to lowest.")
print("\nSolution:")
c1 = df.groupby("Hotel_Category")["Net_Revenue"].sum()
print(c1.sort_values(ascending=False))
print()

# Question 23: Average Customer Rating per Room Type. Sort best to worst.
print("Average Customer Rating per Room Type. Sort best to worst.")
print("\nSolution:")
c2 = df.groupby("Room_Type")["Customer_Rating"].mean()
print(c2.sort_values(ascending=False))
print()

# Question 24: Top 5 cities by total Net Revenue.
print("Top 5 cities by total Net Revenue.")
print("\nSolution:")
c3 = df.groupby("City")["Net_Revenue"].sum()
print(c3.sort_values(ascending=False).head(5))
print()

# Question 25: Average Net Revenue per booking for each Booking Channel. Sort descending.
print("Average Net Revenue per booking for each Booking Channel. Sort descending.")
print("\nSolution:")
c4 = df.groupby("Booking_Channel")["Net_Revenue"].mean()
print(c4.sort_values(ascending=False))
print()

# Question 26: Total Gross Revenue per Month.
print("Total Gross Revenue per Month.")
print("\nSolution:")
c5 = df.groupby("Month")["Gross_Revenue"].sum()
print(c5.sort_index())
print()

# Question 27: Multi-metric aggregation for Hotel Category in one agg() call.
print("Multi-metric aggregation for Hotel Category in one agg() call.")
print("\nSolution:")
c6 = df.groupby("Hotel_Category")["Net_Revenue"].agg(
    Total_Revenue   = "sum",
    Avg_Revenue     = "mean",
    Highest_Booking = "max",
    Lowest_Booking  = "min",
    Booking_Count   = "count"
)
print(c6)
print()

# Question 28: Average Customer Rating and booking count per Hotel Name.
print("Average Customer Rating and booking count per Hotel Name.")
print("\nSolution:")
c7 = df.groupby("Hotel_Name")["Customer_Rating"].agg(
    Avg_Rating    = "mean",
    Booking_Count = "count"
)
print(c7.sort_values(by="Avg_Rating", ascending=False))
print()

# Question 29: Total Net Revenue grouped by Year and Quarter.
print("Total Net Revenue grouped by Year and Quarter.")
print("\nSolution:")
c8 = df.groupby(["Year", "Quarter"])["Net_Revenue"].sum()
print(c8)
print()

# Question 30: Keep only Hotel Categories whose average Net Revenue is above the overall average.
print("Keep only Hotel Categories whose average Net Revenue is above the overall average.")
print("\nSolution:")
overall_avg = df["Net_Revenue"].mean()
c9 = df.groupby("Hotel_Category").filter(lambda x: x["Net_Revenue"].mean() > overall_avg)
print("Overall average Net Revenue:", round(overall_avg, 2))
print("Filtered dataset shape:", c9.shape)
print("Average per category (all):")
print(df.groupby("Hotel_Category")["Net_Revenue"].mean().sort_values(ascending=False))
print("Categories in filtered set:", np.unique(np.array(c9["Hotel_Category"])))
print()

# Question 31: Average Discount_Pct per Customer Type. Sort descending.
print("Average Discount_Pct per Customer Type. Sort descending.")
print("\nSolution:")
c10 = df.groupby("Customer_Type")["Discount_Pct"].mean()
print(c10.sort_values(ascending=False))
print()

# Question 32: Total revenue, avg revenue, and booking count per Payment Mode.
print("Total revenue, avg revenue, and booking count per Payment Mode.")
print("\nSolution:")
c11 = df.groupby("Payment_Mode")["Net_Revenue"].agg(
    Total_Revenue = "sum",
    Avg_Revenue = "mean",
    Booking_Count = "count"
)
print(c11.sort_values(by="Total_Revenue", ascending=False))
print()

# Question 33: Rank all cities by average Net Revenue using rank(method='dense').
print("Rank all cities by average Net Revenue using rank(method='dense').")
print("\nSolution:")
c12 = df.groupby("City")["Net_Revenue"].mean().reset_index()
c12.columns = ["City", "Avg_Revenue"]
c12["Rank"] = c12["Avg_Revenue"].rank(method="dense", ascending=False).astype(np.int32)
c12 = c12.sort_values(by="Rank")
print(c12.to_string(index=False))
print()

# Question 34: All Negative feedback bookings. Count per Hotel Name.
print("All Negative feedback bookings. Count per Hotel Name.")
print("\nSolution:")
neg_df = df[df["Feedback_Status"] == "Negative"]
print("Total Negative feedback bookings :", neg_df.shape[0])
c13 = neg_df.groupby("Hotel_Name")["Feedback_Status"].count()
print(c13.sort_values(ascending=False))
print()

# Business Insights
print("Business Insights")
print()

# Question 35: Which hotel category should be prioritised for expansion?
print("Which hotel category should be prioritised for expansion?")
print("\nSolution:")
d1 = df.groupby("Hotel_Category").agg(
    Total_Revenue = ("Net_Revenue", "sum"),
    Avg_Revenue = ("Net_Revenue", "mean"),
    Avg_Rating = ("Customer_Rating", "mean"),
    Booking_Count = ("Booking_ID", "count")
)
print(d1.sort_values(by="Total_Revenue", ascending=False))
print("\nInsight:")
print("Luxury leads in both total and average revenue per booking.")
print("Resort has the fewest bookings - high growth potential with better marketing.")
print("Prioritise Luxury expansion for maximum revenue return per property.")
print()

# Question 36: Which booking channels should get more marketing investment?
print("Which booking channels should get more marketing investment?")
print("\nSolution:")
d2 = df.groupby("Booking_Channel").agg(
    Total_Revenue = ("Net_Revenue", "sum"),
    Avg_Revenue = ("Net_Revenue", "mean"),
    Avg_Rating = ("Customer_Rating", "mean"),
    Booking_Count = ("Booking_ID", "count")
)
print(d2.sort_values(by="Total_Revenue", ascending=False))
print("\nInsight:")
print("Channels with high total revenue AND high avg rating deserve investment.")
print("OTA channels drive volume - invest in partnerships.")
print("Website and Corporate channels offer higher avg revenue per booking.")
print()

# Question 37: How much does COVID impact level affect per-booking revenue?
print("How much does COVID impact level affect per-booking revenue?")
print("\nSolution:")
d3 = df.groupby("Covid_Impact")["Net_Revenue"].agg(
    Avg_Revenue = "mean",
    Total_Revenue = "sum",
    Booking_Count = "count"
)
print(d3)
avg_low = d3.loc["Low",  "Avg_Revenue"]
avg_high = d3.loc["High", "Avg_Revenue"]
print("\nAvg Revenue (Low impact): Rs.", round(avg_low,  2))
print("Avg Revenue (High impact): Rs.", round(avg_high, 2))
print("Difference per booking: Rs.", round(avg_low - avg_high, 2))
print("\nInsight:")
print("Low-impact periods generate measurably higher revenue per booking.")
print("COVID restrictions directly suppressed booking value.")
print()

# Question 38: Use groupby filter() to isolate high-performing hotel categories.
print("Use groupby filter() to isolate high-performing hotel categories.")
print("\nSolution:")
overall_mean = df["Net_Revenue"].mean()
d4 = df.groupby("Hotel_Category").filter(lambda x: x["Net_Revenue"].mean() > overall_mean)
print("Overall avg Net Revenue:", round(overall_mean, 2))
print("Filtered dataset shape:", d4.shape)
print("Avg revenue in filtered set:")
print(d4.groupby("Hotel_Category")["Net_Revenue"].mean())
print("\nInsight:")
print("Only categories clearing the overall average survive the filter.")
print("These segments drive the business above the baseline.")
print()

# Question 39: Does giving a higher discount lead to a better rating?
print("Does giving a higher discount lead to a better rating?")
print("\nSolution:")
corr_val = df["Discount"].corr(df["Customer_Rating"])
print("Correlation (Discount vs Customer Rating) :", round(corr_val, 4))
print("\nInsight:")
if abs(corr_val) < 0.1:
    print("Near-zero correlation. Discounts do not meaningfully improve ratings.")
    print("Service quality drives satisfaction, not price reductions.")
else:
    print("Moderate correlation of", round(corr_val, 4), "- investigate further.")
print()

# Question 40: What does std() and var() on Net Revenue tell about booking value spread?
print("What does std() and var() on Net Revenue tell about booking value spread?")
print("\nSolution:")
print("Mean: Rs.", round(df["Net_Revenue"].mean(), 2))
print("Std Dev: Rs.", round(df["Net_Revenue"].std(),  2))
print("Variance: Rs.", round(df["Net_Revenue"].var(),  2))
print("\nInsight:")
print("A high standard deviation means booking values vary widely.")
print("ITC Hotels serves both budget-conscious and premium guests.")
print("The large spread indicates an opportunity for targeted packages.")
print()

# Question 41: Compare avg Net Revenue - VIP vs Corporate customers.
print("Compare avg Net Revenue - VIP vs Corporate customers.")
print("\nSolution:")
vip_rev  = df[df["Customer_Type"] == "VIP"]["Net_Revenue"]
corp_rev = df[df["Customer_Type"] == "Corporate"]["Net_Revenue"]
print("VIP       — Count:", vip_rev.count(), "| Avg: Rs.", round(vip_rev.mean(), 2))
print("Corporate — Count:", corp_rev.count(), "| Avg: Rs.", round(corp_rev.mean(), 2))
diff_vc = vip_rev.mean() - corp_rev.mean()
if diff_vc > 0:
    print("\nVIP customers generate Rs.", round(diff_vc, 2), "MORE per booking than Corporate.")
else:
    print("\nCorporate customers generate Rs.", round(abs(diff_vc), 2), "MORE per booking than VIP.")
print()

# Question 42: Top 10 bookings by Net Revenue - which room types dominate?
print("Top 10 bookings by Net Revenue - which room types dominate?")
print("\nSolution:")
d5 = df.sort_values(by="Net_Revenue", ascending=False).head(10)
print(d5[["Booking_ID", "Hotel_Name", "City", "Room_Type",
          "Nights_Stayed", "Net_Revenue", "Customer_Rating"]].to_string(index=False))
print("\nInsight:")
print("The room types appearing most in this list represent the highest-value segment.")
print("Focus upselling and upgrade offers on those room types.")
print()

# Question 43: Payment Mode - which mode should be prioritised?
print("Payment Mode - which mode should be prioritised?")
print("\nSolution:")
d6 = df.groupby("Payment_Mode")["Net_Revenue"].agg(
    Total_Revenue = "sum",
    Avg_Revenue   = "mean",
    Booking_Count = "count"
)
d6 = d6.sort_values(by="Booking_Count", ascending=False)
print(d6)
print("\nInsight:")
print("The mode with the highest booking count needs zero-downtime infrastructure.")
print("The mode with the highest avg revenue targets premium customers.")
print("Offer loyalty rewards on the highest-volume mode to retain users.")
print()

# Visualizations
print("Visualizations")
print()

# Prepare data for all charts
print("Preparing data for all charts")
print()

cat_rev = df.groupby("Hotel_Category")["Net_Revenue"].sum().sort_values(ascending=False)
cat_labels = list(cat_rev.index)
cat_values = list(cat_rev.values)

month_rev = df.groupby("Month")["Net_Revenue"].sum().sort_index()
month_gr = df.groupby("Month")["Gross_Revenue"].sum().sort_index()
m_labels = list(month_rev.index)
m_net = list(month_rev.values)
m_gross = list(month_gr.values)

q2021 = df[df["Year"] == 2021].groupby("Quarter")["Net_Revenue"].sum().sort_index()
q2022 = df[df["Year"] == 2022].groupby("Quarter")["Net_Revenue"].sum().sort_index()
q_labels21 = list(q2021.index)
q_labels22 = list(q2022.index) 
q_vals21 = list(q2021.values)
q_vals22 = list(q2022.values)

ch_count = df.groupby("Booking_Channel")["Net_Revenue"].count().sort_values(ascending=False)
ch_labels = list(ch_count.index)
ch_values = list(ch_count.values)

city_top = df.groupby("City")["Net_Revenue"].sum().sort_values(ascending=False).head(5)
city_lab = list(city_top.index)
city_vals = list(city_top.values)

# Visualization 1: Bar chart - total Net Revenue by Hotel Category.
plt.bar(cat_labels, cat_values, color="steelblue", edgecolor="black")
plt.title("V1: Net Revenue by Hotel Category")
plt.xlabel("Hotel Category")
plt.ylabel("Total Net Revenue (Rs.)")
plt.grid(True)
plt.savefig("V1_category_revenue.png")
plt.show()

# Visualization 2: Line chart - total Net Revenue by Month.
plt.plot(m_labels, m_net, color="green", marker="o")
plt.title("V2: Monthly Net Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Net Revenue (Rs.)")
plt.grid(True)
plt.savefig("V2_monthly_trend.png")
plt.show()

# Visualization 3: Histogram - Customer Rating with custom bins.
plt.hist(list(df["Customer_Rating"]),
         bins=[1, 2, 3, 4, 4.5, 5, 5.1],
         edgecolor="black",
         color="orange")
plt.title("V3: Customer Rating Distribution")
plt.xlabel("Customer Rating")
plt.ylabel("Number of Bookings")
plt.grid(True)
plt.savefig("V3_rating_histogram.png")
plt.show()

# Visualization 4: Two line series - Net Revenue vs Gross Revenue across months.
plt.plot(m_labels, m_net,   color="blue",  marker="o", label="Net Revenue")
plt.plot(m_labels, m_gross, color="green", marker="x", label="Gross Revenue")
plt.title("V4: Monthly Net Revenue vs Gross Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.legend()
plt.grid(True)
plt.savefig("V4_net_vs_gross.png")
plt.show()

# Visualization 5: 3-panel vertical dashboard - subplot(3,1,n).
plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.bar(cat_labels, cat_values, color="steelblue", edgecolor="black")
plt.title("Net Revenue by Hotel Category")
plt.ylabel("Revenue (Rs.)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.bar(ch_labels, ch_values, color="skyblue", edgecolor="black")
plt.title("Booking Count by Channel")
plt.ylabel("Number of Bookings")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.hist(list(df["Net_Revenue"]), 25, edgecolor="black", color="orange")
plt.title("Net Revenue Distribution")
plt.xlabel("Net Revenue (Rs.)")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.savefig("V5_vertical_dashboard.png")
plt.show()

# Visualization 6: 3-panel horizontal dashboard - subplot(1,3,n).
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(m_labels, m_net, color="green", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Net Revenue (Rs.)")
plt.grid(True)

plt.subplot(1, 3, 2)
plt.bar(city_lab, city_vals, color="steelblue", edgecolor="black")
plt.title("Top 5 Cities by Revenue")
plt.xlabel("City")
plt.ylabel("Net Revenue (Rs.)")
plt.grid(True)

plt.subplot(1, 3, 3)
plt.hist(list(df["Customer_Rating"]),
         bins=[1, 2, 3, 4, 4.5, 5, 5.1],
         edgecolor="black",
         color="orange")
plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.savefig("V6_horizontal_dashboard.png")
plt.show()

# Visualization 7: 2021 vs 2022 Quarterly Net Revenue - side by side subplots.
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(q_labels21, q_vals21, color="steelblue", edgecolor="black")
plt.title("V7 (2021): Quarterly Net Revenue")
plt.xlabel("Quarter")
plt.ylabel("Net Revenue (Rs.)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(q_labels22, q_vals22, color="orange", edgecolor="black")
plt.title("V7 (2022): Quarterly Net Revenue")
plt.xlabel("Quarter")
plt.ylabel("Net Revenue (Rs.)")
plt.grid(True)

plt.tight_layout()
plt.savefig("V7_quarterly_comparison.png")
plt.show()

print("All charts saved.")
print()

# Project Summary
print("Project Summary: ITC Hotels ")
print()

print("Total Bookings:", df.shape[0])
print("Total Net Revenue: Rs.", df["Net_Revenue"].sum())
print("Avg Revenue/Booking: Rs.", round(df["Net_Revenue"].mean(), 2))
print("Max Customer Rating:", df["Customer_Rating"].max())
print("Min Customer Rating:", df["Customer_Rating"].min())
print("Total Hotels:", len(np.unique(np.array(df["Hotel_Name"]))))
print("Total Cities:", len(np.unique(np.array(df["City"]))))
print()

top_cat = df.groupby("Hotel_Category")["Net_Revenue"].sum()
top_cat = top_cat.sort_values(ascending=False).head(1)
print("Top Revenue Category:", top_cat.index[0])

top_city = df.groupby("City")["Net_Revenue"].sum()
top_city = top_city.sort_values(ascending=False).head(1)
print("Top Revenue City:", top_city.index[0])

top_room = df.groupby("Room_Type")["Customer_Rating"].mean()
top_room = top_room.sort_values(ascending=False).head(1)
print("Highest Rated Room:", top_room.index[0])
print()

print("Project complete!")
