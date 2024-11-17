import streamlit as st
import time

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    st.title("🌡️ Interactive Temperature Converter")
    st.subheader("Convert temperatures between Celsius and Fahrenheit seamlessly!")

    option = st.radio("Choose a conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    if option == "Celsius to Fahrenheit":
        st.info("💡 Tip: Water freezes at 0°C and boils at 100°C.")
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert to Fahrenheit"):
            with st.spinner("Calculating..."):
                time.sleep(1)  # Simulating a delay for effect
                fahrenheit = celsius_to_fahrenheit(celsius)
                st.success(f"✅ {celsius}°C is equal to {fahrenheit:.2f}°F")
                st.balloons()

    elif option == "Fahrenheit to Celsius":
        st.info("💡 Tip: Water freezes at 32°F and boils at 212°F.")
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert to Celsius"):
            with st.spinner("Calculating..."):
                time.sleep(1)  # Simulating a delay for effect
                celsius = fahrenheit_to_celsius(fahrenheit)
                st.success(f"✅ {fahrenheit}°F is equal to {celsius:.2f}°C")
                st.balloons()

    st.sidebar.header("About this App")
    st.sidebar.write(
        "This interactive temperature converter helps you switch between Celsius and Fahrenheit with ease. "
        "It also provides helpful tips to understand the freezing and boiling points of water in both scales!"
    )

if __name__ == "__main__":
    main()

