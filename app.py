#el link a la pagina es http://localhost:8501/
import streamlit as st

st.title("Mi perfil profesional")

st.header("Hola, soy [Tu Nombre]")
st.write("Data enthusiast | BI | Python | Dashboards")

st.subheader("Links")
st.markdown("[LinkedIn](https://www.linkedin.com/) | [GitHub]")

st.subheader("Proyectos destacados")
st.write("Aquí van tus dashboards o apps interactivas")

st.subheader("CV")
st.markdown("[Descargar CV](ruta/a/tu/cv.pdf)")