import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Home", "About Me", "Contact","Portfolio"])

with tab1:
    st.title("[in progress] CV María Arancibia")

    st.header("Hi there, my name is María")
    st.write("I am a data enthusiast | industrial engineer | BI lead expert")
    st.write("Python | Dashboards")

    st.subheader("Links")
    st.markdown("[LinkedIn](https://www.linkedin.com/) | [GitHub]")

    st.subheader("Proyectos destacados")
    st.write("Aquí van tus dashboards o apps interactivas")

    st.subheader("CV")
    st.markdown("[Descargar CV](ruta/a/tu/cv.pdf)")


with tab2:
    st.write("Contenido Analytics")

with tab4:
    #explorations
    #adding html for mouse trail effect, testing
    st.components.v1.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
        margin: 0;
        height: 100%;
        background-color: black;  /* Fondo negro */
        overflow: hidden;
    }

    .trail {
        position: absolute;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        pointer-events: none;
        animation: fadeOut 0.5s forwards;
    }

    @keyframes fadeOut {
        from { opacity: 1; transform: scale(1); }
        to { opacity: 0; transform: scale(2); }
    }
    </style>
    </head>
    <body>

    <script>
    document.addEventListener("mousemove", function(e) {
        // Crear un punto
        let dot = document.createElement("div");
        dot.className = "trail";

        // Colores aleatorios brillantes
        const colors = ["#ff3c3c", "#ffec3c", "#3cfffb", "#3cff3c", "#ff3cff"];
        dot.style.background = colors[Math.floor(Math.random() * colors.length)];

        dot.style.left = e.pageX + "px";
        dot.style.top = e.pageY + "px";

        document.body.appendChild(dot);

        // Borrar después de la animación
        setTimeout(() => dot.remove(), 500);
    });
    </script>

    </body>
    </html>
    """, height=400)

