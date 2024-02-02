import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_specialch):

    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_specialch:
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Función principal
def main():
    st.title("Password Generator")
    
    password_length = st.slider("Tamaño del Password", 8, 128, 12)
    
    # Opciones para generar Password
    use_uppercase = st.checkbox("Incluir Mayúsculas", value=True)
    use_numbers  = st.checkbox("Incluir Números", value=True)
    use_specialch = st.checkbox("Incluir Caracteres Especiales", value=True)
                                
    
    if st.button("Gemerar Password"):
        password = generate_password(password_length, use_uppercase, use_numbers, use_specialch)
        st.success(f"Password Generada: {password}")
        
    st.markdown("---")
    st.markdown('<p style="display: flex; align-items: center;">Developed by Luis Subiabre <span style="margin-left: 5px;">🤖</span></p>', unsafe_allow_html=True)
    
if __name__=="__main__":
    main()