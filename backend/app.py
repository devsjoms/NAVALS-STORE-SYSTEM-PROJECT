from supabase import create_client, Client

SUPABASE_URL = "https://gvqcnnnwodystwbyztcf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd2cWNubm53b2R5c3R3Ynl6dGNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNzMxODIsImV4cCI6MjA4MTY0OTE4Mn0.ig7wNXtxx8UyA-Q_qBW1Eqfy0RZ6I0aQ1rqkCw07-ds"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_products(search=""):
    query = supabase.table("products").select("*")
    if search:
        query = query.ilike("product_name", f"%{search}%")
    return query.execute().data

def add_product(data):
    supabase.table("products").insert(data).execute()

def update_product(id, data):
    supabase.table("products").update(data).eq("product_id", id).execute()

def delete_product(id):
    supabase.table("products").delete().eq("product_id", id).execute()

def add_user(username, full_name, birthday, password):
    response = supabase.table("users").insert({
        "username": username,
        "full_name": full_name,
        "birthday": birthday,  # YYYY-MM-DD
        "password": password
    }).execute()

    return response.data

def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data

def update_user(user_id, full_name):
    response = supabase.table("users").update({
        "full_name": full_name
    }).eq("user_id", user_id).execute()

    return response.data

def delete_user(user_id):
    response = supabase.table("users").delete().eq("user_id", user_id).execute()
    return response.data

def add_product(name, category, quantity, price):
    return supabase.table("products").insert({
        "product_name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }).execute().data


#def get_products():
#    return supabase.table("products").select("*").execute().data


def update_quantity(product_id, quantity):
    return supabase.table("products").update({
        "quantity": quantity
    }).eq("product_id", product_id).execute().data


def add_transaction(product_id, user_id, product_name, revenue, total_sales):
    return supabase.table("transactions").insert({
        "product_id": product_id,
        "user_id": user_id,
        "products_buy": product_name,
        "revenue": revenue,
        "total_sales": total_sales
    }).execute().data


def get_transactions():
    response = supabase.table("transactions").select(
        "transaction_id, revenue, total_sales, created_at, "
        "users(full_name), products(product_name)"
    ).execute()

    return response.data


def count_total():
    res = supabase.table("products") \
    .select("product_id", count="exact") \
    .execute()

    return res.count