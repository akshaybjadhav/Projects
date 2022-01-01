import pickle
import streamlit  as st
import sklearn

filename = "wine_quality.pickle"
classifier = pickle.load(open(filename, 'rb'))

def data_prediction(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11):
    prediction = classifier.predict([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]])
    print(prediction)
    return prediction


def main():
    st.title('Akshay Jadhav')
    html_temp = """
            <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Wine Quality Classification</h2>
            </div>
            """
    st.markdown(html_temp, unsafe_allow_html=True)
    d1 = st.text_input('Fixed Acidity', '7.4')
    d2 = st.text_input('Volatile Acidity','0.70')
    d3 = st.text_input('Citric Acid','0.00')
    d4 = st.text_input('Residual Sugar','1.9')
    d5 = st.text_input('Chlorides','0.076')
    d6 = st.text_input('Free Sulphur Dioxide', '11.0')
    d7 = st.text_input('Total Sulphur Dioxide','34.0')
    d8 = st.text_input('Density', '0.9978')
    d9 = st.text_input('pH', '3.51')
    d10 = st.text_input('Sulphates', '0.56')
    d11 = st.text_input('Alcohol', '9.4')
    result = ""
    if st.button('Classify'):
        result = data_prediction(d1, d2, d3, d4, d5, d6, d7, d8, d9,d10,d11)
    st.success('Quality of Wine: {}'.format(result))
    if st.button("About"):
        st.text("Bharat Soft Solutions")
        st.text("Yogesh Murumkar")


if __name__ == "__main__":
    main()

