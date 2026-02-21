<<<<<<< HEAD
import streamlit as st
from datetime import date
import tempfile
import os
import streamlit.components.v1 as components

from models import Invoice, InvoiceItem, Issuer
from pdf_generator import generate_invoice_pdf
from utils import pdf_preview
from validator_helper import validar_email
from send_email_helper import send_email

from repositories.invoice_repository import InvoiceRepository
from repositories.client_repository import ClientRepository
from database import SessionLocal

import constant

# page configuration
st.set_page_config(page_title="Make Invoice", layout="wide")

st.title("Invoice Generator") 

if "invoice_items" not in st.session_state:
    st.session_state["invoice_items"] = []

if "preview_pdf_path" not in st.session_state:
    st.session_state["preview_pdf_path"] = None

if "invoice_object" not in st.session_state:
    st.session_state["invoice_object"] = None

if "invoice_number" not in st.session_state:
    st.session_state["invoice_number"] = None

if "invoice_saved" not in st.session_state:
    st.session_state["invoice_saved"] = False

# emisor

issuer = Issuer(
    name=constant.company_name,
    nif=constant.company_nif,
    address=constant.company_address,
    email=constant.email,
)

# customer
db = SessionLocal()
client_repo = ClientRepository(db)
clients = client_repo.get_all()
db.close()

st.subheader("Customer Information")

if not clients:
    st.warning("No clients found. Please add a client first.")
    st.stop()

clients_by_name = {client.name: client for client in clients}
col_client1, col_client2 = st.columns(2)
selected_client_name = col_client1.selectbox("Select Client", options=list(clients_by_name.keys()),index=None, placeholder="Find a client")

client = None
if selected_client_name:
# 7:34
=======
import streamlit as st
from datetime import date
import tempfile
import os
import streamlit.components.v1 as components

from models import Invoice, InvoiceItem, Issuer
from pdf_generator import generate_invoice_pdf
from utils import pdf_preview
from validator_helper import validar_email
from send_email_helper import send_email

from repositories.invoice_repository import InvoiceRepository
from repositories.client_repository import ClientRepository
from database import SessionLocal

import constant

# page configuration
st.set_page_config(page_title="Make Invoice", layout="wide")

st.title("Invoice Generator") 

if "invoice_items" not in st.session_state:
    st.session_state["invoice_items"] = []

if "preview_pdf_path" not in st.session_state:
    st.session_state["preview_pdf_path"] = None

if "invoice_object" not in st.session_state:
    st.session_state["invoice_object"] = None

if "invoice_number" not in st.session_state:
    st.session_state["invoice_number"] = None

if "invoice_saved" not in st.session_state:
    st.session_state["invoice_saved"] = False

# e
>>>>>>> 46ffe8985a887ddd2fba81cc99f7605f576faeb0
