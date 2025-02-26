import streamlit as st
import streamlit.components.v1 as components

st.title(" DRUGTOX PRO CHATBOT")

# Chatbot Embed Code
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
            script.id = "HHB6Gm__pQWPPYvEtn_vd";  // Replace with your actual Chatbase bot ID
            script.domain = "www.chatbase.co";
            document.body.appendChild(script);
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

# Embed chatbot in Streamlit
components.html(chatbot_code, height=500, width=600)
