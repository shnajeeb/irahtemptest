import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    st.title("Temperature Converter")

    option = st.radio("Choose a conversion:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    main()
