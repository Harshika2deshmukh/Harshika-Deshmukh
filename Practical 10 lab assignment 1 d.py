print("Cheapest Book:")
print(df[df['price'] == df['price'].min()])

print("Costliest Book:")
print(df[df['price'] == df['price'].max()])
