import sqlite3
import pandas as pd

# Connect to Chinook database
conn = sqlite3.connect("chinook.db")

# -----------------------------
# Part 1: Customer Purchases Analysis
# -----------------------------

# Load tables
customers = pd.read_sql_query("SELECT * FROM customers;", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices;", conn)

# Merge customers with invoices
customer_invoices = pd.merge(customers, invoices, on='CustomerId')

# Total spent per customer
total_spent = customer_invoices.groupby(
    ['CustomerId', 'FirstName', 'LastName']
)['Total'].sum().reset_index()

# Top 5 customers
top_5_customers = total_spent.sort_values(by='Total', ascending=False).head(5)

# Display customer ID, name, and total spent
top_5_customers['FullName'] = top_5_customers['FirstName'] + ' ' + top_5_customers['LastName']
top_5_customers = top_5_customers[['CustomerId', 'FullName', 'Total']]

print("=== Top 5 Customers by Total Purchase ===")
print(top_5_customers)


# -----------------------------
# Part 2: Album vs. Individual Track Purchases
# -----------------------------

# Load InvoiceLine, Track, and Album tables
invoice_lines = pd.read_sql_query("SELECT * FROM invoice_items;", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Tracks;", conn)

# Merge InvoiceLine with Track to get Album info
purchases = pd.merge(invoice_lines, tracks, left_on='TrackId', right_on='TrackId')

# For each customer and album, count how many tracks they bought
customer_album = pd.merge(invoices[['InvoiceId','CustomerId']], purchases, on='InvoiceId')

# Total tracks per album
album_track_count = tracks.groupby('AlbumId')['TrackId'].count().reset_index().rename(columns={'TrackId':'TotalTracks'})

# Customer's purchased tracks per album
cust_album_count = customer_album.groupby(['CustomerId','AlbumId'])['TrackId'].count().reset_index().rename(columns={'TrackId':'PurchasedTracks'})

# Merge to compare purchased vs. total tracks
cust_album_summary = pd.merge(cust_album_count, album_track_count, on='AlbumId')

# Determine if customer bought full album or partial tracks
cust_album_summary['Preference'] = cust_album_summary.apply(
    lambda x: 'Full Album' if x['PurchasedTracks'] == x['TotalTracks'] else 'Individual Tracks', axis=1
)

# For each customer, decide their overall preference:
# If they bought any partial album, they are counted as 'Individual Tracks'
def customer_overall_pref(df):
    if (df['Preference'] == 'Individual Tracks').any():
        return 'Individual Tracks'
    else:
        return 'Full Album'

customer_pref = cust_album_summary.groupby('CustomerId').apply(customer_overall_pref).reset_index().rename(columns={0:'Preference'})

# Summary percentages
summary = customer_pref['Preference'].value_counts(normalize=True).mul(100).reset_index().rename(columns={'index':'PurchaseType','Preference':'Percentage'})

print("\n=== Customer Purchase Preferences (Full Album vs Individual Tracks) ===")
print(summary)
