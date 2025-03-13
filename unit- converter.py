import streamlit as st
   #first 3 heading
st.title("🌍Unit Converter App")
st.markdown("###Convert Length , Weight And Time Instantly")
st.write("Welcome!!Select a categoriy and enter a value and get the converted result in real-time")

    #1 selectbob

category=st.selectbox("Chosse A Category",["length","Weight","Time"])

def convert_unit(category,unit,value):
    if category=="Length":
      if unit=="Kilometer To mile":
         return value * 0.621371
      elif unit=="Mile To kilometer":
         return value / 0.621371 
      

    elif category == "weight":
       if unit=="Kilogram To pound":
          return value * 2.20462
       elif unit=="Pound To Kilogram":
           return value / 2.20462      

    elif category == "Time":
        if unit == "Second to Minutes":
            return value / 60
        elif unit == "Minutes to Second":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
       
if category == "Length":
   unit= st.selectbox("📏Select Conservation",["Kilometers to miles","Miles to kilometer"])
elif category=="Weight":
   unit=st.selectbox("⚖Select Conservation"["Kilogram to pound","Pound to kilogram"])
elif category == "Time":
   unit=st.selectbox("⏰Select Conservation"["Second to minutes","Minutes to second","Hours to days ","Days to hours"])

value = st.number_input("Enter The Value that you want to convert")

if st.button("Convert"):
   result = convert_unit(category,value,unit)
st.success(f"The Result Is {result:.2f}")