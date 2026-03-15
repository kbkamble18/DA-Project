import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
file_path = os.path.join("data", "OLA_Rides.csv")
df = pd.read_csv(file_path)

st.title("OLA Ride Insights Dashboard")

st.write("Dataset Overview")
st.dataframe(df.head())

# KPIs
st.subheader("Key Metrics")

total_rides = len(df)
total_revenue = df[df["Booking_Status"] == "Success"]["Booking_Value"].sum()
avg_distance = df["Ride_Distance"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Rides", total_rides)
col2.metric("Total Revenue", round(total_revenue, 2))
col3.metric("Avg Distance", round(avg_distance, 2))
# 1
st.subheader("Booking Status Distribution")

status_count = df.groupby("Booking_Status").size().reset_index(name="Total_Rides")

fig4 = px.bar(
    status_count,
    x="Booking_Status",
    y="Total_Rides",
    title="Total Rides by Booking Status",
    color="Booking_Status",
)

st.plotly_chart(fig4)

# 2

st.subheader("Average Ride Distance by Vehicle Type")

distance_vehicle = df.groupby("Vehicle_Type")["Ride_Distance"].mean().reset_index()

fig5 = px.bar(
    distance_vehicle,
    x="Vehicle_Type",
    y="Ride_Distance",
    title="Average Ride Distance by Vehicle Type",
    color="Vehicle_Type",
)

st.plotly_chart(fig5)

# 3

st.subheader("Top 10 Customers by Ride Count")

top_customers = (
    df.groupby("Customer_ID")
    .size()
    .reset_index(name="Total_Rides")
    .sort_values(by="Total_Rides", ascending=False)
    .head(10)
)

fig6 = px.bar(
    top_customers,
    x="Customer_ID",
    y="Total_Rides",
    title="Top 10 Customers by Number of Rides",
)

st.plotly_chart(fig6)
# 4

st.subheader("Driver Cancellation Reasons")

driver_cancel = (
    df[df["Canceled_Rides_by_Driver"].notna()]
    .groupby("Canceled_Rides_by_Driver")
    .size()
    .reset_index(name="Total_Cancellations")
)

fig7 = px.bar(
    driver_cancel,
    x="Canceled_Rides_by_Driver",
    y="Total_Cancellations",
    title="Driver Cancellation Reasons",
)

st.plotly_chart(fig7)

# 5

st.subheader("Incomplete Ride Reasons")

incomplete = (
    df[df["Incomplete_Rides"] == "Yes"]
    .groupby("Incomplete_Rides_Reason")
    .size()
    .reset_index(name="Count")
)

fig8 = px.bar(
    incomplete,
    x="Incomplete_Rides_Reason",
    y="Count",
    title="Reasons for Incomplete Rides",
)

st.plotly_chart(fig8)

# 6

st.subheader("Driver Rating Distribution")

driver_rating = df.groupby("Driver_Ratings").size().reset_index(name="Count")

fig9 = px.bar(
    driver_rating, x="Driver_Ratings", y="Count", title="Driver Rating Distribution"
)

st.plotly_chart(fig9)

# 7
total_revenue = df[df["Booking_Status"] == "Success"]["Booking_Value"].sum()

# 4. Add Interactive Filters

st.sidebar.title("Filters")

vehicle = st.sidebar.selectbox("Vehicle Type", df["Vehicle_Type"].unique())

status = st.sidebar.selectbox("Booking Status", df["Booking_Status"].unique())

filtered = df[(df["Vehicle_Type"] == vehicle) & (df["Booking_Status"] == status)]

st.dataframe(filtered)

# 5. Ride Volume Chart

ride_count = df.groupby("Date").size().reset_index(name="Rides")

fig = px.line(ride_count, x="Date", y="Rides", title="Ride Volume Over Time")

st.plotly_chart(fig, key="fig_chart")

# 6. Revenue by Payment Method

revenue = df.groupby("Payment_Method")["Booking_Value"].sum().reset_index()

fig2 = px.bar(
    revenue, x="Payment_Method", y="Booking_Value", title="Revenue by Payment Method"
)

st.plotly_chart(fig2, key="fig2_chart")

# 7. Customer Ratings Chart

rating = df.groupby("Vehicle_Type")["Customer_Rating"].mean().reset_index()

fig3 = px.bar(
    rating,
    x="Vehicle_Type",
    y="Customer_Rating",
    title="Average Customer Rating by Vehicle",
)

st.plotly_chart(fig3, key="fig3_chart")

# Booking Status vs Total Rides

st.subheader("Booking Status Distribution")

status_count = df.groupby("Booking_Status").size().reset_index(name="Total_Rides")

fig4 = px.bar(
    status_count,
    x="Booking_Status",
    y="Total_Rides",
    title="Total Rides by Booking Status",
    color="Booking_Status",
)

st.plotly_chart(fig4, key="fig4_chart")

# Ride Distance by Vehicle Type

st.subheader("Average Ride Distance by Vehicle Type")

distance_vehicle = df.groupby("Vehicle_Type")["Ride_Distance"].mean().reset_index()

fig5 = px.bar(
    distance_vehicle,
    x="Vehicle_Type",
    y="Ride_Distance",
    title="Average Ride Distance by Vehicle Type",
    color="Vehicle_Type",
)

st.plotly_chart(fig5, key="fig5_chart")

# Top Customers by Ride Count

st.subheader("Top 10 Customers by Ride Count")

top_customers = (
    df.groupby("Customer_ID")
    .size()
    .reset_index(name="Total_Rides")
    .sort_values(by="Total_Rides", ascending=False)
    .head(10)
)

fig6 = px.bar(
    top_customers,
    x="Customer_ID",
    y="Total_Rides",
    title="Top 10 Customers by Number of Rides",
)

st.plotly_chart(fig6, key="fig6_chart")

# Driver Cancellation Reasons

st.subheader("Driver Cancellation Reasons")

driver_cancel = (
    df[df["Canceled_Rides_by_Driver"].notna()]
    .groupby("Canceled_Rides_by_Driver")
    .size()
    .reset_index(name="Total_Cancellations")
)

fig7 = px.bar(
    driver_cancel,
    x="Canceled_Rides_by_Driver",
    y="Total_Cancellations",
    title="Driver Cancellation Reasons",
)

st.plotly_chart(fig7, key="fig7_chart")

# Incomplete Ride Reasons

st.subheader("Incomplete Ride Reasons")

incomplete = (
    df[df["Incomplete_Rides"] == "Yes"]
    .groupby("Incomplete_Rides_Reason")
    .size()
    .reset_index(name="Count")
)

fig8 = px.bar(
    incomplete,
    x="Incomplete_Rides_Reason",
    y="Count",
    title="Reasons for Incomplete Rides",
)

st.plotly_chart(fig8, key="fig8_chart")

# Driver Rating Distribution

st.subheader("Driver Rating Distribution")

driver_rating = df.groupby("Driver_Ratings").size().reset_index(name="Count")

fig9 = px.bar(
    driver_rating, x="Driver_Ratings", y="Count", title="Driver Rating Distribution"
)

st.plotly_chart(fig9, key="fig9_chart")
