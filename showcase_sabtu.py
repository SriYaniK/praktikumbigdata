import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# define the ticker symbol in a dictionary with
ticker_dict = {
    'ANTM.JK': "PT Aneka Tambang Tbk",
    'BMRI.JK': "PT Bank Mandiri (Persero) Tbk",
    'BBNI.JK': "PT Bank Negara Indonesia (Persero) Tbk",
    'PNBN.JK': "PT Bank Pan Indonesia Tbk",
    'ISAT.JK': "PT Indosat Tbk",
    'JSMR.JK': "PT Jasa Marga (Persero) Tbk",
    'LPGI.JK': "PT Lippo General Insurance Tbk",
    'FREN.JK': "PT Smartfren Telecom Tbk",
    'TLKM.JK': "PT Telekomunikasi Indonesia Tbk",
    'EXCL.JK': "PT XL Axiata Tbk",
    'GOOGL': "Google",
    'MSFT' : "Microsoft",
    'AAPL' : "Apple",
    'META' : "Meta Flatform"
}

st.write("""
# Aplikasi Yahoo Finance

## Data saham beberapa perusahaan

""")

tickerSymbols = sorted(ticker_dict.keys())

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = tickerSymbols
)

st.write(f'Ticker perusahaan:**{ticker_dict[ticker]}**')
    
tickerData = yf.Ticker(ticker)

hari_mundur = st.selectbox(
    "pilihan rentang hari",
    options = [7, 10, 20, 30, 60, 90, 180, 365]
)

jumlah_hari = timedelta(days = -int(hari_mundur))

tanggal_mulai = date.today() + jumlah_hari

tanggal_akhir = st.date_input(
    'hingga',
    value = date.today()
)

tickerDF = tickerData.history(
    period = '1d',
    start = str(tanggal_mulai),
    end = str(tanggal_akhir)
)

attributes = st.multiselect(
    'Informasi yang ditampilkan:',
    options=['Open', 'High', 'Low', 'Close', 'Volume'],
    default=['Open', 'Close']
)

st.markdown(f"Lima data pertama:")
st.write(tickerDF.head())
st.markdown(f"Dimensi data:")
st.write(tickerDF.shape)

st.plotly_chart(px.line(tickerDF.Open))
st.plotly_chart(px.line(tickerDF.High))
st.plotly_chart(px.line(tickerDF.Low))
st.plotly_chart(px.line(tickerDF.Close))
st.plotly_chart(px.line(tickerDF.Volume))

judul_chart = f'Harga Saham{ticker_dict[ticker]} ({ticker})'

st.plotly_chart(
    px.line(
        tickerDF,
        title = judul_chart,
        y = attributes
    )
)