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