import streamlit as st
import streamlit.components.v1 as components

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: pink !important;
    }
    .stApp {
        background-color: pink !important;
    }
    iframe {
        background-color: pink !important;
        max-width: 100% !important;
    }
    
    /* Responsive Chatbot Container */
    #chatbot-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    
    @media (max-width: 600px) {
        iframe {
            width: 90% !important;
            height: 400px !important;  /* Adjust height for smaller screens */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("DRUGTOX PRO CHATBOT")

# Chatbot Embed Code with Responsive Styling
chatbot_code = """
<div id="chatbot-container">
    <script>
    (function() {
        if (!window.chatbase || window.chatbase("getState") !== "initialized") {
            window.chatbase = (...arguments) => {
                if (!window.chatbase.q) {
                    window.chatbase.q = [];
                }
                window.chatbase.q.push(arguments);
            };
            window.chatbase = new Proxy(window.chatbase, {
                get(target, prop) {
                    if (prop === "q") {
                        return target.q;
                    }
                    return (...args) => target(prop, ...args);
                }
            });
        }
        
        const onLoad = function() {
            const script = document.createElement("script");
            script.src = "https://www.chatbase.co/embed.min.js";
            script.id = "HHB6Gm__pQWPPYvEtn_vd";  // Replace with your Chatbase bot ID
            script.domain = "www.chatbase.co";
            document.body.appendChild(script);
            
            script.onload = function() {
                setTimeout(() => {
                    let chatWidget = document.querySelector("iframe");
                    if (chatWidget) {
                        chatWidget.style.backgroundColor = "pink";
                        chatWidget.style.width = "100%";  // Make chatbot full-width
                        chatWidget.style.maxWidth = "600px";  // Limit max width on larger screens
                    }
                }, 2000);
            };
        };
        
        if (document.readyState === "complete") {
            onLoad();
        } else {
            window.addEventListener("load", onLoad);
        }
    })();
    </script>
</div>
"""

# Embed chatbot in Streamlit with mobile-friendly dimensions
components.html(chatbot_code, height=500, width=600)
