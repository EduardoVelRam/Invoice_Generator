import streamlit as st
import constant
from datetime import datetime

def login():
    st.title(constant.company_name)
    c1,c2 = st.columns(2)
    with c1:
        st.image(constant.logo_path)
    with c2:
        st.empty()
    st.header("Login")
    if st.button("Login"):
        st.login(constant.logging_method)

def logout():
    st.title("Logout")
    st.write(f"Email: {st.user.email}")
    st.write(f"Name: {st.user.nickname}")
    last_login = datetime.strptime(st.user.updated_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%H:%M:%S %d-%m-%Y")
    st.write(f"Last Login: {last_login}")

    if st.button("Logout"):
        st.logout()

login_page = st.Page(login, title="Login", icon="material/login" )
logout_page = st.Page(logout, title="Logout", icon="material/logout" )

make_invoice = st.Page("invoices/make_invoice.py", title="Make Invoice", icon="material/note_add:", default=True)

my_invoices = st.Page("invoices/my_invoices.py", title="My Invoices", icon="material/list_alt:")

make_customer = st.Page("customers/make_customer.py", title="Make Customer", icon="material/person_add:")
my_customers = st.Page("customers/my_customers.py", title="My Customers", icon="material/people:")

billing_data = st.Page("billing_data/dashboard.py", title="Dashboard", icon="material/bar_chart::")

if st.user.is_logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],   
            "Customers": [make_customer, my_customers],
            "Invoices": [make_invoice, my_invoices],
            "Billing Data": [billing_data]
        }
    )
else:
    pg: st.navigation([login_page])

pg.run()